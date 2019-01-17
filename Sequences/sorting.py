#nums = [2, 5, 7, 8, 1, 9, 2, 7, 4]

#nums.sort()
#nums.sort(reverse = True) 
#nums.reverse()

#print(nums)


class Person:

    def __init__(self, fname, lname):  # Constructure()
       self.fname = fname
       self.lname = lname

    def __repr__(self):
        return "Person: {} {}".format(self.fname, self.lname)


people =[ 
    Person("Bob", "Smith"),
    Person("Tim", "Johnson"),
    Person("Mike", "Collins"),
]

# people.sort(key = lambda p: p.lname) # Sort Last Name

def comparison_value(p):
    return p.lname

people.sort(key = comparison_value) # Sort Last Name

print(people)