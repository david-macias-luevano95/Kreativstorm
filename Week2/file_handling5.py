def remove_blank_lines(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        non_blank_lines = [line for line in lines if line.strip() != '']

        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(non_blank_lines)

        print(f"Blank lines have been removed and the result has been written to '{output_file}'.")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

if __name__ == "__main__":
    input_file_name = "c:/Users/davit/Documents/Kreavistorm/week2/Nueva carpeta/text_with_blank_lines.txt"  
    output_file_name = "text_without_blank_lines.txt" 

    remove_blank_lines(input_file_name, output_file_name)
