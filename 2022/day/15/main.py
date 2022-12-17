def main():
    test()

TEST_SENSORS = [
    (2,18,-2,15),
    (9,16,10,16),
    (13,2,15,3),
    (12,14,10,16),
    (10,20,10,16),
    (14,17,10,16),
    (8,7,2,10),
    (2,0,2,10),
    (0,11,2,10),
    (20,14,25,17),
    (17,20,21,22),
    (16,7,15,3),
    (14,3,15,3),
    (20,1,15,3),
]


def test():
    beacon = Beacon(2,10)
    sensor = Sensor(8,7, beacon)

    coord1 = Coordinate(-1,7)
    coord2 = Coordinate(-2,7)

    assert(sensor.beacon_distance == 9)

    #in_range test
    assert(sensor.in_range(coord1))
    assert(not sensor.in_range(coord2))

    sensors = []
    for sx,sy,bx,by in TEST_SENSORS:
        beacon = Beacon(bx,by)
        sensor = Sensor(sx,sy,beacon)
        sensors.append(sensor)

    board = Board(sensors)
    assert(board.count_empty_columns(10) == 26)


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Beacon(Coordinate):
    def __init__(self, x, y):
        super().__init__(x, y)

class Sensor(Coordinate):
    def __init__(self, x, y, closest_beacon):
        super().__init__(x, y)
        # closest beacon
        self.closest_beacon = closest_beacon

    # manhattan distance for coordinates
    @property
    def beacon_distance(self):
        return distance(self, self.closest_beacon)

    #-1,7 in_range
    #-2,7 not_in_range
    # if range_to_beacon >= range
    def in_range(self, coordinate):
        return self.beacon_distance >= distance(self, coordinate)

class Board:
    def __init__(self, sensors):
        self.sensors = sensors

    # use a Set here for unique Y(column) values
    def count_empty_columns(self, row):
        columns = 0
        for sensor in self.sensors:

        return columns

    def empty_columns(self, row, sensor):
        columns = 0
        for sensor in sensors:
            # TODO
            if sensor.in_range(Coordinate(,row))
                columns++
        return columns

# coordinates
def distance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


if __name__ == '__main__':
    main()
