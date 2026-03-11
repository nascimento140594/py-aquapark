from typing import Type


class Visitor:
    def __init__(self, name: str, age: int, height: int, weight: int) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class ChildrenSlideLimitationValidator:
    def __init__(self, age: int, height: int, weight: int) -> None:
        self.age = age
        self.height = height
        self.weight = weight

    def is_valid(self) -> bool:
        return (
            4 <= self.age <= 14
            and 80 <= self.height <= 120
            and 20 <= self.weight <= 50
        )


class AdultSlideLimitationValidator:
    def __init__(self, age: int, height: int, weight: int) -> None:
        self.age = age
        self.height = height
        self.weight = weight

    def is_valid(self) -> bool:
        return (
            14 <= self.age <= 60
            and 120 <= self.height <= 220
            and 50 <= self.weight <= 120
        )


class Slide:
    def __init__(self, name: str, limitation_class: Type):
        self.name = name
        self.limitation_class = limitation_class

    def can_access(self, visitor: Visitor) -> bool:
        validator = self.limitation_class(
            visitor.age,
            visitor.height,
            visitor.weight
        )
        return validator.is_valid()
