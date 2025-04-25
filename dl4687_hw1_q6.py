class Vector:
    def __init__(self, d):
        if isinstance(d,int):
            self.coords = [0]*d
        else:
            self.coords = d
    def __len__(self):
        return len(self.coords)
    def __getitem__(self, j):
        return self.coords[j]
    def __setitem__(self, j, val):
          self.coords[j] = val
    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError(”dimensions must agree”)
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        return self.coords == other.coords
    def __ne__(self, other):
        return not (self == other)
    def __str__(self): 
        return ’<’+ str(self.coords)[1:−1] + ’>’
    def __repr__(self): 
        return str(self)
    def __sub__(self,other):
        new_lst = Vector()
        new_lst.coords = []
        if len(self.coords) > len(other.coords):
            for i in range(len(other.coords):
                           new_lst.coords.append(self.coords[i] - other.coords[i])
            for i in range(len(other.coords),len(self.coords)):
                           new_lst.coords.append(self.coords[i])
        else:
            for i in range(len(self.coords):
                           new_lst.coords.append(self.coords[i] - other.coords[i])
            for i in range(len(self.coords),len(other.coords)):
                           new_lst.coords.append(-1*other.coords[i])
                           
        return new_lst
    def __neg__(self):
        new_vect = Vector()
        new_vect.coords = self.coords
        for i in range(len(new_vect.coords)):
            new_vect[i]*=-1
        return new_vect
    def __mul__(self,d):
        if isinstance(d,int):
            new_vect = Vector()
            new_vect.coords = self.coords
            for i in range(len(new_vect.coords)):
                new_vect.coords[i] *= d
            return new_vect
        else:
            new_vect = Vector()
            new_vect.coords = self.coords
            for i in range(len(new_vect.coords)):
                new_vect.coords[i] *= d.coords[i]
            return new_vect
            
    def __rmul__(self,d):
        new_vect = Vector()
        new_vect.coords = self.coords
        for i in range(len(new_vect.coords)):
            new_vect.coords[i] *= d
        return new_vect

v1 = Vector(5)
v1[1] = 10
v1[−1] = 10
print(v1)
            





