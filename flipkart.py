import streamlit as st
import pickle

# Load the saved model
with open(r"C:\Users\HP\Naive Bayes_model.pkl", 'rb') as file:
    model = pickle.load(file)

# Define a function to make predictions
def predict(text):
    prediction = model.predict([text])[0]
    if prediction==0:
        return "Negative"
    else:
        return"positive"

# Create the Streamlit app
st.title('Sentiment Analysis App')
text = st.text_input('Enter text:')
if st.button('Predict'):
    prediction = predict(text)
    st.write(f'Prediction: {prediction}')
