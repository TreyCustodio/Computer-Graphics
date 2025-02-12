#   Noise --- Computer Graphics Day 4 --- 1/24/2025
- define a function that looks like the "randomness" of nature

##  White Noise
- random.random() for each pixel
- appears like static
- random colors of pixels
- a bit too noisy

##  Pink Noise
- smooth, more aestetically pleasing
- "aesthetic random"
- fades between light and dark gradually
- computers pretend to be random

##  Wavelength
- the size of each detail
- adding sin waves together gives white noise (full max up/down)
- scaling using an amplitude and then adding gives pink noise
- sort of like a hash function; one input to the random function always gives you the same output

##  Spacing
- convert pixel space into noise space

### Conversion
- Divide by the wavelength (# of pixels per lattice square width)

##  latticeNoise(x)
- not storing information for every pixel -> way too much storage cost
- return white noise value between 0 and 1

### latticeNoise implementation
1. pick an arr size; n = 256
2. create arr of n floats evenly spaced between 0 and 1
  - (0.00, ..., 1.00)
3. randomize the index into a hash table
4. function uses the hash table to index the noise table
5. return noiseTable[hashTable[x%n]]
- note that a smaller hashtable means some values won't be used; larger hashtable means some values get used more than once

### Getting Values
- values = np.linspace(0, 1.0, n)
- permutations = np.arrange(0, n, 1)
- np.random.seed(1234)
- np.random.shuffle -> on both

### Interpolation
- gradually change distance from a to b
- need start value, end value, percentage of distance btwn them
- so lerp(a, b, p) = a + p(b-a)

### Finding lattice points
- px // latice size -> start
  - +1 = end
- px % lattice size

##  S Curve
- given (0,1), convert to (pi, 2pi)
- multiply by pi and add pi

##  smerpNoise
- changes percentage between points by more than lerp()
- divide sum by 2 (limit of summation of 1/2i = 1)

##  2D Interpolation
1. Hash values from (x,y)
2. set the parameter to *args and loop through args

##  SmerpNoise2D
- 