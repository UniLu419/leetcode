import argparse
import re


def create_python_file(file_name: str):
    python_code = """\
from typing import List
from timing_dec import timing


class Solution:
    @timing
    def solve(i: int) -> int:
        pass


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    k = 3
                case 2:
                    # sample 2
                    k = 2
                case 3:
                    # sample 3
                    k = 3
                case _:
                    break
            print(f"ans = {solution.solve(k)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()

"""

    with open(file_name, "w") as file:
        file.write(python_code)


def parse_file_name(file_name: str) -> str:
    if file_name.endswith(".py"):
        file_name = file_name[:-3]

    file_name = re.sub(r"[^a-zA-Z0-9]+", "_", file_name).lower()
    file_name = re.sub(r"_+", "_", file_name)
    if file_name.endswith("_"):
        file_name = file_name[:-1]
    file_name = f"{file_name}.py"
    return file_name


def main():
    parser = argparse.ArgumentParser(
        description="This script is for creating a new python script in current folder and import the template into this file."
    )
    parser.add_argument("file_name", help="Name of the Python script file")
    args = parser.parse_args()
    file_name = args.file_name
    file_name = parse_file_name(file_name)
    create_python_file(file_name)
    print(f"Created {file_name}")


if __name__ == "__main__":
    main()


# Usage:  python3 create.py "2146. K Highest Ranked Items Within a Price Range"
# python3 create.py "68. Text Justification"
