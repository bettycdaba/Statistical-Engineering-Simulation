# Statistical Engineering & Simulation Assessment

## Project Overview

This project implements a **pure-Python statistical engine** from scratch (no NumPy, pandas, or external libraries) and demonstrates the **Law of Large Numbers** through Monte Carlo simulation.

### What It Does:
1. **Statistical Calculations**: Calculates mean, median, mode, variance, standard deviation, and detects outliers
2. **Server Crash Simulation**: Simulates startup server crashes to show how sample size affects probability estimates
3. **Data Analysis**: Analyzes mock startup salary data to identify outliers and patterns

---

## Mathematical Logic

### Mean (Average)
mean = (x1 + x2 + x3 +...+xn)/n

Sum of all values divided by number of values.

### Median (Middle Value)
- **Odd number of elements**: Middle value after sorting
- **Even number of elements**: Average of two middle values after sorting

Example: 
- `[1,2,3,4,5]` → median = 3
- `[1,2,3,4]` → median = (2+3)/2 = 2.5

### Mode (Most Frequent Values)
- Count frequency of each value
- Return ALL values with maximum frequency
- If all values appear once → return message "All values are unique"

### Variance
- **Population Variance** (σ²): Σ(x - μ)² / N
- **Sample Variance** (s²): Σ(x - x̄)² / (n-1) ← Bessel's correction

Bessel's correction (using n-1 instead of n) provides an unbiased estimate of population variance from a sample.

### Standard Deviation

standard variation = sqrt variance


### Outlier Detection
Values that satisfy: `|value - mean| > threshold × standard_deviation`

---

## Setup Instructions

### Prerequisites
- Python 3.6 or higher installed
- VS Code (recommended) or any text editor

### Clone & Run

1. **Clone the repository**:
```bash
git clone https://github.com/bettycdaba/statistical_engine.git
cd statistical_engine

2. Run the main program
python main.py

3. Run unit tests
python -m unittest tests.test_stat_engine