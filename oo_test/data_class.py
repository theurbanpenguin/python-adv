from dataclasses import dataclass


@dataclass
class Car:
    number_of_wheels: int
    number_of_doors: int

if __name__ == '__main__':
    car1 = Car(4,2)
    print(f"{car1.number_of_wheels=}")