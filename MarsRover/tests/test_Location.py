import rover.Constants as const
from rover.Location import Location

def test_TurnLeft_GivenInitial_00N_EndsAt_00W():
    location = Location(0, 0, const.consts.NORTH)

    location.TurnLeft()

    expected = [0, 0, const.consts.WEST]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_TurnLeft_GivenInitial_00W_EndsAt_00S():
    location = Location(0, 0, const.consts.WEST)

    location.TurnLeft()

    expected = [0, 0, const.consts.SOUTH]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_TurnLeft_GivenInitial_00S_EndsAt_00E():
    location = Location(0, 0, const.consts.SOUTH)

    location.TurnLeft()

    expected = [0, 0, const.consts.EAST]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_TurnLeft_GivenInitial_00E_EndsAt_00N():
    location = Location(0, 0, const.consts.EAST)

    location.TurnLeft()

    expected = [0, 0, const.consts.NORTH]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_TurnRight_GivenInitial_00N_EndsAt_00E():
    location = Location(0, 0, const.consts.NORTH)

    location.TurnRight()

    expected = [0, 0, const.consts.EAST]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_TurnRight_GivenInitial_00W_EndsAt_00N():
    location = Location(0, 0, const.consts.WEST)

    location.TurnRight()

    expected = [0, 0, const.consts.NORTH]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_TurnRight_GivenInitial_00S_EndsAt_00W():
    location = Location(0, 0, const.consts.SOUTH)

    location.TurnRight()

    expected = [0, 0, const.consts.WEST]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_TurnRight_GivenInitial_00E_EndsAt_00S():
    location = Location(0, 0, const.consts.EAST)

    location.TurnRight()

    expected = [0, 0, const.consts.SOUTH]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_GetLocation_GivenLocation_87E_Returns_87E():
    location = Location(8, 7, const.consts.EAST)

    expected = [8, 7, const.consts.EAST]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_GetString_GivenLocation_42W_Returns_42W_String():
    location = Location(4, 2, const.consts.WEST)

    expected = "4:2:W"
    actual = location.GetString()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_Given_55N_EndsAt_56N():
    location = Location(5, 5, const.consts.NORTH)

    location.Move()

    expected = [5, 6, const.consts.NORTH]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_Given_59N_EndsAt_50N():
    location = Location(5, 9, const.consts.NORTH)

    location.Move()

    expected = [5, 0, const.consts.NORTH]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_Given_00W_EndsAt_90W():
    location = Location(0, 0, const.consts.WEST)

    location.Move()

    expected = [9, 0, const.consts.WEST]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_Given_50W_EndsAt_40W():
    location = Location(5, 0, const.consts.WEST)

    location.Move()

    expected = [4, 0, const.consts.WEST]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_Given_00S_EndsAt_09S():
    location = Location(0, 0, const.consts.SOUTH)

    location.Move()

    expected = [0, 9, const.consts.SOUTH]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_Given_55S_EndsAt_54S():
    location = Location(5, 5, const.consts.SOUTH)

    location.Move()

    expected = [5, 4, const.consts.SOUTH]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_Given_55E_EndsAt_56E():
    location = Location(5, 5, const.consts.EAST)

    location.Move()

    expected = [6, 5, const.consts.EAST]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_Given_95E_EndsAt_05E():
    location = Location(9, 5, const.consts.EAST)

    location.Move()

    expected = [0, 5, const.consts.EAST]
    actual = location.GetLocation()
    assert actual == expected, f"Expected {expected}, got: {actual}"