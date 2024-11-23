import numpy as np
import pandas as pd
from django.http import JsonResponse
from sklearn.linear_model import LinearRegression

# Load the Excel file and prepare the model
file_path = r"C:\Users\HP\Downloads\Prix-Moyen-Au-m²-Algerie.xlsx"
df = pd.read_excel(file_path)
df.dropna(inplace=True)

# Extract input and output values
list_x = df.iloc[:, 0].tolist()  # Input values
list_y = df.iloc[:, 1].tolist()  # Output values

# Convert lists to numpy arrays
x = np.array(list_x).reshape(-1, 1)
y = np.array(list_y)

# Normalize x
x_mean = np.mean(x)
x_std = np.std(x)
x_normalized = (x - x_mean) / x_std

# Train the model
model = LinearRegression()
model.fit(x_normalized, y)

def predict_price(surface_area):
    # Normalize input surface area before prediction
    surface_area_normalized = (surface_area - x_mean) / x_std
    predicted_price = model.predict(np.array([[surface_area_normalized]]))
    return predicted_price[0]

def predict_view(request):
    surface_area = request.GET.get('surface_area')
    
    if surface_area is not None:
        try:
            surface_area = float(surface_area)
            predicted_price1 = predict_price(surface_area)
            print(predicted_price1)
            return JsonResponse({'predicted_price': predicted_price1})
        except ValueError:
            return JsonResponse({'error': 'Invalid surface area. Please enter a valid number.'}, status=400)
    else:
        return JsonResponse({'error': 'No surface area provided.'}, status=400)