import rover.Constants as const
from rover.Mover import *

def test_Move_StartAt_00N_Given_L_EndsAt_00W():
    mover = Mover(0, 0, const.consts.NORTH)

    actual = mover.Move("L")

    expected = [0, 0, const.consts.WEST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00N_Given_l_EndsAt_00W():
    mover = Mover(0, 0, const.consts.NORTH)

    actual = mover.Move("l")

    expected = [0, 0, const.consts.WEST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00W_Given_L_EndsAt_00S():
    mover = Mover(0, 0, const.consts.WEST)

    actual = mover.Move("L")

    expected = [0, 0, const.consts.SOUTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00W_Given_l_EndsAt_00S():
    mover = Mover(0, 0, const.consts.WEST)

    actual = mover.Move("l")

    expected = [0, 0, const.consts.SOUTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00S_Given_L_EndsAt_00E():
    mover = Mover(0, 0, const.consts.SOUTH)

    actual = mover.Move("L")

    expected = [0, 0, const.consts.EAST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00S_Given_l_EndsAt_00E():
    mover = Mover(0, 0, const.consts.SOUTH)

    actual = mover.Move("l")

    expected = [0, 0, const.consts.EAST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00E_Given_L_EndsAt_00N():
    mover = Mover(0, 0, const.consts.EAST)

    actual = mover.Move("L")

    expected = [0, 0, const.consts.NORTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00E_Given_l_EndsAt_00N():
    mover = Mover(0, 0, const.consts.EAST)

    actual = mover.Move("l")

    expected = [0, 0, const.consts.NORTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00N_Given_R_EndsAt_00E():
    mover = Mover(0, 0, const.consts.NORTH)

    actual = mover.Move("R")

    expected = [0, 0, const.consts.EAST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00N_Given_r_EndsAt_00E():
    mover = Mover(0, 0, const.consts.NORTH)

    actual = mover.Move("r")

    expected = [0, 0, const.consts.EAST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00W_Given_R_EndsAt_00N():
    mover = Mover(0, 0, const.consts.WEST)

    actual = mover.Move("R")

    expected = [0, 0, const.consts.NORTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00W_Given_r_EndsAt_00N():
    mover = Mover(0, 0, const.consts.WEST)

    actual = mover.Move("r")

    expected = [0, 0, const.consts.NORTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00S_Given_R_EndsAt_00W():
    mover = Mover(0, 0, const.consts.SOUTH)

    actual = mover.Move("R")

    expected = [0, 0, const.consts.WEST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00S_Given_r_EndsAt_00W():
    mover = Mover(0, 0, const.consts.SOUTH)

    actual = mover.Move("r")

    expected = [0, 0, const.consts.WEST]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00E_Given_R_EndsAt_00S():
    mover = Mover(0, 0, const.consts.EAST)

    actual = mover.Move("R")

    expected = [0, 0, const.consts.SOUTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00E_Given_r_EndsAt_00S():
    mover = Mover(0, 0, const.consts.EAST)

    actual = mover.Move("r")

    expected = [0, 0, const.consts.SOUTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00N_Given_M_EndsAt_01N():
    mover = Mover(0, 0, const.consts.NORTH)

    actual = mover.Move("M")

    expected = [0, 1, const.consts.NORTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_Move_StartAt_00N_Given_m_EndsAt_01N():
    mover = Mover(0, 0, const.consts.NORTH)

    actual = mover.Move("m")

    expected = [0, 1, const.consts.NORTH]
    assert actual == expected, f"Expected {expected}, got: {actual}"
