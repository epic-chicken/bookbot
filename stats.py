def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    chars = {}
    lowered = text.lower()
    for char in lowered:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sort_on(dict):
    return dict["count"]


def get_sorted_count(char_count):
    sorted = []
    for char in char_count:
        sorted.append({"letter": char, "count": char_count[char]})
    sorted.sort(reverse = True, key = sort_on)
    return sorted