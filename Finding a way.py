class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1
        v1.links.append(self)
        v2.links.append(self)

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        for check_link in self._links:
            if link.v1 in (check_link.v1, check_link.v2) and link.v2 in (check_link.v1, check_link.v2):
                return
        self._links.append(link)
        self.add_vertex(link.v1)
        self.add_vertex(link.v2)

    def find_path(self, start_v, stop_v):
        pass


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist

