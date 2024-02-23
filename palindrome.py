# Check if a given string is a palindrome.

import math
import argparse

def is_palindrome(string) -> bool:
  lower_str = string.lower()
  str_len = len(lower_str)
  for i in range(math.ceil(str_len / 2)):
    left = lower_str[i]
    right = lower_str[str_len-(i + 1)]
    if (left != right):
      return False
  return True

def main():
  parser = argparse.ArgumentParser(description="Determine if a string is a palindrome")
  parser.add_argument('--string', type=str, help="The string to check")
  args = parser.parse_args()
  print(is_palindrome(args.string))

if __name__ == "__main__":
  main()
