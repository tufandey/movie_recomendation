import streamlit as st
from mood_extractor import extract_mood, extract_keywords
from fetch_movies import get_movies_by_genre
from genre_classifier import predict_genre
import os

# Streamlit app
st.title("🎬 Movie Recommendation System")
st.write("Enter a description of the movie you feel like watching, and we'll recommend the best match!")

# Check if required files exist
if not os.path.exists("movies.csv"):
    st.error("Error: 'movies.csv' file not found. Please ensure the dataset is in the correct directory.")
    st.stop()

if not os.path.exists("genre_model.pkl"):
    st.error("Error: 'genre_model.pkl' file not found. Please train the model first.")
    st.stop()

# User input
user_input = st.text_area("Enter your movie preference (e.g., 'I want a happy comedy movie with some action!')")

if st.button("Get Recommendations"):
    if user_input:
        try:
            # Extract mood, keywords, and genre
            mood = extract_mood(user_input)
            keywords = extract_keywords(user_input)
            genre = predict_genre(user_input)

            # Fetch movie recommendations
            movies = get_movies_by_genre(genre)

            # Display results
            st.subheader(f"Mood: {mood}")
            st.subheader(f"Predicted Genre: {genre}")
            
            if movies:
                st.subheader("🎥 Recommended Movies:")
                for movie in movies:
                    st.write(f"**{movie['title']}** (⭐ {movie['vote_average']})")
            else:
                st.write("No recommendations found. Try a different prompt!")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a movie preference.")
