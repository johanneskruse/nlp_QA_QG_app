# Question Answering & Question Generation prototype

# Getting started
It's super easy, we promise!

## Preprare Envirorment
To install necesarry dependencies run the setup file
```
python setup.py install
```

The setup file will install the packages: 
- streamlit 
- gitpython
- nltk (python -m nltk.downloader punkt)
- allennlp (1.0.0)
- allennlp_models
- transformers (3.0.0)

Also a clone of hte clone the git repository `question_generation` will be downloaded. 

All credits to patil-suraj for making a awesome end-to QG framework that mimics 🤗 transformers pipeline for easy inference (https://github.com/patil-suraj/question_generation). 

# ##############################################################################

## Running streamlit 

Once streamlit and the other dependicies are installed you can simple run the app:
```
streamlit run app.py
```

The app will run in a localhost server.

# ##############################################################################

# Models
The app is essential a *wrapper* for a number of models glued together with a friendly user interface. None of the models are fine-tuned and are simple implemented using a user friendly API *pipeline* format.

## Question Answering
For the Question Answering module four pre-trained models have been implemented:
1. ELMo-BiDAF (Trained on SQuAD) 
2. BiDAG (Trained on SQuAD)
3. DistilBERT (distilbert-base-cased-distilled-squad)
4. BERT (bert-large-uncased-whole-word-masking-finetuned-squad)

Where 1) and 2) are AllenNLP models and 3) and 4) are HuggingFace models. 

## Question Generation
The Question Generation is a pre-trained model with three pipeline tasks:
1. question-generation: for single task question generation models
2. multitask-qa-qg: for multi-task qa,qg models
3. e2e-qg: for end-to-end question generation

With the option of using a model sizes "small" or a "base" (https://huggingface.co/models). All models are easily implemented but for this demo ***only the end-to-end question generation is included in this demo (both the small and base model)***. For fine-tuning the models please look at the patil-suraj's git repository. 

# ##############################################################################

# COLAB Notebook
To play around with all of models can be both demanding in storage (~6gb) and can be computationally. To cope with this a COLAB notebook has been developed, which enables you to run the streamlit app through COLAB. Models are now stored and computationen made on using Google service. 
- https://colab.research.google.com/drive/1zjWn1OEvL_OJxQufjCnrtIIq25qT9DMz?usp=sharing

Note you will need to modify the script a little bit by adding your own ngrok to generate the localhost server.