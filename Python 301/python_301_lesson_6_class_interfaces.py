class Animal:
    fur_color = "Orange"

    def speak(self):
        raise NotImplementedError

    def eat(self):
        pass

    def chase(self):
        pass

class HouseCat(Animal):
    def speak(self):
        print("Meeeeowwww")

cat = HouseCat()
cat.speak()
