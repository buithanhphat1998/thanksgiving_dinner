from plate import Plate

# Represents a large, flimsy plate.
# This plate has a fixed area, weight capacity, and initially contains no food items.
class LargePlate(Plate):
    def description(self):
        """
        Provides a description of the plate.

        Returns:
            str: A string describing the plate as "Large Flimsy Plate".
        """
        return "Large Flimsy Plate"
    def area(self):
        """
        Returns the total area of the plate.

        Returns:
            int: The area of the plate in square inches (113).
        """
        return 113
    def weight(self):
        """
        Returns the weight capacity of the plate.

        Returns:
            int: The weight capacity of the plate in ounces (24).
        """
        return 24
    def count(self):
        """
        Returns the initial count of food items on the plate.

        Returns:
            int: The number of food items on the plate (0).
        """
        return 0