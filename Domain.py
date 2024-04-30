import streamlit as st
import pandas as pd

# Function to load data
@st.cache_data
def load_data():
    return pd.read_csv('Datasets\mcq_questions.csv')

# Main function for Streamlit app
def main():
    st.title('Subject Wise Aptitude Tests')

    # Reload data button
    if st.button('Reload Data'):
        st.cache_data.clear()  # Clear the cache
        st.experimental_rerun()  # Rerun the app to reflect changes

    # Load MCQ data
    questions_df = load_data()

    # Domain and subject selection
    domain = st.selectbox('Select Domain', options=questions_df['Domain'].unique())
    subjects = questions_df[questions_df['Domain'] == domain]['Subject'].unique()
    subject = st.selectbox('Select Subject', options=subjects)

    # Generate test
    if st.button('Generate Test'):
        test_questions = questions_df[(questions_df['Domain'] == domain) & (questions_df['Subject'] == subject)]
        st.session_state.test_questions = test_questions
        st.session_state.submitted_answers = [None] * len(test_questions)

    # Display questions and options, collect answers
    if 'test_questions' in st.session_state:
        test_questions = st.session_state.test_questions.reset_index(drop=True)
        for i, row in test_questions.iterrows():
            q = f"Q{i+1}: {row['Question']}"
            options = [row['OptionA'], row['OptionB'], row['OptionC'], row['OptionD']]
            st.session_state.submitted_answers[i] = st.radio(q, options, key=f"question_{i}")

    # Submit answers

    if st.button('Submit Answers'):
        correct_answers = test_questions['CorrectOption'].tolist()
        submitted_answers = st.session_state.submitted_answers
        #st.write(f'Submitted Answers: {submitted_answers}')
        #st.write(f'Correct Answers: {correct_answers}')
        
        # Convert correct answers to option value for comparison
        correct_option_values = test_questions.apply(lambda row: row[f'Option{row["CorrectOption"]}'], axis=1)
        
        # Debugging: Print converted correct option values
        #st.write(f'Correct Option Values: {correct_option_values}')
        
        # Calculate score
        score = sum([1 if submitted_answers[i] == correct_option_values[i] else 0 for i in range(len(correct_answers))])
        st.write(f'Your score is {score} out of {len(correct_answers)}.')


if __name__ == '__main__':
    main()
