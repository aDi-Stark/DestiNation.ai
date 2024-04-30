import streamlit as st

def main():
    st.title("Welcome to DestiNation: Your AI-Powered Career Counselling Platform")
    st.markdown(
        "DestiNation is an AI-powered career counselling project designed to bridge the gap between secondary education and informed career choices. "
        "This innovative platform empowers students with the knowledge and guidance they need to navigate the complex world of career exploration. "
        "DestiNation leverages a powerful combination of cutting-edge technologies to deliver a comprehensive user experience."
    )

    st.image("workflow.png" )

    st.markdown("## Features")
    st.markdown(
        "- Gamified aptitude tests\n"
        "- Comprehensive resource library\n"
        "- Access to mentorship opportunities (premium feature)\n"
        "- Mobile applications for Android and iOS\n"
    )

    st.markdown("## Mission")
    st.markdown(
        "DestiNation goes beyond traditional career counselling by democratizing access to career counselling and fostering a culture of lifelong learning. "
        "We aim to equip students with the skills and knowledge necessary to build fulfilling and successful careers."
    )

    
    


if __name__ == "__main__":
    main()
