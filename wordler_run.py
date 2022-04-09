from wordler import *
import pickle as pkl

[wordCounts,letterCounts] = pkl.load(open("data/model.pkl","rb"))

word = input("What is the word? ")

won, guesses,history = wordler(list(wordCounts.keys()),letterCounts,wordCounts,word)

if won:
    print("Wordler won!")
else:
    print("Wordler lost")

for guess, result in zip(guesses, history):
    print(guess)
    print("".join([str(x) for x in result]))