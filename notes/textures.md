#   Calculated Textures

##  Fog and Sight Distance
- the further away from viewer, the more faded it becomes
- this is called atmospheric haze
- objects become closer to the sky color

###  Approach
- calculate the distance from intersection to camera's view plane center
- calculate what percent the distance is along the sight distance

##  Surface Textures
- wrap a 2D image around a 3D object
### 3D Materials exist in space
- determine color based on world coordinate of intersection btwn x, y, z

### Stripes
- use (x,y,z) at intersection to look up what color it should be
- if x%2 == 0: black else white
- alternating units of x

### Checkerboard
- alternating in 2 directions
- check (x // size) + (y // size) + (z // size) % 2

##  3D Noise
- interpolating between 2 different colors; not materials
- calculating ambient, diffuse, and specular
  - ambient is multiplying by a value less than 1
  - specular is multiplying by a value greater than 1