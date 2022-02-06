"""
Predicted wordle answers with date 

@author: Chitral Patil (https://linktr.ee/Chitral_Patil)
"""
import datetime as dt
import pandas as pd
import numpy as np
from wordleArray import words

# today's answer was elder, so I grabbed the index of "elder" in "wordleArray" and the rest of the code predicts the answers for coming days
x = words.index('elder')

dateArray = []
wordArray = []

# 2081 (2315 - 234)
for i in range(2081):
    startDate = dt.datetime.today()+dt.timedelta(i)
    dateArray.append(startDate.date().strftime("%d-%m-%Y"))
    wordArray.append(words[i + 233])

wordsDateDictionary = {
    "date": dateArray,
    "word": wordArray
}
wordsDateDataframe = pd.DataFrame(wordsDateDictionary)
print(wordsDateDataframe)

#I've exported the dataframe into an excel file so y'all need not run the code 
wordsDateDataframe.to_excel("Predicted_Wordle_Answers.xlsx")

#creating html 
htmlMaal = wordsDateDataframe.to_html()
text_file = open("index.html", "w")
text_file.write(htmlMaal)
text_file.close()
