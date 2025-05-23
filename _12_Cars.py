from random import randint


class Car:
    _count = 0
    _car = None

    def __init__(self, make, model, year, color):
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self.__bRunning = False
        self._serial = self.GenSerial(self._make, self._model, self._year)
        Car._count += 1

    def Start(self):
        if self.__bRunning:
            raise Exception("Car already in running state")
        else:
            self.__bRunning = True
            print("Car started")

    def Stop(self):
        if not self.__bRunning:
            raise Exception("Car already in stopped state")
        else:
            self.__bRunning = False
            print("Car stopped")

    @classmethod
    def GetCar(cls):
        if cls._car:
            return cls._car
        else:
            cls._car = Car("", "", 1, "")

    @classmethod
    def GetCarCount(cls):
        # print(_count)         # Searches for _color attribute in class (as opposed to object)
        # cls._color = "Yellow"     # Creates a class attribute, rather than modify the existing instance attribute
        return cls._count

    @staticmethod
    def GenSerial(make, model, year):
        serialNo = make + model + str(randint(1000, 9999)) + str(year)
        return serialNo

    @property
    def Color(self):
        return self._color
    
    @Color.setter
    def Color(self, color):
        self._color = color

    # def GetCarDetails(self):
    def __str__(self):
        return f"[{self._count}]Make: {self._make}, Model: {self._model}, Year: {self._year}, Color: {self._color}, SerialNo: {self._serial}"

    def PrintRunningStates(self):
        print(f"{self.__bRunning = }, {self._Car__bRunning = }")

    def __del__(self):
        Car._count -= 1
        print(f"Deleting {self}")

# ---------------------------------------------------------

def Test1():
    c1 = Car("Honda", "Accord", 2024, "White")
    c1.Start()
    try:
        c1.Start()
    except Exception as ex:
        print(f"\tEXCEPTION: {ex}")
        print("\tDo not use the starter again and again. Will damage the starter.")

    c1.Stop()

    # c1.Stop()

    # print(f"{c1.GetColor() = }")
    # c1.SetColor("Black")

    # print(f"{c1.GetColor() = }")

    # print(c1.GetCarDetails())


    print(c1.Color)
    c1.Color = "Black"
    print(c1.Color)
    print(c1) # --> print(str(c1))  --> print(c1.__str__())
    print(repr(c1))

def Test2():
    c1 = Car("Honda", "Accord", 2024, "White")
    print(c1)
    c2 = Car("Toyota", "Camry", 2024, "White")
    print(c2)

    # c1.__bRunning = True
    # print(dir(c1))
    # c1.PrintRunningStates()
    # c1.Start()

    print(f"{c1.GetCarCount() = }")
    GenerateCars()
    print(f"{c1.GetCarCount() = }")

def GenerateCars():
    c1 = Car("Honda", "Accord", 2024, "White")
    print(c1)
    c2 = Car("Toyota", "Camry", 2024, "White")
    print(c2)
    del c1
    del c2


def Test3():
    c1 = Car.GetCar()

def Main():
    # Test1()
    Test2()
    # print(Car.GetCarCount())
    Test3()

Main()