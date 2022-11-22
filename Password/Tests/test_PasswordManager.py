import pytest
import re
from PasswordManagerApp.PasswordManagerException import *
from PasswordManagerApp.PasswordManager import PasswordManager

def test_GivenUsernameLessThanThreeCharactersThenThrowsUsernameTooShortError():
    with pytest.raises(UsernameTooShortError, match="Username must be at least 3 characters") as exception:
        manager = PasswordManager()
        manager.SetPassword("us", "Password%45")

def test_GivenUsernameGreaterThan31CharactersThenThrowsUsernameTooLongError():
    with pytest.raises(UsernameTooLongError, match="Username must be less than 31 characters") as exception:
        manager = PasswordManager()
        manager.SetPassword("usernamethatistoolongeventuallyatsomepoint", "Password%45")

def test_GivenUsernameThatContainsExclamationThenThrowsUsernameNotAlphanumericError():
    with pytest.raises(UsernameNotAlphanumericError, match=re.escape("Username must be alphanumeric (consisting of letters and numbers)")) as exception:
        manager = PasswordManager()
        manager.SetPassword("username!", "Password%45")

def test_GivenUsernameStartingWith9ThenThrowUsernameStartError():
    with pytest.raises(UsernameStartError, match="Username must begin with a letter") as exception:
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

def test_GivenOtherwiseValidPasswordLessThan8CharactersThenThrowPasswordErrorIndicatingMustBeAtLeast8Characters():
    with pytest.raises(PasswordError, match="Password must be at least 8 characters long") as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "Pa1^")

def test_GivenOtherwiseValidPasswordGreaterThan255CharactersThenThrowPasswordErrorIndicatingMustBeLessThan255Characters():
    with pytest.raises(PasswordError, match="Password must be less than 255 characters") as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "Password%45Password%45Password%45Password%45Password%45Password%45Password" + \
            "%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45" + \
            "Password%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45" + \
            "Password%45Password%45Password%45Password%45")

def test_GivenOtherwiseValidPasswordWithNoLowerCaseThenThrowPasswordErrorIndicatingMustContainLowerCaseCharacter():
    with pytest.raises(PasswordError, match="Password must contain a lowercase letter") as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "PASSWORD%45")

def test_GivenOtherwiseValidPasswordContainingUsernameThenThrowPasswordErrorIndicatingPasswordMustNotContainUsername():
    with pytest.raises(PasswordError, match="Password must not contain username") as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "UserNAME%45")