"""
Method:         Word Cloud
Data Variables: Text (From Wikipedia Shakespeare biography )
Author:         nan
"""

word_string = ("William Shakespeare (/ˈʃeɪkspɪər/; 26 April 1564 (baptised) – 23 April 1616) was an English poet," +
               "playwright, and actor, widely regarded as the greatest writer in the English language and the world's" +
               "pre-eminent dramatist. He is often called England's national poet, and the 'Bard of Avon'.[nb 2] " +
               "His extant works, including collaborations, consist of approximately 38 plays,[nb 3] 154 sonnets, " +
               "two long narrative poems, and a few other verses, some of uncertain authorship." +
               "His plays have been translated into every major living language and are performed " +
               "more often than those of any other playwright.")

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white',
                      width=1200, height=1000).generate(word_string)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()
