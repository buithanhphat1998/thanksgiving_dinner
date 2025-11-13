from abc import ABC, abstractmethod
from plate import Plate
# Abstract base class for decorating a Plate object.
# Implements the Plate interface and delegates method calls to the wrapped Plate object.
class PlateDecorator(Plate, ABC):
    def __init__(self, p):
        """
        Initializes the PlateDecorator with a Plate object.

        Args:
            p (Plate): The Plate object to be decorated.
        """
        self._plate = p
    def description(self):
        """
        Provides a description of the plate and its contents.

        Returns:
            str: A string describing the plate and the food items on it.
        """
        return self._plate.description()
    def area(self):
        """
        Calculates the remaining area available on the plate.

        Returns:
            int: The remaining area in square inches.
        """
        return self._plate.area()
    def weight(self):
        """
        Calculates the remaining weight capacity of the plate.

        Returns:
            int: The remaining weight capacity in ounces.
        """
        return self._plate.weight()
    def count(self):
        """
        Counts the number of food items currently on the plate.

        Returns:
            int: The number of food items on the plate.
        """
        return self._plate.count()