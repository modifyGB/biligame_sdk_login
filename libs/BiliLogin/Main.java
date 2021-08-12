import java.net.URLEncoder;

public class Main {

    // 获取sign
    public static String sign(String form) throws Exception{
        return URLEncoder.encode(Sign.get_sign(Sign.get_map(form)), "UTF-8");
    }

    // 获取pwd
    public static String pwd(String hash_passwd) throws Exception{
        return Sign.get_pwd(hash_passwd);
    }

}
