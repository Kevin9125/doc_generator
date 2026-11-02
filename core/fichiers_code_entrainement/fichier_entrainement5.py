
import math
from typing import List

class AdaptiveFilter:
    def __init__(self, tap_count: int, step: float):
        self.tap_count = tap_count
        self.step = step
        self.weights: List[float] = [0.0] * tap_count

    def adapt(self, samples: List[float], desired: List[float]) -> float:
        error = 0.0
        for i in range(len(samples)):
            predicted = sum(
                self.weights[j] * samples[i - j - 1]
                for j in range(self.tap_count)
                if i - j - 1 >= 0
            )
            error += desired[i] - predicted
            gradient = [
                samples[i - j - 1] if i - j - 1 >= 0 else 0.0
                for j in range(self.tap_count)
            ]
            self.weights = [
                w + self.step * error * g
                for w, g in zip(self.weights, gradient)
            ]
        return error / len(samples)

    def clear(self) -> None:
        self.weights = [0.0] * self.tap_count