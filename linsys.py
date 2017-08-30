"""
Uwe Maurer 2017
"""

from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def swap_rows(self, row1, row2):
        self[row1], self[row2] = self[row2], self[row1]

    def multiply_coefficient_and_row(self, coefficient, row):
        plane = self[row]
        new_normal_vector = plane.normal_vector.scalar_product(coefficient)
        new_constant_term = plane.constant_term * coefficient
        self[row] = Plane(new_normal_vector, new_constant_term)

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        plane = self[row_to_add]
        plane_to_add = Plane(plane.normal_vector.scalar_product(coefficient), plane.constant_term*coefficient)
        plane = self[row_to_be_added_to]
        self[row_to_be_added_to] = Plane(
            plane.normal_vector.add(plane_to_add.normal_vector),
            plane.constant_term + plane_to_add.constant_term)

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    def clear_coefficients_below(self, column, row):
        """
        Sets coefficients in column to zero in all equations blow the one
        in row.
        """
        for i in range(row+1, len(self)):
            c = -(MyDecimal(self[i].normal_vector[column]) / MyDecimal(self[row].normal_vector[column]))
            self.add_multiple_times_row_to_row(c, row, i)

    def find_nonzero_coefficient_below(self, column, row):
        """
        Returns index of row with first nonzero coefficient in given column,
        starting in given row. Returns None if no nonzero coefficient was found.
        """
        for i in range(row+1, len(self)):
            if self[i].normal_vector[column] != 0:
                return i
        return None

    def compute_triangular_form(self):
        system = deepcopy(self)
        #num_equations = len(system)
        num_variables = system.dimension
        j = 0
        for i, plane in enumerate(system.planes):
            while j < num_variables:
                c = MyDecimal(plane.normal_vector[j])
                if c.is_near_zero():
                    i_nonzero = system.find_nonzero_coefficient_below(j, i)
                    if i_nonzero is not None:
                        system.swap_rows(i, i_nonzero)
                    else:
                        j += 1
                        continue
                system.clear_coefficients_below(j, i)
                j += 1
                break
        # print('triangular form:')
        # print(system)
        return system

    def clear_coefficients_above(self, column, row):
        """
        Sets coefficients in column to zero in all equations above the one
        in row.
        """
        for i in range(row-1, -1 ,-1):
            c = -self[i].normal_vector[column]
            self.add_multiple_times_row_to_row(c, row, i)

    def compute_rref(self):
        """
        Computes the reduced row echelon form of the equation system and
        returns this as a new system.
        """
        tf = self.compute_triangular_form()

        pivot_indices = tf.indices_of_first_nonzero_terms_in_each_row()

        for row in range(len(tf)-1,-1,-1):
            # Set col to first nonzero coefficient in row:
            col = pivot_indices[row]
            # go to next row if there is no nonzero coefficient:
            if col < 0:
                continue
            # Scale row to make coefficient of variable in col be 1:
            factor = Decimal('1.0') / tf[row].normal_vector[col]
            tf.multiply_coefficient_and_row(factor, row)
            # Clear all terms with variable in col in rows above row:
            tf.clear_coefficients_above(col, row)

        return tf

    def solve(self):
        rref = self.compute_rref()
        print(rref)
        # 1. System is inconsistent if one row is 0 = k for k <> 0
        for plane in rref.planes:
            try:
                Plane.first_nonzero_index(plane.normal_vector)
            except Exception as ex:
                if str(ex) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    k = MyDecimal(plane.constant_term)
                    if not k.is_near_zero():
                        # row is 0 = k for k <> 0, so no solution
                        return None
                else:
                    raise ex
        # 2. Indefinite number of solutions, if number of free variables (pivots) < dimension of solution set
        pivot_indices = rref.indices_of_first_nonzero_terms_in_each_row()
        num_pivots = sum([1 if index >= 0 else 0 for index in pivot_indices])
        if num_pivots < rref.dimension:
            return "Indefinite number of solutions (dimension: {})".format(num_pivots)

        # 3. Consistent set has unique solution <=> each variable is a pivot variable
        solution_coords = [rref.planes[row].constant_term for row in range(rref.dimension)]
        return Vector(solution_coords)

    def __len__(self):
        return len(self.planes)

    def __getitem__(self, i):
        return self.planes[i]

    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


if __name__ == '__main__':
    p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
    p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
    p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
    p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

    s = LinearSystem([p0,p1,p2,p3])

    print(s.indices_of_first_nonzero_terms_in_each_row())
    print('{}, {}, {}, {}'.format(s[0], s[1], s[2], s[3]))
    print(len(s))
    print(s)

    s[0] = p1
    print(s)

    print(MyDecimal('1e-9').is_near_zero())
    print(MyDecimal('1e-11').is_near_zero())