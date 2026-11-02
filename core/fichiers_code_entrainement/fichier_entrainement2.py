class SignalProcessor:
    def __init__(self, sample_rate=100, threshold=0.5):
        self.sample_rate = sample_rate
        self.threshold = threshold
        self.buffer = []
        self.history = []
    def normalize(self, samples):
        if not samples:
            return []
        mean = sum(samples) / len(samples)
        variance = sum((x - mean)**2 for x in samples) / len(samples)
        std = variance**0.5
        if std == 0:
            return [0.0 for _ in samples]
        return [(x - mean) / std for x in samples]
    
    def detect_peaks(self, samples, min_distance=1):
        peaks = []
        n = len(samples)
        i = 1
        while i < n - 1:
            if samples[i] > samples[i - 1] and samples[i] > samples[i + 1]:
                if not peaks or i - peaks[-1] >= min_distance:
                    peaks.append(i)
            i += 1
        return peaks