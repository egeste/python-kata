# Write a script to merge two Python dictionaries.

dict_1 = ['a', 'c', '2', 'doe', 'mee', 'and']
dict_2 = ['b', '1', '3', 'rae', 'you', 'me']

def zipper_merge(a, b):
  a_len = len(a)
  b_len = len(b)
  output = []
  for i in range(max(a_len, b_len)):
    if (i < a_len): output.append(a[i])
    if (i < b_len): output.append(b[i])
  return output

def main():
  print(zipper_merge(dict_1, dict_2))

if __name__ == "__main__":
  main()