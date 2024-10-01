from dataclasses import dataclass

from src.app.domain.common.value_objects import DomainValueObject


class DomainEntity[EntityId: DomainValueObject]:
    id: EntityId
