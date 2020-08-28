from question_generation.pipelines import pipeline
import streamlit as st


# from allennlp.predictors.predictor import Predictor
# import allennlp_models.rc

# import torch
# import transformers

# from transformers import BertForQuestionAnswering
# from transformers import BertTokenizer

# import pandas as pd

# from transformers import pipeline

#===============================================================================
class Config:
    models_qg = {
        "1" : "Question generation (without answer supervision) [small]",
        "2" : "Question generation (without answer supervision) [base]",
    }
    
    models_qa = {
        "1" : "ELMo-BiDAF (Trained on SQuAD)", # allennlp
        "2" : "BiDAG (Trained on SQuAD)", # allennlp
        "3" : "Transformer QA (Trained on SQuAD)", # allennlp
        "4" : "distilbert-base-cased-distilled-squad", # huggingface
        "5" : "bert-large-uncased-whole-word-masking-finetuned-squad" # huggingface
        }

    input_messege = "Please enter your text (write 'quit' to exit," \
                    "'new' for model selection, or" \
                    "'demo' for predefined sample text):\n" \
                    "Text input: "
    
    demo_text = "Infosys Limited, is an Indian multinational corporation" \
                "that provides business consulting, information technology" \
                "and outsourcing services. The company is headquartered in" \
                "Bangalore, Karnataka, India. Infosys is the second-largest" \
                "Indian IT company after Tata Consultancy Services by 2017 revenue" \
                "figures and the 596th largest public company in the world based" \
                "on revenue. On 29 March 2019, its market capitalisation was $46.52 billion."



## Load model
@st.cache
def modelsConfig(model):
    
    ## Question Generation: 
    if model == "Question generation (without answer supervision) [small]":
        model_selected = pipeline("e2e-qg", model="valhalla/t5-small-e2e-qg")
        model_library = "qg_model"
    elif model == "Question generation (without answer supervision) [base]":
        model_selected = pipeline("e2e-qg", model="valhalla/t5-base-e2e-qg")
        model_library = "qg_model"

    # ## Question Answering: 
    # if model == "ELMo-BiDAF (Trained on SQuAD)":
    #     model_selected = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/bidaf-elmo-model-2020.03.19.tar.gz")
    #     model_library = "allennlp"
    # elif model == "BiDAG (Trained on SQuAD)":
    #     model_selected = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/bidaf-model-2020.03.19.tar.gz")
    #     model_library = "allennlp"
    # elif model == "Transformer QA (Trained on SQuAD)":
    #     model_selected = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/transformer-qa-2020-05-26.tar.gz")
    #     model_library = "allennlp"
    # elif model == "distilbert-base-cased-distilled-squad":
    #     model_selected = pipeline("question-answering", model=f"{model}")
    #     model_library = "huggingface_pipline"
    # elif model == "bert-large-uncased-whole-word-masking-finetuned-squad":
    #     model_selected = pipeline("question-answering", model=f"{model}")
    #     model_library = "huggingface_pipline"

    
    else:
        raise Exception("Not a valid model")    
    return model_selected, model_library
