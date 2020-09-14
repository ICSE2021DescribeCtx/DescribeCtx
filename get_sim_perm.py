import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

uidir = './UI_context/storage/'
cgdir = './cg2text/storage/'
allui = {}
uilist = []
allcg = {}
for app in os.listdir(uidir):
	if app == '.DS_Store':
		continue
	try:
		f = open(uidir + app + '/' + app + '.txt', 'r')
		ui = f.read()
		allui[app] = ui
		uilist.append(ui)
		f.close()
	except Exception as e:
		continue

for app in os.listdir(cgdir):
	if app == '.DS_Store':
		continue
	f = open(cgdir + app, 'r')
	cg = f.read()
	allcg[app[:app.index('.txt')]] = cg
	f.close()

for app in allcg.keys():
	if app in allui.keys():
		continue
	else:
		print('Find most similar UI context for: ' + app)
		print('----------------------------------')
		uilist.append(allcg[app])
		print(len(uilist))
		tfidf = TfidfVectorizer().fit_transform(uilist)
		pairwise_similarity = tfidf * tfidf.T
		result = pairwise_similarity.toarray()
		np.fill_diagonal(result, np.nan)
		source = allcg[app]
		source_idx = uilist.index(source)
		target_idx = np.nanargmax(result[source_idx])
		print('Call graph context of: ' + app)
		print(allcg[app])
		print('Most similar UI context:')
		print(uilist[target_idx])
		uilist.remove(allcg[app])
		f = open(uidir + app + '/' + app + '.txt', 'w')
		f.write(uilist[target_idx])
		f.close()