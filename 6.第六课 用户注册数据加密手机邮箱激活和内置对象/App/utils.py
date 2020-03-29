import hashlib
import requests
import time


def send_verify_code(phone):
    url = "https://api.netease.im/sms/sendcode.action"
    # 生成一个随机数
    nonce = hashlib.new("sha512", str(time.time()).encode("utf-8")).hexdigest()
    # 设置当前时间
    curtime = str(int(time.time()))

    # 按照开发文档拼接参数
    sha1 = hashlib.sha1()
    secret = "b097df36ba01"
    sha1.update((secret + nonce + curtime).encode("utf-8"))
    # 拼接SHA1(AppSecret + Nonce + CurTime)，三个参数拼接的字符串，进行SHA1哈希计算，转化成16进制字符(String，小写)
    check_sum = sha1.hexdigest()

    header = {
        "AppKey": "36ee4992d9807c047da9423bf8a924c2",
        "Nonce": nonce,
        "CurTime": curtime,
        "CheckSum": check_sum
    }

    post_data = {
        "mobile": phone # 发送给的手机号
    }
    resp = requests.post(url, data=post_data, headers=header)
    return resp
