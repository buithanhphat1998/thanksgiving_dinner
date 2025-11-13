from plate import Plate
# Represents a small, sturdy plate.
# This plate has a fixed area, weight capacity, and initially contains no food items.
class SmallPlate(Plate):
    def description(self):
        """
        Provides a description of the plate.

        Returns:
            str: A string describing the plate as "Small Sturdy Plate".
        """
        return "Small Sturdy Plate"
    def area(self):
        """
        Returns the total area of the plate.

        Returns:
            int: The area of the plate in square inches (78).
        """
        return 78
    def weight(self):
        """
        Returns the weight capacity of the plate.

        Returns:
            int: The weight capacity of the plate in ounces (32).
        """
        return 32
    def count(self):
        """
        Returns the initial count of food items on the plate.

        Returns:
            int: The number of food items on the plate (0).
        """
        return 0