# App for Question Answering & Question Generation

### Welcome 🏆
With this streamlit app you are able to play around with state-of-the-art NLP models in an easy user friendly environment. There are two main task, namely; Question Answering and Question Generation. 

# Getting started 
It's super easy, we promise!

## Preprare Envirorment
To install necesarry dependencies simple run
```
pip install -r requirements.txt
```

This will intall the packages: 
- streamlit 
- gitpython
- nltk
- allennlp (1.0.0)
- allennlp_models (1.0.0)
- transformers (3.0.0)

Next clone you will need to clone the ```question_generation``` git repository. This can either be done in terminal or simple by running the app, as ```functions.py``` will do this for you.

```
git clone https://github.com/patil-suraj/question_generation.git
```

All credits to patil-suraj for making a awesome end-to QG framework that mimics 🤗 transformers pipeline for easy inference (https://github.com/patil-suraj/question_generation). 


**Note AllenNLP is currently only supported on Mac and Linux environment. To run this on Windows you will have to comment/remove the AllenNLP related stuff (```functions.py``` and ```requirements.txt```) and install PyTorch yourself.**

# ##############################################################################

## Running streamlit 

Once streamlit and the other dependicies are installed you can simple run the app:
```
streamlit run app.py
```

The app will now run in a localhost server.

Note, in ```functions.py``` Also a clone of hte clone the git repository `question_generation` will be downloaded. 

# ##############################################################################

# COLAB notebooks

## Question Answering and Question Generation
The final streamlit is essentially a combination of two seperate COLAB prototypes solving Question Answering and Question Generation respectively. They have been merged into one streamlit app with user interface. The seperate notesbook can be found as well. 

## Steamlit app
To play around with all of models can be both demanding in storage (~6gb) and can be computationally. To cope with this a COLAB notebook has been developed, which enables you to run the streamlit app through COLAB. Models are now stored and computationen made on using Google service. 

Note you will need to modify the script a little bit by adding your own ngrok to generate the localhost server.

# ##############################################################################

# Models
The app is essential a *wrapper* for a number of models glued together with a friendly user interface. None of the models are fine-tuned and are simple implemented using a user friendly API *pipeline* format.

## Question Answering
For the Question Answering module four pre-trained models have been implemented:
1. ELMo-BiDAF (Trained on SQuAD) 
2. BiDAG (Trained on SQuAD)
3. DistilBERT (distilbert-base-cased-distilled-squad)
4. BERT (bert-large-uncased-whole-word-masking-finetuned-squad)
5. Finetuned BERT multilingual base model [cased] (mrm8488/bert-multi-cased-finetuned-xquadv1)

Where 1) and 2) are AllenNLP models and 3), 4), and 5) are HuggingFace models. 

## Question Generation
The Question Generation is a pre-trained model with three pipeline tasks:
1. question-generation: for single task question generation models
2. multitask-qa-qg: for multi-task qa,qg models
3. e2e-qg: for end-to-end question generation

With the option of using a model sizes "small" or a "base" (https://huggingface.co/models). All models are easily implemented but for this demo ***only the end-to-end question generation is included in this demo (both the small and base model)***. For fine-tuning the models please look at the patil-suraj's git repository. 

