#Operators Overloading

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    def __add__(self, other):                       #It's how the "+" plus operator will be overloaded, here "self" is an object made from this class, whereby "other" is another object made from any class (not particularly it has to be this class IMP: you can add object from different class).
        galleons = self.galleons + other.galleons      # When we will add the two object(instance), like, -- object1 + object2 -- this special method -- __add__  -- will be called, and the two operands(object1, object2) will be passed as argument -- self, other -- respectively
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


def main():
    potter = Vault(100, 50, 25)
    print(potter)

    weasley = Vault(25, 50, 100)
    print(weasley)

    total = potter + weasley        #It's executing the == __add__ == special method in the class
    print(total)


if __name__ == "__main__":
    main()