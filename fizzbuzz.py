# For numbers 1 through n,
#   print "Fizz" for multiples of 3,
#   "Buzz" for multiples of 5
#   and "FizzBuzz" for multiples of both.

import argparse

def fizzbuzz(n) -> str: 
  output = ""
  if (n == 0): return output
  if (n % 3 == 0): output += "Fizz"
  if (n % 5 == 0): output += "Buzz"
  return output
 
def main():
  parser = argparse.ArgumentParser(description="Fizzbuzz")
  parser.add_argument('-n', type=int, help="The number to check")
  args = parser.parse_args()
  print(fizzbuzz(args.n))

if __name__ == "__main__":
  main()
