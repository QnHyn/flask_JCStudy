import hashlib

import requests
import time


def send_code():
    url = "https://api.netease.im/sms/sendcode.action"

    nonce = hashlib.new("sha512", str(time.time()).encode("utf-8")).hexdigest()

    curtime = str(int(time.time()))

    sha1 = hashlib.sha1()

    secret = "f2f839131b19"

    sha1.update((secret + nonce + curtime).encode("utf-8"))

    check_sum = sha1.hexdigest()

    header = {
        "AppKey": "70e20855fccfff9c86d0353a5e08b996",
        "Nonce": nonce,
        "CurTime": curtime,
        "CheckSum": check_sum
    }

    post_data = {
        "mobile": "15735183437"
    }

    resp = requests.post(url, data=post_data, headers=header)

    print(resp.content)


if __name__ == '__main__':
    send_code()
