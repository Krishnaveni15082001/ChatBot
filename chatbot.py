#import libraries
from newspaper import Article
import random
import string
import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)

article = Article('https://www.nationalgeographic.com/environment/article/global-warming-overview')
article.download()
article.parse()
article.nlp()
corpus = article.text

#print the article text
#print(corpus)

#Tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text) #a list of sentences
#print(sentence_list)

def greetings(text):
  text = text.lower()

  bot_greeting = ['hi','hello','howdy','hola','wassup']
  user_greeting = ['hi','hello','hey','hola']

  for word in text.split():
    if word in user_greeting:
      return random.choice(bot_greeting)

def index_sort(list_var):
  length = len(list_var)
  list_index = list(range(0,length))

  x = list_var
  for i in range(length):
    for j in range(length):
      if x[list_index[i]] > x[list_index[j]]:
        temp = list_index[i]
        list_index[i] = list_index[j]
        list_index[j] = temp
  print(list_index)

#bot response
def bot_response(user_input):
  user_input = user_input.lower()
  sentence_list.append(user_input)
  bot_response = ''
  cm = CountVectorizer().fit_transform(sentence_list)
  similarity_scores = cosine_similarity(cm[-1], cm)
  similarity_scores_list = similarity_scores.flatten()
  index = index_sort(similarity_scores_list)
  index = index[1:]
  response_flag = 0

  j=0
  for i in range(len(index)):
    if similarity_scores_list[index[i]] > 0.0:
      bot_response = bot_response+' '+sentence_list[index[i]]
      response_flag = 1
      j = j+1
      if j>2:
        break
  
  if response_flag == 0:
    bot_response = bot_response+' '+"I apologize, I don't understand."
  
  sentence_list.remove(user_input)

  return bot_response

def output(user_input):
    #start chat
    print("Hi how can i help you?")
    exit_list = ['exit','bye','quit','break','see you later']
    while True:
        user_input = input()
        if user_input.lower() in exit_list:
            print('bye')
            break
        else:
            if greetings(user_input) != None:
                return('Bot :'+greetings(user_input))
            else:
                return('Bot :'+bot_response(user_input))

#Creating GUI with tkinter
import tkinter
from tkinter import *


def send():
    user_input = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if user_input != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + user_input + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

        response = output(user_input)
        ChatLog.insert(END, "Bot: " + response + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

base = Tk()
base.title("Hello")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()
