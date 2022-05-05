
class InvalidDirectionError(Exception):
    def __init__(self, message="Direction must be NORTH (0), EAST (1), SOUTH (2), or WEST (3)") -> None:
        self.message = message
        super().__init__(self.message)