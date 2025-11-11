from small_plate import SmallPlate
from large_plate import LargePlate

from turkey import Turkey
from stuffing import Stuffing
from potatoes import Potatoes
from green_beans import GreenBeans
from pie import Pie
import check_input

def examine_plate(p): 
    while True:
        print("1. Turkey")
        print("2. Stuffing")
        print("3. Potatoes")
        print("4. Green Beans")
        print("5. Pie")
        print("6. Quit")
        match check_input.get_int_range("> ", 1,6):
            case 6: 
                return p
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
        # show plate strength (weight capacity remaining)
        print("Strength: ", end='')
        if (p.weight() >= 13): 
            print("Strong")
        elif p.weight() >= 7 and p.weight() <= 12: 
            print("Weak")
        else:
            print("Bending")
        
        print("Space available: ", end = '')
        if(p.area() >= 41): 
            print("Plenty")
        elif(p.area() >= 21 and p.area() <= 40):
            print("Some")
        else:
            print("Tiny")

        if(p.area() <= 0 or p.weight() <= 0):
            return None
        
def main():
    print("-Thanksgiving Dinner-")
    print("Serve yourself as much food as you\nlike from the buffet, but make sure\nthat your plate will hold without\nspilling everywhere!")
    print("Choose a plate")
    print("1. Small Strudy Plate")
    print("2. Large Flimsy Plate")

    match check_input.get_int_range("> ", 1,2):
        case 1: 
            small_serving_plate = SmallPlate()
            print(small_serving_plate.description())
            result = examine_plate(small_serving_plate)
            if result:
                print(f"Good Job! You made it to the table with {result.count()} items")
                print(f"There was still {result.area()} square inches left on your plate")
                print(f"Your plate could have held {result.weight()} more ounces of food")
                print("Don't worry, you can always go back for more. Happy Thanksgiving!")
            else: 
                print("Your plate isn't big enough for this much food! Your food spills over the edge.")


        case 2: 
            large_serving_plate = LargePlate()
            print(large_serving_plate.description())
            result = examine_plate(large_serving_plate)
            if result:
                print(f"Good Job! You made it to the table with {result.count()} items")
                print(f"There was still {result.area()} square inches left on your plate")
                print(f"Your plate could have held {result.weight()} more ounces of food")
                print("Don't worry, you can always go back for more. Happy Thanksgiving!")
            else: 
                print("Your plate isn't big enough for this much food! Your food spills over the edge.")
    
    
if __name__ == "__main__":
    main()