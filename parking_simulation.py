import random
from collections import deque
import time


# Car class to represent a car with its color
class Car:
    def __init__(self, color):
        self.color = color


# Josephus problem algorithm (returns index of car to remove)
def josephus(n, k):
    circle = deque(range(n))  # Create a circular list of indices
    while len(circle) > 1:  # While more than one car remains
        circle.rotate(-k)  # Rotate k positions to the left
        circle.popleft()  # Remove the car at the current position
    return circle[0]  # Return the index of the last remaining car


# Main simulation function
def parking_simulation():
    colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Brown", "Black", "White", "Gray", "Cyan",
              "Magenta", "Pink", "Olive", "Teal"]
    cars = [Car(color) for color in colors]  # Create list of Car objects
    random.shuffle(cars)  # Shuffle cars for random distribution

    # Initialize parking floors
    ground_floor = deque(cars[:5])  # First 5 cars to ground floor (queue)
    basement = cars[5:10]  # Next 5 cars to basement (stack)
    second_floor = list(cars[10:])  # Remaining cars to second floor (list)

    print("\nInitial state:")  # Print initial state of the garage
    print("Ground Floor:", ", ".join(car.color for car in ground_floor))
    print("Basement:", ", ".join(car.color for car in basement))
    print("Second Floor:", ", ".join(car.color for car in second_floor))

    iterations = 0  # Counter for processed cars
    start_time = time.time()  # Record start time for performance measurement

    while ground_floor:  # Continue until the ground floor is empty
        iterations += 1

        removed_car = ground_floor.popleft()  # Remove the first car from the ground floor
        print(f"\nIteration {iterations}: Removed car {removed_car.color} from the ground floor")

        # Choose a source floor randomly, but only if either basement or second floor is not empty
        source_floor = random.choice(["basement", "second"]) if basement or second_floor else None
        if source_floor == "basement" and basement:  # If basement is chosen and not empty...
            next_car = basement.pop()  # ...remove the last car from the basement...
            print(f"Moved car {next_car.color} from the basement to the ground floor")
            ground_floor.append(next_car)  # ...and add it to the ground floor
        elif source_floor == "second" and second_floor:  # If second floor is chosen and not empty...
            removed_index = josephus(len(second_floor), 2)  # ...use Josephus to find the index of the car to remove...
            next_car = second_floor.pop(removed_index)
            if next_car is not None:  # ...and if it's not an empty slot...
                print(f"Moved car {next_car.color} from the second floor to the ground floor")
                ground_floor.append(next_car)  # ...add it to the ground floor
            second_floor.insert(removed_index, None)  # Mark the slot as empty

        print("Ground Floor:", ", ".join(car.color for car in ground_floor))
        print("Basement:", ", ".join(car.color for car in basement))
        print("Second Floor:",
              ", ".join(car.color if car else "Empty" for car in second_floor))  # Print "Empty" for empty slots

    end_time = time.time()  # Record end time for performance measurement
    total_time = end_time - start_time
    print(f"\nLast car remaining: {ground_floor[0].color if ground_floor else None}")

    # Calculate average problems solved per second
    problems_per_second = iterations / total_time if total_time > 0 else 0
    print(f"\nAverage problems solved in 5 seconds: {problems_per_second * 5:.2f}")


# Run the simulation 100 times to get a more accurate average
for _ in range(100):
    parking_simulation()
