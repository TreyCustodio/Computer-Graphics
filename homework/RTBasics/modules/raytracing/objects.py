"""
Author: Liz Matthews, Geoff Matthews
"""
import numpy as np
from abc import ABC, abstractmethod


class Object3D(ABC):
    """Abstract base class for all objects in the raytraced scene.
       Has a position, material.
       Has getter methods for all material properties.
       Has abstract methods intersect and getNormal."""
    def __init__(self, pos, material):
        self.position = np.array(pos)
        self.material = material
    
    def getAmbient(self, intersection=None):
        """Getter method for the material's ambient color.
           Intersection parameter is unused for Ray Tracing Basics."""
        return self.material.getAmbient()
    
    def getDiffuse(self, intersection=None):
        """Getter method for the material's diffuse color.
           Intersection parameter is unused for Ray Tracing Basics."""
        return self.material.getDiffuse()
    
    def getSpecular(self, intersection=None):
        """Getter method for the material's specular color.
           Intersection parameter is unused for Ray Tracing Basics."""
        return self.material.getSpecular()
      
    def getShine(self):
        """Getter method for the material's shininess factor."""
        return self.material.getShine()
    
    def getSpecularCoefficient(self, intersection=None):
        """Getter method for the material's specular coefficient.
           Intersection parameter is unused for Ray Tracing Basics."""
        return self.material.getSpecularCoefficient()
       
    @abstractmethod
    def intersect(self, ray):
        """Find the intersection for the given object. Must override."""
        pass
   
    @abstractmethod
    def getNormal(self, intersection):
        """Find the normal for the given object. Must override."""
        pass


class Sphere(Object3D):
    def __init__(self, pos, material, radius):
        super().__init__(pos, material)
        self.r = radius
    
    def intersect(self, ray):
        """Find the intersection for the given object. Must override."""

        #   (1) Calculate the coefficients of the quadratic equation
        pos = ray.position - self.position
        a = np.dot(ray.direction, ray.direction)
        b = 2 * np.dot(pos, ray.direction)
        c = np.dot(pos, pos) - (self.r ** 2)


        #   (2) Find the roots = (-b +/- sqrt(b^2 - 4ac)) / 2a

        #   (i) Find the discriminant
        disc = (b**2) - (4*a*c)
        
        #   (ii) Discriminant < 0 means there are no real roots
        if disc < 0:
            return np.inf
        
        #   (iii) Otherwise calculate the roots
        else:
            root_1 = (-b + np.sqrt(disc)) / (2*a)
            root_2 = (-b - np.sqrt(disc)) / (2*a)
        
        #   (iv) Find the smallest, positive root
        if root_1 > 0 and root_2 > 0:
            solution = min(root_1, root_2)
        
        elif root_1 > 0:
            solution = root_1

        elif root_2 > 0:
            solution = root_2
        
        else:
            return np.inf
        
        #   (3) Return the collision point
        return self, solution
   
    def getNormal(self, intersection):
        """Find the normal for the given object. Must override."""
        normal = (intersection - self.position) / np.linalg.norm(intersection - self.position)
        return normal
    
class Plane(Object3D):
    def __init__(self, pos, material, normal):
        super().__init__(pos, material)
        self.normal = normal
    
    def intersect(self, ray):
        #   (1) Set up our calculations
        dot_1 = np.dot(ray.direction, self.normal)

        if dot_1 > 0:
            return None
        
        cosine = np.dot(ray.direction, -self.normal)
        height = np.dot(ray.position - self.position, self.normal)

        #   (2) Calculate and return the collision point
        solution = height / cosine
        if solution < 0:
            return None
        else:
            return self, solution
    
    def getNormal(self, intersection):
        return self.normal