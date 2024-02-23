# Given a string,
# write a Python function that reverses the string
# and prints out every second letter

import argparse

def reverse_compact(string):
  return string[::-2]

def main():
  parser = argparse.ArgumentParser(description="Reverse and compact a string")
  parser.add_argument('--string', type=str, help="The word to reverse and compact")
  args = parser.parse_args()
  print(reverse_compact(args.string))

if __name__ == "__main__":
  main()