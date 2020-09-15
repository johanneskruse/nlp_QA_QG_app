from question_generation.pipelines import pipeline as qg_pipeline
from transformers import pipeline as qa_pipeline
from transformers import AutoTokenizer, AutoModelWithLMHead

import os


model_name_qa = 'distilbert-base-cased-distilled-squad'
qa_pipeline('question-answering', model=f'./models/{model_name_qa}/', tokenizer=f'./models/{model_name_qa}/')


model_name_qg = 'Question generation (without answer supervision) [small]'
qg_pipeline("e2e-qg", model=f'./models/{model_name_qg}/', tokenizer=f'./models/{model_name_qg}/')