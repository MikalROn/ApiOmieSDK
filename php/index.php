<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Omie Api</title>
</head>
<body>

<table>
    <thead>
        <tr>
            <th>id</th>
            <th>nome</th>
            <th>valor</th>
        </tr>
    </thead>
    <tbody>
        <?php
        include("omie.php");

        $loja = new Omie("38333295000", "fed2163e2e8dccb53ff914ce9e2f1258");

        $r = $loja->listarProdutos([
            "pagina"=> 1,
            "registros_por_pagina"=> 50,
            "apenas_importado_api"=> "N",
            "filtrar_apenas_omiepdv"=> "N"

        ])["produto_servico_cadastro"];
        foreach($r as $produto) {
            echo "<tr>";
                echo "<td>".$produto["codigo_produto"]."</td>";
                echo "<td>".$produto["descricao"]."</td>";
                echo "<td>".$produto["valor_unitario"]."</td>";
            echo "</tr>";
        }
        ?>
    </tbody>
</table>

</body>
</html>