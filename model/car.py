class Car:
    def __init__(self, mileage, price):
        self.mileage = mileage
        self.price = price

    def __repr__(self):
        return f"Car(Mileage={self.mileage}, Price={self.price})"