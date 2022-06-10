# packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib import markers
import matplotlib as mpl
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.ticker as mtick


# plot params
wid = .4
alp = .6

axfont = {'family': 'Times New Roman',
        'color':  'k',
        'size': 15
        }
titlefont = {'family': 'Times New Roman',
        'color':  'k',
        'size': 20
        }
plt.figure(figsize=[15,10])

# read raw data
test_data = pd.read_csv("prediction_clean_spc.csv", encoding="latin-1")


# 1 - stacked bar charts(for all category)
# calculate number of tweets by category and sentiment
count_data = test_data.groupby(['category','sentiment'])['real_id'].count().reset_index(). # 'real_id' here is the unique id for each tweet
# remove category 'Immigration approval' because there are only several pieces of tweets about this topic, which is no solid enough
count_data = count_data[count_data['category']!='Immigration approval']

sentiment = ['negative','neutral','positive']
colors = ['y','indianred','steelblue']

# draw the plot
# X axis: category
# Y axis:count(sentiment) 
pivot_data = count_data.pivot_table(index=['category'],columns='sentiment',values='real_id').reset_index()
pivot_data.columns=['category','negative','neutral','positive']

plt.bar(pivot_data.category,
        height=pivot_data.negative,
        width=wid,
        label=sentiment[0],
        color=colors[0],
        alpha=alp)

plt.bar(pivot_data.category,
        height=pivot_data.neutral,
        bottom=pivot_data.negative,
        width=wid,
        label=sentiment[1],
        color=colors[1],
        alpha=alp)

plt.bar(pivot_data.category,
        height=pivot_data.positive,
        width=wid,
        bottom=pivot_data.negative+pivot_data.neutral,
        label=sentiment[2],
        color=colors[2],
        alpha=alp)

for x, y in enumerate(pivot_data.negative):
    plt.text(x, y, '%s' % y, ha='center', va='top')
for x, y in enumerate(pivot_data.neutral):
    plt.text(x, y+pivot_data.negative[x] + 10, '%s' % y, ha='center', va='top')
for x, y in enumerate(pivot_data.positive):
    plt.text(x, y + pivot_data.negative[x] + pivot_data.neutral[x] + 20, '%s' % y, ha='center', va='top')

plt.xlabel("Category",fontdict=axfont)
plt.xticks(fontsize=10)
plt.ylabel("Number",fontdict=axfont)
plt.yticks(fontsize=10)
plt.title('Polarity of Predicted Tweets',fontdict=titlefont)
plt.legend()
plt.show()


