
class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year,make,model,door,roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.door = door
        self.roof = roof

def ask_user():
    vehicle_type = input("what kind of vehicle ")
    year = input("Enter a year ")
    make = input("Enter a make ")
    model = input("enter the model ")
    while True:
        door = input("How many doors 2 or 4 ")
        if door == "2" or "4":
            break
    while True:
        roof = input("what kind of roof sun or regular ")
        if roof == "sun" or "regular":
            break
    car = Automobile(
        vehicle_type=vehicle_type,
        year=year,
        make=make,
        model=model,
        door=door,
        roof=roof,
    )

    print(f"Vehicle type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.door}")
    print(f"Type of roof: {car.roof}")
if __name__ == "__main__":
    ask_user()


   