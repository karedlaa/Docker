Assignment2
===========
This application is about Text Analysis which is done using python.
String operations and sentence statistics are done for a given text.
JSON string is used to get the output.
JSON output consists of number of palindromes and what they are, filtered text which is off of punctuations, sentence statistics like how many sentences and what they are and also reverse words for a given sentence.

In Further project, it can be combined with text mining, word statistics, character statistics developed by whole team.
Front end or user interface will be implemented according to this with many more features.

How to use:

run below commands in docker after  

gzip -d strings.tar.gz 

docker load -i strings.tar.tar

docker tag <image_id> strings

docker run -d -p 5555:5555 strings /home/startme.sh


Give below link in browser.
http://localhost:5555/strings

