"""
Read a file and create an upper-case version of the same.
Read the names of input and output files as CLI args
"""
import argparse


def main():
    parser = argparse.ArgumentParser(description='Converts a given file into an uppercase version of the same')

    parser.add_argument('-f', '--input-file', help='Input filename', required=True)
    parser.add_argument('-o', '--output-file', help='Output filename', required=True)
    args = parser.parse_args()

    # if args.input_file is None:
    #     parser.error('Input file is missing')

    # if args.output_file is None:
    #     parser.error('Output file is missing')

    try:
        with open(args.input_file) as f1:
            content = f1.read()
            with open(args.output_file, 'w') as f2:
                f2.write(content.upper())
                print(f'upper case version of "{args.input_file}" is written to "{args.output_file}"')
            # f2 is closed here
        # f1 is closed here
    except OSError as err:
        print(f'encountered an error - {err}')


if __name__ == '__main__':
    main()
    print('end of script execution')
