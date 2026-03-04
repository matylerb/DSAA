# Sorting Algorithm Performance Analysis

A Python project demonstrating and comparing various sorting algorithms on vehicle data.

## Features

- **5 Sorting Algorithms**: Bubble Sort, Insertion Sort, Merge Sort, Quick Sort, Selection Sort
- **Performance Benchmarking**: Compare algorithm execution times across different data sizes
- **Multiple Entry Points**: Interactive menu, automated testing, and demo scripts

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd assignment
```

### 2. Set Up Virtual Environment (Windows)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Configure VS Code (Optional)

1. Press `Ctrl + Shift + P`
2. Type `Python: Select Interpreter`
3. Choose `.venv\Scripts\python.exe`

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run any of the following scripts:

| Script | Description |
|--------|-------------|
| `python main.py` | Demo sorting by price and mileage across data ranges |
| `python main_menu.py` | Interactive menu-driven interface |
| `python main_tester.py` | Benchmark all algorithms with performance graphs |

## Project Structure

```
assignment/
├── main.py              # Main demo script
├── main_menu.py         # Interactive menu
├── main_tester.py       # Performance benchmarking
├── business/
│   └── company.py       # Company business logic
├── data_loader/
│   └── data_loader.py   # CSV data loading
├── model/
│   └── car.py           # Car model class
├── sorter/
│   ├── bubble_sort.py
│   ├── insertion_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   ├── selection_sort.py
│   └── sorter_adt.py    # Abstract base class
└── Data/
    └── vehicles.csv     # Vehicle dataset
```
