# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_V0Mh8_boE1Xkz7GLfY1vLCJPPBm1tFR
"""

import streamlit as st
from mood_extractor import extract_mood, extract_keywords
from fetch_movies import get_movies_by_genre
from genre_classifier import predict_genre

# Streamlit app
st.title("🎬 Movie Recommendation System")
st.write("Enter a description of the movie you feel like watching, and we'll recommend the best match!")

# User input
user_input = st.text_area("Enter your movie preference (e.g., 'I want a happy comedy movie with some action!')")

if st.button("Get Recommendations"):
    if user_input:
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

    else:
        st.warning("Please enter a movie preference.")