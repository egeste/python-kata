# Write a Python script that reads a file and prints its contents, then writes a new line to it.

import argparse

def file_rw(from_filename) -> bool:
  with open(from_filename, mode='r+') as from_file:
    file_contents = from_file.read()
    from_file.write('\n')
    from_file.close()
    return file_contents

def main():
  parser = argparse.ArgumentParser(description='Read a file and then write a newline to it')
  parser.add_argument('--filename', type=str, help='The file to read/write')
  args = parser.parse_args()
  print(file_rw(args.filename))

if __name__ == '__main__':
  main()
