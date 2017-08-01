from vector import Vector
from line import Line

print('############################################')
print('# parallel, equal, intersection of lines')
l1 = Line(Vector(('4.046','2.836')), '1.21')
l2 = Line(Vector(('10.115','7.09')), '3.025')
l1.equal_to(l2)
print(str(l1),str(l2), l1.intersection(l2), l1.parallel_to(l2), l1.equal_to(l2))

#lx = Line(Vector(('','')), '')