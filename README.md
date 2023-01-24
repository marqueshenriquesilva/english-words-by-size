# List of English Words Organized by Size

> 📜 Collection of text files containing up to 479k English words organized by both size (number of letters) and alphabetical order.

This list is based on the work done on [this](https://github.com/dwyl/english-words) repository.

As I was searching for a good word list for my Wordle app, I found lots of lists organized by alphabetical order, but I had trouble finding a good list of words organized by size (number of letters).

For this reason, I made this list, organized by size *and* alphabetical order, in a simple new-line-delimited text file so you can use it for your apps, databases, games, etc.

Main files:
  - [words_by_size.txt](words_by_size.txt) contains all words (including numbers and symbols).
  - [words_by_size_alpha.txt](words_by_size_alpha.txt) contains words with only alphanumeric characters.
  - [words_with_size.json](words_with_size.json) contains a json file with words ordered **only in alphabetical order**, but with the value of their sizes.
  
I also added some of the script files that I used to do the conversions.
  - [organize_words.py](scripts/organize_words.py).
  - [organize_words_json.py](scripts/organize_words_json.py), for your json projects.
