# newModel.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

@st.cache
def load_data():
    df = pd.read_csv('Datasets\interest_data.csv')
    return df

df = load_data()

course_mapping = {
    'Animation, Graphics and Multimedia': ['Drawing', 'Video Game', 'Designing'],
    'B.Arch- Bachelor of Architecture': ['Drawing', 'Architecture'],
    'B.Com- Bachelor of Commerce': ['Accounting', 'Economics', 'Business'],
    'B.Ed.': ['Teaching', 'Psychology'],
    'B.Sc- Applied Geology': ['Geography', 'Science'],
    'B.Sc- Nursing': ['Biology', 'Chemistry', 'Medical Sciences'],
    'B.Sc. Chemistry': ['Chemistry', 'Science'],
    'B.Sc. Mathematics': ['Mathematics', 'Science'],
    'B.Sc.- Information Technology': ['Coding', 'Computer Parts'],
    'B.Sc.- Physics': ['Physics', 'Science'],
    'B.Tech.-Civil Engineering': ['Architecture', 'Physics', 'Mathematics'],
    'B.Tech.-Computer Science and Engineering': ['Coding', 'Computer Parts'],
    'B.Tech.-Electrical and Electronics Engineering': ['Electricity Components', 'Physics'],
    'B.Tech.-Electronics and Communication Engineering': ['Electricity Components', 'Physics', 'Communication'],
    'B.Tech.-Mechanical Engineering': ['Mechanic Parts', 'Physics'],
    'BA in Economics': ['Economics', 'Mathematics'],
    'BA in English': ['Literature', 'Reading'],
    'BA in Hindi': ['Hindi', 'Literature', 'Reading'],
    'BA in History': ['History', 'Geography', 'Reading'],
    'BBA- Bachelor of Business Administration': ['Business', 'Management', 'Accounting'],
    'BBS- Bachelor of Business Studies': ['Business', 'Management', 'Accounting'],
    'BCA- Bachelor of Computer Applications': ['Coding', 'Computer Parts'],
    'BDS- Bachelor of Dental Surgery': ['Biology', 'Chemistry', 'Medical Sciences'],
    'BEM- Bachelor of Event Management': ['Travelling', 'Event Management'],
    'BFD- Bachelor of Fashion Designing': ['Designing', 'Crafting'],
    'BJMC- Bachelor of Journalism and Mass Communication': ['Journalism', 'Content writing'],
    'BPharma- Bachelor of Pharmacy': ['Chemistry', 'Biology'],
    'BTTM- Bachelor of Travel and Tourism Management': ['Travelling', 'Tourism'],
    'BVA- Bachelor of Visual Arts': ['Drawing', 'Designing', 'Crafting'],
    'CA- Chartered Accountancy': ['Accounting', 'Business'],
    'CS- Company Secretary': ['Accounting', 'Business'],
    'Civil Services': ['Geography', 'History', 'Political Science'],
    'Diploma in Dramatic Arts': ['Acting', 'Drama'],
    'Integrated Law Course- BA + LL.B': ['Law', 'Political Science', 'History'],
    'MBBS': ['Biology', 'Chemistry', 'Medical Sciences'],
    'Diploma in Fine Arts': ['Drawing', 'Designing', 'Crafting'],
    'Bachelor of Science in Environmental Science': ['Botany', 'Zoology', 'Geography'],
    'Bachelor of Science in Psychology': ['Psychology', 'Sociology'],
    'Bachelor of Science in Agriculture': ['Botany', 'Gardening', 'Zoology'],
    'Bachelor of Science in Forestry': ['Botany', 'Forestry'],
    'Bachelor of Science in Biotechnology': ['Biology', 'Chemistry', 'Researching'],
    'Bachelor of Arts in Linguistics': ['English', 'French', 'Hindi', 'Urdu', 'Literature'],
    'Bachelor of Science in Statistics': ['Mathematics', 'Researching'],
    'Bachelor of Science in Anthropology': ['Sociology', 'Psychology', 'History', 'Biology'],
    'Bachelor of Science in Geology': ['Geography', 'Physics', 'Chemistry'],
    'Bachelor of Science in Astronomy': ['Physics', 'Mathematics'],
    'Bachelor of Science in Marine Biology': ['Biology', 'Zoology'],
    'Bachelor of Science in Neuroscience': ['Biology', 'Psychology', 'Researching'],
    'Bachelor of Science in Biochemistry': ['Biology', 'Chemistry', 'Researching'],
    'Bachelor of Science in Environmental Engineering': ['Environmental Science', 'Engineering', 'Researching'],
    'Bachelor of Science in Wildlife Conservation': ['Zoology', 'Botany', 'Environmental Science'],
    'Bachelor of Arts in Music': ['Listening Music', 'Singing'],
    'Bachelor of Fine Arts in Theater Arts': ['Acting', 'Drama'],
    'Bachelor of Science in Nutrition and Dietetics': ['Cooking', 'Biology'],
    'Bachelor of Science in Sports Science': ['Sports', 'Exercise', 'Physiology'],
    'Bachelor of Science in Robotics': ['Coding', 'Electronics'],
    'Bachelor of Arts in Creative Writing': ['Content writing', 'Literature', 'Reading']
}

def get_top_interests(row):
    top_interests = row.sort_values(ascending=False)[:5]
    return top_interests.index.tolist()

def map_interests_to_courses(row):
    courses = []
    course_counter = Counter()

    for interest in row:
        for course, interests in course_mapping.items():
            if interest in interests and course_counter[course] < 5:
                courses.append(course)
                course_counter[course] += 1
                if len(courses) == 5:
                    break
        if len(courses) == 5:
            break

    return courses

def get_top_interests_with_user_input(df, user_input):
    num_interests = sum(1 for value in user_input.values() if value > 0.0)
    sorted_input = sorted(user_input.items(), key=lambda x: x[1], reverse=True)
    top_interests = [subject for subject, likeness in sorted_input[:num_interests]]
    return top_interests

def find_courses_with_common_interests(mapped_interests, course_mapping):
    common_courses = []
    for course, interests in course_mapping.items():
        if set(mapped_interests).intersection(interests):
            common_courses.append(course)
    return common_courses

def main():
    st.title("Course Recommendation System")
    st.header("Give Your Input:")

    user_input = {}
    for column in df.columns:
        if column != 'Top Interests':
            user_input[column] = st.slider(f"Likeness for {column}", 0.0, 1.0, 0.5)

    if st.button("Get Recommendations"):
        if all(value == 1.0 for value in user_input.values()):
            st.error("Error: Highest Interest in every subject is not possible to recommend course")
        elif all(value == 0.0 for value in user_input.values()):
            st.error("Error: No interest in any subject is not possible to recommend course")
        else:
            top_interests = get_top_interests_with_user_input(df, user_input)
            num_interests = min(len(user_input), 5)
            top_interests = top_interests[:num_interests]

            common_courses = find_courses_with_common_interests(top_interests, course_mapping)
            common_courses = common_courses[:len(top_interests)]
            
            st.write("**Top Interests:**")
            for interest in top_interests:
                st.markdown(f"- {interest}")
            
            st.write("**Courses with Common Interests:**")
            for course in common_courses:
                st.markdown(f"- {course}")

    st.header("Distribution of Interests")
    fig, ax = plt.subplots(figsize=(10, 6))
    df_top_interests = pd.Series(user_input).sort_values(ascending=False)[:5]
    sns.barplot(x=df_top_interests.index, y=df_top_interests.values, ax=ax)
    plt.xlabel("Interest")
    plt.ylabel("Likeness")
    plt.title("Top Interests and Likeness")
    plt.xticks(rotation=45)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
