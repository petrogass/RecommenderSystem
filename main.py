import pandas as pd
import numpy as np

data = pd.io.parsers.read_csv('Dataset/ratings.dat', names = ['user_id', 'movie_id', 'rating', 'time'],
                              engine = 'python', sep = '::')
movies = pd.io.parsers.read_csv('Dataset/movies.dat', names = ['movie_id', 'title', 'genre'],
                                engine = 'python', sep = '::', encoding= 'windows-1252')

ratings_mat = np.ndarray(shape = (np.max(data.movie_id.values), np.max(data.user_id.values)),
                         dtype = np.uint8)
ratings_mat[data.movie_id.values-1, data.user_id.values-1] = data.rating.values

norm