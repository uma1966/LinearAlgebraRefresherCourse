from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Plane(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 3

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Plane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Plane.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)

    def parallel_to(self, other):
        # planes are parellel if their normal vectors are parallel
        result = self.normal_vector.is_parallel_to(other.normal_vector)
        return result

    def equal_to(self, other):
        # Check special case normal vector is the zero vector:
        if self.normal_vector.is_zero():
            if not other.normal_vector.is_zero():
                return False
            else:
                # coefficients of equation are zero --> planes are
                # equal if constant terms are equal
                diff = self.constant_term - other.constant_term
                return MyDecimal(diff).is_near_zero()
        elif other.normal_vector.is_zero():
            return False

        if not self.parallel_to(other):
            # non parallel planes can't be equal
            return False
        # Check if vector between one point on each line is orthogonal to the planes normal vectors
        # First connect the basepoints:
        connecting_vector = self.basepoint.sub(other.basepoint)
        # Then check orthogonality to normal vector (as the planes
        # are parallel it is sufficient to check with just one normal vector):
        orthogonal = connecting_vector.is_orthogonal_to(self.normal_vector)
        return orthogonal

    def __eq__(self, other):
        return self.equal_to(other)

    def intersection(self, other):
        """Intersection for 3 dimensions"""
        if self.dimension != 3:
            raise Exception("intersection implemented for 3 dimensions only")
        if self.parallel_to(other):
            if self.equal_to(other):
                # equal planes have an indefinite number of intersections,
                # so we return the plane itself:
                return self
            else:
                # parallel planes have no intersection
                return None
        else:
            return "not parallel"
        # else calculate x,y,z for equation system, assuming
        # A and B are not 0 at the same time (this is the case because
        # they are not parallel). Equation system is:
        #  A*x + B*y + C*z = k1
        #  D*x + E*y + F*z = k2
        """
        A,B,C = self.normal_vector.coordinates
        k1 = self.constant_term
        D,E,F = other.normal_vector.coordinates
        k2 = other.constant_term
        x = 0
        y = 0
        return Vector((x,y))
        """


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps