import argparse

def word_to_dict(string):
  letter_dict = {}
  for char in string:
    if char in letter_dict: letter_dict[char] += 1
    else: letter_dict[char] = 1
  return letter_dict

def are_anagrams(a, b):
  word_1_dict = word_to_dict(a)
  word_2_dict = word_to_dict(b)
  return word_1_dict == word_2_dict

def main():
  parser = argparse.ArgumentParser(description="Check for anagram")
  parser.add_argument('-a', type=str, help="A word to check")
  parser.add_argument('-b', type=str, help="A word to check")
  args = parser.parse_args()
  print(are_anagrams(args.a, args.b))

if __name__ == "__main__":
  main()