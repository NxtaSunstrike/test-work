from typing import Self

class DomainException(Exception):
    def __init__(self: Self, message: str) -> None:
        self.message: str = message


class DomainValidationError(DomainException):
    '''
    Raise this exception in value objects
    '''
    pass