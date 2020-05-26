class Vector():
    """docstring for Vector."""

    def __init__(self, values):
        if isinstance(values, range):
            self.values = []
            for x in values:
                self.values.append(float(x))
        elif (isinstance(values, tuple) and len(values) == 2
              and isinstance(values[0], int) and isinstance(values[1], int)):
            self.values = []
            i = 1 if values[0] <= values[1] else -1
            for x in range(values[0], values[1], i):
                self.values.append(float(x))
        elif isinstance(values, list):
            for x in values:
                if not isinstance(x, float):
                    self.my_exit(
                        f"Bad type for ingredient in values: ({x})")
                self.values = values
        elif isinstance(values, int):
            self.values = []
            for x in range(0, values):
                self.values.append(float(x))
        else:
            self.my_exit(
                f"Bad value or bad type for values: ({values})")

        self.size = len(self.values)

    def __str__(self):
        txt = (f"({self.__class__.__name__}{self.values})")
        return txt

    def __repr__(self):
        txt = (f"{self.__class__.__name__}({self.values}) size: {self.size}")
        return txt

    def __add__(self, other):
        if isinstance(other, Vector) and self.size == other.size:
            if self.size != 0:
                list = []
                for i in range(self.size):
                    list.append(self.values[i] + other.values[i])
                return Vector(list)
            else:
                return Vector(0)
        elif isinstance(other, (int, float)):
            list = []
            for i in range(self.size):
                list.append(self.values[i] + other)
            return Vector(list)

        else:
            self.my_return(f"{other} not a Vector or 2 vector not same size")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector) and self.size == other.size:
            list = []
            for i in range(self.size):
                list.append(self.values[i] - other.values[i])
            return Vector(list)
        elif isinstance(other, (int, float)):
            list = []
            for i in range(self.size):
                list.append(self.values[i] - other)
            return Vector(list)
        else:
            self.my_return(f"{other} not a Vector or 2 vector not same size")

    def __rsub__(self, other):
        if isinstance(other, Vector):
            return other.__sub__(self)
        elif isinstance(other, (int, float)):
            list = []
            for i in range(self.size):
                list.append(other - self.values[i])
            return Vector(list)
        self.my_return(f"{other} not a Vector")

    def __truediv__(self, other):
        if isinstance(other, (int, float)) and other != 0:
            list = []
            for i in range(self.size):
                list.append(self.values[i] / other)
            return Vector(list)
        else:
            self.my_return(f"{other} not a int/float or zero")

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)) and other != 0:
            return self.__mul__(1/other)
        self.my_return(f"{other} not a Int/float or zero")

    def __mul__(self, other):
        if isinstance(other, Vector) and self.size == other.size:
            list = []
            for i in range(self.size):
                list.append(self.values[i] * other.values[i])
            return sum(list)
        elif isinstance(other, (int, float)):
            list = []
            for i in range(self.size):
                list.append(self.values[i] * other)
            return Vector(list)
        else:
            self.my_return(
                f"{other} not a Vector or Int/float,or 2 vector not same size")

    def __rmul__(self, other):
        return self.__mul__(other)

    def my_return(self, str):
        print(str)
        return()

    def my_exit(self, str):
        print(str)
        exit()
