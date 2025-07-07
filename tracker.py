# carbonswipe/tracker.py

import time
import random

class CarbonTracker:
    def __init__(self, model_path: str, device: str = "cpu"):
        self.model_path = model_path
        self.device = device
        # Simulate loading the model
        print(f"Loaded model from {model_path} on {device}")

    def measure(self, input_text: str):
        start_time = time.time()

        # Simulate inference (replace with real model inference)
        print(f"Running inference for: {input_text}")
        time.sleep(1)  # Simulate time delay

        # Fake values (replace with real calculations later)
        energy_kwh = round(random.uniform(0.01, 0.05), 4)
        co2_grams = energy_kwh * 475  # Average CO₂ intensity in g/kWh
        water_ml = energy_kwh * 2000  # Approximate LLM water cost (adjust as needed)

        return energy_kwh, co2_grams, water_ml