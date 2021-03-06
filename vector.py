import math
from decimal import Decimal, getcontext

getcontext().prec = 30


class VectorException(Exception):
    pass


class NormalizeZeroVectorException(VectorException):
    pass


class NoUniqueParallelComponent(NormalizeZeroVectorException):
    pass


class NoUniqueOrthogonalComponent(NormalizeZeroVectorException):
    pass


class Vector(object):

    @classmethod
    def zero(cls, dimension):
        "returns a zero vector of given dimension"
        return Vector([0 for x in range(dimension)])

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector({})'.format([round(x,3) for x in self.coordinates])

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __getitem__(self, i):
        return self.coordinates[i]

    def add(self, other):
        if self.dimension != other.dimension:
            raise ValueError('Dimensions do not match (' + str(self.dimension) + ' != ' + str(other.dimension) + ')')
        result = [x+y for x,y in zip(self.coordinates, other.coordinates)]
        return Vector(result)

    def sub(self,other):
        if self.dimension != other.dimension:
            raise ValueError('Dimensions do not match (' + str(self.dimension) + ' != ' + str(other.dimension) + ')')
        result = [x-y for x,y in zip(self.coordinates, other.coordinates)]
        return Vector(result)

    def scalar_product(self, factor):
        """Skalarprodukt"""
        f = Decimal(factor)
        result = [x*f for x in self.coordinates]
        return Vector(result)

    def magnitude(self):
        """Betrag"""
        result = math.sqrt(sum([x**2 for x in self.coordinates]))
        return Decimal(result)

    def normalized(self):
        """Normalenvektor"""
        try:
            return self.scalar_product(Decimal('1.0') / self.magnitude())
        except ZeroDivisionError:
            raise NormalizeZeroVectorException('Cannot normalize the zero vector')

    def dot_product(self, other):
        """Skalarprodukt"""
        result = sum([x * y for x, y in zip(self.coordinates, other.coordinates)])
        return result

    def angle_with(self, other, in_degrees=False):
        angle = self.magnitude() * other.magnitude()
        angle = self.dot_product(other) / angle
        angle = math.acos(round(angle, 10)) # without rounding there might be numerical issues...
        if in_degrees:
            return 180. / math.pi * angle
        else:
            return angle

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def is_orthogonal_to(self,other, tolerance=1e-10):
        dot = self.dot_product(other)
        return abs(dot) < tolerance

    def is_parallel_to(self,other):
        is_zero = self.is_zero()
        other_zero = other.is_zero()
        angle = self.angle_with(other)
        return is_zero or other_zero or angle == 0 or angle == math.pi

    def projection_parallel(self, base):
        "Projektion von self auf base"
        try:
            b_norm = base.normalized()
            v_mag = self.dot_product(b_norm)
            return base.normalized().scalar_product(v_mag)
        except NormalizeZeroVectorException:
            raise NoUniqueParallelComponent()

    def projection_orthogonal(self, base):
        "Ortogonale zur Projektion von self auf base"
        try:
            projection = self.projection_parallel(base)
            return self.sub(projection)
        except NormalizeZeroVectorException:
            raise NoUniqueOrthogonalComponent()

    def cross_product(self, other):
        "Kreuzprodukt"
        if self.dimension != other.dimension:
            raise ValueError('vectors must have same dimension for building cross product')
        v = Vector(self.coordinates)
        w = Vector(other.coordinates)
        if v.dimension < 3:
            # Extend dimension to 3 assuming 0
            v.coordinates.extend([0 for _ in range(3-v.dimension)])
            w.coordinates.extend([0 for _ in range(3-w.dimension)])
        if v.dimension != 3 or w.dimension != 3:
            raise ValueError('cross product defined for 1-3 dimensions only')
        r1 = v[1]*w[2] - v[2]*w[1]
        r2 = -(v[0]*w[2] - v[2]*w[0])
        r3 = v[0]*w[1] - v[1]*w[0]
        return Vector((r1, r2, r3))

    def area_of_parallelogram(self, other):
        # Alternatively:
        # height = other.projection_orthogonal(self).magnitude()
        # return self.magnitude() * height
        return self.cross_product(other).magnitude()

    def area_of_triangle(self, other):
        return self.area_of_parallelogram(other) / Decimal('2.0')