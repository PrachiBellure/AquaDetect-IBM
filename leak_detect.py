import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

def simulate_water_flow_data():
    """Simulates hourly water flow rate (Liters per hour) for an apartment complex."""
    np.random.seed(42)
    hours = 168
    time_index = pd.date_range(start="2026-11-01", periods=hours, freq="h")
    base_usage = 50 + 30 * np.sin(np.linspace(0, 2 * np.pi, hours)) + np.random.normal(0, 5, hours)
    leak_anomaly = np.zeros(hours)
    leak_anomaly[100:140] = 25.0
    total_flow = base_usage + leak_anomaly
    df = pd.DataFrame({"Timestamp": time_index, "Flow_Rate_Liters": total_flow})
    return df

def detect_leaks(df):
    """Uses Machine Learning (Isolation Forest) to detect water anomalies/leaks."""
    model = IsolationForest(contamination=0.05, random_state=42)
    df['Anomaly'] = model.fit_predict(df[['Flow_Rate_Liters']])
    leaks_detected = df[df['Anomaly'] == -1]
    return leaks_detected

if __name__ == "__main__":
    print("--- AquaDetect AI Engine Initialized ---")
    data = simulate_water_flow_data()
    anomalies = detect_leaks(data)
    print(f"Total data points analyzed: {len(data)}")
    print(f"Potential micro-leaks / anomalies detected: {len(anomalies)}")
    print("\nSample Leak Events Flagged:")
    print(anomalies.head())