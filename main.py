import csv
import os
import time

from data_loader.data_loader import DataLoader
from business.company import VehicleCollection
from main_tester import time_sort

from sorter.bubble_sort import BubbleSort
from sorter.insertion_sort import InsertionSort
from sorter.merge_sort import MergeSort
from sorter.quick_sort import QuickSort
from sorter.selection_sort import SelectionSort


def write_sorted_to_csv(sorted_cars, filepath):
    """Write a list of sorted Car objects to a CSV file."""
    dirname = os.path.dirname(filepath)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Vehicle_ID', 'Brand', 'Model', 'Year',
                         'Mileage', 'Engine_Size', 'Price'])
        for car in sorted_cars:
            writer.writerow([car.vehicle_id, car.brand, car.model,
                             car.year, car.mileage, car.engine_size,
                             car.price])


def sort_vehicles_by_price(company, loader, sorters, sizes):
    """Sort all vehicles for specific ranges by Price using Company methods."""
    print("====================================")
    print("Sorting Vehicles by PRICE")
    print("====================================\n")

    for size in sizes:
        sales_data = loader.get_data_by_size(size)
        company.set_sales(sales_data)
        print(f"Data Size: {size} records")
        print("-" * 40)

        for name, sorter in sorters.items():
            start = time.perf_counter()
            sorted_result = company.sort_vehicles_by_price(sorter)
            end = time.perf_counter()
            print(f"  {name}: {end - start:.6f} seconds")

            filename = f"output/{name.replace(' ', '_').lower()}_price_{size}.csv"
            write_sorted_to_csv(sorted_result, filename)

        print()


def sort_vehicles_by_mileage(company, loader, sorters, sizes):
    """Sort all vehicles by Mileage using Company methods."""
    print("====================================")
    print("Sorting Vehicles by MILEAGE")
    print("====================================\n")

    for size in sizes:
        sales_data = loader.get_data_by_size(size)
        company.set_sales(sales_data)
        print(f"Data Size: {size} records")
        print("-" * 40)

        for name, sorter in sorters.items():
            start = time.perf_counter()
            sorted_result = company.sort_vehicles_by_mileage(sorter)
            end = time.perf_counter()
            print(f"  {name}: {end - start:.6f} seconds")

            filename = f"output/{name.replace(' ', '_').lower()}_mileage_{size}.csv"
            write_sorted_to_csv(sorted_result, filename)

        print()


if __name__ == "__main__":
    print("====================================")
    print("Sales Company Sorting Demo")
    print("====================================\n")

    # -----------------------------------
    # 1. Load Data
    # -----------------------------------
    loader = DataLoader("data/vehicles.csv")
    sales_data = loader.get_data_by_size(1000)

    # -----------------------------------
    # 2. Create Company Object
    # -----------------------------------
    company = VehicleCollection("TechCorp", sales_data)
    print("Company Summary:")
    print(f"Total Records: {company.total_sales()}")
    print(f"Total Revenue: ${company.total_revenue():,.2f}\n")

    # -----------------------------------
    # 3. Set up Sorting Algorithms
    # -----------------------------------
    sorters = {
        "Bubble Sort": BubbleSort(),
        "Insertion Sort": InsertionSort(),
        "Merge Sort": MergeSort(),
        "Quick Sort": QuickSort(),
        "Selection Sort": SelectionSort()
    }

    # Define data size ranges to test
    sizes = [250, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000]

    # -----------------------------------
    # 4. Sort vehicles by Price
    # -----------------------------------
    sort_vehicles_by_price(company, loader, sorters, sizes)

    # -----------------------------------
    # 5. Sort vehicles by Mileage
    # -----------------------------------
    sort_vehicles_by_mileage(company, loader, sorters, sizes)

    # -----------------------------------
    # 6. Display Top 10 by Price
    # -----------------------------------
    print("====================================")
    print("Top 10 Vehicles by Price (Highest):")
    print("====================================")
    company.set_sales(loader.get_data_by_size(1000))
    top_10 = company.get_top_sales(sorters["Merge Sort"], n=10)
    for i, car in enumerate(top_10, 1):
        print(f"  {i}. {car}")
