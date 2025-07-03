import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=f7aa4efe19170a4def02e613279c2722&language=en-US')
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))

    return recommended_movies, recommended_posters

movies_list = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("🎬 Movify")
st.subheader("Your Personal Movie Recommender")
st.markdown("---")

selected_movie_name = st.selectbox(
    'Choose your favorite movie',
    movies['title'].values,
    index=0,
    key="movie_select"
)

if st.button('Recommend'):
    recommended_movies, recommended_posters = recommend(selected_movie_name)
    st.title(f"Recommending other movies like '{selected_movie_name}':")
    st.markdown("---")
    st.write("You might also like:")
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(recommended_posters[idx])
            st.caption(recommended_movies[idx])

