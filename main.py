def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    lowered_string = file_contents.lower()  # takes all text and lower cases it
    words = lowered_string.split()  #not used currently
    charDict = charCount(lowered_string)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    print("")
    for each in charDict:
        print(f"the '{each["Char"]}' character was found {each["Num"]} times ")

    print("--- End Report ---")
    
def charCount(string):  ##char dict needs to say Char: value, Num: value
    char_count_dict = {}
    dictOfChar_string = []

    for char in string: #for each char in string, see if its in dict, if in add 1 to total of that char, if not add it.
        if char.isalpha():
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1

    for key, value in char_count_dict.items(): #Putting each char into its own dict and appending to the list of dicts
        dictOfChar_string.append({"Char": key, "Num": value})
       
    dictOfChar_string.sort(reverse=True, key=sort_on) # sorting list of dicts based on value of "Num" key
    
    return dictOfChar_string


def wordCount(StringArray):
    DictOfWords = {}
    
    
def sort_on(dict):
    return dict["Num"]

main()

