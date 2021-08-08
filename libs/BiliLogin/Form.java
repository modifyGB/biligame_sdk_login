// package BiliLogin;

import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.net.URLDecoder;

public class Form {

    public static void main(String[] args) throws Exception {
        if(args.length > 1){
            System.out.println(get_login(args[0], args[1]));
        }
        else if(args.length == 1){
            System.out.println(get_rsa(args[0]));
        }
    }

    public static String get_rsa(String form) throws NoSuchAlgorithmException, UnsupportedEncodingException{
        HashMap<String, String> hashMap = new HashMap<String, String>();
        for(String kv : form.split("&")){
            String[] kv_ = kv.split("=");
            if(kv_.length > 1){
                hashMap.put(kv_[0], URLDecoder.decode(kv_[1], "UTF-8"));
            }
            else{
                hashMap.put(kv_[0], "");
            }
        }
        return URLEncoder.encode(Sign.get_sign(hashMap), "UTF-8");
    }

    public static HashMap<String, String> get_login(String form, String hash_passwd) throws Exception{
        HashMap<String, String> hashMap = new HashMap<String, String>();
        for(String kv : form.split("&")){
            String[] kv_ = kv.split("=");
            if(kv_.length > 1){
                hashMap.put(kv_[0], URLDecoder.decode(kv_[1], "UTF-8"));
            }
            else{
                hashMap.put(kv_[0], "");
            }
        }
        hashMap.put("pwd", Sign.get_pwd(hash_passwd));
        HashMap<String, String> hashMap2 = new HashMap<String, String>();
        hashMap2.put("pwd", URLEncoder.encode(hashMap.get("pwd"), "UTF-8"));
        hashMap2.put("sign", URLEncoder.encode(Sign.get_sign(hashMap), "UTF-8"));
        return hashMap2;
    }

}
