<?php

class OmieBase {
    private $appKey;
    private $appSecret;
    private $url;
   
    public function __construct(string $app_key, string $app_secret){
        $this->appKey = $app_key;
        $this->appSecret = $app_secret;
        $this->url = "https://app.omie.com.br/api/v1/";
    }
    
    private function gerarJson(string $call, array $params): string {
        // Gera json da requisição
        return json_encode(
            [
                "call" => $call,
                "app_key" => $this->appKey,
                "app_secret" => $this->appSecret,
                "params" => $params
            ]
        );
    }

    protected function chamarApi(string $endpoint, string $call, array $params): array{
        $urlCompleta = $this->url + $endpoint;
        $session = curl_init($urlCompleta);

        curl_setopt($session, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
        curl_setopt($session, CURLOPT_POST, true);
        curl_setopt($session, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($session, CURLOPT_POSTFIELDS, $this->gerarJson($call, $params));
        return json_decode(curl_exec($session));
    }
}
