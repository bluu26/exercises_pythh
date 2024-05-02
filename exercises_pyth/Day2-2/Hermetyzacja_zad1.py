class Square:

    def __init__(self, side):
        self._side = side
        self._calc_all()
    def _calc_all(self):
        self._set_area()
        self._set_perimeter()
        self._set_diagonal()
    def _set_perimeter(self):
        self._perimeter = 4 * self._side

    def _set_area(self):
        self._area = self._side ** 2

    def _set_diagonal(self):
        self._diagonal = self._side * 2 ** 0.5


    def set_perimeter(self, perimeter):
        self._side = perimeter/4
        self._calc_all()

    def set_area(self, area):
        self._side = area**0.5
        self._calc_all()

    def set_diagonal(self, diagonal):
        self._side = diagonal / 2**0.5
        self._calc_all()