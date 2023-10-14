import streamlit as st
import pickle
import pandas as pd

import requests # to hit the API

movies_dict = pickle.load( open('movie_dict.pkl', "rb"))
movies = pd.DataFrame(movies_dict)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=17ff9f4bf16b1c672e9e339da6176f1e'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movies_index=movies[movies['title']==movie].index[0]
    distances=similarity[movies_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]



    recommend_movies = []
    recommend_movies_posters= []

    for i  in movies_list:
        recommend_movies.append((movies.iloc[i[0]].title))
        movie_id = movies.iloc[i[0]].movie_id

        #fetch poster from API
        recommend_movies_posters.append(fetch_poster(movie_id))

    return recommend_movies, recommend_movies_posters


similarity = pickle.load( open('similarity.pkl', "rb"))


st.title("Movies Recommender System")

selected_movie_name = st.selectbox("How would you like to be contacted",movies['title'].values)

# Button code
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.caption(names[0])
        st.image(posters[0])

    with col2:
        st.caption(names[1])
        st.image(posters[1])

    with col3:
        st.caption(names[2])
        st.image(posters[2])

    with col4:
        st.caption(names[3])
        st.image(posters[3])

    with col5:
        st.caption(names[4])
        st.image(posters[4])
    


# if st.button("Recommend"):
    
#     st.title(selected_movie_name)
#     st.selectbox("select",[recommend(selected_movie_name)])



