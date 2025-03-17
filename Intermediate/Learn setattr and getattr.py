class Car:
    pass
data = {"model": "Ford Fiesta", "color": "black", "max_speed": 220, "price": 16000}

car = Car()

#assign attributes from dictionary dynamically
for key, value in data.items():
    setattr(car, key, value)

#dynamic print
for key in data.keys():
    print(f"{key}: {getattr(car, key, 'Not Available')}")  #"Not Available" for missing attributes

setattr(car, "hp", 82)
print("HP:", car.hp)

#if an attribute exists
if hasattr(car, "model"):
    print(f"Normally the car {car.model} will cost you {car.price} euro")


attribute_name = "price"
new_value = 15000
setattr(car, attribute_name, new_value)
print(f"Currently there is a dicount, so the new {attribute_name} is: {getattr(car, attribute_name)} euro")


def add_multiple_attributes(obj, attr_dict):
    for key, value in attr_dict.items():
        setattr(obj, key, value)

add_multiple_attributes(car, {
    "transmission": "5 speed manual transmission",
    "fuel_type": "Gasoline",
    "torque": "114 nm",
    "fuel_tank_capacity": 42,
    "turbo": False
})

# Print the added attributes
print(f"Transmission: {car.transmission}")
print(f"Fuel Type: {car.fuel_type}")
print(f"Torque: {car.torque}")
print(f"Fuel Tank Capacity: {car.fuel_tank_capacity} liters")
print(f"Turbo: {car.turbo}")

#covert to dict
car_dict = {attr: getattr(car, attr) for attr in car.__dict__}
print("Car as dictionary:", car_dict)

def honk(self):
    return f"\n{self.model} says: Honk! Honk!"

setattr(Car, "honk", honk)    #ddding method to the Car class
print(car.honk())             #calling dynamically added method


#get- / setattr(object, attribute_name, default_value)
