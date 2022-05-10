from rover.Coordinate import Coordinate

def test_MoveNorth_GivenInitial_00_EndsAt_01():
    coord = Coordinate(0, 0)

    coord.MoveNorth()

    actual = coord.GetCoordinates()
    expected = [0, 1]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_MoveNorth_GivenInitial_09_EndsAt_00():
    coord = Coordinate(0, 9)

    coord.MoveNorth()

    actual = coord.GetCoordinates()
    expected = [0, 0]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_MoveSouth_GivenInitial_00_EndsAt_09():
    coord = Coordinate(0, 0)

    coord.MoveSouth()

    actual = coord.GetCoordinates()
    expected = [0, 9]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_MoveSouth_GivenInitial_09_EndsAt_08():
    coord = Coordinate(0, 9)

    coord.MoveSouth()

    actual = coord.GetCoordinates()
    expected = [0, 8]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_MoveEast_GivenInitial_90_EndsAt_00():
    coord = Coordinate(9, 0)

    coord.MoveEast()

    actual = coord.GetCoordinates()
    expected = [0, 0]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_MoveEast_GivenInitial_00_EndsAt_10():
    coord = Coordinate(0, 0)

    coord.MoveEast()

    actual = coord.GetCoordinates()
    expected = [1, 0]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_MoveWest_GivenInitial_90_EndsAt8_0():
    coord = Coordinate(9, 0)

    coord.MoveWest()

    actual = coord.GetCoordinates()
    expected = [8, 0]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_MoveWest_GivenInitial_00_EndsAt_90():
    coord = Coordinate(0, 0)

    coord.MoveWest()

    actual = coord.GetCoordinates()
    expected = [9, 0]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_GetString_Given_54():
    coord = Coordinate(5, 4)

    actual = coord.GetString()

    expected = "5:4"
    assert actual == expected, f"Expected {expected}, got: {actual}"
    