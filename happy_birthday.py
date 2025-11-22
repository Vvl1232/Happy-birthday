import streamlit as st
from datetime import datetime

# Predefined name, birth year, and birthday date
name = ''
birthday = datetime.strptime('13/11/2005', '%d/%m/%Y')

# Calculate age based on the predefined birth year and birthday date
today = datetime.today()
age = today.year - birthday.year - ((today.month, today.day) <= (birthday.month, birthday.day)) + 1

# Show a birthday message
st.markdown(
    f"<div class='block'><h3 style='text-align: center; color: red;'>🎂🌹🦚✨ Happy Birthday, {name}! 🦚✨🌹🎂</h3></div>",
    unsafe_allow_html=True
)

st.markdown("")
st.markdown("")
st.markdown("")

# st.markdown(
#     f"<div class='block'><h5 style='text-align: center; color:#FF1493 ;'>🥳 {age} years young today! 🥳</h5></div>",
#     unsafe_allow_html=True
# )

st.markdown("")
st.markdown("")

st.balloons()
st.snow()

# Add an image for extra energy (replace with a valid image URL)
st.markdown(
    f"""
    <div class='block'>
        <img src="https://st2.depositphotos.com/3102403/11122/i/950/depositphotos_111225728-stock-photo-happy-birthday-lettering-over-abstract.jpg" 
             alt="Happy Birthday Image" 
             style="width: 200px; margin: 0 auto; display: block;">
             
        <p style='text-align: center; font-size: 1.2em; color: #FF1493;'> 
            🌟 May your birthday be as extraordinary and wonderful as you are! 🎉🌟 
        </p>
        
        <p style='text-align: center; font-size: 1.2em; color: #FF69B4;'> 
            “Wishing you a day filled with happiness, laughter and as many cupcakes as your heart desires. Happy Birthday!” 
        </p>
        
        <p style='text-align: center; font-size: 1.2em; color: #DA70D6;'> 
            “May your Birthday be filled with the magic of love, joy, and all the things that make you happy. Happy Birthday!” 
        </p>   
    </div>
    """,
    unsafe_allow_html=True
)
