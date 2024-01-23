def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    letters = letter_count(text)
    letters_list = list(letters.items())
    letters_list.sort()
    letter = []
    letter_numbers = []
    for i in letters_list:
        letter.append(i[0])
        letter_numbers.append(i[1])
    print(f"--- Book Report for {book_path}---")
    print(f"There are {words} words in the document. \n")
    for i in range(len(letter)):
         print(f"The '{letter[i]}', character was found {letter_numbers[i]} times.")
    print("\n--- End of Report ---")
    

    
def get_book_text(path):
    with open (path) as f:
        return f.read()

def word_count(text):
    word = 0
    words = text.split()
    for i in words:
        word+=1
    return word

def letter_count(text):
    lower_text = text.lower()
    letters = {}
    for letter in lower_text:
        if letter.isalpha():
            if letter in letters:
                letters[letter] +=1
            else:
                letters[letter] = 1
    return letters

if __name__ == "__main__":
    main()
