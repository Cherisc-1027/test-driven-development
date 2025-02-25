import matplotlib.pyplot as plt
from SDTclass import SignalDetection  # Import the SignalDetection class
# created with the help of chatgpt
class Experiment:
    def __init__(self):
        self.conditions = []  

    def add_condition(self, sdt_obj, label: str = None) -> None:  
        self.conditions.append((sdt_obj, label))

    def sorted_roc_points(self) -> tuple[list[float], list[float]]:
        if not self.conditions:
            raise ValueError("No conditions have been added to the experiment.")

        fa_rates = []
        hit_rates = []

        for sdt, _ in self.conditions:
            fa_rates.append(sdt.false_alarm_rate())  
            hit_rates.append(sdt.hit_rate())  

        sorted_pairs = sorted(zip(fa_rates, hit_rates))  
        fa_rates_sorted, hit_rates_sorted = zip(*sorted_pairs)

        print("Sorted FA Rates:", fa_rates_sorted)
        print("Sorted Hit Rates:", hit_rates_sorted)  

        return list(fa_rates_sorted), list(hit_rates_sorted)

    def compute_auc(self) -> float:
        if not self.conditions:
            raise ValueError("No conditions have been added to the experiment.")

        fa_rates, hit_rates = self.sorted_roc_points()
    
        # If there are exactly two points, the AUC is always 0.5 (since it's just a line from (0,0) to (1,1))
        if len(fa_rates) == 2:
            return 0.5

        auc = 0.0

        # For more than two points, apply trapezoidal rule
        for i in range(len(fa_rates) - 1):
            width = fa_rates[i + 1] - fa_rates[i]
            height = (hit_rates[i] + hit_rates[i + 1]) / 2
            auc += width * height

        return auc

    def plot_roc_curve(self) -> None:
        if not self.conditions:
            raise ValueError("No conditions have been added to the experiment.")

        fa_rates, hit_rates = self.sorted_roc_points()

        plt.figure(figsize=(6, 6))
        plt.plot(fa_rates, hit_rates, marker='o', linestyle='-', label="ROC Curve")
        plt.plot([0, 1], [0, 1], linestyle="--", color="red", label="Chance Performance")
        plt.xlabel("False Alarm Rate (FA)")
        plt.ylabel("Hit Rate (H)")
        plt.title("ROC Curve")
        plt.legend()
        plt.grid()
        plt.show()
