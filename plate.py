from abc import ABC, abstractmethod

class Plate(ABC):
    @abstractmethod
    def description(self):
        """
        Provides a description of the plate and its contents.

        Returns:
            str: A string describing the plate and the food items on it.
        """
        pass
    @abstractmethod
    def area(self):
         """
        Calculates the remaining area available on the plate.

        Returns:
            int: The remaining area in square inches.
        """
         pass
    @abstractmethod
    def weight(self):
        """
        Calculates the remaining weight capacity of the plate.

        Returns:
            int: The remaining weight capacity in ounces.
        """
        pass
    @abstractmethod
    def count(self):
        """
        Counts the number of food items currently on the plate.

        Returns:
            int: The number of food items on the plate.
        """
        pass
