# LinkedIn Learning: "Python Object Oriented Programming" Course, Ch. 4
# Creating immutable data classes = useful when you want to create class data that you KNOW will not be changed or need to be changed

from dataclasses import dataclass

@dataclass(frozen = True) # "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

obj = ImmutableClass()
print(obj.value1)

obj.value1 = "Another value"
print(obj.value1) # should report an error, error is "FrozenInstanceError"