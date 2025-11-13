from plate_decorator import PlateDecorator
# Represents the Potatoes food item as a decorator for a Plate.
class Potatoes(PlateDecorator):
    def description(self):
        """
        Extends the plate's description to include Potatoes.

        Returns:
            str: The updated description of the plate with Potatoes.
        """
        return super().description() +  " and Potatoes"
    def area(self):
        """
        Reduces the available area on the plate due to the addition of Potatoes.

        Returns:
            int: The remaining area on the plate after adding Potatoes.
        """
        return super().area() - 18
    def weight(self):
        """
        Reduces the remaining weight capacity of the plate due to the addition of Potatoes.

        Returns:
            int: The remaining weight capacity of the plate after adding Potatoes.
        """
        return super().weight() - 6
    def count(self):
        """
        Increases the count of food items on the plate by 1 for the addition of Potatoes.

        Returns:
            int: The updated count of food items on the plate.
        """
        return super().count() + 1