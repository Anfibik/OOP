"""Двусвязный список с возможностью удаления объекта по индексу"""


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len_lst = 0  # фиксируем длину списка текущего объекта

    def add_obj(self, obj):
        if self.tail is None:  # первый объект голова и хвост одновременно
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj  # добавление в конец списка
            obj.prev = self.tail
            self.tail = obj
        self.len_lst += 1  # увеличение длины списка

    def find_obj_by_index(self, indx):  # метод нахождения объекта по индексу
        if self.head is not None:
            flag = 0
            this_obj = self.head
            while this_obj.next is not None and indx > flag:
                flag += 1
                this_obj = this_obj.next
            return this_obj

    def remove_obj(self, indx):
        remove_obj = self.find_obj_by_index(indx)
        if remove_obj == self.tail:  # удаление последнего
            self.tail = remove_obj.prev
            self.tail.next = None
        elif remove_obj == self.head:  # удаление первого
            self.head = remove_obj.next
            self.head.prev = None
        else:  # удаление между двумя
            remove_obj.prev.next = remove_obj.next
            remove_obj.next.prev = remove_obj.prev
        self.len_lst -= 1  # уменьшение длины

    def __len__(self):
        return self.len_lst

    def __call__(self, indx, *args, **kwargs):
        return self.find_obj_by_index(indx).get_data()


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    def get_data(self):
        return self.__data





