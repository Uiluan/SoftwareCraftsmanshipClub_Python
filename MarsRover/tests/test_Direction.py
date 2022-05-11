
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

    assert dir.GetDirection() == const.consts.WEST

def test_TurnLeft_GivenInitialDirectionWestFacesSouth():
    dir = Direction(const.consts.WEST)

    dir.TurnLeft()

    assert dir.GetDirection() == const.consts.SOUTH

def test_TurnLeft_GivenInitialDirectionSouthFacesEast():
    dir = Direction(const.consts.SOUTH)

    dir.TurnLeft()

    assert dir.GetDirection() == const.consts.EAST

def test_TurnLeft_GivenInitialDirectionEastFacesNorth():
    dir = Direction(const.consts.EAST)

    dir.TurnLeft()

    assert dir.GetDirection() == const.consts.NORTH

def test_TurnRight_GivenInitialDirectionNorthFacesEast():
    dir = Direction(const.consts.NORTH)

    dir.TurnRight()

    assert dir.GetDirection() == const.consts.EAST

def test_TurnRight_GivenInitialDirectionWestFacesNorth():
    dir = Direction(const.consts.WEST)

    dir.TurnRight()

    assert dir.GetDirection() == const.consts.NORTH

def test_TurnRight_GivenInitialDirectionSouthFacesWest():
    dir = Direction(const.consts.SOUTH)

    dir.TurnRight()

    assert dir.GetDirection() == const.consts.WEST

def test_TurnRight_GivenInitialDirectionEastFacesSouth():
    dir = Direction(const.consts.EAST)

    dir.TurnRight()

    assert dir.GetDirection() == const.consts.SOUTH

def test_GetDirection_GivenNorthReturnsNorth():
    dir = Direction(const.consts.NORTH)

    actual = dir.GetDirection()

    expected = const.consts.NORTH
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_GetDirection_GivenEastReturnsEast():
    dir = Direction(const.consts.EAST)

    actual = dir.GetDirection()

    expected = const.consts.EAST
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_GetDirection_GivenSouthReturnsSouth():
    dir = Direction(const.consts.SOUTH)

    actual = dir.GetDirection()

    expected = const.consts.SOUTH
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_GetDirection_GivenWestReturnsWest():
    dir = Direction(const.consts.WEST)

    actual = dir.GetDirection()

    expected = const.consts.WEST
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_IsNorth():
    dir = Direction(const.consts.NORTH)

    actual = dir.IsNorth()
    expected = True
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_IsEast():
    dir = Direction(const.consts.EAST)

    actual = dir.IsEast()
    expected = True
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_IsSouth():
    dir = Direction(const.consts.SOUTH)

    actual = dir.IsSouth()
    expected = True
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_IsWest():
    dir = Direction(const.consts.WEST)

    actual = dir.IsWest()
    expected = True
    assert actual == expected, f"Expected {expected}, got: {actual}"