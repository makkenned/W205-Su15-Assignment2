from os import listdir
import numpy as np
from sys import exit
from operator import itemgetter
from csv import writer
import nltk, json
import string
import pylab
groups = [('warriors',), ('nbafinals2015',), ('warriors','nbafinals2015')]

mem_list = []
top_30 = []

def sort_top(toplist):
	list.sort(toplist,key=itemgetter(1))

# Keeps track of the top 30 words in each hashtag category. Could be more efficient.
def update_top(str, toplist, i):
	for entry in range(len(toplist)):
		if toplist[entry][0] == str:
			toplist[entry] = (str, mem_list[i][str])
			sort_top(toplist)
			return toplist

	if len(toplist)<30:
		toplist.append((str,mem_list[i][str]))
		if len(toplist) == 29:
			sort_top(toplist)
		return toplist

	if mem_list[i][str] > toplist[0][1]:
		toplist.pop(0)
		toplist.append((str,mem_list[i][str]))
		sort_top(toplist)
		return toplist
	return toplist


# Figures out which hashtag groups the tweet belongs to
def find_groups(tweet_text):
	inx = len(groups)
	flag = []
	for i in range(inx):
		flag.append(True)
		for group in groups[i]:
			if "#"+group not in tweet_text:
				flag[i]= False
	return flag

# Writes word counts as an unsorted csv and draws figures as pngs
def finalize_results():
	for i in range(3):
		labels = []
		values = []
		for x, y in top_30[i]:
			labels.append(x)
			values.append(y)
		print labels, values

		ind = np.arange(30)
		width = 0.8
		pylab.bar(ind+width/2,values,align = 'center')
		pylab.ylabel('Occurences')
		pylab.xlabel('Words')
		pylab.title('Top 30 words in tweets containing the hashtag(s) #'+' #'.join(groups[i]))
		pylab.xticks(ind+width/2,labels, rotation = 'vertical')
		pylab.tight_layout()
		plt.savefig('+'.join(groups[i])+'.png')
		with open('+'.join(groups[i])+'.csv','w') as f:
			for k, v in mem_list[i].iteritems():
				f.write("%s, %d\n" % (k,v))


if __name__ == '__main__':
	for i in groups:
		mem_list.append({})
		top_30.append([])
	for json_list in listdir('./json'):
		with open('json/'+json_list, 'r') as f:
			for tweet in f:
				d = json.loads(tweet)
				try:
					words = d['text'].encode('ascii', 'ignore')
				except KeyError:
					continue
				flag = find_groups(words)
				words = words.translate(string.maketrans('',''), string.punctuation).lower()
				words = words.split()
				for word in words:
					try:
						for i in range(len(groups)):
							if flag[i]:
							# Could probabLy do some optimization here
								if word in mem_list[i]:
									mem_list[i][word]+=1
									top_30[i] = update_top(word,top_30[i],i)
								elif nltk.corpus.wordnet.synsets(word):
									if word not in mem_list[i]:
										mem_list[i][word]=1
									else:
										mem_list[i][word]+=1
									top_30[i] = update_top(word,top_30[i],i)
									
					except TypeError:
						print words, flag
						raise
	finalize_results()
