from vector import *

print('###########################################')
print('Add, Subtract, scalar multiply')
# (1)
v41 = Vector([8.218,-9.341])
# print(v1)
v42 = Vector([-1.129,2.111])
# print(v2)
print(v41.add(v42))

# (2)
v43 = Vector((7.119,8.215))
v44 = Vector((-8.223,0.878))
print(v43.sub(v44))

# (3)
v45 = Vector((1.671,-1.012,-0.318))
print(v45.scalar_product(7.41))

print('###########################################')
print('magnitude & direction')
v61 = Vector((-0.221,7.437))
print(v61.magnitude())

v62 = Vector((8.813,-1.331,-6.247))
print(v62.magnitude())

print(Vector((5.581,-2.136)).normalized())

print(Vector((1.996,3.108,-4.554)).normalized())

#v61 = Vector((1.,1.,1.))
#v62 = v61.mult(2)
#print(str(v61) + ' -norm-> ' + str(v61.normalized()))
#print(str(v62) + ' -norm-> ' + str(v62.normalized()))

print('###########################################')
print('dot product & angle')
print(Vector((7.887,4.138)).dot_product(Vector((-8.802, 6.776))))

print(Vector((-5.955,-4.904,-1.874)).dot_product(Vector((-4.496, -8.755, 7.103))))

print(Vector((3.183,-7.627)).angle_with(Vector((-2.668, 5.319))))

print(Vector((7.35,0.221,5.188)).angle_with(Vector((2.751,8.259,3.985)),True))

print('###########################################')
print('parallel & orthogonal')

v101 = Vector(('-7.579','-7.88'))
v102 = Vector(('22.737','23.64'))
print(v101.is_parallel_to(v102), v101.is_orthogonal_to(v102))

v103 = Vector(('-2.029','9.97','4.172'))
v104 = Vector(('-9.231','-6.639','-7.245'))
print(v103.is_parallel_to(v104), v103.is_orthogonal_to(v104))

v105 = Vector(('-2.328','-7.284','-1.214'))
v106 = Vector(('-1.821','1.072','-2.94'))
print(v105.is_parallel_to(v106), v105.is_orthogonal_to(v106))

v107 = Vector(('2.118','4.827'))
v108 = Vector(('0','0'))
print(v107.is_parallel_to(v108), v107.is_orthogonal_to(v108))

print('###########################################')
print('projection')

v121 = Vector(('3.039', '1.879'))
v122 = Vector(('0.825', '2.036'))
print(v121.projection_parallel(v122))

v123 = Vector(('-9.88','-3.264', '-8.159'))
v124 = Vector(('-2.155', '-9.353', '-9.473'))
print(v123.projection_orthogonal(v124))

v125 = Vector(('3.009', '-6.172', '3.692', '-2.51'))
v126 = Vector(('6.404', '-9.144', '2.759', '8.718'))
v_parallel = v125.projection_parallel(v126)
v_orthogonal = v125.projection_orthogonal(v126)
print(v_parallel)
print(v_orthogonal)
print(v_parallel.add(v_orthogonal) == v125)

print(v125.projection_orthogonal(Vector.zero(v125.dimension)))