
class Person:

    def __init__(self, fname, lname):  # Constructure()
       self.fname = fname
       self.lname = lname

    def get_full_name(self):
        #return self.fname + " " + self.lname
        #or
        return "{} {}".format(self.fname, self.lname)

    def __repr__(self):
        return "Person: {} {}".format(self.fname, self.lname)


p = Person("Bob", "Smith")

print(p.fname)
print(p.lname)
print(p.get_full_name())
print(p) # For __repr__ method!
