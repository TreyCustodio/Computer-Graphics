"""
Author: Liz Matthews, Geoff Matthews
"""
from ..utils.vector import vec, lerp, normalize
from .ray import Ray
import numpy as np

class Camera(object):
    """Camera object for raytracing.
    Initialization camera pointing
    at an arbitrary plane focus. Can get position
    and obtain a ray based on a percentage along
    the x and y of the focus plane."""

    def set(self,
            focus = vec(0,0,0),
            fwd = vec(0,0,-1),
            up = vec(0,1,0),
            fov = 90.0,
            distance = 2.5,
            aspect = 4/3):
        """Sets up the camera given the parameters.
           Calculates position, ul, ur, ll, and lr."""
        
        #   (1) Create some variables to help calculate the camera's positional data
        up = normalize(up)
        fwd = normalize(fwd)
        rt = normalize(np.cross(fwd, up))
        up = normalize(np.cross(rt, fwd))
        width  = 2 * distance * np.tan(np.radians(fov)/2)
        height = 2 * (1/aspect)

        #   (2) Calculate the camera's positional data
        
        ##  (i) Position
        self.position = focus - (fwd * distance)
        center = self.position + (fwd * distance) # same as focus

        ##  (ii) Upper Left
        self.ul = center + ((height / 2) * up) - ((width / 2) * rt)
        
        ##  (iii) Upper Right
        self.ur = center + ((height /2) * up) + ((width / 2) * rt)

        ##  (iv) Lower Left  
        self.ll = center - ((height / 2) * up) - ((width / 2) * rt)

        ##  (v) Lower Right
        self.lr = center - ((height / 2) * up) + ((width / 2) * rt)



    def __init__(self,
                 focus = vec(0,0,0),
                 fwd = vec(0,0,-1),
                 up = vec(0,1,0),
                 fov = 45.0,
                 distance = 2.5,
                 aspect = 4/3):
        self.set(focus, fwd, up, fov, distance, aspect)

    def getRay(self, xPercent, yPercent):
        """Returns a ray based on a percentage for the x and y coordinate."""

        #   Use lerp to calculate the ray's end point
        p0 = lerp(self.ul, self.ur, xPercent)
        p1 = lerp(self.ll, self.lr, xPercent)
        end = lerp(p0, p1, yPercent)

        #   Calculate the direction vector
        direction = (end - self.position)

        return Ray(self.position, direction)

    def getPosition(self):
        """Getter method for position."""
        return self.position
    
    def getDistanceToFocus(self, point):
        """Getter method for distance from the given point to the center of focus."""
        focus = (self.ul + self.ur + self.ll + self.lr) / 4
        return np.linalg.norm(point - focus)
