#Movie ratings processing
#Import urlib and zipfile for downloading and uncompressing
import urllib.request
import zipfile
import os
import pandas as pd

DEBUG = True

#URL for the public data
url = "http://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
#this is the working directory
working_dir="../data/movies/"
#Destination filename
file_name = working_dir +  "movies.zip"
# Download the file from `url` and save it locally under `file_name`:
if os.path.isfile(file_name):
	print('Data is already downloaded')
else:
	print('Downloading...')
	urllib.request.urlretrieve(url, file_name)

#I want to know the names of the extracted files
inner_dir = "ml-latest-small/"
file_names = os.listdir(working_dir + inner_dir)

expected_files=['links.csv', 'movies.csv', 'ratings.csv', 'README.txt', 'tags.csv']

if expected_files==file_names:
	print('You already have them')
else:
	path_to_zip_file = working_dir +  "movies.zip"
	#The work directory
	directory_to_extract_to = working_dir
	#Reference to zipfile
	print('Extracting...')
	zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
	zip_ref.extractall(working_dir)
	#Is important to use .close()
	zip_ref.close()

#I want to know the names of the extracted files 
print(file_names)

movie_names=['movie_id','title','genres']
rating_names=['user_id','movie_id','rating','timestamp']


#Reading the files
movies = pd.read_csv(working_dir +
	inner_dir + 
	expected_files[1], sep = ',',names=movie_names)
ratings = pd.read_csv(working_dir +
	 inner_dir +
	 expected_files[2], sep = ',',names=rating_names)
#Print the first lines
if DEBUG:
	print(movies.head())
	print(ratings.head())

print("the names of our new dataframe are:")
print(list(movies.columns.values))
print(list(ratings.columns.values))

print("The dimensions are:")
print(movies.count())
print(ratings.count())

rated_movies= pd.merge(movies,ratings,on='movie_id')
rated_movies=rated_movies.sort_values('rating',ascending=False)

top20=rated_movies.head(20)

top5_dict={}

for i in range(5):
	title= top20[i]['title']
	for j in rated_movies:
		if rated_movies[j]['title'] == title:
			top5_dict[title] = rated_movies[j]

print(rated_movies.head(50))
print(list(rated_movies.columns.values))



