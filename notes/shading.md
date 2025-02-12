#   Shading -- Computer Graphics Day 6 -- 1/29/2025

##  (1.) Phong Reflection
- estimating light
- need 3 properties for our math:

### Surface Normal
- a vector that represents the direction of a surface
- orientation of the surface
- calculated based on where light hits
- n = p - c

### Light Source
- adds the ability to see a scene
- light can be colored
- 2 kinds of light:

#### Directional Light
- parallel light, moving as though it were a line

#### Point Light
- light radiates outwards from a point

### Vector to the Light Source

####    Point Light
- v = np.norm(hit point - location of light)

####    Directional Light
- a constant direction vector

### Vector to the camera


##  (2.) Diffuse Coloring
- Gives shading falloff of light
- section of an object with light upon it has more color

### Lambertian Reflection
- objects with rough surfaces **reflect light equally in all directions**

### Light Energy
- proporitional to the **cosine of the angle of incidence**

### Calculation
- sign of cosine(theta) -> get colorless shaded objects
- colorful, shaded objects = colorless shaded objects * colored unshaded objects
- 1.0 mode

### Ambient color
- light mixes with objects
- approximate with small amount of light

### Calculation 2
- begin with ambient color
- calculate diffuse cosine value to add diffuse color
- take (colors - ambient color) * diffused colors
- add this to ambient color

##  (3.) Specular Highlights
- specs atop objects conveying shininess
- spots are tiny blurry images of light source
- so if you move, it will change position on the orb

### Reflection Vector
- assume all vectors are normalized

### Specular Shininess


##  (4.) Colored Light

##  (5.) Shadows
- if an object blocks the light source, there should be a shadow on the object below/behind it
- only add diffuse or specular if not shadowed

### Self-shadowing
- dont let an orb shadow itself

####    Offset Hit Point using epsilon
- hit point + epsilon

####    Exclude Object from Collision
- exclude a specific object from the collision method

##  (6.) Classes

### Material Class - material atop objects
- ambient, diffuse, specular

### Object3D - objects to render
- material, position
- obtain surface normal, obtain intersection given a ray



##  Misc
- in a game, in screenmanager, you should add a displayLight(position) method
  - runs and adjusts every frame

- Python has ABC class -> ensures the class is not implemented, erego it is abstract