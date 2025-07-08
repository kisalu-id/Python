class Car:
    DEFAULT_KM_TOLERANCE = 5000
  
    def __init__(self, vin: str, manufacturer: str, model: str, year: int, km: int = 0, km_tolerance: int = None):
        self.vin = vin                     #Vehicle Identificsion Number
        self.manufacturer = manufacturer
        self.model = model
        self.year = year                   #manufacturing year
        self.km = km                       #km driven
        self.km_tolerance = km_tolerance or self.DEFAULT_KM_TOLERANCE

  
    def __eq__(self, other):
        #nly compare with other Car objects
        if not isinstance(other, Car):
            return NotImplemented
        
        #matching vin
        if self.vin !=  other.vin:
            return False
    
        if self.year !=  other.year:
            return False
    
        return (self.manufacturer == other.manufacturer and
                self.model == other.model and
                self.year == other.year and
                abs(self.km - other.km) <= max(self.km_tolerance, other.km_tolerance))

  
    def __repr__(self):
        return (f"Car(vin='{self.vin}', {self.manufacturer} {self.model}, year={self.year}, km={self.km:,})")    
        # !r applies the repr() function, keeping the specian characters (like \n) visible


print("=== Basic Comparisons ===")
car1 = Car(vin="QWER12345", manufacturer="Ford", model="Fiesta", year=2017, km=170000)
car2 = Car(vin="XYZ123456", manufacturer="Nissan", model="240SX", year=1990, km=500000)
car3 = Car(vin="XYZ123456", manufacturer="Nissan", model="240SX", year=1990, km=500000)

print(f"1. {car1}\n   {car2}\n   Is that the same car? {car1 == car2}") 
print(f"\n2. {car2}\n   {car3}\n   Is that the same car? {car2 == car3}")

print("\n=== Kilometer Tolerance Test ===")
car_a = Car(vin="XYZ5678910", manufacturer="Mazda", model="MX-5", year=1997, km=300000)
car_b = Car(vin="XYZ5678910", manufacturer="Mazda", model="MX-5", year=1997, km=300465)

print(f"3. {car_a}\n   {car_b}\n   Is the amount of km driven approximately the same? (DEFAULT_KM_TOLERANCE: {Car.DEFAULT_KM_TOLERANCE}km)  \n{car_a == car_b}\n  ")

print("\n=== Tolerance Override Test ===")
car_x = Car(vin="ABC123", manufacturer="Toyota", model="Corolla", year=2015, km=100000, km_tolerance=100)
car_y = Car(vin="ABC123", manufacturer="Toyota", model="Corolla", year=2015, km=100150)

print(f"4. {car_x} (tolerance: {car_x.km_tolerance}km)\n   {car_y}  \nIs the amount of km driven approximately the same?  (tolerance: {car_y.km_tolerance}km)\n   {car_x == car_y}")
