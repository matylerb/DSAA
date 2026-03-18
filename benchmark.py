import sys
import time
sys.setrecursionlimit(200000)

from data_loader.data_loader import DataLoader
from sorter.bubble_sort import BubbleSort
from sorter.insertion_sort import InsertionSort
from sorter.merge_sort import MergeSort
from sorter.quick_sort import QuickSort
from sorter.selection_sort import SelectionSort

def time_sort(sorter, data, key_function, runs=3):
    total = 0
    for _ in range(runs):
        data_copy = data.copy()
        start = time.perf_counter()
        sorter.sort(data_copy, key=key_function)
        end = time.perf_counter()
        total += (end - start)
    return total / runs

def main():
    loader = DataLoader("data/vehicles.csv")
    sizes = [250, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000]

    algorithms = {
        "Bubble": BubbleSort(),
        "Selection": SelectionSort(),
        "Insertion": InsertionSort(),
        "Quick": QuickSort(),
        "Merge": MergeSort(),
    }

    # Sort by price
    print("=== Sorting by PRICE (avg of 3 runs) ===")
    print(f"{'Size':<10}", end="")
    for name in algorithms:
        print(f"{name:<16}", end="")
    print()

    for size in sizes:
        data = loader.get_data_by_size(size)
        print(f"{size:<10}", end="", flush=True)
        for name, sorter in algorithms.items():
            avg = time_sort(sorter, data, lambda car: car.price)
            print(f"{avg:<16.6f}", end="", flush=True)
        print()

    print()
    print("=== Sorting by MILEAGE (avg of 3 runs, by year) ===")
    years = [2020, 2021, 2022, 2023, 2024]
    print(f"{'Year':<10}", end="")
    for name in algorithms:
        print(f"{name:<16}", end="")
    print()

    for year in years:
        data = loader.get_data_by_year(year)
        print(f"{year:<10}", end="", flush=True)
        for name, sorter in algorithms.items():
            avg = time_sort(sorter, data, lambda car: car.mileage)
            print(f"{avg:<16.6f}", end="", flush=True)
        print()

if __name__ == "__main__":
    main()
