import streamlit as st
import joblib

# Load the trained MLP model
model = joblib.load(r"C:\Users\Alaxo joy\OneDrive\Desktop\recipe project\modeltopaccuracy.pkl")


# Define the Streamlit app
def main():
    st.title("Recipe Generator")

    # User input for ingredients
    ingredients = st.text_input("Enter ingredients (comma-separated)", "")

    # Button to generate recipe
    if st.button("Generate Recipe"):
        # Process user input and generate recipe using the model
        recipe_name, instructions = generate_recipe(ingredients)
        
        # Display the generated recipe
        st.write(f"**Recipe Name:** {recipe_name}")
        st.write(f"**Instructions:** {instructions}")

# Function to generate recipe using the model
def generate_recipe(ingredients):
    # Add your code here to process the user input and generate the recipe using the loaded model
    # Example: recipe_name, instructions = model.predict(ingredients)
    return "Spaghetti Carbonara", "1. Cook spaghetti. 2. Fry bacon. 3. Mix with eggs and cheese. 4. Serve hot."

if __name__ == "__main__":
    main()
