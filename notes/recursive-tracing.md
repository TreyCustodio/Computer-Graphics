#   Recursive Raytracing -- 2/10/2025

##  Reflected Ray
- given ray coming in, ray coming out,
- calculate i and j with dot products

##  Recursive Limit
- computers have finite memory
- base case
- stop recursive call after a set number of rounds

### Implementation
- getColorR includes recursive depth paramater (n)
  - start at 0, increase by 1
  - or start at n, decrease by 1 until 0

##  Reflection Factor
- what percentage of the final color is reflected?
- lerp btwn normal color and reflective color

#   Refraction
- ray coming in, surface normal, 

##  Index of Refraction
- angle depends on start medium and end medium
- denoted with fancy n
- known values
- refractive material mast have this property n
  - then use it to calculate where new direction is

### Snell's Law
- ratio used to calculate angles

- negative radicand = no refraction

##  Room appears upside down thru orb
- rays going thru center don't change much
- other rays get bent towards the surface normal, then away from the surface normal
- as the amount we bend by increases, the more flipped the world appears

##  Calculate Specular last

##  Final Equation
- light ray (u_r) striking transparent surface is split into two rays
- mirror reflected ray (u_m), transmitted ray (u_t)
- both rays lie in the plane formed by u_r and surface normal

##  Questions you should be able to answer
- what is refraction?
- what is fresnel effect?
- more about what the math doing as opposed to why it works
- how does the math affect the image

##  Rainbows
- each rgb component of ray is made of different wavelengths of light, each refracted differently
- red is bent less than violet
- refraction increases as you get closer to purple