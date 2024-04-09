import streamlit as st
import pickle
import numpy as np

pt = pickle.load(open('pt.pkl','rb'))
book = pickle.load(open('book.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))
book_list = pt.index.values

def recommendation(book_name):
    # fetching Index
    index = np.where(np.array(list(pt.index))==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[0])),reverse=True,key=lambda x:x[1])[1:9]

    data =[]
    for i in similar_items:
        item = []
        temp_df = book[book['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)
    return data


st.header("Book Recommender System")
st.sidebar.title("Recommend Books")
selected_book = st.sidebar.selectbox("Type or select a book from the dropdown",book_list)
if st.sidebar.button("Recommend Me"):
    moviee = recommendation(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(moviee[0][2])
        st.text(moviee[0][0])
        st.text(moviee[0][1])
    with col2:
        st.image(moviee[1][2])
        st.text(moviee[1][0])
        st.text(moviee[1][1])
    with col3:
        st.image(moviee[2][2])
        st.text(moviee[2][0])
        st.text(moviee[2][1])
    with col4:
        st.image(moviee[3][2])
        st.text(moviee[3][0])
        st.text(moviee[3][1])
    with col5:
        st.image(moviee[4][2])
        st.text(moviee[4][0])
        st.text(moviee[4][1])