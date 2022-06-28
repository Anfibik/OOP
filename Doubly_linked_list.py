class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if self.head is None:
            self.head = obj

    def remove_obj(self):
        if self.tail is None:
            raise "Стек пустой"
        if self.tail.get_prev():
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        else:
            self.tail = None
            self.head = None

    def get_data(self):
        res = []
        flag = self.head
        while flag:
            res.append(flag.get_data())
            flag = flag.get_next()
        return res


class ObjList:

    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data

