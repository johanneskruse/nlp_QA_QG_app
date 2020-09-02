#===============================================================================
import streamlit as st
from functions import *

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

import numpy as np
#===============================================================================

# Input variables  
models_dict_qg = Config.models_qg
models_dict_qa = Config.models_qa

demo_text_qg = Config.demo_text_qg
demo_text_qa = Config.demo_text_qa["context"]
demo_ques_qa = Config.demo_text_qa["question"]

#===============================================================================

def main_screen():
    st.title("Question Answering & Question Generation")
    st.subheader("Information regadring the demos")
    st.write("In this demo you will find ")
    st.subheader("Github")
    st.write("")
    st.subheader("COLAB demo")
    st.write("It is possible to run the whole app through a COLAB notebook"\
        "just follow the link: ")

#===============================================================================

def QG_screen():
    st.title("Question Generation")	
    
    #####################################
    #### Model select and user input ####
    option_qg = st.selectbox("Select model size:",
                        (list(models_dict_qg.keys())))
    user_input_qg = st.text_area("Please provide context text:", height=200,
                                value=f"{demo_text_qg}", max_chars=500)
    
    ######################################
    # List user context setence by setence
    sentences_qg = sent_tokenize(user_input_qg)
    list_context("Sentences", sentences_qg)

    ######################################
    #### Load the NLP model: ####
    nlp_qg  = modelsConfig_qg(option_qg)
    questions = nlp_qg(user_input_qg)
    
    st.write("**Question Generated:**")
    for i, question in enumerate(questions):
        st.write(f"{i+1}. {question}")


#===============================================================================

def QA_screen():
    st.title("Question Answering")

    #####################################
    #### Model select and user input ####
    st.subheader("Model selection")
    option_qa = st.selectbox("Select model:",
        (list(models_dict_qa.keys())))

    st.subheader("Provide the context:")
    user_context_qa = st.text_area("Please provide context text:", height=100,
                                value=f"{demo_text_qa}", max_chars=500)
    
    #####################################
    #### Context setence by setence ####
    sentences_qa = sent_tokenize(user_context_qa)
    list_context("Sentences", sentences_qa, checkbox=True)
        
    st.subheader("Provide the question(s):")
    user_question_qa = st.text_area("Please provide question text:", height=50,
                                value=f"{demo_ques_qa}", max_chars=200)
    
    questions = sent_tokenize(user_question_qa)

    #####################################
    #### Load the NLP model ####
    nlp_qa = modelsConfig_qa(option_qa)
    
    answers = {}
    for i, question in enumerate(questions):
        st.write(f"{i+1}. **Question**: {question}")
        answer = qa_compute_answer(nlp_qa, questions[i], user_context_qa, models_dict_qa[option_qa])
        
        answers[answer] = answer_index(answer, user_context_qa)
        st.write(f"{i+1}. **Answer**: {answer}")
        
    
    #####################################
    #### Highlight answer in context ####
    st.subheader("Answer shown in context")
    num_answer = range(1, len(answers)+1)
    
    if len(num_answer) == 1: 
        index_range = answers[list(answers)[0]]
        write_answer(user_context_qa, index_range)
    
    elif len(num_answer) > 1:
        option_qa = st.selectbox("Select question in context:", list(num_answer))
        index_range = answers[list(answers)[option_qa-1]]
        write_answer(user_context_qa, index_range)


    #####################################
    
    






