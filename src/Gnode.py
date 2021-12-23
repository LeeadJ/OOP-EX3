import random


class Gnode:
    def __init__(self, key, location: tuple = None):
        self.key = key
        if location is None:
            x = random.uniform(35, 36)
            y = random.uniform(32, 33)
            location = (x, y, 0)
            self.location = location
        else:
            self.location = location
        self.tag = 0

    def __repr__(self):
        return 'Key: %s, location: %s' % (self.key, self.location)
