import sys

from stats import char_histogram, get_book_text, get_num_words, sort_histogram


def main(path):
    text = get_book_text(path)
    word_count = get_num_words(text)
    histogram = char_histogram(text)
    sorted = sort_histogram(histogram)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for entry in sorted:
        print(f"{entry['char']}: {entry['num']}")
        
    print("============= END ===============")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main(sys.argv[1])