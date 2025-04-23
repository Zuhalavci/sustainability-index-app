
import streamlit as st
import numpy as np
import pandas as pd

st.title("Interactive Sustainability Index Calculator")

# Sidebar Sliders for Weights
st.sidebar.header("Adjust Sustainability Weights")

energy_weight = st.sidebar.slider("Energy Consumption", 0, 100, 30)
co2_weight = st.sidebar.slider("Carbon Emissions", 0, 100, 30)
cost_weight = st.sidebar.slider("Production Cost", 0, 100, 18)
tool_weight = st.sidebar.slider("Tool Wear", 0, 100, 12)
fluid_weight = st.sidebar.slider("Fluid Usage", 0, 100, 6)
social_weight = st.sidebar.slider("Social Impact", 0, 100, 4)

# Normalizing the weights
weights = np.array([energy_weight, co2_weight, cost_weight, tool_weight, fluid_weight, social_weight])
weights = weights / weights.sum()

# Sample normalized scores for three methods (for demonstration)
methods = ["Conventional Drilling", "HP-EDM", "LP-EDM"]
scores = {
    "Energy": [0.31, 0.75, 1.0],
    "CO2": [0.28, 0.76, 1.0],
    "Cost": [0.2, 0.7, 1.0],
    "Tool": [1.0, 0.6, 0.8],
    "Fluid": [0.1, 0.8, 0.9],
    "Social": [0.3, 0.6, 1.0]
}

df = pd.DataFrame(scores, index=methods)

# Calculate SI
si_scores = df.values.dot(weights)

# Show results
df["Sustainability Index"] = si_scores
st.write("### Sustainability Index Results")
st.dataframe(df.style.format("{:.3f}"))

# Display SI ranking
ranking = df["Sustainability Index"].sort_values(ascending=False)
st.write("### Ranking")
st.write(ranking)
