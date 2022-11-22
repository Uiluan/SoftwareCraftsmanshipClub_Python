import pytest
import re
from PasswordManagerApp.PasswordManagerException import *
from PasswordManagerApp.PasswordManager import PasswordManager

def test_GivenUsernameLessThanThreeCharactersThenThrowsUsernameErrorIndicatingTooShort():
    with pytest.raises(UsernameError, match="Username must be at least 3 characters") as exception:
        manager = PasswordManager()
        manager.SetPassword("us", "Password%45")

def test_GivenUsernameGreaterThan31CharactersThenThrowsUsernameErrorIndicatingTooLong():
    with pytest.raises(UsernameError, match="Username must be less than 31 characters") as exception:
        manager = PasswordManager()
        manager.SetPassword("usernamethatistoolongeventuallyatsomepoint", "Password%45")

def test_GivenUsernameThatContainsExclamationThenThrowsUsernameErrorForContainingNonAlphanumeric():
    with pytest.raises(UsernameError, match=re.escape("Username must be alphanumeric (consisting of letters and numbers)")) as exception:
        manager = PasswordManager()
        manager.SetPassword("username!", "Password%45")

def test_GivenUsernameStartingWith9ThenThrowUsernameErrorIndicatingUsernameMustStartWithLetter():
    with pytest.raises(UsernameError, match="Username must begin with a letter") as exception:
        manager = PasswordManager()
        manager.SetPassword("9username", "Password%45")

def test_GivenOtherwiseValidPasswordWithNoUpperCaseThenThrowPasswordErrorIndicatingMustHaveUpperCase():
    with pytest.raises(PasswordError, match="Password must contain an uppercase letter") as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "password%45")

def test_GivenOtherwiseValidPasswordWithNoNumberThenThrowPasswordErrorIndicatingMustHaveNumber():
    with pytest.raises(PasswordError, match="Password must contain an digit: 0-9") as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "Password%")

def test_GivenOtherwiseValidPasswordWithNoSpecialCharacterThenThrowPasswordErrorIndicatingMustContainSpecialCharacter():
    with pytest.raises(PasswordError, match=re.escape("Password must contain one of the following: !@#$%^&*()-_=+")) as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "Password45")

def test_GivenOtherwiseValidPasswordWithForwardSlashCharacterThenThrowPasswordErrorIndicatingCorrectSpecialCharacters():
    with pytest.raises(PasswordError, match=re.escape("Password contains bad special character. Must use: !@#$%^&*()-_=+")) as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "Password/45")
