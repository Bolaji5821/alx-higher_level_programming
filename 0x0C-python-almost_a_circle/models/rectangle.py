#!/usr/bin/python3
"""Module rectangle:
Create a rectangle class inheriting from the Base class
"""

import json 
from models.base import Base

class Rectangle(Base):
    """class that describes a rectangle.
    Public instance methods:
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the rectangle instancee 
        

        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property 
        def width(self):
            """getter for the width attr"""

            return self.width

        @property
        def height(self):
            """getter for the height attr"""

            return self.height

        @property 
        def
