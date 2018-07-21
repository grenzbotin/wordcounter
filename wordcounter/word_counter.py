#!/usr/bin/env python
# coding: utf8

import sys,re,collections,io,os,json
import treetaggerwrapper

from os.path import join, dirname
from dotenv import load_dotenv

# Create .env file path.
dotenv_path = join(dirname(__file__), '..', '.env')
 
# Load file from the path.
load_dotenv(dotenv_path)

# patterns that used to find or/and replace particular chars or words
# to find chars that are not a letter, a blank or a quotation
pat_letter = re.compile('[^a-zA-ZüöäÜÖÄ \']+')
# to find the 's following the pronouns. re.I is refers to ignore case
pat_is = re.compile("(it|he|she|that|this|there|here)(\'s)", re.I)
# to find the 's following the letters
pat_s = re.compile("(?<=[a-zA-Z])\'s")
# to find the ' following the words ending by s
pat_s2 = re.compile("(?<=s)\'s?")
# to find the abbreviation of not
pat_not = re.compile("(?<=[a-zA-])n\'t")
# to find the abbreviation of would
pat_would = re.compile("(?<=[a-zA-Z])\'d")
# to find the abbreviation of will
pat_will = re.compile("(?<=[a-zA-Z])\'ll")
# to find the abbreviation of am
pat_am = re.compile("(?<=[I|i])\'m")
# to find the abbreviation of are
pat_are = re.compile("(?<=[a-zA-Z])\'re")
# to find the abbreviation of have
pat_ve = re.compile("(?<=[a-zA-Z])\'ve")

path = 'files'

def get_words(file, language):
    with io.open(path+'/'+file,"r") as f:  
        words_box = []
        for line in f:
            words_box.extend(replace_abbreviations(line, language).split())
    return collections.Counter(words_box)

def replace_abbreviations(text, language):
    new_text = text

    if language == "de":
        new_text = re.sub(r"[0-9-()\"#/@;:<>{}\[\]`+=~|.!?,]", '', text)

    elif language == "en":
        new_text = pat_letter.sub(' ', text).strip().lower()
        new_text = pat_is.sub(r"\1 is", new_text)
        new_text = pat_s.sub("", new_text)
        new_text = pat_s2.sub("", new_text)
        new_text = pat_not.sub(" not", new_text)
        new_text = pat_would.sub(" would", new_text)
        new_text = pat_will.sub(" will", new_text)
        new_text = pat_am.sub(" am", new_text)
        new_text = pat_are.sub(" are", new_text)
        new_text = pat_ve.sub(" have", new_text)
        new_text = new_text.replace('\'', ' ')

    return new_text.lower()

def write_to_json(words, data, destination, tagger):
    if len(destination) > 0:
        listItem = {}
        listItem["party"] = destination[0]
        listItem["lastName"] = destination[1]
        listItem["firstName"] = destination[2]
        listItem["year"] = destination[3]
        listItem["month"] = destination[4]
        listItem["day"] = destination[5][:-4]
        listItem.setdefault("words", [])
    else:
        listItem = []

    for item in words:
        y = {}
        word, count = item
        tag = tagger.tag_text(unicode(word))
        maketags=treetaggerwrapper.make_tags(tag)
        for item in maketags:
            y["tag"] = item[1]
        y["word"] = word
        y["count"] = count

        

        if len(destination) > 0:
            listItem["words"].append(y)
        else: listItem.append(y)

    data.append(listItem)

if __name__=='__main__':
    data = []
    destination = []
    option = ""
    language = 'en'

    if len(sys.argv) > 1:
        language = sys.argv[1]
        if len(sys.argv) > 2: 
            option = sys.argv[2]
    
    tagger = treetaggerwrapper.TreeTagger(TAGLANG=language,TAGDIR=os.getenv('TREETAGGER_DIR'))

    for filename in os.listdir(path):
        if filename.endswith('.txt'):
            print "counting..."
            words = get_words(filename, language)

            if option == "filename":
                destination = filename.split("_")

            print "writing file..."
            write_to_json(words.most_common(), data, destination, tagger)

    with io.open('data.json', 'w',encoding="utf-8") as outfile:
        my_json_str = json.dumps(data, ensure_ascii=False)
        if isinstance(my_json_str, str):
            my_json_str = my_json_str.decode("utf-8")

        outfile.write(my_json_str)
    

