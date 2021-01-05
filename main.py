from tkinter import *
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
import matplotlib.pyplot as plt


def display():
    text1.delete(0.0, "end")
    txt = str(ent.get())
    lower_case = txt.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
    tokenized_words = word_tokenize(cleaned_text, "english")
    final_words = []
    for word in tokenized_words:
        if word not in stopwords.words("english"):
            final_words.append(word)

    emotion_list = []
    with open('emotion.txt', 'r') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in final_words:
                emotion_list.append(emotion)

    def sentiment_analysis(sentiment_text):
        score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
        neg = score['neg']
        pos = score['pos']
        if neg > pos:
            text1.insert(0.0, 'Negative Sentiment')
        elif pos > neg:
            text1.insert(0.0, 'Positive Sentiment')
        else:
            text1.insert(0.0, 'Neutral Sentiment')

    sentiment_analysis(cleaned_text)
    # print(emotion_list)
    w = Counter(emotion_list)
    # print(w)

    # Plotting the emotions on the graph

    fig, ax1 = plt.subplots()
    ax1.bar(w.keys(), w.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    plt.show()


def go():
    quit()


def delete():
    ent.delete(0, "end")


root = Tk()
root.title("Opinion Mining")
root.geometry("850x300")

label1 = Label(root, text="Type Text Here:")
ent = Entry(root, width=100)
button1 = Button(root, text="Submit", bg="green", fg="white", command=display)
button2 = Button(root, text="Reset", bg="yellow", fg="black", command=delete)
button3 = Button(root, text="Quit", bg="red", fg="white", command=go)
text1 = Text(root, width=80, height=10, wrap=WORD)

label1.grid(row=0)
ent.grid(row=0, column=1)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
text1.grid(row=2, columnspan=2)

root.mainloop()
