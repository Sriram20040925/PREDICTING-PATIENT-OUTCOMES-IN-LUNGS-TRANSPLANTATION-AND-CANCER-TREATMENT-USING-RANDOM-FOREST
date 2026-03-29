import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# ----------------------------
# 1. Load Dataset
# ----------------------------
data = pd.read_csv("survey lung cancer.csv")

# Remove unwanted spaces
data.columns = data.columns.str.strip()

# ----------------------------
# 2. Encode ALL string columns
# ----------------------------
label_encoders = {}

for column in data.columns:
    if data[column].dtype == 'object':
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le   # store encoder

# ----------------------------
# 3. Split Features & Target
# ----------------------------
X = data.drop("LUNG_CANCER", axis=1)
y = data["LUNG_CANCER"]

# ----------------------------
# 4. Train Model
# ----------------------------
model = RandomForestClassifier()
model.fit(X, y)

print("\n✅ Model Training Completed Successfully!")

# ----------------------------
# 5. Take User Input
# ----------------------------
print("\nAnswer the Following Questions:")

user_input = []

for column in X.columns:
    
    question = column.replace("_", " ").title()
    
    if column in label_encoders:
        print(f"\n{question} Options:")
        classes = label_encoders[column].classes_
        for i, val in enumerate(classes):
            print(f"{i} = {val}")
        
        value = int(input("Enter option number: "))
    else:
        value = int(input(f"{question}: "))
    
    user_input.append(value)

# ----------------------------
# 6. Prediction
# ----------------------------
prediction = model.predict([user_input])

# Decode output
output = label_encoders["LUNG_CANCER"].inverse_transform(prediction)

# ----------------------------
# 7. Final Result
# ----------------------------
print("\n=========================")
print("Prediction Result:", output[0])
print("=========================")
