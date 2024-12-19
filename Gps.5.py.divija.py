import pandas as pd
import phonetics

# Example dataset: Names and their corresponding genders
data = {
    'Name': ['Hamsika', 'Harshith', 'Sahithya', 'Hasith', 'Anusha', 'Pavan'],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male']
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Apply the Soundex algorithm to create a phonetic code for each name
df['Phonetic_Code'] = df['Name'].apply(phonetics.soundex)

# Display the DataFrame with phonetic codes
print("Dataset with Phonetic Codes:")
print(df)

# Function to predict gender based on phonetic code
def predict_gender(name, df):
    phonetic_code = phonetics.soundex(name)
    
    # Check if the phonetic code matches any in the dataset
    matches = df[df['Phonetic_Code'] == phonetic_code]
    
    if not matches.empty:
        # Return the most common gender for the matched phonetic code
        predicted_gender = matches['Gender'].mode()[0]
        return predicted_gender
    else:
        return "Unknown"

# Test the prediction function
test_names = ['Hamsikha', 'Harshith', 'Sahithya', 'Pavani']

print("\nGender Predictions:")
for name in test_names:
    prediction = predict_gender(name, df)
    print(f"Name: {name}, Predicted Gender: {prediction}")
