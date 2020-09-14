from rake_nltk import Rake
import stanfordnlp
import sys
# stanfordnlp.download('en')
nlp = stanfordnlp.Pipeline()
sensitive_behavior = {'contact':['address book', 'phone book'],
						'microphone': ['microphone', 'record audio', 'records audio'],
						'location': ['location', 'gps']}
sensitive_permissions = {'contact':['android.permission.READ_CONTACTS','android.permission.WRITE_CONTACTS'],
							'microphone':['android.permission.RECORD_AUDIO'],
							'location':['android.permission.ACCESS_FINE_LOCATION','android.permission.ACCESS_COARSE_LOCATION']}
sensitive_description = {'contact': [], 'microphone': [], 'location': []}
r = Rake()
f = open(sys.argv[1], 'r')
texts = []
sent2id = {}
id2sent = {}
ids = 0
for line in f.readlines():
	line = line.strip('\n').split('.')
	for temp in line:
		if temp == '':
			continue
		texts.append(temp)
		sent2id[temp.lower()] = ids
		id2sent[ids] = temp.lower()
		ids += 1


for text in texts:
	for key in sensitive_permissions:
		for permission in sensitive_permissions[key]:
			if permission in text:
				sensitive_description[key].append(text.lower())
	for key in sensitive_behavior:
		for behavior in sensitive_behavior[key]:
			if behavior in text:
				sensitive_description[key].append(text.lower())
	text = text.lower()
	r.extract_keywords_from_text(text)
	key_words = r.get_ranked_phrases_with_scores()
	for word in key_words:
		if 'contact' in word[1]:
			stan = nlp(word[1])
			for s in stan.sentences:
				for w in s.words:
					if 'contact' not in w.text:
						continue
					if w.upos == 'NOUN':
						if text not in sensitive_description['contact']:
							sensitive_description['contact'].append(text)
		if 'location' in word[1]:
			if text not in sensitive_description['location']:
				sensitive_description['location'].append(location)
		if 'microphone' in word[1]:
			if text not in sensitive_description['microphone']:
				sensitive_description['microphone'].append(text)
for key in sensitive_description.keys():
	temp = set(sensitive_description[key])
	for sent in temp:
		print(sent)
		print(sent2id[sent])
		# print(id2sent[sent2id[sent] - 1])
	# for key in sensitive_behavior.keys():
	# 	for value in sensitive_behavior[key]:
	# 		temp_text = ''
	# 		if value in text:
	# 			sentences = text.split('.')
	# 			summary = ''
	# 			if len(sentences) == 1:
	# 				temp = sentences[0].split(' ')
	# 				if len(temp) < 5:
	# 					continue
	# 				else:
	# 					summary = sentences[0]
	# 			else:
	# 				if (len(sentences[0]) < 3):
	# 					summary = sentences[1]
	# 				else:
	# 					summary = sentences[0]
	# 			summary = summary.lower()
	# 			r.extract_keywords_from_text(summary)
	# 			key_words = r.get_ranked_phrases()
	# 			for word in key_words:
	# 				if key in word:
	# 					stan = nlp(word)
	# 					for s in stan.sentences:
	# 						for w in s.words:
	# 							if key in w.text:
	# 								if w.upos == 'NOUN':
	# 									if text not in sensitive_description[key]:
	# 										temp_text = text
	# 										sensitive_description[key].append(temp_text)
	# 									else:
	# 										continue
	# 							else:
	# 								continue
	# 				else:
	# 					continue
	# 			if temp_text == '':
	# 				sensitive_description[key].append(text)

# appname = sys.argv[1]
# print(appname)
# for key in sensitive_description.keys():
# 	target_text = ''
# 	score = 0.0
# 	f = open('/Users/shaoyang/Desktop/API_exp/contact_apps/temp/' + key + '/' + appname, 'w')
# 	for text in sensitive_description[key]:
# 		temp_score = 0.0
# 		r.extract_keywords_from_text(text)
# 		key_words = r.get_ranked_phrases_with_scores()
# 		for i in key_words:
# 			if key in i[1]:
# 				temp_score += i[0]
# 		print(temp_score, score)
# 		if temp_score > score:
# 			target_text = text
# 			score = temp_score
# 	print(target_text)
# 	f.write(target_text + '\n')
# 	f.close()
			# for sent in sentences:
			# 	r.extract_keywords_from_text(sent)
			# 	key_words = r.get_ranked_phrases()
			# 	print(key_words)
			# 	for words in key_words:
			# 		if key not in words:
			# 			continue
			# 		else:
			# 			print(words)
	# print(r.get_ranked_phrases())