from threading import Lock
from .exceptions import ImpossibleStepException
from typing import List, Union


class SingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Game(metaclass=SingletonMeta):

    def __init__(self):
        self._castle: List[List[Union[str, None]]] = [[None for _ in range(3)] for _ in range(3)]
        self.__initialize_castle()

        self._cur_row_ind = 2
        self._cur_col_ind = 0

    def __initialize_castle(self):
        self._castle[0][1] = 'Балкон'

        self._castle[1][0] = 'Спальня'
        self._castle[1][1] = 'Холл'
        self._castle[1][2] = 'Кухня'

        self._castle[2][0] = 'Подземелье'
        self._castle[2][1] = 'Коридор'
        self._castle[2][2] = 'Оружейная'

    def get_room(self):
        row, col = self.get_cur_coords()
        return self._castle[row][col]

    def get_cur_coords(self):
        return self._cur_row_ind, self._cur_col_ind

    def set_new_coords(self, row: int, col: int):
        self._cur_row_ind = row
        self._cur_col_ind = col

    def reinitialize(self):
        self.set_new_coords(row=2, col=0)

    def make_step(self, way: str, num_steps: int):
        row, col = self.get_cur_coords()
        if way == 'Север':
            row -= num_steps

        elif way == 'Юг':
            row += num_steps

        elif way == 'Восток':
            col += num_steps

        else:
            col -= num_steps

        self._check_validation(row, col)
        self.set_new_coords(row, col)

    def _check_validation(self, row: int, col: int):
        if not 0 <= row <= 2 or not 0 <= col <= 2 or self._castle[row][col] is None:
            raise ImpossibleStepException

    @property
    def is_win(self):
        row, col = self.get_cur_coords()
        return self._castle[row][col] == 'Балкон'
