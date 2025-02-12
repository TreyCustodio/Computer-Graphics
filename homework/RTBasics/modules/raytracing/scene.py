"""
Author: Liz Matthews, Geoff Matthews
"""
import numpy as np
from .camera import Camera
from .objects import Sphere, Plane
from .ray import Ray
from .lights import PointLight
from .materials import Material
from ..utils.vector import vec

class Scene(object):
    """A class to contain all items in a scene.
       Contains a camera.
       Contains a list of lights.
       Contains a list of objects."""
    def __init__(self,
                 focus = vec(0,0.2,0),
                 direction = vec(0,0,-1),
                 up = vec(0,1,0),
                 fov = 45.0,
                 distance = 2.5,
                 aspect = 4/3):
        
        #   (1) Lights
        light_1 = PointLight((1,3,0), (1,1,1))
        self.lights = [light_1]
        

        #   (2) Spheres and Planes
        sphere_1 = Sphere(vec(0, 1, -3), material=Material((0.2,0.2,0.4),(0.2,0.2,1),(0.8,0.8,1), shine=5, specCoeff=0.1), radius=0.7)
        sphere_2 = Sphere(vec(-1, -0.2, -4), material=Material((0.2,0.4,0.2),(0.2, 1, 0.2),(0.8,1,0.8), shine=100, specCoeff=1.0), radius=0.7)
        sphere_3 = Sphere(vec(1, 0, -2.3), material=Material((0.4,0.2,0.2),(1,0.2,0.2),(1,0.8,0.8), shine=100, specCoeff=1.0), radius=0.7)
        
        plane_1 = Plane(vec(0,-1,0), material=Material((0.3, 0.3, 0.3), (0.7, 0.7, 0.7), (1,1,1), shine=5, specCoeff=0.1), normal=vec(0,1,0))
        
        self.objects = [
                        sphere_1, 
                        sphere_2, 
                        sphere_3,
                        plane_1
                        ]

        #   (3) Camera
        self.camera = Camera(focus, direction, up, fov, distance, aspect)
        
    
    def findNearest(self, ray, distances):
        """Helper code to find the nearest collision object and the distance to the object"""
        #   (1) Filter out None types
        real_distances = []
        for d in distances:
            if d != None and d != np.inf:
                real_distances.append(d)

        #   (2) Sort the filtered list in ascending order by distance from the ray's position
        #   Is there a more efficient way to do this?
        real_distances.sort(key=lambda x: np.linalg.norm(x[1] - ray.position))

        #   (3) Determine the nearest object and the distance
        if real_distances:
            #   (i) Nearest object is the first element in the sorted list
            nearestObj = real_distances[0][0]

            #   (ii) Minimum distance is in the same tuple as nearestObj
            minDistance = real_distances[0][1]

            #   (iii) Return both values
            return nearestObj, minDistance
        
        #   (5) Return None if there are no collisions
        else:
            return None, np.inf
        
    def nearestObject(self, ray):
        """Returns the nearest collision object and the distance to the object."""
        distances = [(o.intersect(ray)) for o in self.objects]
       
        return self.findNearest(ray, distances)
        

    def shadowed(self, obj, ray):
        """Returns the nearest collision object and the distance to the object,
           excluding obj."""
        distances = [o.intersect(ray) for o in self.objects if not o is obj]
        
        return self.findNearest(ray, distances)
        