import csv
import os
import json
from nltk.tokenize import word_tokenize
from hbconfig import Config
import string
from nltk.corpus import stopwords

Config('kaggle_movie_review')

# Path of training data directory 
train_path = Config.data.train_folder_path
# Take list of classes from train directory (name of each subfolder is name of class)
classes = os.listdir(train_path)
try:
    # Remove .DS_Store file (Desktop Services Store) if present in train directory. Its system generated file
    classes.remove('.DS_Store')
except:
    pass
# JSONIFY class list and store for reference in predict.py
jsonfied_classes_list = json.dumps(classes)
f = open("class_list.txt",'w')
f.write(jsonfied_classes_list)
# Calculate number of classes
num_classes = len(classes)

file = open('./data/kaggle_movie_reviews/train.tsv', mode='w')
filewriter = csv.writer(file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
filewriter.writerow(['PhraseId','SentenceId','Phrase','Sentiment'])


# READ DATA
print('Going to read training articles')
phraseID = 0
articleID = 0
for fields in classes:   
    # Get the index of class 
    index = classes.index(fields)
    print('Now going to read {} files (Index: {})'.format(fields, index))
    path = os.path.join(train_path, fields)
    # Take list of all files present in subfolder. Remove .DS_Store file (Desktop Services Store) if present.
    files = os.listdir(path)
    try:
        files.remove('.DS_Store')
    except:
        pass
    for fl in files:
        articleID = articleID +1
        filepath = os.path.join(path,fl)        # Prepare file path
        f=open(filepath, "r")
        contents =f.readlines()                      # Read file contents
        f.close()

        contents = [x.strip() for x in contents] 
        try:
            while(contents.index('')+1):
                contents.remove('')
        except: 
            pass
        try:
            while(contents.index('\t')+1):
                contents.remove('\t')
        except: 
            pass


        for line in contents:
            tokens = word_tokenize(line)
            # convert to lower case
            tokens = [w.lower() for w in tokens]
            # remove punctuation from each word
            table = str.maketrans('', '', string.punctuation)
            stripped = [w.translate(table) for w in tokens]
            # remove remaining tokens that are not alphabetic
            words = [word for word in stripped if word.isalpha()]
            # filter out stop words
            stop_words = set(stopwords.words('english'))
            words = [w for w in words if not w in stop_words]

            line = ' '.join(words)
            # If data presents write that data in TSV file
            phraseID = phraseID + 1
            if len(words) != 0:
                filewriter.writerow([phraseID , articleID, line,index])


