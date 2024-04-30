import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the pre-trained model
model = joblib.load('model .pkl')

# Define the mapping from numeric values to categories
numeric_to_category = {
    0: 'Animation, Graphics and Multimedia',
    1: 'B.Arch- Bachelor of Architecture',
    2: 'B.Com- Bachelor of Commerce',
    3: 'B.Ed.',
    4: 'B.Sc- Applied Geology',
    5: 'B.Sc- Nursing',
    6: 'B.Sc. Chemistry',
    7: 'B.Sc. Mathematics',
    8: 'B.Sc.- Information Technology',
    9: 'B.Sc.- Physics',
    10: 'B.Tech.-Civil Engineering',
    11: 'B.Tech.-Computer Science and Engineering',
    12: 'B.Tech.-Electrical and Electronics Engineering',
    13: 'B.Tech.-Electronics and Communication Engineering',
    14: 'B.Tech.-Mechanical Engineering',
    15: 'BA in Economics',
    16: 'BA in English',
    17: 'BA in Hindi',
    18: 'BA in History',
    19: 'BBA- Bachelor of Business Administration',
    20: 'BBS- Bachelor of Business Studies',
    21: 'BCA- Bachelor of Computer Applications',
    22: 'BDS- Bachelor of Dental Surgery',
    23: 'BEM- Bachelor of Event Management',
    24: 'BFD- Bachelor of Fashion Designing',
    25: 'BJMC- Bachelor of Journalism and Mass Communication',
    26: 'BPharma- Bachelor of Pharmacy',
    27: 'BTTM- Bachelor of Travel and Tourism Management',
    28: 'BVA- Bachelor of Visual Arts',
    29: 'CA- Chartered Accountancy',
    30: 'CS- Company Secretary',
    31: 'Civil Services',
    32: 'Diploma in Dramatic Arts',
    33: 'Integrated Law Course- BA + LL.B',
    34: 'MBBS'
    # Add the rest of the categories here...
}

# Function to make predictions
def predict_course(user_input):
    # Make a prediction using the model
    prediction = model.predict(user_input)

    # Convert the numeric prediction to a categorical label
    categorical_prediction = numeric_to_category.get(prediction[0], "Unknown")

    return categorical_prediction

def main():
    st.title("DestiNation - Interest Inventory Test")

    # Collect user input
    st.subheader("Select Interests")
    user_input = {}
    feature_names = ['Drawing','Dancing','Singing','Sports','Video Game','Acting','Travelling','Gardening','Animals','Photography','Teaching','Exercise','Coding','Electricity Components','Mechanic Parts','Computer Parts','Researching','Architecture','Historic Collection','Botany','Zoology','Physics','Accounting','Economics','Sociology','Geography','Psycology','History','Science','Bussiness Education','Chemistry','Mathematics','Biology','Makeup','Designing','Content writing','Crafting','Literature','Reading','Cartooning','Debating','Asrtology','Hindi','French','English','Urdu','Other Language','Solving Puzzles','Gymnastics','Yoga','Engeeniering','Doctor','Pharmisist','Cycling','Knitting','Director','Journalism','Bussiness','Listening Music']
    for feature in feature_names:
        user_value = st.slider(f"Select value for {feature}", 0, 1, 0)
        user_input[feature] = user_value

    # Create a DataFrame from user input
    user_data = pd.DataFrame([user_input])

    # Display submit button
    if st.button("Submit"):
        # Make a prediction
        prediction = predict_course(user_data)

        # Display prediction
        st.subheader("Recommended Course")
        st.write(prediction)

if __name__ == "__main__":
    main()
