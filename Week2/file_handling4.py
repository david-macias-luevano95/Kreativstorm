def calculate_sum_from_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_sum = 0

            for line in lines:
                try:
                    number = float(line.strip())  
                    total_sum += number
                except ValueError:
                    print(f"Skipping line '{line.strip()}' as it is not a valid number.")

        return total_sum

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

if __name__ == "__main__":
    file_name = "c:/Users/davit/Documents/Kreavistorm/week2/Nueva carpeta/numbers.txt"  
    total_sum = calculate_sum_from_file(file_name)

    if total_sum is not None:
        print(f"The sum of numbers in '{file_name}' is: {total_sum}")
