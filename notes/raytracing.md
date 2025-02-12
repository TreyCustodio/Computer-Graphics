#   Raytracing -- Computer Graphics Day 5 1/27

##  Object Order
- openGL
- for each object in the world, find the colors it would place on the screen

##  Image Order
- for each pixel on the screen, find the color it should be
- pixels go onto the objects

## Process
- seeing a mere fraction of the rays emitted by light source
- light hits the object and bounces off,
- hitting our eyes and creating shadows

##  Ray
- a portion of a line; mimicking rays emitted from light source
- each point on the line defined by p and v
  - p + xv

### Calculate the Ray
- v = start - end
  - = (q, v)
- normalize the vector

##  Right Handed Coordinate System
- orientation of x,y,z is arbitrary
- normalize vectors; find center
  - c = p + df

##  Ray Collision
- eventually the ray will collide with an object
- and the ray after that point should be the color of the object
- where did it hit? determines shadow
- calculate collision point (some distance t along the ray)

##  Collision on Sphere
- center and radius
- find t s.t. the ray touches the sphere at t
- 2 collision points

### Calculating t
- p + tv = 2 points
- | p + tv |^2 = r^2
  - magnitude
- quadratic formula to find t
- (p dot p) + 2(p dot v)t + (v dot v)t^2 - r^2 = 0
- a = (v dot v)
- b = 2(p dot v)
- c = (p dot p) - r^2

##  Planes
- defined by point and vector
- n is the center vector; v is the ray
- want to find the point where v collides with the plane
- v dot n -> if (-), moving toward object; if (+), moving away from object
- h = (p-q) dot n
- t = distance from v to collision point
- find theta between v and the normal, negative (gravity) vector
- 