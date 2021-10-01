"""
Заданы координаты слона, стоящего на клетке шахматной доски (номер строки и номер столбца).
Напишите цикл (или циклы) для вывода координат всех клеток, находящихся под ударом.
Слон ходит на любое число полей по диагонали.
"""
from typing import Final

MIN_SIZE: Final = 1
MAX_SIZE: Final = 8


def bishop_moves(x, y):
    """
    Print all bishop's attack positions

    :param x: x-pos
    :param y: y-pos
    :return: none
    """
    for dt in range(MIN_SIZE, MAX_SIZE):
        for pos_x, pos_y in [(x+dt, y+dt), (x-dt, y+dt), (x+dt, y-dt), (x-dt, y-dt)]:
            if MIN_SIZE <= pos_x <= MAX_SIZE:
                if MIN_SIZE <= pos_y <= MAX_SIZE:
                    print('({0}, {1})'.format(pos_x, pos_y))


if __name__ == '__main__':
    bishop_moves(4, 5)
