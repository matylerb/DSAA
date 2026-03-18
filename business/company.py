class VehicleCollection:

    def __init__(self, name, sales_list=None):
        self.name = name
        self.__sale_list = sales_list if sales_list else []

    def add_sale(self, sale):
        self.__sale_list.append(sale)

    def get_sales(self):
        return self.__sale_list.copy()

    def set_sales(self, sales_list):
        self.__sale_list = sales_list if sales_list else []

    def total_sales(self):
        return len(self.__sale_list)

    def sort_sales(self, sorter, key=lambda x: x.price):
        return sorter.sort(self.__sale_list.copy(), key)

    def sort_vehicles_by_price(self, sorter):
        return self.sort_sales(sorter, key=lambda x: x.price)

    def sort_vehicles_by_mileage(self, sorter):
        return self.sort_sales(sorter, key=lambda x: x.mileage)

    def total_revenue(self):
        return sum(car.price for car in self.__sale_list)

    def get_top_sales(self, sorter, n=10):
        sorted_sales = sorter.sort(self.__sale_list.copy(), key=lambda x: x.price)
        top_sales = []

        index = len(sorted_sales) - 1

        while len(top_sales) < n and index >= 0:
            top_sales.append(sorted_sales[index])
            index -= 1

        return top_sales