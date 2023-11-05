import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('model_pkl.pkl','rb'))


def main():
  st.sidebar.header("Stroke Risk Prediction")
  st.sidebar.text("This a Web app that predicts wether you will have a stoke or not.")
  st.sidebar.header("Just fill in the information below")
  st.sidebar.text("The NaiveBayes Classifier was used.")



  age = st.slider("Input Your age", 0, 100)
  hypertension = st.slider("Input your if you have hypertension with 0 for no and 1 for yes",0, 1)
  heartdisease = st.slider("Input your if you have heartdisease with 0 for no and 1 for yes",0 ,1)
  sugar = st.slider("Put your average glucose level",50.0, 300.000)
  bmi = st.slider("Input your BMI",0.0,70.0)

  inputs = [[age,hypertension,heartdisease,sugar,bmi]]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(int)
    if updated_res == 0:
       st.write("Probability of stroke -> Low. Take good care of yourself regardless")
    else:
       st.write("Probability of stroke -> High. Take better care of yourself")
   


if __name__ =='__main__':
  main()
