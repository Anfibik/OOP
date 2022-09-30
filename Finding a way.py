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

    @staticmethod
    def check_link(link1, link2):
        return link1.v1 in (link2.v1, link2.v2) and link1.v2 in (link2.v1, link2.v2)

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        for check_link in self._links:
            if self.check_link(link, check_link):
                return
        self._links.append(link)
        self.add_vertex(link.v1)
        self.add_vertex(link.v2)

    def find_path(self, start_v, stop_v):
        self.start_v = start_v
        self.stop_v = stop_v
        return

    def _next_node(self, current_start, this_path):
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


# -----------------------------------------------------------------------
map_metro = LinkedGraph()
v1 = Station("Оболонь")
v2 = Station("Демеевка")
v3 = Station("ВДНХ")
v4 = Station("Харьковская")


map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 2))
map_metro.add_link(LinkMetro(v1, v4, 3))
map_metro.add_link(LinkMetro(v2, v4, 4))

print(len(map_metro._links))
print(len(map_metro._vertex))


path = map_metro.find_path(v1, v3)  # от сретенского бульвара до китай-город 1
# print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
# print(sum([x.dist for x in path[1]]))  # 7

print()