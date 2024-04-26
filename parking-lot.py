import time  #Importing the time module for delaying the first input
import random  #Importing the random module for generating random numbers

class Vehicle:  #Defining a class to represent a vehicle
    def __init__(self, license_plate):  #Constructor method to initialize a vehicle with a license plate
        self.license_plate = license_plate  #Assigning the license plate to the vehicle object

class ParkingSpot:  #Defining a class to represent a parking spot
    def __init__(self, spot_number):  #Constructor method to initialize a parking spot with a spot number
        self.spot_number = spot_number  #Assigning the spot number to the parking spot object
        self.is_available = True  #Initializing the availability of the parking spot to True (empty)
        self.parked_vehicle = None  #Initializing the parked vehicle to None (no vehicle parked)

    def park_vehicle(self, vehicle):  #Method to park a vehicle in the parking spot
        self.is_available = False  #Setting the availability of the spot to False (occupied)
        self.parked_vehicle = vehicle  #Assigning the parked vehicle object to the parking spot

    def remove_vehicle(self):  #Method to remove a vehicle from the parking spot
        self.is_available = True  #Setting the availability of the spot to True (empty)
        removed_vehicle = self.parked_vehicle  #Storing the parked vehicle before removal
        self.parked_vehicle = None  #Removing the parked vehicle from the spot
        return removed_vehicle  #Returning the removed vehicle

class ParkingLot:  #Defining a class to represent a parking lot
    def __init__(self, capacity):  #Constructor method to initialize the parking lot with a capacity
        self.capacity = capacity  #Assigning the capacity of the parking lot
        self.spots = [ParkingSpot(i) for i in range(1, capacity + 1)]  #Creating parking spots in the lot
        self.queue = 0  #Initializing the queue count to 0

    def display_current_status(self):  #Method to display the current status of the parking lot
        print("Current Status:")  #Printing the header for current status
        for spot in self.spots:  #Iterating through each parking spot in the lot
            if spot.is_available:  #Checking if the spot is available (empty)
                print(f"{spot.spot_number}. Vacant at G{spot.spot_number}")  #Printing vacant spot info
            else:
                print(f"{spot.spot_number}. {spot.parked_vehicle.license_plate} parked at G{spot.spot_number}")  #Printing occupied spot info
        vacant_spots = sum(spot.is_available for spot in self.spots)  #Counting vacant spots
        occupied_spots = self.capacity - vacant_spots  #Calculating occupied spots
        print("Vacant spots available -->", vacant_spots)  #Printing vacant spots count
        print("Vehicles occupied -->", occupied_spots)  #Printing occupied spots count
        print("Vehicles in the Queue -->", self.queue)  #Printing vehicles in the queue count
        print("Total number of parking spots -->", self.capacity)  #Printing total parking spots count

    def update_status(self, vehicles_in, vehicles_out):  #Method to update the parking lot status based on vehicles in and out
        for _ in range(vehicles_in):  #Loop to handle vehicles going inside the parking lot
            available_spot = self.find_farthest_available_spot()  # Finding the farthest available spot
            if available_spot:  #Checking if there is an available spot
                license_plate = f"Dubai-A-{random.randint(10, 99)}"  #Generating a random Dubai license plate
                vehicle = Vehicle(license_plate)  #Creating a vehicle object
                available_spot.park_vehicle(vehicle)  #Parking the vehicle in the spot
                print(f"{available_spot.spot_number}. {vehicle.license_plate} parked at G{available_spot.spot_number} (just parked)")  #Printing parking info
            else:
                if self.queue > 0:  #Checking if there are vehicles in the queue
                    self.queue -= 1  #Decrementing the queue count
                    print("Vehicle added to the Queue.")  #Printing queue update info
                else:
                    print("PARKING IS FULL! You are in the Queue, Expected waiting time is 3 minutes")  #Printing parking full info
                break  #Exiting loop if parking is full

        for _ in range(vehicles_out):  #Loop to handle vehicles leaving the parking lot
            occupied_spots = [spot for spot in self.spots if not spot.is_available]  #Finding occupied spots
            if occupied_spots:  #Checking if there are occupied spots
                spot_to_remove = random.choice(occupied_spots)  #Choosing a spot to remove vehicle randomly
                removed_vehicle = spot_to_remove.remove_vehicle()  #Removing vehicle from the spot
                print(f"{spot_to_remove.spot_number}. {removed_vehicle.license_plate} left from G{spot_to_remove.spot_number} (Just left)")  #Printing leaving vehicle info
            else:
                print("No vehicles to remove.")  #Printing no vehicles to remove info
                break  #Exiting loop if no vehicles to remove

    def find_farthest_available_spot(self):  #Method to find the farthest available spot in the parking lot
        farthest_spot = None  #Initializing variable to store the farthest spot
        max_distance = 0  #Initializing variable to store the maximum distance
        for spot in self.spots:  #Iterating through each parking spot in the lot
            if spot.is_available:  #Checking if the spot is available (empty)
                if spot.spot_number > max_distance:  #Checking if the spot is farther than current max
                    max_distance = spot.spot_number  #updating max distance
                    farthest_spot = spot  #Updating farthest spot
        return farthest_spot  #Returning the farthest available spot

if __name__ == "__main__":  #Main execution block
    print("Welcome to Dubai Paid parking zone")  #Printing welcome message
    time.sleep(3)  #Pausing for 3 seconds
    print("3")  #Printing countdown
    time.sleep(1)  #Pausing for 1 second
    print("2")  #Printing countdown
    time.sleep(1)  #Pausing for 1 second
    print("1")  #Printing countdown
    time.sleep(1)  #Pausing for 1 second

    parking_lot = ParkingLot(25)  #Creating a parking lot with 25 spots

    #Randomly fill some parking lots
    for _ in range(random.randint(1, 10)):  #Loop to randomly fill some parking spots
        available_spot = parking_lot.find_farthest_available_spot()  #Finding available spot
        if available_spot:  #Checking if there is an available spot
            license_plate = f"Dubai-A-{random.randint(10, 99)}"  #Generating random license plate
            vehicle = Vehicle(license_plate)  #Creating a vehicle object
            available_spot.park_vehicle(vehicle)  #Parking the vehicle in the spot

    #display current status
    parking_lot.display_current_status()  #Displaying the current status of the parking lot

    #First input
    vehicles_in = int(input("First Input: how many vehicles going inside the parking lot --> "))  #getting number of vehicles going inside

    #Update status after vehicles going inside
    vacant_spots = sum(spot.is_available for spot in parking_lot.spots)  #counting vacant spots
    if vehicles_in > vacant_spots:  #Checking if more vehicles are going inside than vacant spots available
        parking_lot.queue += vehicles_in - vacant_spots  #Adding extra vehicles to the queue
        vehicles_in = vacant_spots  #Limiting the number of vehicles going inside to vacant spots

    parking_lot.update_status(vehicles_in, 0)  #updating parking lot status after vehicles going inside

    #display status before second input
    parking_lot.display_current_status()  #Displaying the current status of the parking lot

    #Second input
    vehicles_out = int(input("Second Input: how many vehicles leaving the parking lot --> "))  # Getting number of vehicles leaving

    #Update status after vehicles leaving
    parking_lot.update_status(0, vehicles_out)  #Updating parking lot status after vehicles leaving

    #Display final status
    parking_lot.display_current_status()  #Displaying the final status of the parking lot
