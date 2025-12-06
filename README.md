# 🌸 Iris Flower Prediction App

This project predicts the species of an Iris flower based on four input features:
sepal length, sepal width, petal length and petal width.

I trained and compared two models — 
- Logistic Regression
- KNN 
inside a Google Colab notebook. After evaluating both, Logistic Regression gave the most stable performance, so I saved that model and used it for deployment.

The app is built with Streamlit, and you can try the live version here:
[Iris_Prediction_Streamlit_App](https://irisflowerpredictionstremlit.streamlit.app/)

## Project Structure
Iris_Flower_Prediction_Streamlit/
│
├── best_model.pkl                 # Saved Logistic Regression model
├── app.py                         # Streamlit application
├── setosa.jpg                     # Flower image
├── versicolor.jpg                 # Flower image
├── virginica.jpg                  # Flower image
├── iris_model_training.ipynb      # Google Colab notebook (model training + comparison)
└── README.md

## How the Model Was Built
Inside the Colab notebook:
1- Loaded and explored the Iris dataset.
2- Trained two models:
   Logistic Regression
   K-Nearest Neighbors (KNN)
3- Compared performance using accuracy and validation scores.
4- Logistic Regression performed better, so I saved it using Joblib.
5- This saved model is used in the Streamlit app for real-time predictions.

## Using the Streamlit App
The app asks for four inputs:
```
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width
```
After clicking Predict Flower, the app shows:
- The predicted Iris species
- A matching flower image

## How to Run Locally
Clone the repository:
```
git clone https://github.com/Naima-Yaqub/Iris_Flower_Prediction_Streamlit.git
cd Iris_Flower_Prediction_Streamlit
```
Install dependencies:
```
git clone https://github.com/Naima-Yaqub/Iris_Flower_Prediction_Streamlit.git
cd Iris_Flower_Prediction_Streamlit
```
Run the app:
```
streamlit run app.py
```

## Technologies Used
- Python
- Logistic Regression
- KNN
- Joblib
- Streamlit
- NumPy
- Matplotlib / Seaborn (for exploration)
