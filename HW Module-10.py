class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom = bottom_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        print(f"\nMoving elevator {elevator_number} to floor {destination_floor}:")
        self.elevators[elevator_number - 1].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("\n--- FIRE ALARM! ALL ELEVATORS RETURNING TO BOTTOM FLOOR ---")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)

my_building = Building(0, 15, 3)
my_building.run_elevator(1, 7)
my_building.run_elevator(2, 10)
my_building.fire_alarm()

import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed = max(0, min(self.max_speed, self.current_speed + change))

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"\n{self.name} - Status Update")
        print(f"{'Plate':<10} | {'Max Speed':<10} | {'Current Speed':<15} | {'Distance':<10}")
        print("-" * 60)
        for car in self.cars:
            print(f"{car.registration_number:<10} | {car.max_speed:<10} | "
                  f"{car.current_speed:<15} | {car.travelled_distance:<10.1f} km")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False



participating_cars = []
for i in range(1, 11):
    new_car = Car(f"ABC-{i}", random.randint(100, 200))
    participating_cars.append(new_car)

derby_race = Race("Grand Demolition Derby", 8000, participating_cars)

hours_passed = 0
while not derby_race.race_finished():
    derby_race.hour_passes()
    hours_passed += 1

    if hours_passed % 10 == 0:
        print(f"\nTime passed: {hours_passed} hours")
        derby_race.print_status()

print(f"\nRace Finished after {hours_passed} hours!")
derby_race.print_status()