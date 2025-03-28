import streamlit as st
import main
import pandas as pd

author = st.sidebar.text_input("Name of Author:", value="Lakshan Suresh")
headlines_slider = st.sidebar.slider("Number of Headlines:", min_value=1, max_value=6, value=4, step=1, key="hlines")
sports_slider = st.sidebar.slider("Number of Sports Results per League/Sport", min_value=1, max_value=4, value=4)
tech_slider = st.sidebar.slider("Number of Tech News:", min_value=1, max_value=6, value=4, step=1, key="tech")
science_slider = st.sidebar.slider("Number of Science News:", min_value=1, max_value=6, value=4, step=1, key="science")

def create_newsletter(name, headlines_slider, sports_slider, tech_slider, science_slider):
    main.create(name, headlines_slider, sports_slider, tech_slider, science_slider)
    st.dataframe(pd.DataFrame(main.headlines, columns=["Image", "Title", "Description", "URL"]), width=400)
    st.dataframe(pd.DataFrame(main.soccer, columns=["Team Name 1", "Team Name 2", "Team 1 Logo", "Team 2 Logo", "Team 1 Score", "Team 2 Score"]), width=400)
    st.dataframe(pd.DataFrame(main.bball, columns=["Team Name 1", "Team Name 2", "Team 1 Logo", "Team 2 Logo", "Team 1 Score", "Team 2 Score"]), width=400)
    st.dataframe(pd.DataFrame(main.madness, columns=["Team Name 1", "Team Name 2", "Team 1 Logo", "Team 2 Logo", "Team 1 Score", "Team 2 Score"]), width=400)
    st.dataframe(pd.DataFrame(main.tech_res, columns=["Image", "Title", "Description", "URL"]), width=400)
    st.dataframe(pd.DataFrame(main.news, columns=["Image", "Title", "Description", "URL"]), width=400)

st.header("The Weekly Pulse Automation", divider="gray")
st.write("Customize your newsletter effortlessly! Adjust the parameters in the sidebar, then hit the button below to generate a fresh, engaging newsletter with the latest global news, sports, finance, and tech updates—automated in seconds! 🚀")
create_button = st.button("Create Newsletter", icon=":material/rocket_launch:")

if create_button:
    create_newsletter(author, headlines_slider, sports_slider, tech_slider, science_slider)