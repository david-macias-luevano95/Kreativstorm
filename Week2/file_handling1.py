def lines_words_characters(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            lines = text.split('\n')
            words = text.split()
            char_count = len(text)

        num_lines = len(lines)
        num_words = len(words)

        return num_lines, num_words, char_count

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None, None, None

if __name__ == "__main__":
    file_name = "c:/Users/davit/Documents/Kreavistorm/week2/Nueva carpeta/example.txt"  

    num_lines, num_words, char_count = lines_words_characters(file_name)

    if num_lines is not None:
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {char_count}")
