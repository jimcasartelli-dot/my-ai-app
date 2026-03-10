import streamlit as st
from openai import OpenAI

# Setup the App Title
st.title("🚀 Your Personal Hype Man")
st.subheader("Tell me what you did today, and I'll celebrate you!")

# Get the User Input
user_goal = st.text_input("What did you accomplish?", "I finally organized my garage.")

# The "Brain" of the app
if st.button("Hype Me Up!"):
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an incredibly enthusiastic hype man. Use emojis and all caps."},
            {"role": "user", "content": f"Celebrate this accomplishment: {user_goal}"}
        ]
    )
    
    st.balloons() # This adds a fun animation!
    st.success(response.choices[0].message.content)
