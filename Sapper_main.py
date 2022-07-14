from random import randint


class Cell:
    """Init cell in the field"""
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    """Init game field"""
    def __init__(self, N, M):
        self._m = M
        self._n = N
        self.pole = [[Cell() for i in range(N)] for i in range(N)]
        self.init()

    def init(self):
        """Init mines on the field"""
        m = 0
        while m < self._m:
            i = randint(0, self._n - 1)
            j = randint(0, self._n - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1

        # init amount mine around the cell
        check_index = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for i in range(self._n):
            for j in range(self._n):
                if not self.pole[i][j].mine:
                    mines = sum((self.pole[i+x][j+y].mine for x, y in check_index if 0 <= i+x < self._n and 0 <= j+y < self._n))
                    self.pole[i][j].around_mines = mines

    def show(self):
        for row in self.pole:
            for cell in row:
                if cell.fl_open:
                    if cell.mine:
                        print('*', end=' ')
                    else:
                        print(cell.around_mines, end=' ')
                else:
                    print('#', end=' ')
            print()

pole_game = GamePole(10, 12)
pole_game.show()



