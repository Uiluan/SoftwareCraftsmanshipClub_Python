import pytest
import re
from PasswordManagerApp.PasswordManagerException import *
from PasswordManagerApp.PasswordManager import PasswordManager

def test_GivenUsernameLessThanThreeCharactersThenThrowsUsernameTooShortError():
    with pytest.raises(UsernameTooShortError, match="Username must be at least 3 characters") as exception:
        manager = PasswordManager()
        manager.SetPassword("us", "Password%45")

def test_GivenEmptyStringUsernameThenThrowsUsernameTooShortError():
    with pytest.raises(UsernameTooShortError, match="Username must be at least 3 characters") as exception:
        manager = PasswordManager()
        manager.SetPassword("", "Password%45")

def test_GivenUsernameGreaterThan31CharactersThenThrowsUsernameTooLongError():
    with pytest.raises(UsernameTooLongError, match="Username must be less than 31 characters") as exception:
        manager = PasswordManager()
        manager.SetPassword("usernamethatistoolongeventuallyatsomepoint", "Password%45")

def test_GivenUsernameThatContainsExclamationThenThrowsUsernameNotAlphanumericError():
    with pytest.raises(UsernameNotAlphanumericError, match=re.escape("Username must be alphanumeric (consisting of letters and numbers)")) as exception:
        manager = PasswordManager()
        manager.SetPassword("username!", "Password%45")

def test_GivenUsernameStartingWithSpaceThenThrowsUsernameNotAlphanumericError():
    with pytest.raises(UsernameNotAlphanumericError, match=re.escape("Username must be alphanumeric (consisting of letters and numbers)")) as exception:
        manager = PasswordManager()
        manager.SetPassword(" username", "Password%45")

def test_GivenUsernameOfOnlySpacesThenThrowsUsernameNotAlphanumericError():
    with pytest.raises(UsernameNotAlphanumericError, match=re.escape("Username must be alphanumeric (consisting of letters and numbers)")) as exception:
        manager = PasswordManager()
        manager.SetPassword("     ", "Password%45")

def test_GivenUsernameStartingWith9ThenThrowUsernameStartError():
    with pytest.raises(UsernameStartError, match="Username must begin with a letter") as exception:
        manager = PasswordManager()
        manager.SetPassword("9username", "Password%45")

def test_GivenNoneAsUsernameDoesNotThrowException():
    # The PasswordManager should turn any input into a string. 'None' as a string is considered valid input
    manager = PasswordManager()
    manager.SetPassword(None, "Password%45")

def test_GivenNoneAsPasswordThrowsPasswordNoSpecialCharError():
    # PasswordManager should turn any input into a string. 'None' As a string is considered valid other than not following other password rules
    with pytest.raises(PasswordNoSpecialCharError, match=re.escape("Password must contain one of the following: !@#$%^&*()-_=+")) as exception:
        manager = PasswordManager()
        manager.SetPassword("username", None)

def test_GivenEmptyStringAsPasswordThrowsPasswordNoSpecialCharError():
    with pytest.raises(PasswordNoSpecialCharError, match=re.escape("Password must contain one of the following: !@#$%^&*()-_=+")) as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "")

def test_GivenSpacesAsPasswordThrowsPasswordBadCharactersError():
    with pytest.raises(PasswordBadCharactersError, match=re.escape("Password contains bad special character. Must use: !@#$%^&*()-_=+")) as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "    ")

def test_GivenOtherwiseValidPasswordWithNoUpperCaseThenThrowPasswordNoUpperAlphaError():
    with pytest.raises(PasswordNoUpperAlphaError, match="Password must contain an uppercase letter") as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "password%45")

def test_GivenOtherwiseValidPasswordWithNoNumberThenThrowPasswordNoDigitError():
    with pytest.raises(PasswordNoDigitError, match="Password must contain an digit: 0-9") as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "Password%")

def test_GivenOtherwiseValidPasswordWithNoSpecialCharacterThenThrowPasswordNoSpecialCharacterError():
    with pytest.raises(PasswordNoSpecialCharError, match=re.escape("Password must contain one of the following: !@#$%^&*()-_=+")) as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "Password45")

def test_GivenOtherwiseValidPasswordWithForwardSlashCharacterThenThrowPasswordBadCharactersError():
    with pytest.raises(PasswordBadCharactersError, match=re.escape("Password contains bad special character. Must use: !@#$%^&*()-_=+")) as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "Password/45")

def test_GivenOtherwiseValidPasswordLessThan8CharactersThenThrowPasswordTooShortError():
    with pytest.raises(PasswordTooShortError, match="Password must be at least 8 characters long") as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "Pa1^")

def test_GivenOtherwiseValidPasswordGreaterThan255CharactersThenThrowPasswordToLongError():
    with pytest.raises(PasswordTooLongError, match="Password must be less than 255 characters") as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "Password%45Password%45Password%45Password%45Password%45Password%45Password" + \
            "%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45" + \
            "Password%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45" + \
            "Password%45Password%45Password%45Password%45")

def test_GivenOtherwiseValidPasswordWithNoLowerCaseThenThrowPasswordNoLowerAlphaError():
    with pytest.raises(PasswordNoLowerAlphaError, match="Password must contain a lowercase letter") as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "PASSWORD%45")

def test_GivenOtherwiseValidPasswordContainingUsernameThenThrowPasswordContainsUsernameError():
    with pytest.raises(PasswordContainsUsernameError, match="Password must not contain username") as exception:
        manager = PasswordManager()
        manager.SetPassword("username", "UserNAME%45")

def test_GetUserAfterAValidUserIsAddedReturnsTrue():
    manager = PasswordManager()
    manager.SetPassword("username", "Password%45")

    actual = manager.GetUser("username")
    expected = True
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_GetUserNotInDatabaseReturnsFalse():
    manager = PasswordManager()

    actual = manager.GetUser("username")
    expected = False
    assert actual == expected, f"Expected {expected}, got: {actual}"