#   Coordinates, Linear Algebra, and NumPy Computer --- Graphics Day 2 -- 1/15/2025

##  Points
- points exist in space without a coordinate system

##  Vectors
- subtracting two points = a vector (euclid dist)
- a direction and a magnitude
- no position
- (end - start)
- u = r - s
- vectors do not have positions
  - vectors of equal value at different positions are the same
  - consider 2 game objects at different positions with the same vel

###  Scalars
- Multiplication is repeated addition
- with v = (3 + 5), 2v = 2(3 + 5)

### Magnitude
- length of the vector
- how much distance one instance of that vector will travel
- calculate with pythagorean theorem
- the sqrt of the dimensions dxd

### Unit Vector
- a unit vector is a vector whose magnitude is one
- achieve by dividing by magnitude
- consistent distance calculations
- u / |u|
- diagonal movement in top-down games

### Plane
- at point p, two vectors (u, v) originate
- any point on this plane is defined by p, u, v
- origin point of <0, 0> and unit vectors <1,0> and <0,1>

### Frames
- tuple consisting of the origin point and n vectors
- gives coordinates to points
- f = <p, u, v>
- you can solve the linear equation
- given p = (4,7), u = (-2, 3), v = (0,-2), q = (5,2)
- p + au + bv = q
- 4 + a(-2) + b(0) = 5 (for x)
- -2a = 1
- a = 1/2
- 7 + 3a + (-2)b = 2
- 7 + (3/2) - 2b = 2
- b = 1.75

### Affine Sums
- define a sum 0<= a <= 1
- v = (1-a)v_1 + av_2

### NumPy Arrays
- adding / subtracting is frequent in graphics
- python's built-n lists do not support vector operations
- NumPy has arrays that support vector operations

##  Trig

### Dot product
- defined in 2D
- u (dot) v = cos(angle between u and v) * |u| |v|
- normalizing two vectors and calculating dot product gives you the angle
- consider angles between light sources
- so x = cos(theta) |V|
- all about rearranging known equations to find unknown values
- scalar = v (dot) u / |u|

##  Reflected Ray
- looking into a mirror, light is reflected off the surface
- we want to find what the reflected value
- projection of a onto r
- n changes
- find i and j
- assume |n| == 1
- then a = i + h
- r = -i + j
- i = (a dot n)*|n|
- or i = (a(dot n) / n(dot n)) * n
- j = a - i

##  Distance point to line
- how to find distance from point q to point r
- define a vector v from q to r
- define a vector u from q to p
- now we have x (connecting p to the line v) and y
- use dot product to solve for x and y
- 