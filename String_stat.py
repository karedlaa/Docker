# -*- coding: UTF-8 -*-

import flask;
import re;
import string;
import urllib;
import json;
import operator;
from collections import Counter, OrderedDict;

textFile = "Welcome to to to the online text analysis tool, the  refer detailed statistics of your text, perfect for translators " \
           "(quoting), for webmasters (ranking) or for normal users, to know the subject of a text. Now with new features " \
           "as the analysis of words groups, solos finding out the keyword density, analyse the prominence of word or " \
           "expressions. Webmasters can analyse the links on their pages. More instructions are about to be written, " \
           "please civic send us your feedback !";

clean_text = ''
for x in textFile:
    if x not in string.punctuation:
        clean_text += x

app = flask.Flask(__name__)

@app.route("/")
def textAnalysis():
    return " Text Analysis <br> Keys for<br> Given text----> textFile <br> String Operations----> strings"

@app.route("/textFile")
def print_text():
    return textFile



# string operations
@app.route('/strings', methods=['GET', 'POST'])
def strings():
    if flask.request.method == 'POST':
        print "test"
        fp = flask.request.files['the_file']
        print "test"
        #print fp.read()
        abc = fp.read()
        print abc
        fp.close()
        res_word = string_operations(abc)
        return res_word
    else:
        res_word = string_operations(textFile)
        return res_word

@app.route("/stringoperations")

def string_operations(textFile):
    
    
    string_dict = dict()
   
    
    count_pali = 0
    string = textFile.split();
    pal_list = list()
    sentence_rev = " ".join(reversed(string))
    
    for pali in string:
        if pali == pali[::-1]:
            if len(pali) >1:
                count_pali += 1
                pal_list.append(pali)
                
    string_dict['Number of palidromes'] = count_pali
    string_dict['palindromes'] = pal_list

    string_dict['filtered_text'] = clean_text
    string_dict['reverse_words'] = sentence_rev

    sentences = re.split(r'[.!?]+', textFile);


    string_dict['sentence_count'] = len(sentences)
    string_dict['sentences'] = sentences

    return json.dumps(string_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0');


