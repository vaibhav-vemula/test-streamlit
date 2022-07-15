from tensorflow.keras.models import load_model
import streamlit as st

def main():
    st.title("Test diabetic predictor")
    
    data = [[
        int(st.text_input("Pregnancies", 6)),
        int(st.text_input("Glucose", 148)),
        int(st.text_input("BloodPressure", 72)),
        int(st.text_input("SkinThickness",35)),
        int(st.text_input("Insulin",0)),
        float(st.text_input("BMI", 33.6)),
        float(st.text_input("DiabetesPedigreeFunction", 0.627)),
        int(st.text_input("Age",50))
    ]]
    
    if st.button("Predict"):
        result = model.predict(data)
        
        result = result[0][0]
        if result > 0.5:
            st.error("Person is Diabetic")
        else:
            st.success("Person is not Diabetic, Yayyy!!!")

if __name__ == '__main__':
    model = load_model('model.h5')
    main()