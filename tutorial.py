import streamlit as st
st.set_page_config(page_title="MyStreamlit",page_icon="random")
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Download'))
st.image("https://thumbs.dreamstime.com/z/back-to-school-happy-child-sitting-desk-girl-doing-homework-online-education-204282761.jpg")

st.title ("online python classes")

st.header("By Jyotsna Giri")
st.text ("this is tutorial on streamlit library")
st.image("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png")
if (mymenu=="Home"):
    st.markdown('<centre><h1>WELCOME</h1></centre>',unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=kqtD5dpn9C8&t=3s")
elif(mymenu=="FillForm"):
    with st.form('My Form'):
        name=st.text_input("Enter name")
        dob=st.date_input("enter dob")
        marks=st.slider("Marks")
        k=st.form_submit_button("submit")
        if k:
            st.write("name:",name,"DOB:",dob,"Marks:",marks)
elif(mymenu=="Download"):
    st.header("Downloads")
    st.download_button('Download Now' ,'this is download data','python.txt')


