import json


def load_words(filename):
    # reads word file and returns words
    with open(filename) as word_file:
        valid_words = word_file.read().split()
    word_file.close()
    return valid_words


def calculate_word_and_size(word_list, index):
    # from the words file, reads word of given index, returning tuple with size and value
    word = word_list[index]
    word_size = len(word)
    return (word_size, word)


def writes_words_with_size(filename):
    # writes json file with key words and value of sizes
    json_words = json.dumps(words_by_size, indent=4)
    with open(filename, "w") as outfile:
        outfile.write(json_words)


if __name__ == '__main__':
    # load word list
    english_words = load_words("words_alpha.txt")

    # words dictionary for json file
    words_by_size = {}

    # take word from list and calculates size
    for i in range(len(english_words)):
        word_info = calculate_word_and_size(english_words, i)
        word_size = word_info[0]
        word = word_info[1]
        # adds key word and value size to dictionary
        words_by_size[word] = word_size

    # writes words with sizes into json file
    writes_words_with_size("words_alpha_with_size.json")

    print("Finished")
