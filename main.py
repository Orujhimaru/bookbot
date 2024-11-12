with open("books/frankenstein.txt") as book:
    file_contents = book.read()
  
def main():
    # print(file_contents)
    word_count = file_contents.split()
    print(word_count)
    char_dict = {}
    for word in word_count:
        for char in word:
            lower_char = char.lower()
            if lower_char not in char_dict:
                char_dict[lower_char]=0
            else: char_dict[lower_char] = char_dict[lower_char]+1
    # print(char_dict)
    for i in char_dict:
        print(f"The'${i}' character was found ${char_dict[i]} times")
    

if __name__=="__main__":
    main()