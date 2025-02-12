#   Pygame Basics - in reference to graphics

##  General Algorithm
1. Display rendered images
2. Check for input
3. Update the display based on the input

##  Setup
screen = pygame.display.set_mode(<size>) -> surface

##  Double Buffered Rendering
- double buffered drawing -> why we invoke flip() to avoid flickering
- secret surface that you draw to when you invoke draw on the screen
- does not draw to the visual screen until you invoke flip()

##  Checking Input
- in order to quit
- event queue contains the events in the order they occur (first in, first out)
- for event in pygame.event.get() -> the event queue
- pygame.QUIT -> tells pygame to terminate itself
  - if event.type == pygame.QUIT

##  event.mod
- bitmask representing all modifying keys pressed at the same time

#  Progressive Renderer
- render pictures in progressively higher resolutions
- rough first, then better and better
- begins with 256x256 pixel-sized chunks
- you'll get smaller and smaller pixels
- shows what current pixel size is in the command line


#  MISC
- changing pixels on a computer screen is one of the slowest processes a computer performs