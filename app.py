import streamlit as st
import pickle
import pandas as pd

# Page setup
st.set_page_config(page_title="Book Recommender", layout="centered")
st.title("📚 Book Recommendation System")

# Load our saved files
books = pickle.load(open('books_list.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# UI for User ID
user_id = st.number_input("Enter User ID to get recommendations", min_value=1, step=1)

if st.button('Predict Recommendations'):
    # Logic to find books the user hasn't read (Simplified for now)
    # We will just show the logic you used in your notebook here
    unique_isbns = books['ISBN'].unique()[:100] # checking first 100 for speed
    
    predictions = []
    for isbn in unique_isbns:
        pred = model.predict(user_id, isbn)
        predictions.append((isbn, pred.est))
    
    # Sort and get top 5
    predictions.sort(key=lambda x: x[1], reverse=True)
    top_5 = predictions[:5]
    
    st.write("### Top Recommendations for you:")
    for isbn, rating in top_5:
        title = books[books["ISBN"] == isbn]["Book-Title"].values[0]
        st.success(f"**{title}** (Predicted Rating: {round(rating, 2)})")

        
