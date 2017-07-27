from vector import *




##########################################
# Add, Subtract, scalar multiply
print('Add, Subtract, scalar multiply')
# (1)
v1 = Vector([8.218,-9.341])
# print(v1)
v2 = Vector([-1.129,2.111])
# print(v2)
print(v1.add(v2))

# (2)
v3 = Vector((7.119,8.215))
v4 = Vector((-8.223,0.878))
print(v3.sub(v4))

# (3)
v4 = Vector((1.671,-1.012,-0.318))
print(v4.scalar_product(7.41))

###########################################
# magnitude & direction

print('magnitude & direction')
v5 = Vector((-0.221,7.437))
print(v5.magnitude())

v6 = Vector((8.813,-1.331,-6.247))
print(v6.magnitude())

print(Vector((5.581,-2.136)).normalized())

print(Vector((1.996,3.108,-4.554)).normalized())

#v61 = Vector((1.,1.,1.))
#v62 = v61.mult(2)
#print(str(v61) + ' -norm-> ' + str(v61.normalized()))
#print(str(v62) + ' -norm-> ' + str(v62.normalized()))

###########################################
# dot product & angle
print('dot product & angle')
print(Vector((7.887,4.138)).dot_product(Vector((-8.802, 6.776))))

print(Vector((-5.955,-4.904,-1.874)).dot_product(Vector((-4.496, -8.755, 7.103))))

print(Vector((3.183,-7.627)).angle_with(Vector((-2.668, 5.319))))

print(Vector((7.35,0.221,5.188)).angle_with(Vector((2.751,8.259,3.985)),True))

###########################################
# parallel & orthogonal
print('parallel & orthogonal')

v71 = Vector(('-7.597','-7.88'))
v72 = Vector(('22.737','23.64'))
print(v71.is_parallel_to(v72), v71.is_orthogonal_to(v72))

v71 = Vector(('-2.029','9.97','4.172'))
v72 = Vector(('-9.231','-6.639','-7.245'))
print(v71.is_parallel_to(v72), v71.is_orthogonal_to(v72))

v71 = Vector(('-2.328','-7.284','-1.214'))
v72 = Vector(('-1.821','1.072','-2.94'))
print(v71.is_parallel_to(v72), v71.is_orthogonal_to(v72))

v71 = Vector(('2.118','4.827'))
v72 = Vector(('0','0'))
print(v71.is_parallel_to(v72), v71.is_orthogonal_to(v72))
