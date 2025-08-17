🏠 House Price Prediction

A Machine Learning project to predict house prices based on features like square footage, bedrooms, bathrooms, year built, and neighborhood.
Built with Python, Scikit-learn, and Streamlit.

🚀 Features

Data preprocessing & Exploratory Data Analysis (EDA)

Multiple ML models implemented: Linear Regression, Random Forest, Gradient Boosting, XGBoost

Model comparison with performance metrics (R², MAE, RMSE)

Interactive Streamlit web app for predictions

Currency conversion: Predict prices in USD or INR

📊 Dataset

Dataset used: Boston House Prices / Kaggle Dataset
Contains features like:

SquareFeet

Bedrooms

Bathrooms

YearBuilt

Neighborhood (Suburb / Urban)

Price (target variable)

📂 Project Structure
House-Price-Prediction/
│── app.py                
│── best_model.pkl       
│── requirements.txt     
│── README.md             
│── notebook.ipynb       

⚡ Installation

Clone the repository

git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction


Install dependencies

pip install -r requirements.txt


Run the app

streamlit run app.py

🎯 Example Predictions

Input:

SquareFeet: 2000

Bedrooms: 3

Bathrooms: 2

Year Built: 2010

Neighborhood: Urban

Output:

Estimated House Price: ₹ 82,45,670

📊 Models Used

Linear Regression

Random Forest Regressor

Gradient Boosting Regressor

XGBoost Regressor

📈 Final model chosen: Random Forest (Best Performance)

📌 Future Improvements

Add more advanced models (CatBoost, LightGBM)

Improve feature engineering

Deploy on Streamlit Cloud / Hugging Face Spaces

Build a full-stack version with database integration

🙌 Acknowledgements

Dataset: Kaggle House Prices

Libraries: Scikit-learn, Pandas, NumPy, Streamlit, Matplotlib, Seaborn

✨ Made by Priyanshi Chaurasiapython test.py
