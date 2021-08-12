from login import *

user_id = "" # 用户名
password = "" # 密码
version = 1 # api接口版本


if __name__ == "__main__":
    js = login(user_id, password, 1)
    if 'access_key' in js:
        print("登录成功，access_key: " + js['access_key'])
    else:
        print("登录失败，message: " + js['message'])