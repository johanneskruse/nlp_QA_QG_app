# App for Question Answering & Question Generation

**Repository for Windows setup.** 

For Windows it is **not** possible to cache the models due some unsolved issues with the *st.cache*. This means that models are constantly having to re-run slowing down the process and the user experience. If possible it is recommended run this app using Mac or Linux system. 

### Welcome 🏆
This is a repository for a Streamlit App that enables you to play around with state-of-the-art NLP models in an easy user friendly environment. There are two main task, namely; Question Answering and Question Generation. 

# Getting started 
It's super easy, we promise!

## Preprare Envirorment
To install necesarry dependencies simple run
```
pip install -r requirements.txt
```
and then
```
conda install pytorch torchvision cpuonly -c pytorch
```

This will intall the packages: 
- streamlit 
- gitpython
- nltk
- transformers (3.0.0)
- langdetect
- pytorch

The ```question_generation``` is a git repository that has been added used for Question Generation. The ```functions.py``` script will check that it exists and if not download it. 

All credits to patil-suraj for making an awesome end-to QG framework that mimics 🤗 transformers pipeline for easy inference (https://github.com/patil-suraj/question_generation). 

Cloning the ```question_generation``` yourself: 
```
git clone https://github.com/patil-suraj/question_generation.git
```

# ##############################################################################

## Running streamlit 

Once streamlit and the other dependicies are installed you can simple run the app:
```
streamlit run app.py
```
The app will now run in a localhost server.

# ##############################################################################

# COLAB notebooks

## Question Answering and Question Generation
The final streamlit is essentially a combination of two seperate COLAB prototypes solving Question Answering and Question Generation respectively. They have been merged into one streamlit app with user interface. The seperate notesbook can be found as well. 

## Steamlit app
To play around with all of models require some storage (~4-5gb) and computation power. To cope with this a COLAB notebook has been developed, which enables you to run the streamlit app through COLAB.

Note you will need to make a small modification, as you need to add your own ngrok to generate the localhost server (follow COLAB instructions).

Running the COLAB will give you access to all models used for the Linux and Mac setup.

# ##############################################################################

# Models
The app is essential a *wrapper* for a number of models that have been put together with a friendly user interface. All models are pre-trained and have not been fine-tuned further and are simple implemented using a user friendly API *pipeline* format.

## Question Answering
For the Question Answering module four pre-trained models have been implemented:
1. DistilBERT (distilbert-base-cased-distilled-squad)
2. BERT (bert-large-uncased-whole-word-masking-finetuned-squad)
3. Finetuned BERT multilingual base model [cased] (mrm8488/bert-multi-cased-finetuned-xquadv1)


## Question Generation
The Question Generation is a pre-trained model with three pipeline tasks:
1. question-generation: for single task question generation models
2. multitask-qa-qg: for multi-task qa,qg models
3. e2e-qg: for end-to-end question generation

With the option of using a model sizes "small" or a "base" (https://huggingface.co/models). All models are easily implemented but ***only the end-to-end question generation is included in this demo (both the small and base model)***. 

# Store and Run models from local machine
It is possible to store the models on your local machine, to do so run
```
python run_locally/download_model_local.py 
```
This will allow you to download the models one-by-one. The models are stored in ```models```. To run the models using the locally stored models replace ```screens.py``` and ```functions.py``` with the repective file from ```run_locally```. Note this will be without the AllenNLP models.
