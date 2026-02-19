# Spatial Analysis of Chicago: Crime & Socioeconomic Factors (GWR)

## 📌 Project Overview
This project investigates the spatial relationship between crime rates and various socioeconomic factors (such as poverty, unemployment, and income per capita) across the city of Chicago. Instead of using traditional global regression models, this analysis utilizes **Geographically Weighted Regression (GWR)** to understand how these relationships change from one neighborhood to another.

## 🚀 Technologies Used
* **Python 3.14.2**
* **GeoPandas:** For spatial data manipulation and reading Shapefiles.
* **MGWR:** For calibrating the Geographically Weighted Regression model and calculating optimal bandwidth.
* **Matplotlib / NumPy / Pandas:** For data processing and spatial visualization.

## 🧠 Methodology
Traditional regression models assume that the relationship between variables is constant across space. However, urban dynamics are highly localized. By using **GWR**, this project maps local coefficients to reveal how factors like *poverty* might have a stronger correlation with crime in certain districts compared to others.

### Key Variables Analyzed:
* **Dependent Variable:** Number of Crimes (`num_crimes`)
* **Independent Variables:** Per capita income (X1), poverty rate (X2), unemployment rate (X3), education level/without HS (X4), and hardship index (X5).

## 📊 Model Statistics & Console Output
The terminal outputs during the model execution clearly show the superiority of the spatial approach. The GWR model significantly outperformed the global model, increasing the explanatory power ($R^2$) from **0.278 to 0.441**.

```text
Global Regression Results
---------------------------------------------------------------------------  
Residual sum of squares:                                       1738116954.711
AICc:                                                              1330.934  
R2:                                                                   0.278  

Geographically Weighted Regression (GWR) Results
---------------------------------------------------------------------------
Spatial kernel:                                           Adaptive bisquare
Bandwidth used:                                                      55.000
Residual sum of squares:                                       1344904470.536
AICc:                                                              1329.523
R2:                                                                   0.441

Summary Statistics For GWR Parameter Estimates
---------------------------------------------------------------------------
Variable                   Mean        STD        Min     Median        Max
-------------------- ---------- ---------- ---------- ---------- ----------
Intercept (X0)        -8261.958   3021.114 -13675.687  -7351.714  -4068.955
Income (X1)               0.212      0.017      0.162      0.213      0.235
Poverty (X2)            227.642    139.428     48.683    220.268    462.021
Unemployed (X3)         351.551    290.462     87.621    167.425    962.589
Without HS (X4)          10.548    133.506   -154.869    -18.626    200.818
Hardship Idx (X5)         4.973    118.911   -197.164     26.140    141.891
===========================================================================

## 📊 Key Findings & Insights
Based on the statistical outputs and spatial mapping:

* **Model Performance:** The GWR model significantly outperformed the traditional Global Regression model, increasing the R-squared (explanatory power) from **0.278 to 0.441**. This proves that the drivers of crime vary significantly depending on the geography of the neighborhood.
* **The "Poverty" Effect:** While poverty generally increases crime across the city, the GWR coefficients reveal that its impact is up to **10 times stronger** in specific neighborhoods compared to others. 
* **The "Education" Paradox:** Interestingly, the lack of a high school diploma showed a positive correlation with crime in some areas, but a *negative* correlation in others. This highlights how complex and localized urban socio-economic relationships can be.

## 🗺️ Visual Insights from the Maps

**1. The Spatial Impact of Poverty**
The GWR coefficient map reveals a stark divide in Chicago. The deep red areas in the South and West sides indicate a highly positive, aggressive correlation between poverty and crime. In these neighborhoods, poverty is the primary driver of crime. However, in the Northern (blue) districts, the coefficient drops near zero, meaning crime in those areas is driven by entirely different, non-poverty-related dynamics.

<img width="1536" height="772" alt="poverty_map png" src="https://github.com/user-attachments/assets/c4733b12-4529-4686-a0a0-c35ac0cf5f42" />

**2. Model Accuracy and Residual Anomalies**
The residual map shows that the model accurately predicts crime rates for the vast majority of the city (indicated by the neutral yellow tones). However, there is a massive positive residual anomaly (dark red) in the city's eastern central core (likely the Downtown/Loop area). The model significantly under-predicted crime here because socioeconomic factors (like residential poverty) fail to account for crimes driven by high commercial activity and tourist density in the city center.

<img width="1536" height="772" alt="residuals_map png" src="https://github.com/user-attachments/assets/e0d48dbd-8072-44a3-89d5-4b28332fea9e" />
