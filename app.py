import streamlit as st
import qrcode
from PIL import Image

st.title("qr code genrator")
data=st.text_input("enter url")
if st.button("genrate QR"):
  if data:
    qr = qrcode.make(data)
    qr.save("qr.png")
    img = Image(img, caption="genrated QR code")
    with open("qr.png","rb")as f:
      st.download_button("Download QR",f,file_name="qr.png")
  else:
    st.warning("please enter some text"
