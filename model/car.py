class Vehicle:
    def __init__(self, vehicle_id=None, brand=None, model=None, year=None,
                 mileage=0, engine_size=None, price=0.0):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.engine_size = engine_size
        self.price = price

    def __repr__(self):
        return (f"Vehicle(Vehicle_ID={self.vehicle_id}, Brand={self.brand}, "
                f"Model={self.model}, Year={self.year}, "
                f"Mileage={self.mileage}, Engine_Size={self.engine_size}, "
                f"Price={self.price})")

    def __str__(self):
        return (f"{self.brand} {self.model} ({self.year}) - "
                f"Mileage: {self.mileage:,}, Price: ${self.price:,.2f}")