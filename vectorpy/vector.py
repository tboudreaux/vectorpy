import numpy as np

class vector:  # Data type name
    def __init__(self, i=0, j=0, k=0, orig=None):  # default parameters
        if orig is None:
            self.x = i
            self.y = j
            self.z = k
        else:
            self.__copy_constructor__(orig)

    def __copy_constructor__(self, orig):
        self.x = orig.x
        self.y = orig.y
        self.z = orig.z

    def __repr__(self):      # overload print function
        return '<' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '>'

    def __add__(self, other):       # overload addition
        return vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):       # overload multiplication
        if type(other) is type(self):   # check if types are equivelent
            return self.x*other.x + self.y*other.y + self.z*other.z     # default to dot product
        elif 'int' in str(type(other)) or 'float' in str(type(other)):
            return vector(self.x*other, self.y*other, self.z*other)     # if scalar scalar multiply

    def __sub__(self, other):       # Overload subtraction
        return vector(self.x-other.x, self.y-other.y, self.z-other.z)

    def __radd__(self, other):      # Overload reverse addtion
        return self + other

    def __rmul__(self, other):      # overload reverse multiplication
        return self*other

    def __rsub__(self, other):      # overload reverse subtraction
        return self-other

    def __abs__(self):              # overload absolute value
        return np.sqrt((self.x**2) + (self.y**2) + (self.z**2))

    def __len__(self):
        return np.sqrt((self.x**2) + (self.y**2) + (self.z**2))

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return vector(self.x/other, self.y/other, self.z/other)

    def cx(self): return float(self.x)      # get x coord

    def cy(self): return float(self.y)      # get y coord

    def cz(self): return float(self.z)      # get z coord

    def __eq__(self, other):                # overload equality test
        if isinstance(other, self.__class__):       # check is types are equivilent
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):                # overload inequality test
        return not self.__eq__(other)

    def cross(self, other):     # Corss product
        return vector(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)

    def dot(self, other):       # dot product
        return self.x*other.x + self.y*other.y + self.z*other.z

    def __getitem__(self, key):
        try:
            assert isinstance(key, int)
        except AssertionError as e:
            e.args += ('Error! Index type must be int not {}'.format(type(key)), 'try with int')
            raise
        try:
            assert 0 <= key <= 2
        except AssertionError as e:
            e.args += ('Error! Vector index out of range', 'Valid indecies between 0 and 2')
            raise
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z

    def __setitem__(self, key, value):
        try:
            assert isinstance(key, int)
        except AssertionError as e:
            e.args += ('Error! Index type must be int not {}'.format(type(key)), 'try with int')
            raise
        try:
            assert 0 <= key <= 2
        except AssertionError as e:
            e.args += ('Error! Vector index out of range', 'Valid indecies between 0 and 2')
            raise
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value

    def aslist(self):
        return [self.x, self.y, self.z]