#TODO: move more error text here, rely less on AccountManager
class UsernameError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class UsernameTooShortError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class UsernameTooLongError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class UsernameNotAlphanumericError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class UsernameStartError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class PasswordError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class PasswordTooShortError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class PasswordTooLongError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class PasswordBadCharactersError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class PasswordNoLowerAlphaError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class PasswordNoUpperAlphaError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class PasswordNoDigitError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class PasswordNoSpecialCharError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class PasswordContainsUsernameError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
