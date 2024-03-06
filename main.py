def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    lowered_string = file_contents.lower()  # takes all text and lower cases it
    words = lowered_string.split()  #not used currently
    charDict = charCount(lowered_string)
    wordDict = wordCount(words)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    print("")
    for each in charDict:
        print(f"the '{each["Char"]}' character was found {each["Num"]} times ")
    print("")
    print("--- Most used Words used atleast 50 times ---")
    for each in wordDict:
        print(f"the word '{each["Word"]}' was used {each["Num"]} times ")
    print("") 
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


def wordCount(stringArray):
    DictOfWords = {}
    StringOfDictWords = []
    for word in stringArray:
        if word.isalnum():
            if word in DictOfWords:
                DictOfWords[word] += 1
            else:
                DictOfWords[word] = 1

    for key, value in DictOfWords.items():
            if value > 49:
                StringOfDictWords.append({"Word": key, "Num": value})
    
    StringOfDictWords.sort(reverse=True, key=sort_on)
    return StringOfDictWords
    
    
def sort_on(dict):
    return dict["Num"]

main()

