def count_words(text):
      words = len(text.split())
      return words

def count_chars(text):
      
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_dict(dictionary):
    sorted_list = [{"char": c, "num": n} for c, n in dictionary.items()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
