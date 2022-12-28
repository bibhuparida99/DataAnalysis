
import pandas as pd
import numpyexample as np
import matplotlib.pyplot as plt
if __name__ == '__main__':
    unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
    users = pd.read_table('/Users/bibhu/Documents/DataAnalysis/python/ml-1m/users.dat', sep='::', header=None, names=unames, engine='python', encoding='utf-8')

    rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
    ratings = pd.read_table('/Users/bibhu/Documents/DataAnalysis/python/ml-1m/ratings.dat', sep='::', header=None, names=rnames, encoding='utf-8')
    mnames = ['movie_id', 'title', 'genres']
    movies = pd.read_table('/Users/bibhu/Documents/DataAnalysis/python/ml-1m/movies.dat', sep='::', header=None, names=mnames, encoding='ISO-8859-1')
    #to check sample data
    #print(users[:5])
    #print(ratings[:5])
    #print(movies[:5])

    #merge all three data with pandas merge method
    data = pd.merge(pd.merge(ratings, users), movies)
    #print(data.columns)

    #with panda.pivottable get mean rating
    mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
    print(mean_ratings)
