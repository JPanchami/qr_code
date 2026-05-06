!pip install streamlit
import streamlit as st
import qrcode
from PIL import Image
#page title
st.title("QR Code Generator")
data=st.text_input("enter the url")
if st.button("generate QR code"):
  if data:
       qr = qrcode.make(data)
       qr.save("qr.png")
       img=Image.open("qr.png")
       st.image(img,caption ="generated QR code")
       with open ("qr.png","rb") as f:
             st.download_button("Download QR Code",f.read(),mime="image/png")  
  else:
      st.warning("please enter some text")
