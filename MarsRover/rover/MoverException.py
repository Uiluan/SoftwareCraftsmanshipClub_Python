class InvalidCommandError(Exception):
    def __init__(self, message="Command must be: M, m, R, r, L, or l") -> None:
        self.message = message
        super().__init__(self.message)