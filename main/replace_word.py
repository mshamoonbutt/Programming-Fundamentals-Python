def replace_word(input_file, output_file, search, replacement):
    try:
        with open(input_file, 'r') as file_input:
            content = file_input.read()

            # Custom implementation for replacing word
            replaced_content = ""
            i = 0
            while i < len(content):
                index = content.lower().find(search.lower(), i)
                if index == -1:
                    replaced_content += content[i:]
                    break
                replaced_content += content[i:index] + replacement
                i = index + len(search)

        with open(output_file, 'w') as file_output:
            file_output.write(replaced_content)

        # Custom implementation for counting occurrences
        occurrences = 0
        i = 0
        while i < len(content):
            index = content.lower().find(search.lower(), i)
            if index == -1:
                break
            occurrences += 1
            i = index + 1

        return occurrences
    except FileNotFoundError:
        return -1

def main():
    input_file = input("Enter input file name: ")
    output_file = input("Enter output file name: ")
    search_word = input("Enter word to search: ")
    replacement_word = input("Enter replacement word: ")

    replacements = replace_word(input_file, output_file, search_word, replacement_word)

    if replacements == -1:
        print(f"Error: Input file '{input_file}' not found.")
    else:
        print(f"I replaced {replacements} instance(s) of {search_word} with {replacement_word}\n")

if __name__ == "__main__":
    main()