import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_lottie import st_lottie

# --- Page Configuration ---
st.set_page_config(page_title="Movify", layout="wide")

# --- Load Data ---
movies_list = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# --- Helper Functions ---
def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=f7aa4efe19170a4def02e613279c2722&language=en-US')
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies, recommended_posters

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Custom CSS ---
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stButton button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            padding: 0.6rem 1.5rem;
            font-size: 16px;
        }
        .stSelectbox label {
            font-weight: 600;
            font-size: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("🎬 Movify")
        st.subheader("Discover Similar Movies Using Content-Based Filtering")
        st.markdown("Get top 5 similar movies based on your favorite pick!")
    with col2:
        lottie = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json")
        st_lottie(lottie, height=180, key="movie_lottie")

st.markdown("---")

# --- Input Section ---
with st.container():
    selected_movie_name = st.selectbox(
        '📽️ Select a movie you like:',
        movies['title'].values,
        index=0
    )

    recommend_btn = st.button("🎯 Recommend Movies")

# --- Recommendation Output ---
if recommend_btn:
    with st.spinner("🔍 Fetching similar movies..."):
        recommended_movies, recommended_posters = recommend(selected_movie_name)

    st.success("✅ Recommendations ready!")

    st.subheader(f"Because you liked **{selected_movie_name}**, you might enjoy:")
    st.markdown("### 🎞️ Top 5 Recommendations")

    with st.container():
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.image(recommended_posters[idx])
                st.caption(recommended_movies[idx])


