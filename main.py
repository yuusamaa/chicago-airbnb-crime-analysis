import os
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from mgwr.gwr import GWR
from mgwr.sel_bw import Sel_BW

# ---------------------------------------------------------
# 1. DATA LOADING AND PREPARATION
# ---------------------------------------------------------
# Set dynamic file paths (GitHub-friendly relative paths)
base_path = os.path.dirname(os.path.abspath(__file__))
shp_path = os.path.join(base_path, "data", "airbnb_Chicago 2015.shp")

# Load the Shapefile using GeoPandas
print("Loading the dataset...")
gdf = gpd.read_file(shp_path)

# Drop missing values (NaN) to prevent model fitting errors
gdf = gdf.dropna()

# ---------------------------------------------------------
# 2. DEFINING MODEL VARIABLES
# ---------------------------------------------------------
# Dependent Variable (What we want to predict: Number of Crimes)
y = gdf['num_crimes'].values.reshape((-1, 1))

# Independent Variables (Socioeconomic factors affecting crime)
# Variables: Per capita income, Poverty, Unemployment, Without High School diploma, Hardship index
X_cols = ["income_pc", "poverty", "unemployed", "without_hs", "harship_in"]
X = gdf[X_cols].values

# Extract geographic coordinates (X, Y) from polygon centroids for GWR
coords = np.array([(geom.centroid.x, geom.centroid.y) for geom in gdf.geometry])

# ---------------------------------------------------------
# 3. GEOGRAPHICALLY WEIGHTED REGRESSION (GWR) MODEL SETUP
# ---------------------------------------------------------
# Calculate the optimal bandwidth for the spatial kernel
print("Calculating optimal bandwidth, this may take a moment...")
bw = Sel_BW(coords, y, X).search()
print(f"Optimal Bandwidth: {bw}")

# Fit the GWR model
model = GWR(coords, y, X, bw)
results = model.fit()

# Print the statistical summary of the model
print(results.summary())

# ---------------------------------------------------------
# 4. PROCESSING DATA FOR VISUALIZATION
# ---------------------------------------------------------
# Append the calculated local coefficients (betas) to the GeoDataFrame for mapping.
# The 0th index in results.params is the 'Intercept', so variable coefficients start at index 1.
for i, name in enumerate(X_cols):
    gdf[f"beta_{name}"] = results.params[:, i + 1]

# Append the model residuals (prediction errors)
gdf['residuals'] = results.resid_response

# ---------------------------------------------------------
# 5. VISUALIZATION (MAPPING)
# ---------------------------------------------------------
print("Generating maps...")

# Map 1: Spatial Distribution of the Poverty Coefficient
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
gdf.plot(column="beta_poverty", cmap="coolwarm", edgecolor="black", legend=True, ax=ax)
plt.title("GWR Coefficient: Poverty vs. Crime Rate")
plt.axis("off")
plt.tight_layout()
plt.show()

# Map 2: Model Residuals
# High residual areas indicate where the model under/over-predicts crime rates.
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
gdf.plot(column="residuals", cmap="RdYlBu_r", edgecolor="black", legend=True, ax=ax)
plt.title("GWR Model Residuals (Prediction Errors)")
plt.axis("off")
plt.tight_layout()
plt.show()