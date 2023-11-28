"""
Example for:
1. file handling
2. exception handling
3. handling CLI args
4. working with dicts
"""
import argparse
import time
import json


def main():
    parser = argparse.ArgumentParser(description='Converts the input CSV file into a JSON file')

    parser.add_argument('-f', '--input-file', help='Input filename', required=True)
    parser.add_argument('-o', '--output-file', help='Output filename')
    args = parser.parse_args()

    csv_filename = args.input_file
    json_filename = args.output_file
    if json_filename is None:
        json_filename = f'{csv_filename[:-4]}_{time.time()}.json'

    try:
        with open(csv_filename, encoding='utf-8') as f:
            # skip all blank lines, so that we can read the header line
            while True:
                line = f.readline()
                if line != '\n':
                    break

            data = []
            fields = line.rstrip().split(',')  # read the header line
            for line in f:
                if line == '\n':
                    continue  # skip the rest of the loop body
                vals = line.rstrip().split(',')
                d = dict(zip(fields, vals))
                data.append(d)

            with open(json_filename, 'w', encoding='utf-8') as f1:
                json.dump(data, f1)
                print(f'"{csv_filename}" converted into a JSON file and stored in "{json_filename}".')

    except FileNotFoundError:
        print(f'The input file "{csv_filename}" does not exist.')
        exit(1)


if __name__ == '__main__':
    main()
