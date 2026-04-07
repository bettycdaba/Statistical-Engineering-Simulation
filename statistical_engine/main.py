import json
from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes

# Load dataset
with open("data/sample_salaries.json") as f:
    salaries = json.load(f)

engine = StatEngine(salaries)

print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())
print("Standard Deviation:", engine.get_standard_deviation())
print("Outliers:", engine.get_outliers())

print("\n--- Monte Carlo Simulation ---")

for days in [30, 365, 10000]:
    prob = simulate_crashes(days)
    print(f"{days} days -> Crash Probability: {prob}")