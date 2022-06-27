class Router:
    def __init__(self):
        self.servers = {}
        self.buffer = []

    def link(self, server):
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server):
        self.servers.pop(server.ip)

    def send_data(self):
        for i in self.buffer:
            self.servers[i.ip].buffer.append(i)
        self.buffer.clear()


class Server:
    NUM_IP = 0

    def __init__(self):
        self.generate_ip()
        self.buffer = []
        self.router = None
        self.ip = self.NUM_IP

    @classmethod
    def generate_ip(cls):
        cls.NUM_IP += 1

    def send_data(self, data):
        self.router.buffer.append(data)

    def get_data(self):
        cache = [i for i in self.buffer]
        self.buffer.clear()
        return cache

    def get_ip(self):
        return self.ip


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
