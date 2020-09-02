# Question Answering & Question Generation prototype


# Getting started
It's super easy, we promise!

## Preprare Envirorment
To install necesarry dependencies run the setup file
```
python setup.py
```

The necesarry dependencies
It will install the following: 
- streamlit 
- gitpython
- nltk (python -m nltk.downloader punkt)
- allennlp (1.0.0)
- allennlp_models
- transformers (3.0.0)

Also, the Question Generation is an end-to-end QG framework that mimics 🤗 transformers pipeline for easy inference. All credits to patil-suraj for creating this awesome framework (https://github.com/patil-suraj/question_generation). In the 

## Running streamlit 

Once streamlit is installed simple run the app:
```
streamlit run app.py
```

You can now open the local hosted server and try out the demos! 

# Prototypes


The final streamlit is essentially a combination of two seperate COLAB prototypes solving Question Answering and Question Generation respectively. These are now put together in a nice streamlit app with user interface.



# COLAB
If you are to try all model implemented in the prototype it is both demanding in storage (~6gb) and can be computationally demanding. To cope with this a COLAB notebook has been developed, which enables you to run the streamlit app through COLAB. 

https://colab.research.google.com/drive/1zjWn1OEvL_OJxQufjCnrtIIq25qT9DMz?usp=sharing