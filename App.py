import streamlit as st
import pandas as pd
import spacy

# Load the spaCy model with word vectors
nlp = spacy.load("en_core_web_md")

# Function to calculate cosine similarity between job description and resumes
def calculate_similarity(job_description, df):
    # Process job description with spaCy
    job_doc = nlp(job_description)

    similarity_list = []

    # Ensure the DataFrame has 'ID' and 'Resume_str' columns
    if 'ID' in df.columns and 'Resume_str' in df.columns:
        for index, row in df.iterrows():
            resume_id = row['ID']
            resume_text = row['Resume_str']
            resume_doc = nlp(resume_text)

            # Calculate cosine similarity between job description and resume
            similarity_score = job_doc.similarity(resume_doc)

            similarity_list.append({
                'resume_id': resume_id,
                'resume_text': resume_text,
                'similarity_score': similarity_score
            })

        # Construct a DataFrame from the similarity_list
        similarity_df = pd.DataFrame(similarity_list)

        # Sort the DataFrame by the 'similarity_score' column in descending order
        similarity_df.sort_values(by='similarity_score', ascending=False, inplace=True)

        return similarity_df
    else:
        return pd.DataFrame(columns=['resume_id', 'resume_text', 'similarity_score'])

# Streamlit app
def main():
    st.title("Resume Matching App")

    # Upload resume data
    uploaded_file = st.file_uploader("Upload resume data (CSV)", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Display the DataFrame
        st.write(df.head())

        # Get user input for job description
        job_description = st.text_area("Enter job description")

        if st.button("Match Resumes"):
            similarity_df = calculate_similarity(job_description, df)

            # # Display top 10 matches
            # st.subheader("Top 10 Matches")
            if not similarity_df.empty:
                st.subheader("Top 10 Matches")
                top_10_matches = similarity_df.head(10)
                st.write(top_10_matches)
            else:
                st.write("Please ensure the CSV file contains 'ID' and 'Resume_str' columns.")

if __name__ == "__main__":
    main()