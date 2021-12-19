class Gnode:
    def __init__(self, key, location):
        self.key = key
        self.location = location

    def __repr__(self):
        return 'Key: %s, location: %s' % (self.key, self.location)
