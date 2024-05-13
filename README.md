---

# Resume Matching App 📄🔍

The Resume Matching App is a simple web application built with Streamlit that allows users to match a job description with a collection of resumes to identify the most suitable candidates for a job opening.

[Dataset That I Have Use](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)

[App](https://fuubh7ljw7rawdhds7fmyv.streamlit.app/)

## Objective

The objective of this app is to streamline the process of screening resumes by automating the matching process. Traditional methods of resume screening can be time-consuming and subjective. By leveraging natural language processing (NLP) techniques, this app aims to provide a more efficient and objective way to match job descriptions with candidate resumes.

## How to Use

1. **Upload Resumes**: Click on the "Upload resume data (CSV)" button and select a CSV file containing resume data. The CSV file should contain two columns: "ID" and "Resume_str", where "ID" is a unique identifier for each resume and "Resume_str" contains the text of the resumes.

2. **Enter Job Description**: Enter the job description in the text area provided.

3. **Match Resumes**: Click on the "Match Resumes" button to initiate the matching process.

4. **View Results**: The top 10 matches will be displayed, showing the resume ID, resume text, and similarity score.

## Features

- Simple and intuitive user interface
- Automatic matching of job descriptions with resumes using cosine similarity
- Ability to upload custom resume datasets
- Real-time matching results displayed in a table format

## Technologies Used

- Python
- Streamlit
- pandas
- nltk
- scikit-learn

## Installation

To run the app locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the app with `streamlit run app.py`.

## Deployment

The app can be deployed using Streamlit Cloud or any other hosting platform that supports Streamlit apps. Simply upload the code and required files to the hosting platform, and the app will be accessible via a web browser.

---
