from plate_decorator import PlateDecorator
# Represents the Stuffing food item as a decorator for a Plate.
class Stuffing(PlateDecorator):
    def description(self):
        """
        Extends the plate's description to include Stuffing.

        Returns:
            str: The updated description of the plate with Stuffing.
        """
        return super().description() +  " and Stuffing"
    def area(self):
        """
        Reduces the available area on the plate due to the addition of Stuffing.

        Returns:
            int: The remaining area on the plate after adding Stuffing.
        """
        return super().area() - 18
    def weight(self):
        """
        Reduces the remaining weight capacity of the plate due to the addition of Stuffing.

        Returns:
            int: The remaining weight capacity of the plate after adding Stuffing.
        """
        return super().weight() - 7
    def count(self):
        """
        Increases the count of food items on the plate by 1 for the addition of Stuffing.

        Returns:
            int: The updated count of food items on the plate.
        """
        return super().count() + 1