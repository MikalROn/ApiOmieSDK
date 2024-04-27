package omie;


public class OmieApi {

    public static OmieObject gerarOmieObject(String appKey, String appSecret){
        return  new OmieObject(appKey, appSecret);
    }
    public static  OmieObject gerarOmieObjectHomologacao(){
        return  new OmieObject("1560731700", "226dcf372489bb45ceede61bfd98f0f1");
    }
    public static Omie gerarOmie(String appKey, String appSecret){
        return new Omie(appKey, appSecret);
    }

    public static Omie gerarOmieHomologacao(){
        return new Omie("1560731700", "226dcf372489bb45ceede61bfd98f0f1");
    }
}