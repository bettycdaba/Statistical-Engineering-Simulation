import math

class StatEngine:
    def __init__(self, data):
        # Handle empty input
        if not data:
            raise ValueError("Data cannot be empty")

        # Validate and clean data
        self.data = []
        for item in data:
            if isinstance(item, (int, float)):
                self.data.append(item)
            else:
                raise TypeError(f"Invalid data type: {item}")

        if len(self.data) == 0:
            raise ValueError("No valid numeric data")

        self.n = len(self.data)

    # ---------------- CENTRAL TENDENCY ---------------- #

    def get_mean(self):
        return sum(self.data) / self.n

    def get_median(self):
        sorted_data = sorted(self.data)
        mid = self.n // 2

        if self.n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def get_mode(self):
        frequency = {}

        for num in self.data:
            frequency[num] = frequency.get(num, 0) + 1

        max_freq = max(frequency.values())

        if max_freq == 1:
            return "No mode (all values are unique)"

        return [k for k, v in frequency.items() if v == max_freq]

    # ---------------- DISPERSION ---------------- #

    def get_variance(self, is_sample=True):
        if is_sample and self.n < 2:
            raise ValueError("Sample variance requires at least 2 data points")

        mean = self.get_mean()
        squared_diff = [(x - mean) ** 2 for x in self.data]

        if is_sample:
            return sum(squared_diff) / (self.n - 1)
        return sum(squared_diff) / self.n

    def get_standard_deviation(self, is_sample=True):
        return math.sqrt(self.get_variance(is_sample))

    # ---------------- OUTLIERS ---------------- #

    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_standard_deviation()

        if std == 0:
            return []

        outliers = []
        for x in self.data:
            z = abs((x - mean) / std)
            if z > threshold:
                outliers.append(x)

        return outliers