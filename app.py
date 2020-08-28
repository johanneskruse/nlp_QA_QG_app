
import streamlit as st
import pandas as pd
import os
import git
from nltk.tokenize import sent_tokenize

if not os.path.exists(f"{os.getcwd()}/question_generation/"):
    git.Git(os.getcwd()).clone("https://github.com/patil-suraj/question_generation.git")

from function_streamlit import *


#===============================================================================
# Input variables  
models_dict_qg = Config.models_qg
demo_text = Config.demo_text

models_dict_qa = Config.models_qa

#===============================================================================

PAGE_CONFIG = {"page_title":"QG_QA_demo.io","page_icon":":shark:","layout":"centered"}
st.beta_set_page_config(**PAGE_CONFIG)


# App start: 
def main():
    menu = ["Main", "Question Generation", "Question Answering"]
    choice = st.sidebar.selectbox("Menu", menu)

    #===========================================================================
    # Main Page: 
    if choice == "Main":
        st.title("Stremlit demos")
        st.subheader("How to run streamlit from colab")

    #===========================================================================
    # QG Page: 
    if choice == "Question Generation":
        st.title("Question Generation demo")	

        option_qg = st.selectbox("Select model size:",
                            (list(models_dict_qg.values())))

        nlp_qg, model_library = modelsConfig(option_qg)

        user_input = st.text_area("Please provide context text:", height=200,
                                    value=f"{demo_text}", max_chars=500)

        setences = sent_tokenize(user_input)

        st.write("**Sentence:**")
        for sent in setences:
            st.write(f"- {sent}")

        questions = nlp_qg(user_input)

        st.write("**Question Generated:**")
        for i, question in enumerate(questions):
            st.write(f"{i+1}. {question}")


    #===========================================================================
    # QA Page: 
    if choice == "Question Answering": 
        st.title("Question Answering demo")
 
        option_qa = st.selectbox("Select model size:",
            (list(models_dict_qa.values())))

        # nlp_qa = modelsConfig(option_qa)






if __name__ == '__main__':
    main()