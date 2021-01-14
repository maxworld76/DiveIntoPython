import socket
import time


class ClientError(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self._sock = socket.create_connection((self.host, self.port), self.timeout)
        if self.timeout is not None:
            self._sock.settimeout(self.timeout)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, '_sock'):
            self._sock.close()

    def close(self):
        try:
            self._sock.close()
        except socket.error as ex:
            print(f"failed to close socket: {ex}")

    @staticmethod
    def parse_data_row(row):
        field_list = row.split(" ")
        if len(field_list) != 3:
            raise ClientError(f"server returned invalid data row: {field_list}")
        name, value, timestamp = field_list
        # validate name
        # sep_ind = str(name).rfind('.')  # valid value of name must be host.metric_name
        # if sep_ind < 0 or sep_ind == 0 or sep_ind == len(name)-1:
        #    raise ClientError(f"invalid value of metric name in row: {field_list}")
        # validate value
        try:
            value = float(value)
        except ValueError:
            raise ClientError(f"invalid metric value in row: {field_list}")
        # validate timestamp
        if str(timestamp).isnumeric():
            timestamp = int(timestamp)
        else:
            raise ClientError(f"invalid timestamp value in row: {field_list}")
        return name, value, timestamp

    def exec_command(self, cmd, buffer_size=1024):
        try:
            self._sock.sendall(cmd.encode("utf-8"))
            resp = self._sock.recv(buffer_size)
            try:
                resp = resp.decode("utf-8")
            except UnicodeDecodeError:
                raise ClientError('failed to decode server message from byte string')
            if not resp.endswith('\n\n'):
                raise ClientError('invalid client response, must end with\\n\\n')
            resp_list = resp[:-2].split("\n")
            if len(resp_list) >= 1 and resp_list[0] == "ok":
                resp_data = {}
                for d in resp_list[1:]:
                    metric, value, timestamp = self.parse_data_row(d)
                    if metric not in resp_data:
                        resp_data[metric] = [(timestamp, value)]
                    else:
                        resp_data[metric].append((timestamp, value))
                    for d1 in resp_data.values():
                        d1.sort(key=lambda tup: tup[0])
                return resp_data
            elif len(resp_list) == 2 and resp_list[0] == 'error':
                raise ClientError(f"server response: {resp_list[0]} - {resp_list[1]}")
            else:
                raise ClientError(f"unrecognized server response")
        except socket.timeout:
            raise ClientError("Timeout reading from client")
        except UnicodeDecodeError:
            raise ClientError("Failed to decode received message")

    def put(self, metric, value, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time())
        try:
            self.exec_command(f"put {metric} {value} {timestamp}\n")
        except TimeoutError:
            raise ClientError("Timeout reading from client")
        except UnicodeDecodeError:
            raise ClientError("Failed to decode received message")

    def get(self, metric: str):
        try:
            return self.exec_command(f"get {metric}\n")
        except TimeoutError:
            raise ClientError("Timeout reading from client")
        except UnicodeDecodeError:
            raise ClientError("Failed to decode received message")


if __name__ == '__main__':
    with Client('127.0.0.1', 10001, 5) as client:
        print(client.get('localhost.cpu'))
        print(client.put('localhost.cpu', 10))
        print(client.get('localhost.cpu'))
        print(client.put('localhost.cpu', 20))
        print(client.get('localhost.cpu'))
