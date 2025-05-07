def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents

def get_num_words(text):
    return len(text.split())

def char_histogram(text):
    chars = {}
    for char in text:
        c = char.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def create_report_entry(char, count):
    return {
        "char": char,
        "num": count
    }

def sort_key(dict):
     return dict["num"]

def sort_histogram(dict):
    report_entries = []
    for key in dict:
        report_entries.append(create_report_entry(key, dict[key]))
    report_entries.sort(reverse=True, key=sort_key)
    return report_entries