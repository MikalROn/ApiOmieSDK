package omie;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

/**
 * The OmieObject class handles API communication with the Omie API.
 * It uses HttpClient to send HTTP requests and parse responses in JSON format.
 */

public  class OmieObject {

    private String url;
    private String appKey;
    private String appSecret;
    private HttpClient client;

    public OmieObject(String appKey, String appSecreet){
        this.url = "https://app.omie.com.br/api/v1/";
        this.client = HttpClient.newHttpClient();
        this.appKey = appKey;
        this.appSecret = appSecreet;
    }

    protected JSONObject chamarApi(String endpoint, String call, JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        // Conecta com api e devolve um JSON
        String jsonEmString = gerarJson(call, parametros);
        HttpRequest request = HttpRequest.newBuilder()
                .uri(new URI(this.url + endpoint))
                .header("Content-type", "application/json")
                .POST(HttpRequest
                        .BodyPublishers
                        .ofString(jsonEmString)
                )
                .build();
        HttpResponse<String> response =  this.client.send(request,
                        HttpResponse.BodyHandlers.ofString());
        return new JSONObject(response.body());
    }


    public JSONObject concatarApi(String endpoint, String call, JSONArray parametros) throws URISyntaxException, IOException, InterruptedException{
        return this.chamarApi(
                endpoint,
                call,
                parametros
        );
    }

    private String gerarJson(String call, JSONArray parametros) {
        return new JSONObject()
                .put("call",  call)
                .put("app_key",  this.appKey)
                .put("app_secret", this.appSecret)
                .put("param", parametros)
                .toString();
    }
}


