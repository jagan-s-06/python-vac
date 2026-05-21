import socket
s=socket.socket()
s.settimeout(5)
status=s.connect_ex(("127.0.0.1",8080))
if status==0:
    print("port 8080 is open")
else:
    print("port 8080 is closed")
    print(f"error code:{status}")
    if status==10061:
        print("Reason: connection refused")
    elif status==10060:
        print("Reason: connection timed out")
    elif status==10035:
        print("Reason: operation would block")
    else:
        print("Reason: unknown")
