from typing import Self
from dataclasses import dataclass


@dataclass(frozen=True)
class DomainValueObject[Type]:
    object: Type

    def validate(self: Self) -> None:
        '''
        must be implemented in value objects
        '''

    def __post_init__(self: Self) -> None:
        self.validate()
