# 📊 Statistical Engine & Monte Carlo Simulation

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()

A **pure-Python** statistical engine built from scratch to demonstrate core statistical concepts and the **Law of Large Numbers** through Monte Carlo simulation. No external libraries like NumPy or pandas — just clean, educational Python code.

---

## 🎯 What It Does

- **Statistical Calculations**: Computes mean, median, mode, variance, standard deviation, and detects outliers
- **Server Crash Simulation**: Simulates startup server crashes to show how sample size affects probability estimates
- **Salary Data Analysis**: Analyzes mock startup salary data to identify outliers and patterns

---

## 🧮 Mathematical Foundation

| Metric | Formula | Description |
|--------|---------|-------------|
| **Mean** | `Σx / n` | Average of all values |
| **Median** | Middle value(s) | Central value after sorting |
| **Mode** | Most frequent value(s) | Returns all values with max frequency |
| **Variance (Sample)** | `Σ(x - x̄)² / (n-1)` | Bessel's correction for unbiased estimation |
| **Variance (Population)** | `Σ(x - μ)² / N` | Population variance |
| **Std Deviation** | `√variance` | Spread of data around mean |
| **Outliers** | `\|x - μ\| > 2σ` | Values beyond 2 standard deviations |

### Bessel's Correction
Using `n-1` instead of `n` provides an unbiased estimate of population variance from a sample.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher

### Installation

```bash
# Clone the repository
git clone https://github.com/bettycdaba/statistical_engine.git
cd statistical_engine

# Run the main program
python main.py

# Run unit tests
python -m unittest tests.test_stat_engine
