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


def make_word_slot(words_by_size, word_size):
    # makes new list(s) in words by size for words bigger than existing categories
    for i in range(word_size - len(words_by_size)):
        words_by_size.append([])


def writes_words_by_size(filename):
    # writes word file organized by size of words
    file_wordsize = open(filename, 'w')
    for i in range(len(words_by_size)):
        for j in range(len(words_by_size[i])):
            file_wordsize.writelines(f"{words_by_size[i][j]}\n")
    file_wordsize.close()


def user_word_list_selection(words_by_size):
    # user selects list of words according to words size
    while (True):
        select = input("Select word by number of letters (type X to escape): ")

        if (select == 'X' or select == 'x'):
            break
        elif (int(select) > len(words_by_size)):
            print(f"Index out of range. Maximun range: {len(words_by_size)}.")
        else:
            for i in words_by_size[int(select) - 1]:
                print(i, end=' ')
            print('\n')


if __name__ == '__main__':
    english_words = load_words("words.txt")

    words_by_size = []

    # take word from list and calculates size
    for i in range(len(english_words)):
        word_info = calculate_word_and_size(english_words, i)
        word_size = word_info[0]
        word = word_info[1]

        # create empty slot(s) for the word in words_by_size if necessary
        if (len(words_by_size) < word_size):
            make_word_slot(words_by_size, word_size)

        # append word to slot
        words_by_size[word_size - 1].append(word)

    # writes words organized by size in file
    writes_words_by_size("words_by_size.txt")

    # user prompt for words list per number of letters
    user_word_list_selection(words_by_size)

    print("Finished")
