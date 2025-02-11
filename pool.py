"""docstring pool"""
import random
import math
import config

POOL_WIDTH = int(config.CONFIG['Pool']['Width'])
POOL_HEIGHT = int(config.CONFIG['Pool']['Height'])


class Pool:
    """DOCSTRING"""
    def __init__(self):
        self._width = POOL_WIDTH
        self._height = POOL_HEIGHT
        self.fishes = []

    def get_size(self):
        """DOCSTRING"""
        return self._width, self._height

    def fill(self, fish_type, number: int):
        """DOCSTRING"""
        self.fishes += [fish_type(
            random.randint(0, self._width - 1),
            random.randint(0, self._height - 1)
        ) for _ in range(number)]

    def __str__(self):
        some = '+' + '-' * self._width + '+\n'
        pakala = [[' '] * self._width for _ in range(self._height)]
        for fish in self.fishes:
            pakala[fish.get_pos()[0]][fish.get_pos()[1]] = repr(fish)
        for row in pakala:
            some += '|' + ''.join(row) + '|\n'
        some += '+' + '-' * self._width + '+\n'
        return some

    def tick(self):
        """DOCSTRING"""
        for fish in self.fishes:
            fish.move(self)
            fish.eat(self)

        for fish in self.fishes.copy():
            if not fish.is_alive():
                self.kill(fish)

        for fish in self.fishes.copy():
            fish.born(self)

    def get_nearest_victim(self, coordx, coordy):
        """DOCSTRING"""
        nearest_victims = [fish.get_pos() for fish in self.fishes
                           if fish.is_victim]
        if not nearest_victims:
            return (0, 0)
        return tuple(min(nearest_victims,
                         key=lambda f: math.hypot(f[0] - coordx,
                                                  f[1] - coordy)))

    def get_victim(self, pos):
        """DOCSTRING"""
        return [fish for fish in self.fishes
                if fish.get_pos() == pos and fish.is_victim]

    def kill(self, victim):
        """DOCSTRING"""
        self.fishes.remove(victim)
