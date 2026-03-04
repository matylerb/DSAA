from data_loader.data_loader import load_data
from business.company import Company
from sorter.bubble_sort import BubbleSort
from sorter.insertion_sort import InsertionSort
from sorter.merge_sort import MergeSort
from sorter.quick_sort import QuickSort
from sorter.selection_sort import selectionSort
import time


def print_menu():
    print("====================================")
    print("Sales Company Sorting Demo")
    print("====================================\n")
    print("1. Show total sales count")
    print("2. Show total revenue")
    print("3. Choose Sorting Algorithm")
    print("4. Sort sales using chosen algorithm")
    print("5. Display Top N Sales")
    print("6. Exit")
    print("====================================\n")


def choose_sorter():
    print("Choose a sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")
    print("4. Quick Sort")
    print("5. Selection Sort")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        return BubbleSort()
    elif choice == '2':
        return InsertionSort()
    elif choice == '3':
        return MergeSort()
    elif choice == '4':
        return QuickSort()
    elif choice == '5':
        return selectionSort()
    else:
        print("Invalid choice, defaulting to Bubble Sort.")
        return BubbleSort()
    
def main():

    loader = load_data("data/vehicles.csv")
    sales_data = loader.get_data_by_size(1000)

    company = Company("", sales_data)

    curret_sorter = None


    while True:

        print_menu()
        choice = input("Enter your choice (1-6): ")

        match choice:
            case '1':
                print(f"Total Sales Count: {company.total_sales()}\n")
            case '2':
                print(f"Total Revenue: {company.total_revenue():,.2f}\n")
            case '3':
                curret_sorter = choose_sorter()#
                print("Sorting algorithm chosen.\n")
            case '4':
                start = time.perf_counter()

                sorted_sales = company.sort_sales(curret_sorter, key=lambda x: x.price)

                print(f"Sorting Time: {time.perf_counter() - start:.6f} seconds\n")

                print("First 5 results:")
                for sale in sorted_sales[:5]:
                    print(sale)

            case '5':
                n = int(input("Enter the number of top sales to display: "))

                print(f"Retreiving top {n} sales... using {curret_sorter.__class__.__name__}...")

                top_sales = company.get_top_sales(curret_sorter, n)

                print(f"top {n} sales retreived.\n")

                for sale in top_sales:
                    print(sale) 


            case '6':
                print("Exiting program. Goodbye!")
                break


            case _:
                print("Invalid choice. Please try again.\n")



if __name__ == "__main__":
    main()