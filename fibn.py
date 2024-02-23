# fib(n)

import argparse

def fib(n):
  output = [0, 1]
  for n in range(n):
    x, y = output[-2:]
    output.append(x + y)
  return output
 
def main():
  parser = argparse.ArgumentParser(description="fib(n)")
  parser.add_argument('-n', type=int, help="The number to check")
  args = parser.parse_args()
  [print(n) for n in fib(args.n)]

if __name__ == "__main__":
  main()