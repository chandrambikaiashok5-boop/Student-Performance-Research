import os
import subprocess
import sys

# Run the pipeline
result = subprocess.run(
    [sys.executable, "run_pipeline.py"],
    capture_output=True,
    text=True
)

# Check that the pipeline ran successfully
assert result.returncode == 0, "Pipeline failed to run"

# Check that the expected files were created
assert os.path.exists("data/raw/synthetic_students.csv"), \
    "Raw data file was not created"

assert os.path.exists("data/processed/processed_students.csv"), \
    "Processed data file was not created"

assert os.path.exists("reports/pipeline_output.txt"), \
    "Pipeline report was not created"

print("All synthetic pipeline tests passed successfully!")