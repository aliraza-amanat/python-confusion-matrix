# Monosnap Confusion Matrix

This Python script computes a confusion matrix from two CSV files: `kewords-reran.csv` and `refrence.csv`. It then saves the confusion matrix as a CSV file and plots it as an image.

## Usage

1. Make sure you have Python installed on your system.

2. Install the required dependencies using pip:


3. Place your input CSV files `kewords-reran.csv` and `refrence.csv` in the same directory as the script.


4. The script will compute the confusion matrix and print the values (true positives, false positives, true negatives, false negatives). It will also save the confusion matrix to `confusion_matrix_summary.csv` and plot it as `confusion_matrix_plot.png`.

## Files

- `confusion_matrix.py`: Python script to generate the confusion matrix.
- `kewords-reran.csv`: CSV file containing data with columns `object_key`, `has_keyword`, `reference`, `true pos`, `false pos`, `true neg`, `false neg`.
- `refrence.csv`: CSV file containing data with column `object_key`.
- `confusion_matrix_summary.csv`: Output CSV file containing the confusion matrix summary.
- `confusion_matrix_plot.png`: Plot image of the confusion matrix.

## Make Sure to create a virtualenv
   ```
   python3 -m venv venv
   ```
## Dependencies
   ```
   pip install -r requirements.txt
   ```

## Run the Script
   ```
   python3 confusion_matrix.py
   ```
