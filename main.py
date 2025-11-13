""" CECS 277 – Lab 12 – Class Relationships
11/12/2025
    Group 4
    Student 1: Thanh Phat Bui
    Student 2: Ha Gia Bao Hoang
Description: Thanksgiving Dinner : Using the Decorator pattern, create a game that has the user add food to their plate without going
over the weight or area limit of a paper plate. There are two different base types of plates: a
small, sturdy 10-inch paper plate, or a large, flimsy, 12-inch plate. The plates can then be
decorated with five different types of food: Turkey, Stuffing, Potatoes, Green Beans, and
Pumpkin Pie. Each serving of the different foods has a weight, in ounces, and an area, in square
inches. The user may load up their plate at the buffet as much as they like, but if the area or
weight limit of the plate is surpassed, then their food falls to the floor."""
from small_plate import SmallPlate
from large_plate import LargePlate

from turkey import Turkey
from stuffing import Stuffing
from potatoes import Potatoes
from green_beans import GreenBeans
from pie import Pie
import check_input

def examine_plate(p): 
    """
    Allows the user to add food items to their plate and checks the plate's capacity.

    Args:
        p (Plate): The plate object to be examined and decorated with food items.

    Returns:
        Plate or None: The updated plate object if it can hold the food, or None if the plate's limits are exceeded.
    """
    while True:
        # Display food options
        print("1. Turkey")
        print("2. Stuffing")
        print("3. Potatoes")
        print("4. Green Beans")
        print("5. Pie")
        print("6. Quit")

        # Get user input for food selection
        match check_input.get_int_range("> ", 1,6):
            case 6: 
                return p  # Exit and return the plate
            case 1: 
                p = Turkey(p)
                print(p.description())
            case 2: 
                p = Stuffing(p)
                print(p.description())
            case 3: 
                p = Potatoes(p)
                print(p.description())
            case 4: 
                p = GreenBeans(p)
                print(p.description())
            case 5: 
                p = Pie(p)
                print(p.description())
       # Display the plate's current strength (weight capacity remaining)
        print("Strength: ", end='')
        if (p.weight() >= 13): 
            print("Strong")
        elif p.weight() >= 7 and p.weight() <= 12: 
            print("Weak")
        else:
            print("Bending")
         # Display the plate's current space availability (area remaining)
        print("Space available: ", end = '')
        if(p.area() >= 41): 
            print("Plenty")
        elif(p.area() >= 21 and p.area() <= 40):
            print("Some")
        else:
            print("Tiny")
        # Check if the plate has exceeded its limits
        if(p.area() <= 0 or p.weight() <= 0):
            return None
        
def main():
    print("-Thanksgiving Dinner-")
    print("Serve yourself as much food as you\nlike from the buffet, but make sure\nthat your plate will hold without\nspilling everywhere!")
    print("Choose a plate")
    print("1. Small Strudy Plate")
    print("2. Large Flimsy Plate")
     # Get user input for plate selection
    match check_input.get_int_range("> ", 1,2):
        case 1: 
            small_serving_plate = SmallPlate()
            print(small_serving_plate.description())
            result = examine_plate(small_serving_plate)
            if result:
                # Display success message
                print(f"Good Job! You made it to the table with {result.count()} items")
                print(f"There was still {result.area()} square inches left on your plate")
                print(f"Your plate could have held {result.weight()} more ounces of food")
                print("Don't worry, you can always go back for more. Happy Thanksgiving!")
            else:
                # Display failure message
                print("Your plate isn't big enough for this much food! Your food spills over the edge.")


        case 2: 
            large_serving_plate = LargePlate()
            print(large_serving_plate.description())
            result = examine_plate(large_serving_plate)
            if result:
                # Display success message
                print(f"Good Job! You made it to the table with {result.count()} items")
                print(f"There was still {result.area()} square inches left on your plate")
                print(f"Your plate could have held {result.weight()} more ounces of food")
                print("Don't worry, you can always go back for more. Happy Thanksgiving!")
            else: 
                # Display failure message
                print("Your plate isn't big enough for this much food! Your food spills over the edge.")
    
    
if __name__ == "__main__":
    main()