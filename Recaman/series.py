""" Read and print an integer series."""

import sys

def read_series(filename):
        lines = []
        with open(filename, mode="rt", encoding="utf-8") as f:
            for line in f:
                try:
                    value = int(line)
                except:
                    continue
                lines.append(value)
            return lines


def main(filename):
    series = read_series(filename)
    print(series)

if __name__ == "__main__":
    main(sys.argv[1])