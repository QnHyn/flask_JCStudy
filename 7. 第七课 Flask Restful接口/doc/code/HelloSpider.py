import requests


def get_data():

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }

    resp = requests.get("http://127.0.0.1:9000/goods/?g_name=110", headers=headers)

    print(resp.json())


if __name__ == '__main__':
    get_data()