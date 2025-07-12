character_count = {}
sorted_list = []

def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
    return len(words)

def get_num_characters(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read().lower()
        characters = list(file_contents)
        for character in characters:
            if character.isalpha() and character in character_count:
                character_count[character] += 1
            elif character.isalpha():
                character_count[character] = 1
    return character_count

def sort_on(items):
    return items["num"]

def get_sorted_characters(character_dict):
    for characters in character_dict:
        count = character_dict[characters]
        sorted_list.append({"char": characters, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list