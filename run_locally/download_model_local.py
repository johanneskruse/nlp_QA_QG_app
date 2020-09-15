# Download models of interst

from transformers import pipeline as qa_pipline
import os 
from transformers import AutoTokenizer, AutoModelWithLMHead

#wd = input('Working path input: ')
#os.chdir(f'{wd}')

if not os.path.exists(f'{os.getcwd()}/models'):
    os.mkdir('./models')

print(f'Your wokring path is: {os.getcwd()}')

#===============================================================================
class models:
    models_qg = {
        "Question generation (without answer supervision) [small]" : "qg",
        "Question generation (without answer supervision) [base]" : "qg",
    }
    
    models_qa = {
        #"ELMo-BiDAF (Trained on SQuAD)" : "allennlp",
        #"BiDAG (Trained on SQuAD)" : "allennlp",
        # "Transformer QA (Trained on SQuAD)" : "allennlp", # not working [hack]
        "distilbert-base-cased-distilled-squad" : "huggingface_pipline", 
        "bert-base-uncased"  : "huggingface_pipline",
        "bert-large-uncased-whole-word-masking-finetuned-squad"  : "huggingface_pipline",
        "mrm8488/bert-multi-cased-finetuned-xquadv1"  : "huggingface_pipline" 
        }

    model_type = ['Quesion Answering', 'Question Generation']


def modelsConfig_qa(model):
    ## Question Answering: 
    if model == "distilbert-base-cased-distilled-squad":
        model_selected = qa_pipline("question-answering", model=f"{model}")
    elif model == "bert-large-uncased-whole-word-masking-finetuned-squad":
        model_selected = qa_pipline("question-answering", model=f"{model}")
    elif model == "bert-base-uncased":
        model_selected = qa_pipline("question-answering", model=f"{model}")
    else:
        raise Exception("Not a valid model")    
    return model_selected


def modelsConfig_qg(model):
    ## Question Generation: 
    if model == "Question generation (without answer supervision) [small]":
        model_name = "valhalla/t5-small-e2e-qg"
    
    elif model == "Question generation (without answer supervision) [base]":
        model_name = "valhalla/t5-base-e2e-qg"  
    
    else:
        raise Exception("Not a valid model")   
    return model_name

#===============================================================================

for i, model_type in enumerate(models.model_type):
    print(f'[{i+1}] {model_type}')

model_type_input = input('Select model type:' )

task = models.model_type[int(model_type_input)-1]

if task == 'Quesion Answering':
    for i, model in enumerate(models.models_qa):
        print(f'[{i+1}] {model}')
    model_download = input('Download model:' )

    model = list(models.models_qa)[int(model_download)-1]

    if model == 'mrm8488/bert-multi-cased-finetuned-xquadv1':
        os.mkdir(f'{os.getcwd()}/models/bert-multi-cased-finetuned-xquadv1')
        model_n = 'bert-multi-cased-finetuned-xquadv1'
        qa_pipline("question-answering", model=model).save_pretrained(save_directory=f'{os.getcwd()}/models/{model_n}')
    else:
        os.mkdir(f'{os.getcwd()}/models/{model}')
        qa_pipline("question-answering", model=model).save_pretrained(save_directory=f'{os.getcwd()}/models/{model}')

elif task == 'Question Generation':
    for i, model in enumerate(models.models_qg):
        print(f'[{i+1}] {model}')
    model_download = input('Download model:' )

    model = list(models.models_qg)[int(model_download)-1]
    
    if not os.path.exists(f'{os.getcwd()}/models/{model}'):
        os.mkdir(f'{os.getcwd()}/models/{model}')
    
    model_qg_name = modelsConfig_qg(model)

    AutoTokenizer.from_pretrained(model_qg_name).save_pretrained(save_directory=f'{os.getcwd()}/models/{model}')
    AutoModelWithLMHead.from_pretrained(model_qg_name).save_pretrained(save_directory=f'{os.getcwd()}/models/{model}')


print(f'Download complete')


