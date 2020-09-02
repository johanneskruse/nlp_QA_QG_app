
from setuptools import setup, find_packages

setup(
    name="qa_qg_streamlit",
    version="1.0.0",
    author="Johannes Kruse",
    description="Question Answering Question Generation streamlit app",
    url="https://github.com/JKrse/nlp_streamlit_QG_QA",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "pandas",
        # Stramlit app
        "streamlit",
        # Download git repository
        "gitpython",
        # Preposseing
        "nltk",
        # for allennlp models
        "allennlp == 1.0.0",
        # for allennlp models
        "allennlp_models",
        # for Transformers
        "transformers==3.0.0",
    ],
    python_requires=">=3.6.0"
)




