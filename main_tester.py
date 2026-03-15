import time
import matplotlib.pyplot as plt
from data_loader.data_loader import load_data
from sorter.bubble_sort import BubbleSort
from sorter.insertion_sort import InsertionSort
from sorter.merge_sort import MergeSort
from sorter.quick_sort import QuickSort
from sorter.selection_sort import selectionSort

def time_sort( sorter, data, key_function, run=3):

    total  = 0
    for _ in range(run):
        data_copy = data.copy()
        start = time.perf_counter()
        sorter.sort(data_copy, key=key_function)
        end = time.perf_counter()
        total += (end - start)
    return total / run

def main():
    data_set_sizes = [100, 500, 1000, 5000]

    loader = load_data("data/vehicles.csv")

    algorithms = {
        "Bubble Sort": BubbleSort(),
        "Insertion Sort": InsertionSort(),
        "Merge Sort": MergeSort(),
        "Quick Sort": QuickSort(),
        "Selection Sort": selectionSort()
    }

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- Price sorting benchmark ---
    price_results = {name: [] for name in algorithms}
    print("Timing sorting algorithms by Price...\n")

    for size in data_set_sizes:
        print(f"Testing with {size} records...")
        data = loader.get_data_by_size(size)      
        for name, sorter in algorithms.items():
            avg_time = time_sort(sorter, data, lambda car: car.price)
            price_results[name].append(avg_time)
            print(f"  {name}: {avg_time:.6f} seconds")
        print()

    for name, times in price_results.items():
        ax1.plot(data_set_sizes, times, label=name)
    ax1.set_xlabel("Data Set Size")
    ax1.set_ylabel("Average Time (seconds)")
    ax1.set_title("Sorting Algorithm Performance (Price)")
    ax1.legend()
    ax1.grid(True)

    # --- Mileage sorting benchmark ---
    mileage_results = {name: [] for name in algorithms}
    print("Timing sorting algorithms by Mileage...\n")

    for size in data_set_sizes:
        print(f"Testing with {size} records...")
        data = loader.get_data_by_size(size)

        for name, sorter in algorithms.items():
            avg_time = time_sort(sorter, data, lambda car: car.mileage)
            mileage_results[name].append(avg_time)
            print(f"  {name}: {avg_time:.6f} seconds")
        print()

    for name, times in mileage_results.items():
        ax2.plot(data_set_sizes, times, label=name)
        ax2.set_xlabel("Data Set Size")
        ax2.set_ylabel("Average Time (seconds)")
        ax2.set_title("Sorting Algorithm Performance (Mileage)")
        ax2.legend()
        ax2.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
