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
#print(file_names)

#movie_names=['movie_id','title','genres']
#rating_names=['user_id','movie_id','rating','timestamp']


#Reading the files
movies = pd.read_csv(working_dir +
	inner_dir + 
	expected_files[1], sep = ',')
ratings = pd.read_csv(working_dir +
	 inner_dir +
	 expected_files[2], sep = ',')
#Print the first lines
if DEBUG:
	print(movies.head(1))
	print(ratings.head(1))

#Doing the merge between movies and ratings
rated_movies= pd.merge(movies,ratings,on='movieId')

#Getting the sum of the ratings of the movies and grouping by name
top20=rated_movies['rating'].groupby(rated_movies['title']).sum()

#Sorting the values and getting the top 20 of the sum
top20=top20.sort_values(ascending=False).head(20)

#Getting the sum of the ratings of the movies and grouping by movieId
#top5ids=rated_movies['rating'].groupby(rated_movies['movieId']).sum()

#Sorting the values and getting the top 5 of the sum
#top5ids=top5ids.sort_values(ascending=False).head(5)
top5titles=top20.head(5)
#Getting the movieIds of the top 5 films
index=top5titles.index.get_level_values('title')

#Initialize top5 dataframe
top5=pd.DataFrame()

print('---------------------------------------------------------------------------------------------------------')
print('Top 20 películas basado en la suma de sus ratings')
print(top20)

#Getting all the information and ratings from the top 5 films
print('---------------------------------------------------------------------------------------------------------')
print('Toda la información de las primeras cinco películas del Top 20')
for i in index:
	#Loading info into top5 dataframe
	top5=top5.append(rated_movies.loc[rated_movies['title']==i])
	#Printing top 5 movies info	
	print(rated_movies.loc[rated_movies['title']==i])
print('---------------------------------------------------------------------------------------------------------')
#print(top5)



