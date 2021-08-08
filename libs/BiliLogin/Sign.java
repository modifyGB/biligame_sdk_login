// package BiliLogin;

import java.nio.charset.Charset;
import java.security.KeyFactory;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.PublicKey;
import java.security.spec.X509EncodedKeySpec;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Map;

import javax.crypto.Cipher;

public class Sign {

    private static final char[] chartist = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
    private static String appkey = "8783abfb533544c59e598cddc933d1bf"; //是常量？
    private static String public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDjb4V7EidX/ym28t2ybo0U6t0n\n6p4ej8VjqKHg100va6jkNbNTrLQqMCQCAYtXMXXp2Fwkk6WR+12N9zknLjf+C9sx\n/+l48mjUU8RqahiFD1XT/u2e0m2EN029OhCgkHx3Fc/KlFSIbak93EH/XlYis0w+\nXl69GV6klzgxW6d2xQIDAQAB"; //公钥

    // 获取sign
    public static String get_sign(Map<String, String> map) throws NoSuchAlgorithmException {
        return md5(map_format(map), appkey);
    }
    // com.bsgamesdk.android.api.e.a
    public static String map_format(Map<String, String> map) {
        String str;
        ArrayList arrayList = new ArrayList(map.keySet());
        Collections.sort(arrayList);
        String str2 = "";
        int i = 0;
        while (i < arrayList.size()) {
            String str3 = (String) arrayList.get(i);
            if (str3 == null || str3.equalsIgnoreCase("item_name")) {
                str = str2;
            } else if (str3.equalsIgnoreCase("item_desc")) {
                str = str2;
            } else {
                str = str2 + map.get(str3);
            }
            i++;
            str2 = str;
        }
        return str2;
    }

    public static final String md5(String str, String str2) throws NoSuchAlgorithmException {
        MessageDigest instance = MessageDigest.getInstance("MD5");
        instance.update((str + str2).getBytes(Charset.defaultCharset()));
        return format(instance.digest());
    }

    public static String format(byte[] bArr) {
        StringBuilder sb = new StringBuilder(bArr.length * 2);
        for (int i = 0; i < bArr.length; i++) {
            sb.append(chartist[(bArr[i] & 240) >>> 4]);
            sb.append(chartist[bArr[i] & 15]);
        }
        return sb.toString();
    }
    // 获取pwd
    public static String get_pwd(String hash_passwd) throws NoSuchAlgorithmException, Exception {
        return rsa(hash_passwd, public_key);
    }

    public static String rsa(String str, String str2) throws NoSuchAlgorithmException, Exception {
        PublicKey b = rea_format2("RSA", str2);
        Cipher instance = Cipher.getInstance("RSA/ECB/PKCS1Padding");
        instance.init(1, b);
        return new String(Format.a(instance.doFinal(str.getBytes("UTF-8"))));
    }

    public static PublicKey rea_format2(String str, String str2) throws NoSuchAlgorithmException, Exception {
        return KeyFactory.getInstance(str).generatePublic(new X509EncodedKeySpec(Format.a(str2)));
    }
}



