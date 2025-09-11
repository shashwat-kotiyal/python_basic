import socket
import requests

def scan_ports(ip,ports):
    for port in ports:
        try:
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(1)
            result =sock.connect_ex((ip,port))
            if result==0:
                print(f"port:{port} is open")
            sock.close()
        except Exception as e:
            print(f"Error:{e}")


def sql_injestion(url,param):
    payloads= ["'OR '1'='1","'OR 'a'='a","';--"]
    #SELECT * FROM users WHERE username = '' OR 1=1 --'   return all users
    for payload in payloads:
        full_url=f"{url}?{param}=payload"
        response=requests.get(full_url)

        if "syntax error" in response.text.lower() or "mysql" in response.text.lower():
            print(f"Possible SQL Injection vulnerability with payload: {payload}")
        else:
            print(f"No obvious vulnerability with payload: {payload}")


def brute_force(url):
    uname= 'admin'
    passwords =['admin','admin123','Admin@123']
    for password in passwords:
        response= requests.post(url,data={"username" : uname,"password": password})

            if "Login failed" not in response.text or response.status_code==200:
                print(f"success password is {password}")
            else:
                print(f"failed password: {password}")

def analysis_header():
    try:
        url = "https://www.programiz.com/python-programming/online-compiler/"
        response = requests.get(url)
        print(dir(response))
        for header, value in response.headers.items():
            print(f"{header}:{value}")

        # Content-Security-Policy  : default-src 'self'   -> prevent cross site scripting
        # X-Frame-Options : DENY: Don't allow framing or SAMEORIGIN: Only allow framing from the same origin. -> prvent iframe
        # Strict-Transport-Security   ->Prevents downgrade attacks and cookie hijacking over HTTP.
        # X-Content-Type-Options  -> Stops browsers from interpreting files as a different content type (e.g., treating a text file as HTML).
        # Access-Control-Allow-Origin

    except requests.RequestException as e:
        print(f"Expection: {e}")



if __name__ =='__main__':
    # target_ip = "192.168.1.1"
    # port_list = [21, 22, 23, 80, 443]
    # scan_ports(target_ip, port_list)
    #sql_injestion("http://example.com/login", "user")
    #How can you use Python to analyze the response headers of a website?
    analysis_header()




