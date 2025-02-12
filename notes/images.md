#   Images -- Computer Graphics Day 1 -- 1/13/2025
- computers deal with images constantly

##  Pixels
- how we store information about an image
- individual small points -> **pointillism**
- there is an infinite amount of information you can see with your eyes
- combined pixels appear to be one continuous image

##  Primary Colors
- how do we combine colors together to make new ones?
- traditionally, they are **red, blue, yellow**
- computers use **red, green, blue**

### Additive vs Subtractive
- rgb combine to create white, they are absorbing light -> **additive**
- ryb combine to create black, they are reducing light -> **subtractive**

### Wavelength
- our eyes are most sensitive to green
- least sensitive to blue

## RGB Values
- color values are stored as rgb values
- represented as some amount of red, green, and blue out of a maximum intensity

### RGB Modes
1. 255 mode
  - 255 possibilities in 8 bits used to represent one color

2. 1.0 mode
  - each value is between 0 and 1.0
  - more intuitive for humans; represents percentage
  - better for multiplying

3. Convert by multiplying / dividing by 255

##  Raster
- an array of pixels
- displayed on a screen, arranged in a 2D grid
- rasterization = converting data into an array of pixels

##  Rendering
- generating 2D images from 3D scenes
- convert 3D into 2D

##  Scenes
- describe what we are trying to rasterize

##  Frustrum

##  Projection
- projecting objects onto a line or plane
- convert N dimensions to M dimensions (M < N)
- take a 3D set of data and smush down to 2D
- captures perspective; objects increase in size the further away from the projector

### Orthographic
- constant projection, no perspective

##  Objects
- objects describe physical properties in a scene
- have color
- have material that determines how light affects it

##  Light and Shading
- Light needs to exist for a color to be seen
- The source of light in a scene tells what lights are available
- Anywhere light can't reach creates a shadow

##  Textures
- images applied to a surface
- coloring, map of an objects surface 
- bump-mapping -> adjusting a surface to make it look bumpy

##  Spaces
- everything is relative to a point of view
- left in reference to who?

### World Space
- longitude, latitude
- from the perspective of the world

### Screen Space
- stage left, left on screen

### Object Space
- from an object's perspective (you, me, it)

###  Converting from World Space to Screen Space
- cameras in 2D video games -> position = top-left of the screen
- knowing the top-left of the world and its width and height,

##  Aspect Ratio
- width (x) versus height (y) ration
- 16:9 -> widescreen
- if translation source has different aspect ratio, your image will be squished or stretched
- constantly getting pixels from the world and rendering it to the screen

##  Programming for Computers vs Humans
- LaTex assumes you are writing plaintext
- so you use an escape character to indicate you are coding / formatting
- traditional APIs assume you are coding, and you use an escape char to indicate plaintext

## LaTeX Syntax
### Useful commands
- % -> comments
- \\ -> newline
- \ -> escape char
- / -> command
- \textbf{} -> bold
- \textit{} -> italics
- ''quote'' -> quotation marks
- \verb|| -> display verbatim
- \vfill -> fill out verticle

### Lists
- \begin{itemize} -> begin an itemized list
  - \item
- \end{itemize}

- \begin{enumerate} -> begin a numbered list
  - \item



### Math Mode
- $ -> switch to math mode; symbols take on new meaning
- log_{2}, x^2, \frac{1}{2}, \vect{1}{2}
- remember to stop math mode with another $

### Graphicx Package
- extra graphics functionality
- can add pdf pages directly

### Tabular format
- \begin{tabular}
- \end{tabular}
- | -> indicate vertical lines
- \hline -> draw horizontal line

###  TikZ
- package for drawing diagrams
- \begin{tikzpicture}
- \draw (2,1) -- (x,y) -- (x,y);
- \draw [dashed] (0,2) -- (x,y) -- (x,y)
- \fill (x,y) circle (2pt) node[anchor=south] {$p0$};
- \end{tikzpicture}

### Alternatives
- gimp, google images, anything so that your image is clear

### Errors
- compile frequently