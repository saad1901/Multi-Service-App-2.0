
import streamlit as st
import time

st.header('Email Service by saad.BravoAPI')
a,b = st.columns(2)
to = a.text_input("Enter Recipient's Address")
fr = b.text_input("From (optional)")
msg = st.text_area('Enter Message to Send')
if fr =="":
    fr = "test.service@saad"

sub = st.button('Send')
if sub:
    if to == "" or msg == "":
        st.subheader(fr)
        warn = st.warning("Field required")
        time.sleep(2)
        warn.empty()