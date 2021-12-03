import pandas as pd
import numpy as np
import time
def top_cosine_similarity(data, movie_id, top_n = 10):
        index = movie_id -1



data = pd.read_csv('Dataset/ratings.dat', usecols = [0, 1, 2], names=['user_id', 'movie_id', 'rating'],
                              engine='python', sep='::')
movies = pd.read_csv('Dataset/movies.dat', names=['movie_id', 'title', 'genre'],
                                engine='python', sep='::', encoding='windows-1252')
data_mat = np.array(data.pivot(index = 'movie_id', columns = 'user_id', values = 'rating'))
data_mat = np.nan_to_num(data_mat)

movies = data_mat.shape[0]
users = data_mat.shape[1]
A = (data_mat - np.asarray([np.mean(data_mat, axis = 1)]).T)/np.asarray([np.std(data_mat, axis = 1 )]).T
print(A)
print(np.mean(A[0, :]))
print(np.std(A[0,:]))
print(A.shape[0])
print(A.shape[1])

U, S, V = np.linalg.svd(A)
print(U.shape)
print(S.shape)
print(V.shape)



"""
normalised_mat = ratings_mat - np.asarray([np.mean(ratings_mat, axis=1)]).T

A = normalised_mat/np.sqrt(ratings_mat.shape[0] - 1)

start = time.perf_counter()
U, S, V = np.linalg.svd(A)
elapsed = time.perf_counter()-start
print(elapsed)"""
