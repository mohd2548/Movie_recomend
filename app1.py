import pandas as pd
import streamlit as st
import pickle

# Function to recommend movies
def recommend(movie_name, movies, similarity):
    try:
        # Find the index of the selected movie
        movie_index = movies[movies['title'] == movie_name].index[0]
        distances = similarity[movie_index]

        # Get the top 5 most similar movies (excluding the first, which is the movie itself)
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        # Fetch recommended movie titles
        recommended_movies = [movies.iloc[i[0]].title for i in movie_list]
        return recommended_movies
    except IndexError:
        return ["Movie not found!"]

# Load the data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))  # Ensure this is a dictionary
movies = pd.DataFrame(movies_dict)  # Convert the dictionary to a DataFrame
similarity = pickle.load(open('similarity.pkl', 'rb'))  # Load the similarity matrix

# Streamlit app title
st.title('FlickFinder')

# Dropdown for selecting a movie
selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values  # Use movie titles for the dropdown
)

# Button to generate recommendations
if st.button('Recommend'):
    # Call the recommendation function
    recommendations = recommend(selected_movie_name, movies, similarity)

    # Display the recommended movies
    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)
