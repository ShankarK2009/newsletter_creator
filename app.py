import streamlit as st
import main
import pandas as pd
import pyperclip

st.sidebar.title("Parameters")
news_api = st.sidebar.text_input("News API Key:", value="")
serp_api = st.sidebar.text_input("Serp API Key:", value="")

author = st.sidebar.text_input("Name of Author:", value="Lakshan Suresh")
headlines_slider = st.sidebar.slider("Number of Headlines:", min_value=1, max_value=6, value=4, step=1, key="hlines")
sports_slider = st.sidebar.slider("Number of Sports Results per League/Sport", min_value=1, max_value=4, value=4)
tech_slider = st.sidebar.slider("Number of Tech News:", min_value=1, max_value=6, value=4, step=1, key="tech")
science_slider = st.sidebar.slider("Number of Science News:", min_value=1, max_value=6, value=4, step=1, key="science")
inline_css = st.sidebar.checkbox("Make CSS Inline", value=True)
minify = st.sidebar.checkbox("Minify HTML", value=True)

def create_newsletter(name, headlines_slider, sports_slider, tech_slider, science_slider, inline_css, minify):
    env_file = open(".env", "w")
    print(news_api)
    print(serp_api)

    api_keys = f"""NEWS_API={news_api}
SERP_API={serp_api}
    """

    print(news_api)
    print(serp_api)

    env_file.write(api_keys)
    
    code = main.create(name, headlines_slider, sports_slider, tech_slider, science_slider, inline_css, minify)
    
    @st.fragment    
    def download():
        if st.download_button("Download HTML File", data=code,file_name="generated_newsletter.html"):
            @st.dialog("Successfully downloaded HTML file!")
            def dialog():
                st.write("Happy Reading!")
            dialog()
    download()

    with st.expander("See HTML Code"):
        st.text_area("HTML Code", code, 500)

    st.subheader("Headlines")
    st.dataframe(pd.DataFrame(main.headlines, columns=["Image", "Title", "Description", "URL"]), width=700)
    st.divider()
    st.subheader("Soccer")
    st.dataframe(pd.DataFrame(main.soccer, columns=["Team Name 1", "Team Name 2", "Team 1 Logo", "Team 2 Logo", "Team 1 Score", "Team 2 Score"]), width=700)
    st.divider()
    st.subheader("NBA")
    st.dataframe(pd.DataFrame(main.bball, columns=["Team Name 1", "Team Name 2", "Team 1 Logo", "Team 2 Logo", "Team 1 Score", "Team 2 Score"]), width=700)
    st.divider()
    st.subheader("March Madness")
    st.dataframe(pd.DataFrame(main.madness, columns=["Team Name 1", "Team Name 2", "Team 1 Logo", "Team 2 Logo", "Team 1 Score", "Team 2 Score"]), width=700)
    st.divider()
    st.subheader("Technology")
    st.dataframe(pd.DataFrame(main.tech_res, columns=["Image", "Title", "Description", "URL"]), width=700)
    st.divider()
    st.subheader("Science")
    st.dataframe(pd.DataFrame(main.news, columns=["Image", "Title", "Description", "URL"]), width=700)

st.header("The Weekly Pulse Automation", divider="gray")
st.write("Customize your newsletter effortlessly! Adjust the parameters in the sidebar, then hit the button below to generate a fresh, engaging newsletter with the latest global news, sports, finance, and tech updates—automated in seconds! 🚀")
create_button = st.button("Create Newsletter", icon=":material/rocket_launch:")

if create_button:
    create_newsletter(author, headlines_slider, sports_slider, tech_slider, science_slider, inline_css, minify)