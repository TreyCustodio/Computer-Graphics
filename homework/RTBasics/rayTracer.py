"""
Author: Liz Matthews, Geoff Matthews
"""
import numpy as np
import pygame

from render import ProgressiveRenderer, ShowTypes

from modules.raytracing.scene import Scene
from modules.utils.vector import vec, normalize
from modules.raytracing.lights import AbstractLight
from modules.raytracing.ray import Ray
from modules.utils.definitions import EPSILON

class RayTracer(ProgressiveRenderer):
    def __init__(self, width=800, height=600, show=ShowTypes.PerColumn):
        super().__init__(width, height, show=show)
        self.fog = vec(0.7,0.9,1.0)
        self.scene = Scene(aspect=width/height, fov=45)
    
    def getColorR(self, ray):
        # Start with zero color
        color = np.zeros((3))
        
        # Find any objects it collides with and calculate color
        nearest, dist = self.scene.nearestObject(ray)

        #   Return the color of the object
        if nearest:

            pos = ray.getPositionAt(dist)
            total = nearest.getAmbient()
            normal = nearest.getNormal(pos)
            diffuse = nearest.getDiffuse()
            specular = nearest.getSpecular()

            
            for light in self.scene.lights:
                
                #   Calculating the shadow with ray fills in the missing part of the green and red orb
                #   with gray. But why isn't the ray picking up on these colors in the first place?
                new_ray = Ray(pos + normal * EPSILON, light.getVectorToLight(pos))
                shadowed, shadow_dist = self.scene.shadowed(nearest, new_ray)
                
                if shadowed:
                    continue
                

                d = (diffuse - total) * max(0, np.dot(normal, light.getVectorToLight(pos)))
                total += d


                s = (specular - total) * (np.dot(normal, normalize(light.getVectorToLight(pos) - ray.direction)) ** nearest.getShine()) * nearest.getSpecularCoefficient()
                total += s
           
            return total

        # Return fog if doesn't hit anything
        else:
            return self.fog


    def getColor(self, x, y):
        # Calculate the percentages for x and y
        xPercent = x / 640
        yPercent = y / 480

        # Get the ray from the camera
        cameraRay = self.scene.camera.getRay(xPercent, yPercent)

        # Get the color based on the ray
        color = self.getColorR(cameraRay)

        # Fixing any NaNs in numpy, clipping to 0, 1.
        color = np.nan_to_num(np.clip(color, 0, 1), 0)
            
        return color

# Calls the 'main' function when this script is executed
if __name__ == '__main__':
    RayTracer.main("Ray Tracer Basics")
    pygame.quit()
