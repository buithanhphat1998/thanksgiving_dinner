from plate_decorator import PlateDecorator

# Represents the Green Beans food item as a decorator for a Plate.
class GreenBeans(PlateDecorator):
    def description(self):
        """
        Extends the plate's description to include Green Beans.

        Returns:
            str: The updated description of the plate with Green Beans.
        """
        return super().description() +  " and Green Beans"
    def area(self):
        """
        Reduces the available area on the plate due to the addition of Green Beans.

        Returns:
            int: The remaining area on the plate after adding Green Beans.
        """
        return super().area() - 20
    def weight(self):
        """
        Reduces the remaining weight capacity of the plate due to the addition of Green Beans.

        Returns:
            int: The remaining weight capacity of the plate after adding Green Beans.
        """
        return super().weight() - 3
    def count(self):
        """
        Increases the count of food items on the plate by 1 for the addition of Green Beans.

        Returns:
            int: The updated count of food items on the plate.
        """
        return super().count() + 1