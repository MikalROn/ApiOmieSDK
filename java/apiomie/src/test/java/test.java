import omie.Omie;
import omie.OmieApi;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.IOException;
import java.net.URISyntaxException;

public class test {

    public static void main(String[] args) throws URISyntaxException, IOException, InterruptedException {
        Omie app = OmieApi.gerarOmieHomologacao();
        JSONObject produtos = app.listarProdutos(
                new JSONArray().put(new JSONObject().put("pagina", 1))
        );
        System.out.println(produtos.toString());
    }
}
