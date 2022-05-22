import json
from pprint import pprint
import collections
import xml.etree.ElementTree as ET

def json_to_list(path_file, word_len = 6,top_words = 10):
	title_list = []
	word_list = []
	word_list2 = []
	with open(path_file, encoding="utf-8") as f:
		json_data = json.load(f)
		news_list = json_data["rss"]["channel"]["items"]
		for news in news_list:
			title_list = news['title'].split(' ')
			word_list.extend(title_list)
		for word in word_list:
			if len(word) >= word_len:
				word_list2.append(word) 
		curent_words = collections.Counter(word_list2)
	pprint(curent_words.most_common(top_words))

def xml_to_list(path_file, word_len = 6,top_words = 10):
	title_list = []
	word_list = []
	word_list2 = []
	parser = ET.XMLParser(encoding="utf-8")
	tree = ET.parse(path_file, parser)
	xml_root = tree.getroot()
	titles_list = xml_root.findall("channel/item/title")
	for title in titles_list:
		title_list = title.text.split(' ')
		word_list.extend(title_list)
		for word in word_list:
			if len(word) >= word_len:
				word_list2.append(word) 
		curent_words = collections.Counter(word_list2)
	pprint(curent_words.most_common(top_words))
	
json_to_list('files/newsafr.json')
xml_to_list('files/newsafr.xml')