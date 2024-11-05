import streamlit as st
import segno
import time

# add a banner
st.image("https://i.pinimg.com/564x/1e/fe/5e/1efe5e318f2721e364158bacf33855d0.jpg")

# add a title
st.title("QR Code Generator")

# add a textbox
url = st.text_input("Please enter the data you want to encode:")

def generate_qrcode(url):
    qrcode = segno.make_qr(url)
    qrcode.save("images/qrcode_streamlit.png",
                scale=10)

if url:
    with st.spinner("Generate QR Code"):
        time.sleep(3)
    generate_qrcode(url)
    st.image("images/qrcode_streamlit.png",
             caption="Here is the qr code")

st.markdown("cunt")