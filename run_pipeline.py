import os
import pandas as pd
import numpy as np

# Create project folders if they do not exist
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/interim", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Create a synthetic student dataset
np.random.seed(42)

study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
scores = np.array([52, 55, 60, 63, 68, 72, 76, 81, 85, 90])

data = pd.DataFrame({
    "study_hours": study_hours,
    "final_score": scores
})

# Save the synthetic raw data
data.to_csv("data/raw/synthetic_students.csv", index=False)

# Simple data processing
processed_data = data.dropna()

# Save processed data
processed_data.to_csv(
    "data/processed/processed_students.csv",
    index=False
)

# Calculate the correlation
correlation = processed_data["study_hours"].corr(
    processed_data["final_score"]
)

# Create a simple report
with open("reports/pipeline_output.txt", "w") as file:
    file.write("Synthetic pipeline test completed successfully.\n")
    file.write(f"Number of records: {len(processed_data)}\n")
    file.write(f"Correlation: {correlation:.4f}\n")

print("Pipeline completed successfully!")
print(f"Number of records: {len(processed_data)}")
print(f"Correlation: {correlation:.4f}")