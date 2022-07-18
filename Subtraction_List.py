class NewList:
    def __init__(self, lst=None):
        if lst is None:
            lst = []
        self.lst = lst

    def get_list(self):
        return self.lst

    def __sub__(self, other):
        other = self.check_type(other)
        return NewList(self.calculating(self.lst, other))

    def __rsub__(self, other):
        return NewList(other) - self.lst

    @staticmethod
    def check_type(check_lst):
        return check_lst.lst.copy() if type(check_lst) == NewList else check_lst.copy()

    @staticmethod
    def calculating(min, subtr):
        diff = []
        for i in min:
            for j in subtr:
                if str(i) == str(j):
                    subtr.remove(j)
                    break
            else:
                diff.append(i)
        return diff
