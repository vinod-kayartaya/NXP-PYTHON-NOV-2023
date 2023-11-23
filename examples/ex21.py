"""
Handle CLI args
"""
import argparse


def main():
    parser = argparse.ArgumentParser(description='A simple example for handling CLI args')
    parser.add_argument('-o', '--outfile', help='Specify the output filename')
    parser.add_argument('-r', '--format', help='Specify the output format')
    parser.add_argument('-f', '--file', help='Specify the source CSV file')
    args = parser.parse_args()
    # print(args)

    file_name = args.file
    out_file = args.outfile
    frmt = args.format

    # print(f'type of args.outfile is {type(args.outfile)}')

    if file_name is None:
        file_name = input('Enter the source CSV filename: ')
    if out_file is None:
        out_file = file_name[:-4] + '.json'
    if frmt is None:
        frmt = 'json'

    # do stuff here....
    print(f'{out_file} has been generated successfully using {file_name} in {frmt} format.')


if __name__ == '__main__':
    main()
