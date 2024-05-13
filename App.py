import streamlit as st
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

def calculate_similarity(job_description, df):
    # Tokenize job description
    job_tokens = nltk.word_tokenize(job_description.lower())

    # Convert resumes to lowercase
    df['Resume_str'] = df['Resume_str'].str.lower()

    # Initialize TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')

    # Fit and transform resumes
    resume_vectors = vectorizer.fit_transform(df['Resume_str'])

    # Transform job description
    job_vector = vectorizer.transform([job_description])

    # Calculate cosine similarity between job description and resumes
    similarity_scores = cosine_similarity(job_vector, resume_vectors)

    # Add similarity scores to DataFrame
    df['Similarity'] = similarity_scores.flatten()

    # Sort DataFrame by similarity scores
    df.sort_values(by='Similarity', ascending=False, inplace=True)

    return df[['ID', 'Resume_str', 'Similarity']].head(10)

# Streamlit app
def main():
    st.title("📄 Resume Matching App 🎯")

    uploaded_file = st.file_uploader("Upload resume data (CSV)", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())

        job_description = st.text_area("Enter job description 📝")

        if st.button("Match Resumes 🔍"):
            top_matches = calculate_similarity(job_description, df)
            if not top_matches.empty:
                st.subheader("Top 10 Matches 🚀")
                st.write(top_matches)
            else:
                st.write("Please ensure the CSV file contains 'ID' and 'Resume_str' columns.")

if __name__ == "__main__":
    main()
