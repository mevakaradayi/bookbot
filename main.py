from stats import word_count, count_char, sorted_characters

import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 

def get_book_text(file_path):

    with open(file_path) as f:
        return f.read()

file_path = sys.argv[1]

def main():

    book_contents = get_book_text(file_path)
    #print(book_contents)
    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {file_path}...")
    
    print("----------- Word Count ----------")
    word_count(book_contents)
    
    print("--------- Character Count -------")
    char_counts = count_char(book_contents)
    #print(char_counts)

    list_sorted = sorted_characters(char_counts)
    for item in list_sorted:
        ch = item['char']
        cnt = item['num']
        if ch != ' ':
            print(f"{ch}: {cnt}")
    print("============= END ===============")


main()

