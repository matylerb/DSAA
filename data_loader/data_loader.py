import csv
from model.car import Car

class load_data:
    def __init__(self, file_path):
        self.file_path = file_path
        self.__cars = []
        self.load_cars()

    def load_cars(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                sale = Car(
                    vehicle_id=row['Vehicle_ID'],
                    brand=row['Brand'],
                    model=row['Model'],
                    year=int(row['Year']),
                    mileage=int(row['Mileage']),
                    engine_size=float(row['Engine_Size']),
                    price=float(row['Price']),
                )
                self.__cars.append(sale)

    def get_all_data(self):
        return self.__cars.copy()
    
    def get_data_by_size(self, size):
        if size > len(self.__cars):
            raise ValueError("Requested size exceeds the number of available cars.")    
        return self.__cars[:size].copy()
    