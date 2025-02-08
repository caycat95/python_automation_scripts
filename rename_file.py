import os
import sys


def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
    except Exception as e:
        print("An error occurred:", e)


def main():
    rename_file(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
