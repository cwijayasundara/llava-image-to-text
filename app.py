import replicate
import streamlit as st

from dotenv import load_dotenv

load_dotenv()
#  Use replicate deployed LLaVA instance for image to text
prompt = ("You are an insurance underwriter. Extract all the information from the image thats useful for your "
          "insurance underwriting process!")

server_url = "yorickvp/llava-13b:2facb4a474a0462c15041b78b1ad70952ea46b5ec6ad29583c0b29dbd4249591"

st.header("Please Upload an Image For Analysis")
file = st.file_uploader("", type=["jpeg", "jpg", "png"])

if file:
    st.image(file)
    output = replicate.run(server_url, input={"image": file, "prompt": prompt})
    response = []
    for item in output:
        response.append(item)
    response = ''.join(response)
    response = response.split('.')
    response = list(filter(None, response))
    st.write(response)
