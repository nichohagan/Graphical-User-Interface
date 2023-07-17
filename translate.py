#!/usr/bin/env python

# Required libraries
# pip install googletrans
# pip install textblob
from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox


root = Tk()
root.title('Custom Language Translator')
root.iconbitmap('/Users/nick/Documents/Portfolio/Translate/icon.png')
root.geometry('880x300')

def translateIt():
    #pass
    # Delete any previous translations
    translatedText.delete(1.0, END)
    try:
        # Use languages from dictionary keys
        # 1. Get the From Language Keys (origianl)
        for key, value in languages.items():
            if (value == originalCombo.get()):
                fromLangKey = key

        # 2. get the To Language Keys (translated)
        for key, value in languages.items():
            if (value == translatedCombo.get()):
                toLangKey = key

        # Turn original text into a textblob
        words = textblob.TextBlob(originalText.get(1.0, END))

        # Translate the words
        words = words.translate(from_lang=fromLangKey, to=toLangKey)

        # Output translated text to screen
        translatedText.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator", e)


def clear():
    # Clear the text boxes
    originalText.delete(1.0, END)
    translatedText.delete(1.0, END)

#Grab LanguageList from googleTrans
languages = googletrans.LANGUAGES
print(languages)
# Convert language dictionary to list
languageList = list(languages.values())
#print(languageList)

# Text Boxes
originalText = Text(root, height=10, width=40)
originalText.grid(row=0, column=0, pady=20, padx=10)

translateButton = Button(root, text="Translate!", font=("Helvetica", 24), command=translateIt)
translateButton.grid(row=0, column=1, padx=10)

translatedText = Text(root, height=10, width=40)
translatedText.grid(row=0, column=2, pady=20, padx=10)

# Combo Boxes
originalCombo = ttk.Combobox(root, width=50, values=languageList)
originalCombo.current(21)                                           # Default original language, English
originalCombo.grid(row=1, column=0)

translatedCombo = ttk.Combobox(root, width=50, values=languageList)
translatedCombo.current(26)                                         # Default translated language
translatedCombo.grid(row=1, column=2)

# Clear Button
clearButton = Button(root, text="Clear", command=clear)
clearButton.grid(row=2, column=1)

root.mainloop()