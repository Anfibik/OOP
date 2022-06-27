from random import randint


class Cell:
    """Инициализация ячейки"""
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    """Создание поля с ячейками"""
    def __init__(self, N, M):
        self._m = M
        self._n = N
        self.pole = [[Cell() for i in range(N)] for i in range(N)]
        self.init()

    def init(self):
        """Заполняем поле"""
        #установка мин
        m = 0
        while m < self._m:
            i = randint(0, self._n - 1)
            j = randint(0, self._n - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1
        #генерируем цифровое значение мин вокруг ячейки
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._n):
                if not self.pole[x][y].mine:
                    mines = sum((self.pole[x + i][y + j].mine for i, j in indx if
                                 0 <= x + i < self._n and 0 <= y + j < self._n))
                    self.pole[x][y].around_mines = mines

    def show(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))


pole_game = GamePole(10, 12)
pole_game.show()

