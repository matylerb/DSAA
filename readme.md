# Sorting Algorithm Performance Analysis

A Python project that benchmarks and compares five sorting algorithms (Bubble, Insertion, Merge, Quick, Selection) on a vehicle dataset, with interactive menus, automated benchmarking, data analysis, and performance visualisation.

## Features

- **5 Sorting Algorithms**: Bubble Sort, Insertion Sort, Merge Sort, Quick Sort, Selection Sort — each implementing a common `Sorter` abstract base class
- **Performance Benchmarking**: Compare algorithm execution times across multiple data sizes (250–64 000 records) and by model year, averaged over multiple runs
- **Visualisation**: Matplotlib charts plotting time vs. data size / year for every algorithm
- **Data Analysis**: Pandas-based exploratory analysis of the vehicle dataset (statistics, distributions, correlations)
- **CSV Export**: Sorted results written to the `output/` directory
- **Multiple Entry Points**: Interactive menu, automated benchmarking, demo script, and standalone data analysis

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/matylerb/DSAA.git
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

Key dependencies: `matplotlib`, `numpy`, `pandas` (see `requirements.txt` for the full list).

## Usage

| Script | Description |
|--------|-------------|
| `python main.py` | Demo sorting by price and mileage across data-size ranges, exports sorted CSVs to `output/` |
| `python main_menu.py` | Interactive menu: view sales count, total revenue, choose a sorting algorithm, sort, and display top-N sales |
| `python main_tester.py` | Benchmark all algorithms by price (various sizes) and by mileage (per year), prints a formatted table |
| `python benchmark.py` | Benchmark + Matplotlib charts comparing algorithm performance by price and mileage |
| `python data_analysis.py` | Exploratory analysis of `Data/vehicles.csv` (record count, statistics, correlations, price distribution) |

## Project Structure

```
assignment/
├── main.py                # Demo: sort by price & mileage, export CSVs
├── main_menu.py           # Interactive menu-driven interface
├── main_tester.py         # Tabular benchmark (price by size, mileage by year)
├── benchmark.py           # Graphical benchmark with Matplotlib
├── data_analysis.py       # Pandas exploratory data analysis
├── requirements.txt       # Python dependencies
├── business/
│   └── company.py         # VehicleCollection: sales logic, sorting, revenue
├── data_loader/
│   └── data_loader.py     # DataLoader: CSV → Vehicle objects, size/year filtering
├── model/
│   └── car.py             # Vehicle model class
├── sorter/
│   ├── sorter_adt.py      # Sorter abstract base class
│   ├── bubble_sort.py
│   ├── insertion_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   └── selection_sort.py
├── Data/
│   └── vehicles.csv       # Vehicle dataset (~64 000 records)
└── output/                # Generated sorted CSV files
```
