import streamlit as st

# import time

# my_bar = st.progress(0)

# for percent_complete in range(100):
#      time.sleep(0.1)
#      my_bar.progress(percent_complete + 1)
     


# st.success('This is a success message!')

# st.title('Page Title')
# st.header('Page Subtitle')
# st.subheader('Page SubHeader')

# st.markdown("""
# <h1> A faster way to build and share data apps </h1>
#             """, unsafe_allow_html= True)

st.title('Streamlit')
# st.image('./images/animated.jpg', use_column_width = False)

sidebar = st.sidebar
sidebar.header('Streamlit.io')
sidebar.markdown('----')

myname = sidebar.text_input('Enter your name')
btn = sidebar.button("Enter")

if btn:
    st.subheader("Welcome "+myname)
    st.balloons()
    # st.snow()

st.markdown("""

<center>
<h1 style="font-size: 70px; font-weight: 700;"> A faster way to build <br>
and share data apps </h1>

<h6 style="color: grey; font-size: 30px;">
Streamlit turns data scripts into shareable web apps in minutes. <br>
All in pure Python. No front‑end experience required.
</h6>

<button type=click> <a href="https://streamlit.io/"  style="padding: 15px 32px; text-decoration: none; color: black; font-size: 18px;"> Try Streamlit Now </button>


<video width="70%" height="50%" controls autoplay> 
  <source src="https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4" type="video/mp4">
</video>

</center>
            """, unsafe_allow_html= True)

st.markdown('Streamlit is **_really_ cool**.')

st.markdown('**Print Function**')

code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')

