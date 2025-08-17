import pickle

with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)


# Example input (SquareFeet, Bedrooms, Bathrooms, YearBuilt, Neighborhood_Suburb, Neighborhood_Urban)
sample_input = [[2000, 3, 2, 2010, 1, 0]]   # Urban=0, Suburb=1

# Prediction
pred = model.predict(sample_input)

# Dollar to Rupees conversion
price_in_rupees = pred[0] * 83  # 1 USD ~ 83 INR

print("Predicted Price (USD):", round(pred[0], 2))
print("Predicted Price (INR): ₹", round(price_in_rupees, 2))
