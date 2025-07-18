from f_romanos import de_arabigo_a_romano, de_romano_a_arabigo

class RomanNumber:
    def __init__(self, value: str | int):
        if type(value) == str:
            self.symbol = value
            self.value = de_romano_a_arabigo(value)
        else:
            self.value = value
            self.symbol = de_arabigo_a_romano(value)

    def __repr__(self):
        return self.symbol
    
    def __str__(self):
        return self.__repr__()
    
    def __eq__(self, other):

        """""
        Comparar valores
        devolver true si son iguales y false en caso contrario
        """""
        return self.value == other.value
    
    def __hash__(self):
        hash((self.value, self.symbol))
    
    def __add__(self, other):
        if isinstance(other, int):
            resultado = self.value + other
        elif isinstance(other, RomanNumber):
            resultado = self.value + other.value
        else:
            super().__add__(other)
        return RomanNumber(resultado)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, int):
            resultado = self.value - other
        elif isinstance(other, RomanNumber):
            resultado = self.value - other.value
        else:
            super().__add__(other)
        return RomanNumber(resultado)
    
    def __rsub__(self, other):
        if isinstance(other, int):
            return RomanNumber(other) - self.value
        else:
            super().__rsub__(other)
    
    def __pow__(self, other):
        if isinstance(other, int):
            resultado = self.value ** other
        elif isinstance(other, RomanNumber):
            resultado = self.value ** other.value
        else:
            super().__add__(other)
        return RomanNumber(resultado)
    
    def __mod__(self, other):
        if isinstance(other, int):
            resultado = self.value % other
        elif isinstance(other, RomanNumber):
            resultado = self.value % other.value
        else:
            super().__add__(other)
        return RomanNumber(resultado)
    
    def __rmod__(self, other):
        if isinstance(other, int):
            return RomanNumber(other % self.value)
        else:
            return self.__rtruediv__(other)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            resultado = self.value // other
        elif isinstance(other, RomanNumber):
            resultado = self.value // other.value
        else:
            super().__add__(other)
        return RomanNumber(resultado)
    
    def __rtruediv__(self, other):
        if isinstance(other, int):
            return RomanNumber(other // self.value)
        else:
            return self.__rtruediv__(other)
    
    def __mul__(self, other):
        if isinstance(other, int):
            resultado = self.value * other
        elif isinstance(other, RomanNumber):
            resultado = self.value * other.value
        else:
            super().__add__(other)
        return RomanNumber(resultado)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    