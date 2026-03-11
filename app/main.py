from abc import ABC
from typing import Type


class IntegerRange:
    def __init__(self, min_value: int, max_value: int) -> None:
        self.min_value = min_value
        self.max_value = max_value
        self.private_name = None

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Value must be integer")

        if not self.min_value <= value <= self.max_value:
            raise ValueError("Value out of allowed range")

        setattr(instance, self.private_name, value)


class SlideLimitationValidator(ABC):
    def __init__(
        self,
        age: int,
        height: int,
        weight: int
    ) -> None:
        self.age = age
        self.height = height
        self.weight = weight


class ChildrenSlideLimitationValidator(SlideLimitationValidator):
    age = IntegerRange(3, 12)
    height = IntegerRange(80, 150)
    weight = IntegerRange(20, 60)


class AdultSlideLimitationValidator(SlideLimitationValidator):
    age = IntegerRange(18, 60)
    height = IntegerRange(120, 220)
    weight = IntegerRange(50, 120)


class Visitor:
    def __init__(
        self,
        name: str,
        age: int,
        height: int,
        weight: int
    ) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class Slide:
    def __init__(self, name: str, limitation_class: Type):
        self.name = name
        self.limitation_class = limitation_class

    def can_access(self, visitor: Visitor) -> bool:
        try:
            self.limitation_class(
                visitor.age,
                visitor.height,
                visitor.weight
            )
            return True
        except (TypeError, ValueError):
            return False
