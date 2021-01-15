import asyncio

storage = {}

class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        super().__init__()
        self.in_buffer = ''

    def connection_made(self, transport):
        self.transport = transport
        print(f"accepted new connection")

    def connection_lost(self, exc):
        print("connection closed")

    @staticmethod
    def get_error_message():
        return "error\nwrong command\n\n"

    def data_received(self, data):
        try:
            resp = self.process_data(data.decode())
        except UnicodeDecodeError:
            resp = self.get_error_message()
        if resp:
            self.transport.write(resp.encode())
        print(f"storage: {storage}")

    def get(self, metric):
        print(f"get: {metric}")
        out_list = []
        if metric == "*":
            for metric in storage:
                for timestamp in storage[metric]:
                    row = (metric, str(storage[metric][timestamp]), str(timestamp))
                    out_list.append(" ".join(row))
            return "ok\n" + "\n".join(out_list) + "\n\n"
        else:
            if metric in storage:
                for timestamp in storage[metric]:
                    row = (metric, str(storage[metric][timestamp]), str(timestamp))
                    out_list.append(" ".join(row))
                return "ok\n" + "\n".join(out_list) + "\n\n"
            else:
                return "ok\n\n"

    def put(self, name, value, timestamp):
        try:
            value = float(value)
            timestamp = int(timestamp)
        except ValueError:
            return self.get_error_message()
        if timestamp < 0:
            return self.get_error_message()
        if name in storage:
            storage[name][timestamp] = value
        else:
            storage[name] = {timestamp: value}
        return "ok\n\n"

    def process_data(self, req):
        if not req.endswith('\n'):
            self.in_buffer += req
        else:
            req = self.in_buffer + req
            self.in_buffer = ''
            print(f'received: {req}')
            params = req.strip().split(" ")
            if len(params) == 2 and params[0] == 'get':
                return self.get(params[1])
            elif len(params) == 4 and params[0] == 'put':
                return self.put(params[1], params[2], params[3])
            else:
                return self.get_error_message()


def run_server(host, port):
    print(f'starting server on {host}:{port}')
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    print('waiting for connections to close')
    loop.run_until_complete(server.wait_closed())
    loop.close()
    print('program exit')


if __name__ == '__main__':
    run_server('127.0.0.1', 8181)

