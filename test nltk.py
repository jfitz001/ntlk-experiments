
import nltk
import pandas as pd
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
pd.set_option('display.max_columns', 1000)
sid = SentimentIntensityAnalyzer()
results =[]

train = ["President Trump in comments Saturday said stock-rallying reports this week that trade talks with China would include the lifting of tariffs",
  "Why Tencent Music Stock Popped 10%", "The stock market closed higher Friday, extending its winning streak to a fourth session, on media reports that stoked hopes for progress",
  "They helped the 30-stock average, up 1.4 Friday, to rise more than 2%",
  "Tesla's 13 percent stock slump on Friday was the biggest of the new year",
  "Job Cuts, Sees 'Tiny Profit,' As Shares Tumble",
  "cutting 7 percent of the company's workforce", 
  "Quarter 1 earning are solid...through the roof!",
  "Stock pricing are soaring!",
  "The economy has bounced back and earnings season is very strong."
]


sid = SentimentIntensityAnalyzer()
for sentence in train:
  print(sentence)
  ss = sid.polarity_scores(sentence)
  for k in sorted(ss):
     print('{0}: {1}, '.format(k, ss[k]), end='')
print()

