import streamlit as st
import pickle
import pandas as pd

# Load data
movies = pickle.load(open('model/movies.pkl', 'rb'))
cosine_sim = pickle.load(open('model/similarity.pkl', 'rb'))


def recommend(movie_title):
    movie_title = movie_title.strip()

    matches = movies[movies['title'] == movie_title]

    if matches.empty:
        return []

    idx = matches.index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:10]
    movie_indices = [i[0] for i in sim_scores]

    recommended = movies.iloc[movie_indices]

    if 'rating' in recommended.columns:
        recommended = recommended.sort_values(by='rating', ascending=False)

    return recommended[['title', 'rating']].values.tolist()


# UI
st.set_page_config(page_title="Movie Recommender", layout="centered")

st.title("Movie Recommendation System")

st.markdown("Enter a movie name to get similar recommendations.")

movie_list = movies['title'].values

selected_movie = st.selectbox("Select a movie", movie_list)

if st.button("Recommend"):
    results = recommend(selected_movie)

    st.subheader("Top Recommendations:")

    if not results:
        st.error("Movie not found.")
    else:
        for i, item in enumerate(results, 1):
            title, rating = item
            st.write(f"{i}. {title} (Rating: {round(rating, 2)})")

st.subheader("Top Rated Movies")

top_movies = movies.sort_values(by='rating', ascending=False).head(10)

for i, row in top_movies.iterrows():
    st.write(f"{i+1}. {row['title']} (Rating: {round(row['rating'], 2)})")

st.subheader("Dataset Info")
st.write(f"Total Movies: {movies.shape[0]}")
