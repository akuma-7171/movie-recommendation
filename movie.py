import streamlit as st
import pickle
import pandas as pd


def recommender(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distance = similarities[movie_index]

    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommened_movies = []

    for i in movie_list:
        recommened_movies.append(movies.iloc[i[0]].title)

    return recommened_movies

movies_list = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)

similarities = pickle.load(open('similarities.pkl', 'rb'))

st.title("movie recommendation system")

selected_movie = st.selectbox('search for movies', movies['title'].values)

if st.button('recommended'):

    r = recommender(selected_movie)
    for i in r:
        st.write(i)

