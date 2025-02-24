import streamlit as st

st.set_page_config(page_title='Growth Mindset Project', page_icon='⭐')
st.title('Growth Mindset Challenge: Web App with Streamlit')
st.header("🌱 Welcome to your growth journey!")
st.write(
    "This is a project to help you develop a growth mindset. A growth mindset is the belief that you can develop your "
    "abilities through hard work, good strategies, and input from others. People with a growth mindset tend to achieve "
    "more than those with a fixed mindset, who believe that their abilities are static."
)

# Quote section
st.header(" 🌱 Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill")

# Challenge input
st.header("🔧What's your challenge today?")
user_input = st.text_input('Describe a challenge you are facing today')

if user_input:
    st.success(f'You are facing: {user_input}. Keep going! You can do it! 💪')
else:
    st.warning('Please enter a challenge you are facing today.')

# Reflection
st.header('✨Reflect on your challenge')
reflection = st.text_area('How do you feel about the challenge?')

if reflection:
    st.success(f'✨Great! Your reflection: {reflection}')
else:
    st.warning('Reflecting on your thoughts about the challenge will help you grow.')

# Achievements
st.header('🎇Celebrate your wins!')
achievement = st.text_input('What did you achieve today?')

if achievement:
    st.success(f'Congratulations! You achieved: {achievement} 🎉')
else:
    st.warning('Please enter an achievement you had today.')

# Footer
st.write("You are on your way to developing a growth mindset! 🌟")
st.write("Keep believing in yourself and keep growing! 🌱")
st.write("Made with ❤️ by Kiran Adnan")
