import os
import urllib.parse
import copy
import re
import requests
import json

header = {
    "User-Agent": "Mozilla/5.0 BSGameSDK",
    # "Content-Length": "756",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "line1-sdk-center-login-sh.biligame.net",
    "Connection": "Keep-Alive",
}
form1 = {
    "merchant_id": "328",
    "timestamp": "1628330079265",
    "version": "1",
    "server_id": "1178",
    "game_id": "952",

    # "sign": "dcfc2709d88f0c9dff2eb3bfed114340", # 签名
    # "pwd": "", # 加密密码
    # "user_id": "" # 账号

    # "operators": "1",
    # "isRoot": "1",
    # "domain_switch_count": "0",
    # "sdk_type": "1",
    # "sdk_log_type": "1",
    # "support_abis": "x86,armeabi-v7a,armeabi",
    # "access_key": "",
    # "sdk_ver": "3.10.4",
    # "oaid": "",
    # "dp": "",
    # "original_domain": "",
    # "imei": "540000000140886",
    # "udid": "KREhESMUdUV0RyIXaxdrEWlYPws5WipAJA==",
    # "apk_sign": "4502a02a00395dec05a4134ad593224d",
    # "platform_type": "3",
    # "old_buvid": "XZ7F9B979B64C22B1F124F89C659252A8A09B",
    # "android_id": "dc428b9ba0b6b4d1",
    # "fingerprint": "",
    # "mac": "08:00:27:A0:13:E5",
    # "domain": "line1-sdk-center-login-sh.biligame.net",
    # "app_id": "952",
    # "version_code": "29",
    # "net": "4",
    # "pf_ver": "6.0.1",
    # "cur_buvid": "XZ7F9B979B64C22B1F124F89C659252A8A09B",
    # "c": "1",
    # "brand": "HUAWEI",
    # "client_timestamp": "1628330078528",
    # "channel_id": "1",
    # "uid": "",
    # "ver": "1.5.60",
    # "model": "ALP-AL00",
}
form3 = {
    "merchant_id": "328",
    "timestamp": "1628330079265",
    "version": "3",
    "server_id": "1178",
    "game_id": "952",
    "cipher_type": "bili_login_rsa",
}
url_rsa1 = "https://line1-sdk-center-login-sh.biligame.net/api/client/rsa"
url_rsa3 = "https://line1-sdk-center-login-sh.biligame.net/api/external/issue/cipher/v3"
url_login1 = "https://line1-sdk-center-login-sh.biligame.net/api/client/login"
url_login3 = "https://line1-sdk-center-login-sh.biligame.net/api/external/login/v3"

user_id = ""
password = ""

def get_rsa_form(form_):
    form2 = format_form(form_)
    sign = os.popen("java -jar libs/BiliLogin.jar \"{}\"".format(form2)).read().replace('\n','')
    return form2 + "&sign={}".format(sign)

def get_login_form(form_, passwd):
    form2 = format_form(form_)
    js = os.popen("java -jar libs/BiliLogin.jar \"{}\" \"{}\"".format(form2, passwd)).read()
    sign = re.findall(r"sign=(\S+?),", js)[0]
    pwd = re.findall(r"pwd=(\S+?)}", js)[0]
    return form2 + "&sign={}&pwd={}".format(sign, pwd)

def format_form(form_):
    return "&".join(["{}={}".format(i, urllib.parse.quote(form_[i])) for i in form_.keys()])

def main():
    js = json.loads(requests.post(url_rsa1,headers=header, data=get_rsa_form(form1)).text)
    form_ = copy.deepcopy(form1)
    form_['user_id'] = user_id
    print(requests.post(url_login1,headers=header, data=get_login_form(form_, js['hash'] + password)).text)

if __name__ == "__main__":
    main()