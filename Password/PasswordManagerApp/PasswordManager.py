import string
from unicodedata import name
from PasswordManagerApp.PasswordManagerException import *

#TODO: SetPassword() creates a user, make it only set password for existing user, and have an AddUser function
class PasswordManager():
    def __init__(self) -> None:
        self.users = {}
        pass

    # TODO: Doesn't get user, just returns if user exists. Refactor.
    # Could require other operations on a user to require getting a user object. Then GetUser can exist and can throw exceptions.
    # Getting a user object should require a password?
    def GetUser(self, username: string):
        if username in self.users:
            return True
        else:
            return False

    def SetPassword(self, username: string, password: string):
        name = _Username(username)
        key = _Password(username, password)
        try:
            if name.isValid() and key.isValid():
                self.users[username] = password
        except Exception as error:
            raise error

class _Username():
    MIN_USERNAME_LENGTH = 3
    MAX_USERNAME_LENGTH = 31

    def __init__(self, username: string) -> None:
        self.username = str(username)

    def isValid(self):
        try:
            self.checkIfLengthBelowMin()
            self.checkIfLengthAboveMax()
            self.checkIfAlphanumeric()
            self.checkIfStartsWithLetter()
        except Exception as error:
            raise error

        return True

    def checkIfLengthBelowMin(self):
        if len(self.username) < self.MIN_USERNAME_LENGTH:
            raise UsernameTooShortError("Username must be at least 3 characters")

    def checkIfLengthAboveMax(self):
        if len(self.username) > self.MAX_USERNAME_LENGTH:
            raise UsernameTooLongError("Username must be less than 31 characters")

    def checkIfAlphanumeric(self):
        if not self.username.isalnum():
            raise UsernameNotAlphanumericError("Username must be alphanumeric (consisting of letters and numbers)")

    def checkIfStartsWithLetter(self):
        if not self.username[0].isalpha():
            raise UsernameStartError("Username must begin with a letter")

class _Password():
    MIN_PASSWORD_LENGTH = 8
    MAX_PASSWORD_LENGTH = 255
    PASS_SPECIAL_CHARS = "!@#$%^&*()-_=+"

    def __init__(self, username: string, password: string) -> None:
        self.password = str(password)
        self.username = str(username)

    def isValid(self):
        try:
            self.checkIfContainsBadSpecialCharacters()
            self.checkIfContainsSpecialCharacters()
            self.checkIfHasDigit()
            self.checkIfHasLowercase()
            self.checkIfHasUppercase()
            self.checkIfTooLong()
            self.checkIfTooShort()
            self.checkIfContainsUsername(self.username)
        except Exception as error:
            raise error
        
        return True

    def checkIfContainsUsername(self, username: string):
        if str(username).lower() in self.password.lower():
            raise PasswordContainsUsernameError("Password must not contain username")

    def checkIfTooShort(self):
        if len(self.password) < self.MIN_PASSWORD_LENGTH:
            raise PasswordTooShortError("Password must be at least 8 characters long")

    def checkIfTooLong(self):
        if len(self.password) > self.MAX_PASSWORD_LENGTH:
            raise PasswordTooLongError("Password must be less than 255 characters")

    def checkIfHasLowercase(self):
        if not any(char.islower() for char in self.password):
            raise PasswordNoLowerAlphaError("Password must contain a lowercase letter")

    def checkIfHasUppercase(self):
        if not any(char.isupper() for char in self.password):
            raise PasswordNoUpperAlphaError("Password must contain an uppercase letter")

    def checkIfHasDigit(self):
        if not any(char.isdigit() for char in self.password):
            raise PasswordNoDigitError("Password must contain an digit: 0-9")

    def checkIfContainsSpecialCharacters(self):
        if not any(char in self.PASS_SPECIAL_CHARS for char in self.password):
            raise PasswordNoSpecialCharError("Password must contain one of the following: " + self.PASS_SPECIAL_CHARS)

    def checkIfContainsBadSpecialCharacters(self):
        validSet = string.ascii_letters + string.digits + self.PASS_SPECIAL_CHARS
        if any(not (char in validSet) for char in self.password):
            raise PasswordBadCharactersError("Password contains bad special character. Must use: " + self.PASS_SPECIAL_CHARS)
