package omie;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public  class OmieObject {

    private String url;
    private String appKey;
    private String appSecreet;
    private HttpClient client;

    public OmieObject(String appKey, String appSecreet){
        this.url = "https://app.omie.com.br/api/v1/";
        this.client = HttpClient.newHttpClient();
        this.appKey = appKey;
        this.appSecreet = appSecreet;
    }

    protected JSONObject chamarApi(String endpoint, String call, JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        String jsonEmString = gerarJson(call, parametros);
        System.out.println(jsonEmString);
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
        System.out.println(response.body());
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
                .put("app_secret", this.appSecreet)
                .put("param", parametros)
                .toString();
    }
}


