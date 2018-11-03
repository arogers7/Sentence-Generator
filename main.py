import nltk
from nltk.tokenize import sent_tokenize

def OpenBook(title):
    book = open(title + ".txt", "r")

    return book.read();

if __name__ == '__main__':
    title = "SignOfFour"
    bookRawText = OpenBook(title)
    sentences = sent_tokenize(bookRawText)

    unigrams = {}
    bigrams = {}

    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)

        for i in range(len(tokens) - 1):
            word = tokens[i]
            nextWord = tokens[i+1]
            if word not in unigrams:
                unigrams[word] = 1
            else:
                unigrams[word] += 1

            if word not in bigrams:
                bigrams[word] = {nextWord:1}
            else:
                pass
                #bigrams[word][nextWord] += 1
    print(bigrams['undivided'])

    #print(bigrams)
