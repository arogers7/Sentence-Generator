import nltk

def OpenBook(title):
    book = open(title + ".txt", "r")

    return book.read();

if __name__ == '__main__':
    title = "SignOfFour"
    bookRawText = OpenBook(title)
