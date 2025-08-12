def word_count(book_contents):
    words = book_contents.split()
    num_words = len(words)
    print(f"Found {num_words} total words")


def count_char(book_contents):

    characters = {}
    
    for char in book_contents.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters

def sorted_characters(char_counts):
    
    list_of_characters = [{"char": ch, "num": cnt} for ch, cnt in char_counts.items()]

    sorted_list = sorted(list_of_characters, key=lambda x: x['num'], reverse=True)

    return sorted_list



        