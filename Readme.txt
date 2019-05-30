Data will be present either in folder or in MongoDB

If It is in folder execute folder2TSV.py to convert data in tsv format.

If it is in MongoDB execute mongod2tsv.py to convert data in tsv format.

Now our data is ready in tsv format.

update configuration file config/kaggle_movie_review.yml

To process data, means train-test split, train data, train labels, test data, test labels execute data_loader.py

Before training delete the contents of logs folder (if any)

now for actual training execute main.py




After training 

copy config/kaggle_movie_review.yml and paste it in prediction code cofig folder (replace if already present there)

copy data/kaggle_processed_data  and paste in prediction code (replace if already present there)

copy logs folder  and paste in prediction code (replace if already present there)


