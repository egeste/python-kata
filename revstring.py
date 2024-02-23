# Write a Python program to reverse a string.

import argparse

def revstring(string) -> str: 
  output = ""
  for char in string:
    output = char + output
  return output
 
def main():
  parser = argparse.ArgumentParser(description="Reverse string")
  parser.add_argument('--string', type=str, help="The string to reverse")
  args = parser.parse_args()
  print(revstring(args.string))

if __name__ == "__main__":
  main()
