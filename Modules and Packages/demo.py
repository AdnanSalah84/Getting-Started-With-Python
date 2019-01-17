# import calc
# from calc import add as calcAdd, pi, Person

import my_math.calc
from my_math import calc
from my_math.calc import add as calcAdd, pi, Person

def main():

    # print("running the program")
    # print(calc.add(1,2))
    # print(calc.pi)

    # p = calc.Person("Bob", "Smith")
    # print(p.get_full_name())

    print("running the program")
    print(calcAdd(1,2))
    print(pi)

    p = Person("Bob", "Smith")
    print(p.get_full_name())

    # print("running the program")
    # print(my_math.calc.add(1,2))
    # print(my_math.calc.pi)

    # p = my_math.calc.Person("Bob", "Smith")
    # print(p.get_full_name())

    # print("running the program")
    # print(calc.add(1,2))
    # print(calc.pi)

    # p = calc.Person("Bob", "Smith")
    # print(p.get_full_name())

if __name__ == "__main__":
    main()
