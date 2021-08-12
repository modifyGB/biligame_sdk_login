import urllib.parse
import copy
import requests
import json
import jpype

header = {
    "User-Agent": "Mozilla/5.0 BSGameSDK",
    # "Content-Length": "756",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "line1-sdk-center-login-sh.biligame.net",
    "Connection": "Keep-Alive",
}
form_v1 = {
    "merchant_id": "328",
    "timestamp": "1628780911000",
    "version": "1",
    "server_id": "1178",
    "game_id": "952",

    # "sign": "dcfc2709d88f0c9dff2eb3bfed114340", # 签名
    # "pwd": "", # 加密密码
    # "user_id": "" # 账号
}
form_v3 = {
    "merchant_id": "328",
    "timestamp": "1628330079265",
    "version": "3",
    "server_id": "1178",
    "game_id": "952",
    "cipher_type": "bili_login_rsa",
}
url_rsa_v1 = "https://line1-sdk-center-login-sh.biligame.net/api/client/rsa"
url_rsa_v3 = "https://line1-sdk-center-login-sh.biligame.net/api/external/issue/cipher/v3"
url_login_v1 = "https://line1-sdk-center-login-sh.biligame.net/api/client/login"
url_login_v3 = "https://line1-sdk-center-login-sh.biligame.net/api/external/login/v3"


def format_form(form):
    return "&".join(["{}={}".format(i, urllib.parse.quote(str(form[i]))) for i in form.keys()])

def login(name, password, version):
    jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=./libs/BiliLogin.jar")
    mainClass = jpype.JClass("Main")

    if version == 1:
        form = format_form(form_v1)
        form += "&sign={}".format(mainClass.sign(form))
        json_rsa = json.loads(requests.post(url_rsa_v1,headers=header, data=form).text)

        form = copy.deepcopy(form_v1)
        form['user_id'] = name
        form['pwd'] = mainClass.pwd(json_rsa['hash'] + password)
        form = format_form(form)
        form += "&sign={}".format(mainClass.sign(form))
        return json.loads(requests.post(url_login_v1, headers=header, data=form).text)
        
    elif version == 3:
        form = format_form(form_v3)
        form += "&sign={}".format(mainClass.sign(form))
        json_rsa = json.loads(requests.post(url_rsa_v3,headers=header, data=form).text)

        form = copy.deepcopy(form_v3)
        form['user_id'] = name
        form['pwd'] = mainClass.pwd(json_rsa['hash'] + password)
        form = format_form(form)
        form += "&sign={}".format(mainClass.sign(form))
        return json.loads(requests.post(url_login_v3, headers=header, data=form).text)
