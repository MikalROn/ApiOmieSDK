import pytest
from unittest.mock import Mock, patch
import httpx
from requests import Session, post
from omieapi.core.omiebase import OmieBase
import json

@pytest.fixture
def omie_base():
    return OmieBase(
        omie_app_key="test_app_key",
        omie_app_secret="test_app_secret",
        session=False,
        use_httpx=False,
        log=False,
        limite_requisicoes=2
    )


@pytest.fixture
def omie_base_httpx():
    return OmieBase(
        omie_app_key="test_app_key",
        omie_app_secret="test_app_secret",
        session=False,
        use_httpx=True,
        log=False,
        limite_requisicoes=2
    )

@pytest.fixture
def omie_base_session():
    return OmieBase(
        omie_app_key="test_app_key",
        omie_app_secret="test_app_secret",
        session=True,
        use_httpx=False,
        log=False,
        limite_requisicoes=2
    )

def test_init(omie_base):
    assert omie_base._appkey == "test_app_key"
    assert omie_base._appsecret == "test_app_secret"
    assert omie_base._endpoint == "https://app.omie.com.br/api/v1/"
    assert omie_base._has_session is False
    assert omie_base._httpx is False
    assert omie_base._limite_requisicoes == 2

def test_init_with_session(omie_base_session):
    assert omie_base_session._has_session is True
    assert isinstance(omie_base_session._session, Session)

def test_init_with_httpx(omie_base_httpx):
    assert omie_base_httpx._has_session is False
    assert omie_base_httpx._httpx is True

def test_abrir_session(omie_base, mocker):
    mocker.patch("requests.Session", return_value=Mock())
    omie_base.abrir_session()
    assert omie_base._has_session == True

def test_abrir_session_already_open(omie_base_session):
    with pytest.raises(RuntimeError, match="Session já está aberta"):
        omie_base_session.abrir_session()

def test_fechar_session(omie_base_session, mocker):
    mock_close = mocker.patch.object(Session, "close")
    omie_base_session.fechar_session()
    assert omie_base_session._has_session is False
    mock_close.assert_called_once()

def test_fechar_session_not_open(omie_base):
    with pytest.raises(RuntimeError, match="Não exite sessão aberta"):
        omie_base.fechar_session()

def test_context_manager(omie_base, mocker):
    mocker.patch("requests.Session", return_value=Mock())
    with omie_base as ob:
        assert ob._has_session is True
    assert ob._has_session is False

def test_gerar_json(omie_base):
    param = {"pagina": 1, "registros_por_pagina": 100}
    result = omie_base._gerar_json(call="ListarContasCorrentes", param=param)
    expected = {
        "call": "ListarContasCorrentes",
        "app_key": "test_app_key",
        "app_secret": "test_app_secret",
        "param": [{"pagina": 1, "registros_por_pagina": 100}]
    }
    assert result == expected

def test_post_request_success(omie_base, mocker):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"success": "ok"}
    mocker.patch("requests.post", return_value=mock_response)

    result = omie_base._post_request(
        url="https://app.omie.com.br/api/v1/test/",
        json={"call": "TestCall", "param": [{}]}
    )
    assert result == {"success": "ok"}
    mock_response.json.assert_called_once()

def test_post_request_httpx_success(omie_base_httpx, mocker):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"success": "ok"}
    mocker.patch("httpx.post", return_value=mock_response)

    result = omie_base_httpx._post_request(
        url="https://app.omie.com.br/api/v1/test/",
        json={"call": "TestCall", "param": [{}]}
    )
    assert result == {"success": "ok"}
    mock_response.json.assert_called_once()

def test_post_request_429_retry(omie_base, mocker):
    mock_response = Mock()
    mock_response.status_code = 429
    mocker.patch("requests.post", return_value=mock_response)
    mocker.patch("time.sleep")  # Mock sleep para evitar espera real

    with pytest.raises(Exception, match="Limite ecedido! erro 429."):
        omie_base._post_request(
            url="https://app.omie.com.br/api/v1/test/",
            json={"call": "TestCall", "param": [{}]}
        )

def test_post_request_425_retry(omie_base, mocker):
    mock_response_425 = Mock(status_code=425, content=b"Tente novamente em 5 segundos")
    mock_response_success = Mock(status_code=200, json=Mock(return_value={"success": "ok"}))
    mocker.patch("requests.post", side_effect=[mock_response_425, mock_response_success])
    mocker.patch("time.sleep")  # Mock sleep para evitar espera real

    result = omie_base._post_request(
        url="https://app.omie.com.br/api/v1/test/",
        json={"call": "TestCall", "param": [{}]}
    )
    assert result == {"success": "ok"}

def test_post_request_json_decode_error(omie_base, mocker):
    mock_response = Mock(status_code=200)
    mock_response.json.side_effect = json.decoder.JSONDecodeError("Invalid JSON", "", 0)
    mocker.patch("requests.post", return_value=mock_response)

    result = omie_base._post_request(
        url="https://app.omie.com.br/api/v1/test/",
        json={"call": "TestCall", "param": [{}]}
    )
    assert "Error" in result
    assert result["Error"] == "JSON Decode Error"

def test_post_request_connection_error(omie_base, mocker):
    mock_response = Mock(status_code=200, json=Mock(return_value={"success": "ok"}))
    mocker.patch("requests.post", side_effect=[ConnectionError, mock_response])

    result = omie_base._post_request(
        url="https://app.omie.com.br/api/v1/test/",
        json={"call": "TestCall", "param": [{}]}
    )
    assert result == {"success": "ok"}

def test_conectar_api(omie_base, mocker):
    mock_response = Mock(status_code=200, json=Mock(return_value={"success": "ok"}))
    mocker.patch("requests.post", return_value=mock_response)

    result = omie_base.conectar_api(
        metodo="ListarContasCorrentes",
        endpoint="geral/contacorrente/",
        parametros={"pagina": 1, "registros_por_pagina": 100}
    )
    assert result == {"success": "ok"}

def test_gerar_log_success(omie_base, mocker):
    omie_base._log = True
    mock_response = Mock(status_code=200, headers={"Content-Type": "application/json"})
    mocker.patch("builtins.open", mocker.mock_open())
    
    omie_base._gerar_log(mock_response)
    open.assert_called_with("log.txt", "a")
    open().write.assert_called_with(
        "'status_code': 200, 'headers': {'Content-Type': 'application/json'}, 'Mensagem': 'Sucesso'\n"
    )

def test_gerar_log_error(omie_base, mocker):
    omie_base._log = True
    mock_response = Mock(status_code=400, headers={"Content-Type": "application/json"}, json=Mock(return_value={"error": "bad request"}))
    mocker.patch("builtins.open", mocker.mock_open())
    
    omie_base._gerar_log(mock_response)
    open.assert_called_with("log.txt", "a")
    open().write.assert_called_with(
        "'status_code': 400, 'headers': {'Content-Type': 'application/json'}, 'Mensagem': {'error': 'bad request'}\n"
    )
