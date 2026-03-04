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

    key_function = lambda car: car.price

    results = {name: [] for name in algorithms.keys()}
    print("Timing sorting algorithms...\n")

    for size in data_set_sizes:

        print(f"Testing with {size} records...")
        data = loader.get_data_by_size(size)

        for name, sorter in algorithms.items():
            avg_time = time_sort(sorter, data, key_function)
            results[name].append(avg_time)
            print(f"  {name}: {avg_time:.6f} seconds"  )
        print()

    plt.figure()

    for name, times in results.items():
        plt.plot(data_set_sizes, times, label=name)
    plt.xlabel("Data Set Size")
    plt.ylabel("Average Time (seconds)")
    plt.title("Sorting Algorithm Performance")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
