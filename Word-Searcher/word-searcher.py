import os

# Program for searching certain words in multiple files.
# Originally written to search for profanities.

words = []

def GetFiles(path, extensions):
    files = []

    for root, _, filenames in os.walk(path):
        for filename in filenames:
            if any(filename.endswith(extension) for extension in extensions):
                files.append(os.path.join(root,filename))
    return files

def CheckWord(line):
    global words
    converted_line = line.lower()
    detected = False

    for word in words:
        if word in converted_line:
            detected = True

    return detected

def ReadFile(path):
    lines = []
    line_number = 0
    number_detected = 0

    lines.append("-----" + path + "-----")

    try:
        with open(path, 'r') as file:
            for line in file:
                line_number = line_number + 1
                if CheckWord(line) == True:
                    lines.append("[" + str(line_number) + "]\t" + line.strip())
                    number_detected = number_detected + 1
    except Exception as e:
        print("error: " + e)

    if number_detected == 0:
        lines.append("NOT FOUND\n")
    else:
        lines.append("[" + str(number_detected) + " LINES]\n")

    return lines

if __name__ == '__main__':
    print("Enter a directory (Subdirectories are also read): ")
    directory = input()

    extensions = []
    ext_input = True
    print("Enter file extensions to search (Example: .py ; Leave blank and press enter to confirm list): ")
    while ext_input is True:
        to_add = input()
        if to_add != "":
            extensions.append(to_add)
        else:
            if len(extensions) == 0:
                print("Enter at least 1 file extension")
            else:
                ext_input = False

    word_input = True
    print("Enter words to search (Leave blank and press enter to confirm list): ")
    while word_input is True:
        to_add = str(input()).strip().lower()
        if to_add != "":
            words.append(to_add)
        else:
            if len(words) == 0:
                print("Enter at least 1 word to search")
            else:
                word_input = False

    if len(extensions) > 0 and len(words) > 0:
        try:
            files = GetFiles(directory, extensions)

            lines = []
            for file in files:
                lines.extend(ReadFile(file))

            for line in lines:
                print(line)
        except Exception as e:
            print("error: " + e)
    else:
        print("Extensions or Words list is empty")

    print("Press enter to exit")
    input()