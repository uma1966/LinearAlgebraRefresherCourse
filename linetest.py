from vector import Vector
from line import Line

print('############################################')
print('# parallel, equal, intersection of lines')
print('Equation1    Equation2   Intersection  parallel  equal')
l1 = Line(Vector(('4.046','2.836')), '1.21')
l2 = Line(Vector(('10.115','7.09')), '3.025')
print(str(l1),str(l2), str(l1.intersection(l2)), l1.parallel_to(l2), l1.equal_to(l2))

l3 = Line(Vector(('7.204','3.182')), '8.68')
l4 = Line(Vector(('8.172','4.114')), '9.883')
print(str(l3),str(l4), str(l3.intersection(l4)), l3.parallel_to(l4), l3.equal_to(l4))


l5 = Line(Vector(('1.182','5.562')), '6.744')
l6 = Line(Vector(('1.773','8.343')), '9.525')
print(str(l5),str(l6), str(l5.intersection(l6)), l5.parallel_to(l6), l5.equal_to(l6))

