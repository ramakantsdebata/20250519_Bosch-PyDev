class Car:
    def __init__(self, make, model, year, color):
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self._bRunning = False

    def Start(self):
        if self._bRunning:
            raise Exception("Car already in running state")
        else:
            self._bRunning = True
            print("Car started")

    def Stop(self):
        if not self._bRunning:
            raise Exception("Car already in stopped state")
        else:
            self._bRunning = False
            print("Car stopped")



# ---------------------------------------------------------

c1 = Car("Honda", "Accord", 2024, "White")
c1.Start()
try:
    c1.Start()
except Exception as ex:
    print(f"\tEXCEPTION: {ex}")
    print("\tDo not use the starter again and again. Will damage the starter.")
    raise

c1.Stop()

# c1.Stop()