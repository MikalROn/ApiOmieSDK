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
    private String appSecreet;
    private HttpClient client;

    /**
     * Constructor to initialize the OmieObject with appKey and appSecret.
     * 
     * @param appKey The application key for Omie API authentication.
     * @param appSecret The application secret for Omie API authentication.
     */

    public OmieObject(String appKey, String appSecreet){
        this.url = "https://app.omie.com.br/api/v1/";
        this.client = HttpClient.newHttpClient();
        this.appKey = appKey;
        this.appSecreet = appSecreet;
    }
    /**
     * Sends a request to the Omie API and returns a JSON response.
     * 
     * @param endpoint The API endpoint to connect to.
     * @param call The method being called in the Omie API.
     * @param parametros The parameters for the API call in a JSONArray format.
     * @return A JSONObject with the API response.
     * @throws URISyntaxException If the URI syntax is invalid.
     * @throws IOException If an I/O error occurs during the request.
     * @throws InterruptedException If the request is interrupted.
     */

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

    /**
     * A public method that allows API requests with the specified endpoint, call, and parameters.
     * 
     * @param endpoint The API endpoint to connect to.
     * @param call The method being called in the Omie API.
     * @param parametros The parameters for the API call in a JSONArray format.
     * @return A JSONObject with the API response.
     * @throws URISyntaxException If the URI syntax is invalid.
     * @throws IOException If an I/O error occurs during the request.
     * @throws InterruptedException If the request is interrupted.
     */

    public JSONObject concatarApi(String endpoint, String call, JSONArray parametros) throws URISyntaxException, IOException, InterruptedException{
        return this.chamarApi(
                endpoint,
                call,
                parametros
        );
    }

    /**
     * Generates a JSON string for the API request body.
     * 
     * @param call The method being called in the Omie API.
     * @param parametros The parameters for the API call in a JSONArray format.
     * @return A string containing the JSON request body.
     */

    private String gerarJson(String call, JSONArray parametros) {
        return new JSONObject()
                .put("call",  call)
                .put("app_key",  this.appKey)
                .put("app_secret", this.appSecreet)
                .put("param", parametros)
                .toString();
    }
}


