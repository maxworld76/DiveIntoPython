import socket
import time
with socket.socket() as sock:
    sock.bind(("127.0.0.1", 10001))
    sock.listen()
    while True:
        print(f"accepting connections {sock}")
        conn, addr = sock.accept()
        conn.settimeout(60) # timeout := None|0|gt 0
        print(f"connection established: {addr}")
        with conn:
            while True:
                try:
                    data = conn.recv(1024)
                except socket.timeout:
                    print("close connection by timeout")
                    break
                if not data:
                    print("client disconnected")
                    break
                data = data.decode("utf8")
                print(data)
                if data.startswith('put'):
                    conn.sendall("ok\n\n".encode("utf-8"))
                else:
                    conn.sendall(f"""ok

""".encode("utf-8"))


