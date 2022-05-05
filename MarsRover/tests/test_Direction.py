
import pytest
import rover.Constants as const
from rover.DirectionException import *
from rover.Direction import Direction
import random

def test_GetString_GivenNorthReturnsNorth():
    dir = Direction(const.consts.NORTH)

    actual = dir.GetString()

    expected = "N"
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_GetString_GivenEastReturnsEast():
    dir = Direction(const.consts.EAST)

    actual = dir.GetString()

    expected = "E"
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_GetString_GivenSouthReturnsSouth():
    dir = Direction(const.consts.SOUTH)

    actual = dir.GetString()

    expected = "S"
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_GetString_GivenWestReturnsWest():
    dir = Direction(const.consts.WEST)

    actual = dir.GetString()

    expected = "W"
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_DirectionConstructor_GivenDirectionGreaterThan4ThrowsInvalidDirectionError():
    with pytest.raises(InvalidDirectionError) as exception:
        randomizer = random.Random()
        dir = Direction(randomizer.randint(4,25))

def test_DirectionConstructor_GivenDirectionLessThan0ThrowsInvalidDirectionError():
    with pytest.raises(InvalidDirectionError) as exception:
        randomizer = random.Random()
        dir = Direction(randomizer.randint(-25,-1))

def test_TurnLeft_GivenInitialDirectionNorthFacesWest():
    dir = Direction(const.consts.NORTH)

    dir.TurnLeft()

    assert dir.GetString() == "W"

def test_TurnLeft_GivenInitialDirectionWestFacesSouth():
    dir = Direction(const.consts.WEST)

    dir.TurnLeft()

    assert dir.GetString() == "S"

def test_TurnLeft_GivenInitialDirectionSouthFacesEast():
    dir = Direction(const.consts.SOUTH)

    dir.TurnLeft()

    assert dir.GetString() == "E"

def test_TurnLeft_GivenInitialDirectionEastFacesNorth():
    dir = Direction(const.consts.EAST)

    dir.TurnLeft()

    assert dir.GetString() == "N"

def test_TurnRight_GivenInitialDirectionNorthFacesEast():
    dir = Direction(const.consts.NORTH)

    dir.TurnRight()

    assert dir.GetString() == "E"

def test_TurnRight_GivenInitialDirectionWestFacesNorth():
    dir = Direction(const.consts.WEST)

    dir.TurnRight()

    assert dir.GetString() == "N"

def test_TurnRight_GivenInitialDirectionSouthFacesWest():
    dir = Direction(const.consts.SOUTH)

    dir.TurnRight()

    assert dir.GetString() == "W"

def test_TurnRight_GivenInitialDirectionEastFacesSouth():
    dir = Direction(const.consts.EAST)

    dir.TurnRight()

    assert dir.GetString() == "S"