import streamlit as st 
import pandas as pd
import nltk 
import pickle
import joblib

st.title("Movie Recommendation System")

with open("movies_List.pkl",'rb') as movie:
    movies=pickle.load(movie)

name=movies['title'].values

similarity=joblib.load("similar_movies.joblib")

def recommend(movie):
    
    movie_index=movies[movies['title']==movie].index[0]
    
    recommended_movie=similarity[movie_index]

    movie_list=sorted(enumerate(recommended_movie),reverse=True,key=lambda x:x[1])[1:6]
    
    recommendations=[]

    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)
    
    return recommendations

name_movie=st.selectbox("Enter the Movie Name",name)

if st.button("Recommend"):
    recommendations=recommend(name_movie)
    
    st.write("The Recommended Movies are :")

    for i in recommendations:
        st.write(i)