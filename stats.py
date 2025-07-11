def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
    return len(words)

def get_num_characters(path_to_file):
    character_count = {}
    with open(path_to_file) as f:
        file_contents = f.read().lower()
        characters = list(file_contents)
        for character in characters:
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    return character_count