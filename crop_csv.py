import pandas as pd

def export_first_500_rows(input_csv_file, output_csv_file):
    # Read the CSV file with '|' separator
    df = pd.read_csv(input_csv_file, sep='|')
    
    # Export only the first 500 rows
    df[:500].to_csv(output_csv_file, sep='|', index=False)

# Usage example
input_csv_file = 'putusan_data2.csv'  # Change this to your input file name
output_csv_file = 'cropped.csv'  # Change this to your desired output file name

export_first_500_rows(input_csv_file, output_csv_file)