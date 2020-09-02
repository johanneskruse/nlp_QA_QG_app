#===============================================================================
import streamlit as st

from allennlp.predictors.predictor import Predictor
import allennlp_models.rc

import torch
import transformers

import git
import os
if not os.path.exists(f"{os.getcwd()}/question_generation/"):
    git.Git(os.getcwd()).clone("https://github.com/patil-suraj/question_generation.git")

from question_generation.pipelines import pipeline as qg_pipline
from transformers import pipeline as qa_pipline

#===============================================================================
class Config:
    models_qg = {
        "Question generation (without answer supervision) [small]" : "qg",
        "Question generation (without answer supervision) [base]" : "qg",
    }
    
    models_qa = {
        "ELMo-BiDAF (Trained on SQuAD)" : "allennlp",
        "BiDAG (Trained on SQuAD)" : "allennlp",
        # "Transformer QA (Trained on SQuAD)" : "allennlp", # not working [hack]
        "distilbert-base-cased-distilled-squad" : "huggingface_pipline", 
        "bert-large-uncased-whole-word-masking-finetuned-squad"  : "huggingface_pipline" 
        }


    demo_text_qg = "Infosys Limited, is an Indian multinational corporation" \
        "that provides business consulting, information technology" \
        "and outsourcing services. The company is headquartered in" \
        "Bangalore, Karnataka, India. Infosys is the second-largest" \
        "Indian IT company after Tata Consultancy Services by 2017 revenue" \
        "figures and the 596th largest public company in the world based" \
        "on revenue. On 29 March 2019, its market capitalisation was $46.52 billion."


    demo_text_qa = {"context" : "Python is a programming language. Created by Guido van Rossum and first released in 1991.",
                    "question" : "Who created Python? When was Python first released?"}

def list_context(title, list_input, checkbox = False):
    
    if checkbox:
        checkbox_sent = st.checkbox(f"Show {str(title).lower()}")
        
        if checkbox_sent:
            st.write(f"**{title}:**")
            for sent in list_input:
                st.write(f"- {sent}")
    else: 
        st.write(f"**{title}:**")
        for sent in list_input:
            st.write(f"- {sent}")


## Load model
@st.cache
def modelsConfig_qg(model):
    ## Question Generation: 
    if model == "Question generation (without answer supervision) [small]":
        model_selected = qg_pipline("e2e-qg", model="valhalla/t5-small-e2e-qg")
    
    elif model == "Question generation (without answer supervision) [base]":
        model_selected = qg_pipline("e2e-qg", model="valhalla/t5-base-e2e-qg")    
    
    else:
        raise Exception("Not a valid model")   

    return model_selected


@st.cache(allow_output_mutation=True)
def modelsConfig_qa(model):
    ## Question Answering: 
    if model == "ELMo-BiDAF (Trained on SQuAD)":
        model_selected = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/bidaf-elmo-model-2020.03.19.tar.gz")
    elif model == "BiDAG (Trained on SQuAD)":
        model_selected = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/bidaf-model-2020.03.19.tar.gz")
    elif model == "Transformer QA (Trained on SQuAD)":
        model_selected = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/transformer-qa-2020-05-26.tar.gz")
    elif model == "distilbert-base-cased-distilled-squad":
        model_selected = qa_pipline("question-answering", model=f"{model}")
    elif model == "bert-large-uncased-whole-word-masking-finetuned-squad":
        model_selected = qa_pipline("question-answering", model=f"{model}")
    else:
        raise Exception("Not a valid model")    
    return model_selected



def qa_compute_answer(model, question, context, model_library):
    if model_library == "allennlp":
        answer = predict_QnA_allennlp(question, context, model)["best_span_str"]
    
    elif model_library == "huggingface_pipline":
        answer = model(question=question, context=context)["answer"]
    return answer


def predict_QnA_allennlp(question, passage, model): 
    ''' 
    Helper function for input convention used in hugging face implementation:
        [QUESTION : ANSWER_TEXT]
    '''
    prediction = model.predict(passage=passage, question=question)
    return prediction


def answer_index(answer, context):
    index_range = []
    word_len = []    

    for word in answer.split():
        word.lower()
        idx = context.find(word)
        
        word_len.append(len(word))    
        index_range.append(idx)

    index_range[-1]+word_len[-1]

    answer_span = [index_range[0], index_range[-1]+word_len[-1]]

    return answer_span


def write_answer(context, answer_span):
    st.write(f"{context[0: answer_span[0]]}"\
            f"**{context[answer_span[0]: answer_span[1]]}**"
            f"{context[answer_span[1]:]}")    