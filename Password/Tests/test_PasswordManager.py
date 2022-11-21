import pytest
from PasswordManagerApp.PasswordManagerException import *
from PasswordManagerApp.PasswordManager import PasswordManager

def test_GivenPasswordLessThanThreeCharactersThenThrowsUsernameErrorIndicatingTooShort():
    with pytest.raises(UsernameError, match="Username must be at least 3 characters") as exception:
        manager = PasswordManager()
        manager.SetPassword("us", "Password%45")

def test_GivenPasswordGreaterThan31CharactersThenThrowsUsernameErrorIndicatingTooLong():
    with pytest.raises(UsernameError, match="Username must be less than 31 characters") as exception:
        manager = PasswordManager()
        manager.SetPassword("usernamethatistoolongeventuallyatsomepoint", "Password%45")