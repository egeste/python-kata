# Given a list of numbers, find the missing number in the sequence.

import argparse

def find_missing_seq(nums):
  nums.sort()
  for i in range(0, len(nums)):
    num = nums[i]
    if (i > 0):
      prev_num = nums[i-1]
      expected_num = prev_num + 1
      if (num != expected_num): return expected_num

def main():
  parser = argparse.ArgumentParser(description="Find the missing number in a sequece")
  parser.add_argument('--nums', type=str, help="Sequence to check (comma separated)")
  args = parser.parse_args()
  numbers = res = [int(n) for n in args.nums.split(',')]
  print(find_missing_seq(numbers))

if __name__ == "__main__":
  main()
