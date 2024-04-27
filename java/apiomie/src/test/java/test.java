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
                new JSONArray().put(new JSONObject()
                        .put("pagina", 1)
                        .put("registros_por_pagina", 50)
                        .put("filtrar_apenas_omiepdv", "N")
                )
        );
        System.out.println(produtos.toString());
    }
}
