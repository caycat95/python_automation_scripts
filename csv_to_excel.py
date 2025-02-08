import pandas as pd
import sys


def convert_to_excel():
    csv_file_path = sys.argv[1]
    df = pd.read_csv(csv_file_path)
    excel_file_path = sys.argv[2]
    df.to_excel(excel_file_path, sheet_name='Sheet1', index=False,)


def main():
    convert_to_excel()


if __name__ == "__main__":
    main()
