import streamlit as st
from pint import UnitRegistry

# Initialize unit registry
ureg = UnitRegistry()

# Unit conversion categories
unit_categories = {
    "Length": ["meters", "kilometers", "miles", "inches", "feet", "centimeters", "millimeters"],
    "Weight": ["grams", "kilograms", "pounds", "ounces", "tons"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["seconds", "minutes", "hours", "days", "weeks"],
    "Speed": ["meters per second", "kilometers per hour", "miles per hour"],
    "Volume": ["liters", "milliliters", "gallons", "cubic meters"],
    "Data Storage": ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"]
}

# Streamlit App UI
st.set_page_config(page_title="Unit Converter", layout="wide")
st.title("🔄 Universal Unit Converter")
st.write("Convert various units seamlessly across multiple categories.")

# User selects category
category = st.selectbox("Select Conversion Category:", list(unit_categories.keys()))

# Select units within chosen category
if category:
    from_unit = st.selectbox("From Unit:", unit_categories[category])
    to_unit = st.selectbox("To Unit:", unit_categories[category])
    value = st.number_input(f"Enter Value in {from_unit}:", min_value=0.0, step=0.1)
    
    # Convert Units
    if st.button("Convert"):
        try:
            if category == "Temperature":
                # Special conversion for temperature (Pint doesn't support direct conversion)
                if from_unit == "celsius" and to_unit == "fahrenheit":
                    result = (value * 9/5) + 32
                elif from_unit == "fahrenheit" and to_unit == "celsius":
                    result = (value - 32) * 5/9
                elif from_unit == "celsius" and to_unit == "kelvin":
                    result = value + 273.15
                elif from_unit == "kelvin" and to_unit == "celsius":
                    result = value - 273.15
                elif from_unit == "fahrenheit" and to_unit == "kelvin":
                    result = (value - 32) * 5/9 + 273.15
                elif from_unit == "kelvin" and to_unit == "fahrenheit":
                    result = (value - 273.15) * 9/5 + 32
                else:
                    result = value  # If same unit selected
            else:
                # General unit conversion
                result = (value * ureg(from_unit)).to(to_unit).magnitude
            
            st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
        except Exception as e:
            st.error(f"Conversion Error: {e}")
