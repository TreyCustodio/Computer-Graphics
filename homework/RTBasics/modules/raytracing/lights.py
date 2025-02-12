from abc import ABC, abstractmethod
from ..utils.vector import vec, normalize
import numpy as np

class AbstractLight(ABC):
    def __init__(self, color):
        self.color = color
    
    def getColor(self):
        """Returns the color of the light"""
        return self.color
        
    @abstractmethod
    def getVectorToLight(self, point):
        """Returns a vector pointing towards the light"""
        pass
    
    @abstractmethod
    def getDistance(self, point):
        """Returns the distance to the light"""
        pass

class PointLight(AbstractLight):
    def __init__(self, position, color):
        super().__init__(color)
        self.position = vec(position)

    def getVectorToLight(self, point):
        """Returns a vector pointing towards the light"""
        return normalize(self.position - point)
    
    def getDistance(self, point):
        """Returns the distance to the light"""
        return np.linalg.norm(point - self.position)