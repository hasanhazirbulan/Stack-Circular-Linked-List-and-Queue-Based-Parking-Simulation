# Stack-Circular-Linked-List-and-Queue-Based-Parking-Simulation



The project simulates the operation of a multi-level parking garage using Python. Its primary goal is to model the movement and management of cars within the garage while demonstrating the use of different data structures and algorithms.

Garage Structure:

The garage consists of three levels:

Ground Floor: The entry and exit point for cars, modeled as a queue (first-in, first-out).
Basement: A storage area for cars, modeled as a stack (last-in, first-out).
Second Floor: A circular parking area, modeled as a circular linked list.
Car Movement:

Cars enter the ground floor and join the queue to exit.
Cars can only leave the garage from the ground floor.
When a car leaves the ground floor, a random decision is made to either bring a car from the basement or the second floor to replace it.
If the basement is chosen, the last car in the stack (the most recently parked car) moves to the ground floor.
If the second floor is chosen, the Josephus Problem algorithm is used to select a car from the circular linked list, which then moves to the ground floor.
Josephus Problem:

This algorithm is used to select a car from the circular linked list on the second floor. It works by systematically eliminating cars in a circle based on a skipping pattern until only one car remains.

Empty Space Retention:

After a car is removed from the second floor, the empty space is retained in the circular linked list.

Simulation Output:

The simulation provides a detailed output showing:

The initial state of the garage (cars on each floor).
Each step of the simulation, including which car is removed from which floor and which car replaces it on the ground floor.
The final state of the garage (the last car remaining).
The average number of "parking problems" (cars processed) that the computer can solve in 5 seconds.
Project Objectives:

Educational: Demonstrate the application of various data structures (queue, stack, circular linked list) and algorithms (Josephus Problem) in a practical scenario.
Simulation: Model the real-world behavior of a multi-level parking garage.
Performance Analysis: Evaluate the efficiency of the simulation algorithm and data structures by measuring the average number of operations per second.
This project is a valuable learning tool for understanding fundamental data structures, algorithms, and simulation techniques in computer science.
