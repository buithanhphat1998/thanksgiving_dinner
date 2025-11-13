from plate_decorator import PlateDecorator
# Represents the Pie food item as a decorator for a Plate.
class Pie(PlateDecorator):
    def description(self):
        """
        Extends the plate's description to include Pie.

        Returns:
            str: The updated description of the plate with Pie.
        """
        return super().description() + " and Pie"
    def area(self):
        """
        Reduces the available area on the plate due to the addition of Pie.

        Returns:
            int: The remaining area on the plate after adding Pie.
        """
        return super().area() - 19
    def weight(self):
        """
        Reduces the remaining weight capacity of the plate due to the addition of Pie.

        Returns:
            int: The remaining weight capacity of the plate after adding Pie.
        """
        return super().weight() - 8
    def count(self):
        """
        Increases the count of food items on the plate by 1 for the addition of Pie.

        Returns:
            int: The updated count of food items on the plate.
        """
        return super().count() + 1