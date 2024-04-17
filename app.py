import streamlit as st
import pandas as pd
from joblib import dump, load
from final import predict_power_generation, predict_custom_input

# Load the trained model
model = load('gradient_boosting_model.joblib')

# Define Streamlit app
def main():
    st.title("Power Generation Prediction")

    # Sidebar section for user input
    st.sidebar.header("User Input")

    # Dropdown for selecting stability
    stability_options = ["All", "Stable", "Unstable"]
    selected_stability = st.sidebar.selectbox("Select Stability:", stability_options)

    # Load the dataset
    data = load_data()

    # Filter data based on selected stability
    if selected_stability == "All":
        filtered_data = data
    elif selected_stability == "Stable":
        filtered_data = data[data['stability'] == 'stable']
    else:
        filtered_data = data[data['stability'] == 'unstable']

    # Display filtered data
    st.subheader("Filtered Data of 2019-2023")
    st.write(filtered_data)

    # Load the predicted data for 2024
    data1 = load_data1()

    # Display the predicted data
    st.subheader("Predicted Data for 2024")
    st.write(data1)

    # Main content section for power generation prediction
    st.subheader("Power Generation Prediction")

    # User input for pressure, wind, and air temperature
    pressure = st.number_input("Enter Pressure (atm):", step=0.01)
    wind_speed = st.number_input("Enter Wind Speed (m/s):", step=0.01)
    air_temperature = st.number_input("Enter Air Temperature (°C):", step=0.01)

    
    # Perform prediction based on user input parameters
    if st.button("Predict Power Generation from Parameters"):
        power_prediction_param = predict_power_generation_param(air_temperature, pressure, wind_speed, data1)
        st.write(f"Predicted Power Generation: {power_prediction_param}")  

    # Add section for Power BI dashboard
    st.subheader("Power BI Dashboard")
    power_bi_dashboard = """
    <iframe width="800" height="506" src="https://app.powerbi.com/view?r=eyJrIjoiNjE3N2IzNTUtNzlhZi00NGVmLWI3MzUtODY1YjJiZmJhYzZiIiwidCI6IjNkNmVhYjlkLTc5MmMtNGFmOS05NDYwLTc5MzljYTkwYjZhYiJ9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>
    """
    st.markdown(power_bi_dashboard, unsafe_allow_html=True)

# Function to load the dataset
def load_data():
    return pd.read_csv("C:\\Users\\admin\\Downloads\\Hackwave-vs\\9_Sustainability_and_Environment\\gbr_updated_dataset.csv")  

# Function to load the predicted data for 2024
def load_data1():
    return pd.read_csv("C:\\Users\\admin\\Downloads\\Hackwave-vs\\9_Sustainability_and_Environment\\forecasted_power_generation_2024.csv")  


def predict_power_generation_param(air_temperature, pressure, wind_speed, filtered_data):
    # Prepare the input data for prediction
    
    predictions = predict_custom_input(air_temperature, pressure, wind_speed)
    # Display predictions
    print("Predicted power generation:", predictions)
    
    return predictions

# Load the dataset
data = pd.read_csv("C:\\Users\\admin\\Downloads\\Hackwave-vs\\9_Sustainability_and_Environment\\final_data.csv")  # Update with your dataset path

# Run the Streamlit app
if __name__ == "__main__":
    main()
