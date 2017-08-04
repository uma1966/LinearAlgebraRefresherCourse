from vector import Vector
from plane import Plane

print('############################################')
print('# parallel, equal, intersection of lines')
print('Equation1    Equation2   Intersection  parallel  equal')
l1 = Plane(Vector(('-0.412','3.806','0.728')), '-3.46')
l2 = Plane(Vector(('1.03','-9.515','-1.82')), '8.65')
print(str(l1),str(l2), str(l1.intersection(l2)), l1.parallel_to(l2), l1 == l2)

l3 = Plane(Vector(('2.611','5.528','0.283')), '4.6')
l4 = Plane(Vector(('7.715','8.306','5.342')), '3.76')
print(str(l3),str(l4), str(l3.intersection(l4)), l3.parallel_to(l4), l3 == l4)


l5 = Plane(Vector(('-7.926','8.625','-7.217')), '-7.952')
l6 = Plane(Vector(('-2.642','2.875','-2.404')), '-2.443')
print(str(l5),str(l6), str(l5.intersection(l6)), l5.parallel_to(l6), l5 == l6)

