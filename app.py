import streamlit as st
import pickle

# Load the recommendation models from pickle files
popular_recommendations = pickle.load(open('PopularBookRecommendation.pkl', 'rb'))
collaborative_filtering_pt = pickle.load(open('pt.pkl', 'rb'))
books_data = pickle.load(open('book.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

st.title('Book Recommendation System')

if st.button('Get Popular Recommendations'):
    st.write(popular_recommendations.to_dict(orient='records'))

book_name = st.text_input('Enter a book name for recommendations')
if book_name:
    recommendations = recommendation(book_name)
    st.write(recommendations)
