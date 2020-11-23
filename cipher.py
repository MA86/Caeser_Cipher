def cipher(shft: int, text: str):
  """
  Computes a Caesar cipher on text input.

  Input: text, shift
  """

  import string

  cipher = ''
  eng_alphabet = string.ascii_lowercase

  for i in range(len(text)):
    if text[i] == ' ' or text[i] == '.':
      cipher += text[i]
      continue
    index_of_chr = eng_alphabet.index(text[i])
    if index_of_chr >= (len(eng_alphabet) - shft):
      cipher += eng_alphabet[(shft - (len(eng_alphabet) - index_of_chr))] 
    else:
      cipher += eng_alphabet[index_of_chr + shft]
  return cipher

if __name__ == "__main__":
  import sys
  shift = int(sys.argv[1])
  txt = sys.argv[2]

  print('Your Caesar cipher is: ', cipher(shift, txt))

