
from functools import total_ordering

@total_ordering
class Special_Methods:
    def __init__(self,value,module):
        if not isinstance(module,int):
            raise TypeError("incompatibility for module")
        if not isinstance(value, int):
            raise TypeError("incompatibility for value")
        if module <=0:
            raise ValueError("the modulus must be positive")


        self._module=module
        self._value=value%module


    @property
    def module(self):
        return self._module

    @property
    def value(self):
        return self._value

    def __repr__(self):
        return f"Special methods-->({self.value}, {self.module})"


    def __int__(self):
        return self.value


    def __eq__(self,other):
        if isinstance(other,Special_Methods):
            if self.module != other.module:
                return NotImplemented
            else:
                return self.value==other.value
        elif isinstance(other,int):
            return other % self.module==self.value
        else:
            return NotImplemented

    
    def __hash__(self):
        return hash((self.value, self.module))

    def __neg__(self):
        return Special_Methods(-self.value, self.module)

    def __add__(self,other):
        if isinstance(other,Special_Methods) and self.module==other.module:
            return Special_Methods(self.value+other.value, self.module)
        if isinstance(other,int):
            return Special_Methods(self.value+other, self.module)
        return NotImplemented

    def __sub__(self,other):
        if isinstance(other,Special_Methods) and self.module==other.module:
            return Special_Methods(self.value-other.value, self.module)
        if isinstance(other,int):
            return Special_Methods(self.value-other, self.module)
        return NotImplemented


    def __mul__(self,other):
        if isinstance(other,Special_Methods) and self.module==other.module:
            return Special_Methods(self.value*other.value, self.module)
        if isinstance(other,int):
            return Special_Methods(self.value*(other % self.module), self.module)
        return NotImplemented

    def __pow__(self,other):
        if isinstance(other,Special_Methods) and self.module==other.module:
            return Special_Methods(self.value**other.value, self.module)
        if isinstance(other,int):
            return Special_Methods(self.value**(other % self.module), self.module)
        return NotImplemented

    def __iadd__(self,other):
        if isinstance(other,Special_Methods) and self.module==other.module:
            self.value=(self.value+other.value)% self.module
            return self
        if isinstance(other,int):
            self.value=(self.value+other)%self.module
            return self
        return NotImplemented


    def __isub__(self,other):
        if isinstance(other,Special_Methods) and self.module==other.module:
            self.value=(self.value-other.value)% self.module
            return self
        if isinstance(other,int):
            self.value=(self.value-other)%self.module
            return self
        return NotImplemented

    def __imul__(self,other):
        if isinstance(other,Special_Methods) and self.module==other.module:
            self.value=(self.value*other.value)% self.module
            return self
        if isinstance(other,int):
            self.value=(self.value*other)%self.module
            return self
        return NotImplemented

    def __ipow__(self,other):
        if isinstance(other,Special_Methods) and self.module==other.module:
            self.value=(self.value**other.value)% self.module
            return self
        if isinstance(other,int):
            self.value=(self.value**(other % self.module))%self.module
            return self
        return NotImplemented


    def __lt__(self,other):
        if isinstance(other,Special_Methods) and self.module==other.module:
            return self.value < other.value
        if isinstance(other,int):
            return self.value < other % self.module
        return NotImplemented







