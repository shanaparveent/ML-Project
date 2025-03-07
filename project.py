import streamlit as st
import joblib
import os

# Load the model
model_path =  r"C:\Users\shana\python 2\ML\project"
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("Model file not found. Please check the file path.")
    st.stop()

# App title
st.title("Astronomical Object Class Prediction")
st.sidebar.info("This app predicts whether an object is a Star, Galaxy, or Quasar.")




# Single Entry
if input_method == "Single Entry":
    st.subheader("Enter Feature Values")

    # Magnitudes
    u = st.number_input("u (Ultraviolet Magnitude)", value=0.0, format="%.2f")
    g = st.number_input("g (Green Magnitude)", value=0.0, format="%.2f")
    r = st.number_input("r (Red Magnitude)", value=0.0, format="%.2f")
    i = st.number_input("i (Infrared Magnitude)", value=0.0, format="%.2f")
    z = st.number_input("z (Far Infrared Magnitude)", value=0.0, format="%.2f")

    # Redshift
    redshift = st.number_input("Redshift (z)", value=0.0, format="%.6f")

    # Derived Colors
    u_g = u - g
    g_r = g - r
    r_i = r - i
    i_z = i - z

    st.write(f"Derived Features: u-g = {u_g:.2f}, g-r = {g_r:.2f}, r-i = {r_i:.2f}, i-z = {i_z:.2f}")

    # Predict button
    if st.button("Predict Class"):
        # Prepare the input for the model
        input_data = np.array([[u, g, r, i, z, redshift]])
        prediction = model.predict(input_data)
        predicted_class = class_labels[prediction[0]]
        st.success(f"The predicted class is: **{predicted_class}**")