import time

from data_loader.data_loader import load_data
from business.company import Company
from main_tester import time_sort

from sorter.bubble_sort import BubbleSort       
from sorter.insertion_sort import InsertionSort
from sorter.merge_sort import MergeSort
from sorter.quick_sort import QuickSort
from sorter.selection_sort import selectionSort


def sort_vehicles_by_price(loader, sorters, sizes):
    """Sort all vehicles for specific ranges by Price"""
    print("====================================")
    print("Sorting Vehicles by PRICE")
    print("====================================\n")
    
    key_function = lambda car: car.price
    
    for size in sizes:
        sales_data = loader.get_data_by_size(size)
        print(f"Data Size: {size} records")
        print("-" * 40)
        
        for name, sorter in sorters.items():
            data_copy = sales_data.copy()
            start = time.perf_counter()
            sorter.sort(data_copy, key=key_function)
            end = time.perf_counter()
            print(f"  {name}: {end - start:.6f} seconds")
        
        print()


def sort_vehicles_by_mileage(loader, sorters, sizes):
    """Sort all vehicles by Mileage"""
    print("====================================")
    print("Sorting Vehicles by MILEAGE")
    print("====================================\n")
    
    key_function = lambda car: car.mileage
    
    for size in sizes:
        sales_data = loader.get_data_by_size(size)
        print(f"Data Size: {size} records")
        print("-" * 40)
        
        for name, sorter in sorters.items():
            data_copy = sales_data.copy()
            start = time.perf_counter()
            sorter.sort(data_copy, key=key_function)
            end = time.perf_counter()
            print(f"  {name}: {end - start:.6f} seconds")
        
        print()


if __name__ == "__main__":
    print("====================================")
    print("Sales Company Sorting Demo")
    print("====================================\n")

    # -----------------------------------
    # 1. Load Data
    # -----------------------------------
    loader = load_data("data/vehicles.csv")
    sales_data = loader.get_data_by_size(1000)

    # -----------------------------------
    # 2. Create Company Object
    # -----------------------------------
    company = Company("TechCorp", sales_data)
    print("Company Summary:")
    print(f"Total Records: {company.total_sales()}")
    print(f"Total Revenue: {company.total_revenue():,.2f}\n")

    # -----------------------------------
    # 3. Set up Sorting Algorithms
    # -----------------------------------
    sorters = {
        "Bubble Sort": BubbleSort(),
        "Insertion Sort": InsertionSort(),
        "Merge Sort": MergeSort(),
        "Quick Sort": QuickSort(),
        "Selection Sort": selectionSort()
    }

    # Define data size ranges to test
    sizes = [250, 500, 1000, 2000, 4000, 8000, 16000, 32000]

    # -----------------------------------
    # 4. Sort vehicles by Price
    # -----------------------------------
    sort_vehicles_by_price(loader, sorters, sizes)

    # -----------------------------------
    # 5. Sort vehicles by Mileage
    # -----------------------------------
    sort_vehicles_by_mileage(loader, sorters, sizes)

    # -----------------------------------
    # 6. Display Top 10 by Price
    # -----------------------------------
    print("====================================")
    print("Top 10 Vehicles by Price (Highest):")
    print("====================================")
    sorted_by_price = sorters["Merge Sort"].sort(sales_data.copy(), key=lambda car: car.price)
    for i, car in enumerate(sorted_by_price[-10:][::-1], 1):
        print(f"  {i}. {car}")