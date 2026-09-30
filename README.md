# ATS Resume Analyzer

An NLP-based tool that evaluates how well a resume matches a job description — giving candidates actionable feedback before they apply.

## What it does
- Scores resume-JD compatibility using **keyword matching** and **cosine similarity**
- Identifies missing keywords and categorizes them into **Programming Languages, Tools & Platforms, ML/Data Science, and Soft Skills**
- Deployed as an interactive web app using **Streamlit**

## Tech Stack
Python · NLTK · scikit-learn · Streamlit · PyPDF2

## How it works
1. Upload your resume (PDF) and paste a job description
2. The NLP pipeline tokenizes, removes stopwords, and stems both texts using Porter Stemmer
3. Keyword match score is calculated using set intersection
4. Semantic similarity score is calculated using CountVectorizer + cosine similarity
5. Skills Gap Analysis categorizes missing keywords into actionable buckets

## How to run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Built by
Vansh Dhankar | B.Tech IT, MAIT GGSIPU
