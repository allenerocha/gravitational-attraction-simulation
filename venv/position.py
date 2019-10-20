class position:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def get_position(self):
        return self.x, self.y, self.z

    def set_position(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return 'x={}, y={}, z={}'.format(self.x, self.y, self.z)
