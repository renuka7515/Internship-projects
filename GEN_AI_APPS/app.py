from openai import OpenAI
import streamlit as st

f = open("keys/.OpenAI_API_Key.txt")
key = f.read()
client = OpenAI(api_key=key)

st.title("AI Code Reviewer")

prompt = st.text_area("Enter your python code")

if st.button("Review code")== True:

    response = client.chat.completions.create(
                model="gpt-3.5-turbo-0301",
                messages=[
                {"role":"system","content":"""You are a experienced and friendly AI python code reviewer and debugger,
                                            your role is to verify the python code given by the user as input and 
                                            you need to review the code the fix the code and provide output like the bugs you 
                                            find and the fixed code with explanation in an undestanding way"""},
                {"role":"user","content":prompt}
                ]
            
    )

    st.write(response.choices[0].message.content)
