package omie;


public class OmieApi {
    public static OmieObject gerarOmieObject(String appKey, String appSecret){
        return  new OmieObject(appKey, appSecret);
    }
    public static  OmieObject gerarOmieObjectHomologacao(){
        return  new OmieObject("38333295000", "fed2163e2e8dccb53ff914ce9e2f1258");
    }
    public static Omie gerarOmie(String appKey, String appSecret){
        return new Omie(appKey, appSecret);
    }

    public static Omie gerarOmieHomologacao(){
        return new Omie("38333295000", "fed2163e2e8dccb53ff914ce9e2f1258");
    }
}