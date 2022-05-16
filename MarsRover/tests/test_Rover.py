import pytest
import rover.Constants as const
from rover.Rover import Rover
from rover.MoverException import *
from rover.DirectionException import *
from rover.RoverException import *

#TODO: GetString method
def test_Move_StartAt_55N_Given_M_EndsAt_56N():
    rover = Rover(5, 5, const.consts.NORTH)

    actual = rover.Move("M")

    expected = [5, 6, const.consts.NORTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_18W_Given_M_EndsAt_08W():
    rover = Rover(1, 8, const.consts.WEST)

    actual = rover.Move("M")

    expected = [0, 8, const.consts.WEST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_69E_Given_M_EndsAt_79E():
    rover = Rover(6, 9, const.consts.EAST)

    actual = rover.Move("M")

    expected = [7, 9, const.consts.EAST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_82S_Given_M_EndsAt_81S():
    rover = Rover(8, 2, const.consts.SOUTH)

    actual = rover.Move("M")

    expected = [8, 1, const.consts.SOUTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_59N_Given_M_EndsAt_50N():
    rover = Rover(5, 9, const.consts.NORTH)

    actual = rover.Move("M")

    expected = [5, 0, const.consts.NORTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_08W_Given_M_EndsAt_98W():
    rover = Rover(0, 8, const.consts.WEST)

    actual = rover.Move("M")

    expected = [9, 8, const.consts.WEST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_99E_Given_M_EndsAt_09E():
    rover = Rover(9, 9, const.consts.EAST)

    actual = rover.Move("M")

    expected = [0, 9, const.consts.EAST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_80S_Given_M_EndsAt_89S():
    rover = Rover(8, 0, const.consts.SOUTH)

    actual = rover.Move("M")

    expected = [8, 9, const.consts.SOUTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_80S_Given_mml_EndsAt_88E():
    rover = Rover(8, 0, const.consts.SOUTH)

    actual = rover.Move("mml")

    expected = [8, 8, const.consts.EAST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_35W_Given_mlMMRmm_EndsAt_03W():
    rover = Rover(3, 5, const.consts.WEST)

    actual = rover.Move("mlMMRmm")

    expected = [0, 3, const.consts.WEST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_02E_Given_rmMrmlRLmlrrmMMm_EndsAt_59W():
    rover = Rover(0, 2, const.consts.EAST)

    actual = rover.Move("rmMrmlRLmlrrmMMm")

    expected = [5, 9, const.consts.WEST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_GivenInvalidCommand_ThrowsInvalidCommandError():
    with pytest.raises(InvalidCommandError) as exception:
        rover = Rover(5, 5, const.consts.EAST)

        result = rover.Move("mMv")

def test_RoverConstructor_NoInitialPositionGiven_HasLocation_00N():
    rover = Rover()

    actual = rover.GetLocation()

    expected = [0, 0, const.consts.NORTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_RoverConstructor_GivenXCoordinateLargerThanMax_ThrowsInvalidXCoordinateError():
    with pytest.raises(InvalidXCoordinateError) as exception:
        rover = Rover(10, 0, const.consts.NORTH)

def test_RoverConstructor_GivenYCoordinateLargerThanMax_ThrowsInvalidYCoordinateError():
    with pytest.raises(InvalidYCoordinateError) as exception:
        rover = Rover(0, 10, const.consts.NORTH)

def test_RoverConstructor_GivenDirectionOutOfBounds_ThrowsInvalidDirectionError():
    with pytest.raises(InvalidDirectionError) as exception:
        rover = Rover(0, 0, 5)