# Reading from a text file
def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("Contents of {}:".format(file_name))
            print(content)
    except FileNotFoundError:
        print("File '{}' not found.".format(file_name))
    except Exception as e:
        print("An error occurred:", e)

# Writing to a text file
def write_text_file(file_name, text):
    try:
        with open(file_name, 'w') as file:
            file.write(text)
            print("Text written to {}.".format(file_name))
    except Exception as e:
        print("An error occurred:", e)

# Example usage
if __name__ == "__main__":
    read_file_name = "input.txt"
    write_file_name = "output.txt"
    sample_text = "This is a sample text to write to the output file."

    # Reading from a text file
    read_text_file(read_file_name)

    # Writing to a text file
    write_text_file(write_file_name, sample_text)

