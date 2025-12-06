import streamlit as st
import joblib
import numpy as np

# --------- PAGE SETTINGS ---------
st.set_page_config(page_title="Iris Flower Classifier")

# Custom CSS for styling
st.markdown("""
<style>

    /* ----------- PAGE BACKGROUND ----------- */
    .stApp {
        background: linear-gradient(to bottom right, #faf5ff, #f3e8ff, #e5dbff);
    }

    /* center main content */
    .block-container {
        padding-top: 2rem;
    }

    /* purple input boxes */
    div[data-baseweb="input"] > div {
        background-color: #f3e8ff !important;
        border-radius: 8px !important;
    }
    input {
        background-color: #f3e8ff !important;
    }

    /* title styling */
    .app-title {
        text-align: center;
        color: #7b2cbf;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 20px;
    }

    /* ----------- PURPLE BUTTON ----------- */
    div.stButton > button {
        background-color: #7b2cbf;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 18px;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #5a189a;
        color: white;
    }

</style>
""", unsafe_allow_html=True)

# --------- TITLE ---------
st.markdown("<div class='app-title'>🌸 Iris Flower Prediction App</div>", unsafe_allow_html=True)

# --------- LOAD MODEL ----------
model = joblib.load("best_model.pkl")

# mapping output to names + images
class_map = {
    0: ("Setosa", "setosa.jpg"),
    1: ("Versicolor", "versicolor.jpg"),
    2: ("Virginica", "virginica.jpg")
}

# --------- INPUT SECTION ---------
st.write("### Enter flower measurements below")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input("Sepal Length", min_value=0.0, step=0.1)
    sepal_width = st.number_input("Sepal Width", min_value=0.0, step=0.1)

with col2:
    petal_length = st.number_input("Petal Length", min_value=0.0, step=0.1)
    petal_width = st.number_input("Petal Width", min_value=0.0, step=0.1)

st.write("---")

# --------- PREDICTION ---------
if st.button("Predict Flower"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    pred = model.predict(features)[0]

    flower_name, flower_img = class_map[pred]

    # Result card
    st.markdown(
        f"""
        <div style='padding: 20px; border-radius: 12px; background-color: #f8f8ff; 
                    text-align: center; box-shadow: 0px 0px 10px #ddd;'>
            <h2 style='color:#5a189a;'>Prediction Result</h2>
            <h3 style='color:#7b2cbf;'>{flower_name} 🌼</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.image(flower_img, caption=f"{flower_name}", use_container_width=True)
