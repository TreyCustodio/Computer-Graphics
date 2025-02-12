from render import ProgressiveRenderer, ShowTypes
from modules.utils.noise import NoisePatterns
from modules.utils.vector import lerp, smerp
import numpy as np
import pygame
import random


class RandomRenderer(ProgressiveRenderer):
    def __init__(self, width=640, height=480,
                 showTime=True,
                 show=ShowTypes.PerColumn,
                 minimumPixel=0,
                 startPixelSize=256):
        """An unnecessary override but provided to show how
        to override the __init__ in future inheritance classes."""
        super().__init__(width, height,
                 showTime,
                 show,
                 minimumPixel,
                 startPixelSize)
        
    def getColor(self, x, y):
        """Gives a random color per pixel."""
        return np.array((random.random(),
                         random.random(),
                         random.random()))
    
    def handleOtherInput(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            type(self).restart()


class RainbowRenderer(ProgressiveRenderer):
    """
    The color it will create is based on the x and y coordinates
    as a percentage of the total width and height.
    """
    def __init__(self, width=640, height=480,
                showTime=True,
                show=ShowTypes.PerColumn,
                minimumPixel=0,
                startPixelSize=256):
        
        super().__init__(width, height,
                 showTime,
                 show,
                 minimumPixel,
                 startPixelSize)
        
        #   Red, Green, and Blue Visualization Options
        ##  0 -> horizontal percentage
        ##  1 -> vertical percentage
        ##  2 -> 100% - horizontal percentage
        ##  3 -> 100% - vertical percentage
        self.red_option = 0
        self.green_option = 1
        self.blue_option = 2

    def getColor(self, x, y):
        """
        Defines the red, green, and blue components
        based on the horizontal percentage,
        vertical percentage, 100% - horizontal%,
        and 100% - vertical%.
        
        """
        #   (1.) Define our r,g,b components
        horizontal_percentage = (x / self.width)
        vertical_percentage = (y / self.height)
        horizontal_difference = (1 - horizontal_percentage)
        vertical_difference = (1 - vertical_percentage)


        #   (2.) Print statements for debugging
        # print("horizontal: " + str(horizontal_percentage))
        # print("vertical: " + str(vertical_percentage))
        # print("blue: " + str(horizontal_difference))
        # print()


        #   (3.) Set each color component
        
        #   (i.) Red
        if self.red_option == 0:
            red = horizontal_percentage
        elif self.red_option == 1:
            red = vertical_percentage
        elif self.red_option == 2:
            red = horizontal_difference
        elif self.red_option == 3:
            red = vertical_difference

        #   (ii.) Green
        if self.green_option == 0:
            green = horizontal_percentage
        elif self.green_option == 1:
            green = vertical_percentage
        elif self.green_option == 2:
            green = horizontal_difference
        elif self.green_option == 3:
            green = vertical_difference

        #   (iii.) Blue
        if self.blue_option == 0:
            blue = horizontal_percentage
        elif self.blue_option == 1:
            blue = vertical_percentage
        elif self.blue_option == 2:
            blue = horizontal_difference
        elif self.blue_option == 3:
            blue = vertical_difference


        #   (4.) Return the color in the form of a numpy array
        return np.array((red,
                         green,
                         blue))
    
    def handleOtherInput(self, event):
        """
        Pressing the 1, 2, or 3 keys
        advance the red, green, or blue components
        as follows:
        
        horizontal percentage -> vertical percentage ->
        100% - horizontal percentage -> 100% - vertical percentage
        """
        if event.type == pygame.KEYDOWN:

            #   (1.) Advance Red
            if event.key == pygame.K_1:
                self.red_option += 1
                self.red_option %= 4
            
            #   (2.) Advance Green
            elif event.key == pygame.K_2:
                self.green_option += 1
                self.green_option %= 4
            
            #   (3.) Advance Blue
            elif event.key == pygame.K_3:
                self.blue_option += 1
                self.blue_option %= 4  
            
            #   (4.) Space -> Restart
            elif event.key == pygame.K_SPACE:
                type(self).restart()


class NoiseRenderer(ProgressiveRenderer):
    def __init__(self, width=640, height=480,
                showTime=True,
                show=ShowTypes.PerColumn,
                minimumPixel=0,
                startPixelSize=256):
        
        super().__init__(width, height,
                 showTime,
                 show,
                 minimumPixel,
                 startPixelSize)
        
        self.id = 0
        instance = NoisePatterns.getInstance()
        self.patterns = [instance.clouds, 
                         instance.cloudsTiled,
                         instance.marble,
                         instance.wood,
                         instance.fire
                         ]
    
    
    def getColor(self, x, y, scale=64):
        """
        Divides x and y by the scale
        and then calls the current method of noise.
        """
        #   No integer division here
        return self.patterns[self.id](x / scale, y / scale)
    

    def handleOtherInput(self, event):
        """
        Handle other inputs from the user.
        """
        if event.type == pygame.KEYDOWN:

            #   (1.) Space -> Restart
            if event.key == pygame.K_SPACE:
                type(self).restart()

            #   (2.) q -> decrease pattern id
            elif event.key == pygame.K_q:
                if self.id > 0:
                    self.id -= 1
                else:
                    self.id = 4

            #   (3.) w -> increase pattern id
            elif event.key == pygame.K_w:
                self.id += 1
                self.id %= len(self.patterns)
            
            #   (4.) e -> call previous()
            elif event.key == pygame.K_e:
                NoisePatterns.getInstance().previous()
            
            #   (5.) r -> call next()
            elif event.key == pygame.K_r:
                NoisePatterns.getInstance().next()
    
# Calls the 'main' function when this script is executed
if __name__ == '__main__':
    try:
        #RandomRenderer.main()
        RainbowRenderer.main()
        NoiseRenderer.main()

    finally:
        pygame.quit()
