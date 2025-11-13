from plate_decorator import PlateDecorator
from plate import Plate 
# Represents the Turkey food item as a decorator for a Plate.
class Turkey(PlateDecorator):
    def description(self):
        """
        Extends the plate's description to include Turkey.

        Returns:
            str: The updated description of the plate with Turkey.
        """
        return super().description() +  " and Turkey"
    def area(self):
        """
        Reduces the available area on the plate due to the addition of Turkey.

        Returns:
            int: The remaining area on the plate after adding Turkey.
        """
        return super().area() - 15
    def weight(self):
        """
        Reduces the remaining weight capacity of the plate due to the addition of Turkey.

        Returns:
            int: The remaining weight capacity of the plate after adding Turkey.
        """
        return super().weight() - 4
    def count(self):
        """
        Increases the count of food items on the plate by 1 for the addition of Turkey.

        Returns:
            int: The updated count of food items on the plate.
        """
        return super().count() + 1