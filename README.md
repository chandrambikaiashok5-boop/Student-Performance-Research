# Student Performance Research

## Project Overview

This project investigates the relationship between students' study hours and their final exam scores. It uses a synthetic dataset and a reproducible Python pipeline to demonstrate the complete analysis process.

## Research Question

Does the number of hours students spend studying affect their final exam scores?

## Project Objectives

- Analyze the relationship between study hours and final scores.
- Create and process a synthetic student dataset.
- Calculate the correlation between study hours and final scores.
- Provide a reproducible analysis pipeline.
- Test the pipeline using synthetic data.

## Tools and Technologies

- Python
- Pandas
- NumPy

## Project Structure

- `data/raw/` – Synthetic raw student data.
- `data/interim/` – Intermediate data files.
- `data/processed/` – Processed student data.
- `reports/` – Pipeline output reports.
- `test_pipeline.py` – Synthetic pipeline tests.
- `run_pipeline.py` – Main reproducible analysis pipeline.
- `analysis-preregistration.md` – Research question and analysis plan.
- `requirements.txt` – Project dependencies.
- `requirements.lock` – Environment lockfile.

## Installation

Install the required dependencies:

    py -m pip install -r requirements.txt

## Run the Analysis Pipeline

Run the following command from the project folder:

    py run_pipeline.py

The pipeline will:

1. Create a synthetic student dataset.
2. Save the raw data.
3. Process the data.
4. Calculate the correlation between study hours and final scores.
5. Create an output report.

## Run the Synthetic Pipeline Test

Run:

    py test_pipeline.py

Expected output:

    All synthetic pipeline tests passed successfully!

## Reproducibility

This repository contains a preregistered analysis plan, environment dependency files, a reproducible data pipeline, and a synthetic pipeline test to verify that the project runs successfully.
