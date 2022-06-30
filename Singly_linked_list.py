"""Односвязный список, когда один объект ссылается на следующий и так по цепочке до последнего с возможностью
удаления и возвращения последнего объекта"""


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            last_obj = self.top
            while last_obj.next:
                last_obj = last_obj.next
            last_obj.next = obj

    def pop(self):
        if self.top is None:
            return None
        if self.top.next is None:
            returned_obj = self.top
            self.top = None
            return returned_obj

        penultimate_obj = self.top
        last_obj = self.top.next
        while last_obj.next:
            penultimate_obj = last_obj
            last_obj = last_obj.next
        penultimate_obj.next = None
        return last_obj

    def get_data(self):
        if self.top is None:
            return []
        list_data = []
        next_obj = self.top
        while next_obj:
            list_data.append(next_obj.data)
            next_obj = next_obj.next
        return list_data


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_obj):
        if self.check_link(next_obj):
            self.__next = next_obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @staticmethod
    def check_link(link_obj):
        return type(link_obj) is StackObj or link_obj is None
