import string
from typing import Dict 
def main():
  book_name ="books/frankenstein.txt"
  with open(f"{book_name}", "r") as f:
    file_content = f.read()
    print(f"--- Begin report of {book_name} ---")
    print(f"{count_words(file_content)} words found in the document")
    characters_count=count_characters(file_content)
    for character,value in characters_count.items():
      print(f"The '{character}' character was found {value} times")
    print("--- End report ---")

def count_words(txt:str) -> int: 
  if txt:
    content_list = txt.split()
    return len(content_list)
  else:
    return 0 
def count_characters(content:str)->Dict[str, int]:
  characters_count = {}
  if content:
    for c in string.ascii_lowercase:
      characters_count[c] = content.lower().count(c)
    return characters_count


if __name__=="__main__":
  main()
