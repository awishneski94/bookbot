def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    letters = letter_count(text)
    print(f"--- Book Report for {book_path}---")
    print(f"There are {words} words in the document")
    print(letters)
    

    
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
    letters_list = list(letters.items())
    letters_list.sort()
    return letters_list

if __name__ == "__main__":
    main()
