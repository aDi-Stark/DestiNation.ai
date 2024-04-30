import streamlit as st

# Define questions for the Holland Personality Test (RIASEC model)
holland_questions = {
    "R": [
        "I enjoy working with machines and tools.",
        "I like to work with numbers and solve mathematical problems.",
        "I prefer practical tasks over abstract ones."
    ],
    "I": [
        "I enjoy solving puzzles and brain teasers.",
        "I like conducting experiments and exploring new ideas.",
        "I enjoy analyzing data to find patterns and trends."
    ],
    "A": [
        "I enjoy drawing, painting, or creating visual art.",
        "I like expressing myself through music or dance.",
        "I like writing poetry or stories."
    ],
    "S": [
        "I enjoy helping people solve their problems.",
        "I like volunteering and contributing to my community.",
        "I enjoy teaching and educating others."
    ],
    "E": [
        "I enjoy taking on leadership roles and responsibilities.",
        "I like persuading and convincing others.",
        "I like organizing events and gatherings."
    ],
    "C": [
        "I prefer working with numbers and data.",
        "I like creating and following organized systems.",
        "I enjoy record-keeping and data analysis."
    ]
}

# Define information and career recommendations for each Holland Personality Type
personality_info = {
    "R": {
        "name": "Realistic",
        "description": "Realistic individuals are practical, hands-on, and enjoy working with tools and machines.",
        "careers": [
            "Carpenter",
            "Electrician",
            "Mechanic",
            "Plumber",
            "Welder"
        ]
    },
    "I": {
        "name": "Investigative",
        "description": "Investigative individuals are analytical and enjoy solving complex problems.",
        "careers": [
            "Scientist",
            "Engineer",
            "Researcher",
            "Computer Programmer",
            "Mathematician"
        ]
    },
    "A": {
        "name": "Artistic",
        "description": "Artistic individuals are creative and enjoy expressing themselves through art and design.",
        "careers": [
            "Artist",
            "Graphic Designer",
            "Writer",
            "Interior Designer",
            "Photographer"
        ]
    },
    "S": {
        "name": "Social",
        "description": "Social individuals are compassionate and enjoy helping and caring for others.",
        "careers": [
            "Teacher",
            "Social Worker",
            "Nurse",
            "Counselor",
            "Psychologist"
        ]
    },
    "E": {
        "name": "Enterprising",
        "description": "Enterprising individuals are ambitious and enjoy leadership roles and entrepreneurship.",
        "careers": [
            "Entrepreneur",
            "Sales Manager",
            "Marketing Manager",
            "Business Consultant",
            "Politician"
        ]
    },
    "C": {
        "name": "Conventional",
        "description": "Conventional individuals are detail-oriented and enjoy organizing and managing tasks and data.",
        "careers": [
            "Accountant",
            "Financial Analyst",
            "Data Analyst",
            "Office Manager",
            "Banker"
        ]
    }
}

# Main function
def main():
    st.title("DestiNation - Personality/Psychometry Test")
    selected_choices = {}  # Store selected answers for each question

    # Create windows for each personality type
    for personality_type, questions in holland_questions.items():
        #st.subheader(f"Holland Personality Test - {personality_info[personality_type]['name']} Type")
        for i, question in enumerate(questions):
            st.write(question)
            key = f"{personality_type}_{i}"  # Ensure unique key for each question
            selected_choices[key] = st.radio("Select your choice:", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key=key)

    # Submit button
    if st.button("Submit Test"):
        submit_test(selected_choices)

def submit_test(selected_choices):
    # Calculate the Holland Codes based on the user's answers
    codes = {personality_type: 0 for personality_type in holland_questions.keys()}
    for question_key, selected_choice in selected_choices.items():
        personality_type, _ = question_key.split('_')
        # Convert the selected choice to the corresponding index (0 for 'Strongly Disagree', 1 for 'Disagree', etc.)
        selected_index = convert_choice_to_index(selected_choice)
        codes[personality_type] += selected_index

    # Show the result
    dominant_personality = max(codes, key=codes.get)
    st.success(f"Your Holland Personality Type is: {personality_info[dominant_personality]['name']}")
    st.write(f"Description: {personality_info[dominant_personality]['description']}")
    st.write("Recommended Careers:")
    st.write(", ".join(personality_info[dominant_personality]['careers']))

def convert_choice_to_index(choice):
    choices = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
    return choices.index(choice)

if __name__ == "__main__":
    main()
