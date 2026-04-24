# Dynamic Fare Pricing ML Engine

## Overview

This project implements an end-to-end machine learning system for dynamic fare pricing, inspired by real-world ride-hailing platforms. The system predicts ride prices based on demand patterns, temporal features, and trip-related variables.

It also simulates a demand-based pricing strategy and compares it with static pricing to evaluate revenue impact.

---

## Objectives

* Build a predictive model for ride pricing
* Analyze demand variation across different times of the day
* Understand the relationship between demand and pricing
* Simulate dynamic pricing strategies
* Evaluate revenue improvement over static pricing

---

## Tech Stack

* Python (Pandas, NumPy)
* Data Visualization: Matplotlib, Seaborn
* Machine Learning: Scikit-learn
* Development Environment: Jupyter Notebook

---

## Dataset

This project uses multiple publicly available datasets:

1. NYC Taxi Trip Data
   https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

2. India Weather Dataset (Kaggle)
   https://www.kaggle.com/datasets/developerghost/climate-in-india-daily-weather-data-2000-2024

3. Bangalore Traffic Dataset (Kaggle)
   https://www.kaggle.com/datasets/preethamgouda/banglore-city-traffic-dataset

Note: Due to file size and licensing constraints, datasets are not included in this repository.

To run the project:

1. Download the datasets from the links above
2. Place them inside the `data/` directory
3. Update file paths in the notebook if required

---

## Workflow

### Data Preprocessing

* Cleaned and structured trip data
* Removed missing values and duplicates
* Filtered outliers in pricing and demand
* Converted timestamps into usable features

### Feature Engineering

* Extracted hour of day and day of week
* Created peak-hour indicator
* Derived demand score
* Generated features capturing temporal patterns

### Exploratory Data Analysis

* Analyzed demand variation across hours
* Studied distribution of demand scores
* Examined relationship between demand and pricing

### Model Development

* Implemented regression-based models for fare prediction
* Compared model performance across different approaches

### Dynamic Pricing Simulation

* Adjusted pricing based on demand levels
* Compared revenue against static pricing baseline

---

## Dashboard Overview

The project includes a dashboard that visualizes:

* Demand pattern across different hours of the day
* Distribution of demand levels
* Relationship between demand and ride price
* Price comparison between peak and normal hours
* Revenue comparison between static and dynamic pricing

---

## Results

* Dynamic pricing demonstrates a significant increase in total revenue
* Pricing responds effectively to demand fluctuations
* The model captures key relationships between demand and fare

---

## Project Structure

```plaintext
dynamic-fare-pricing-ml-engine/
│
├── data/
│
├── notebooks/
│   └── dynamic_pricing_analysis.ipynb
│
├── images/
│   └── dashboard.png
│
├── README.md
├── INSIGHTS.md
```

---

## Future Improvements

* Integrate real-time traffic and weather APIs
* Use advanced models such as Gradient Boosting or XGBoost
* Deploy as an interactive web application
* Improve robustness for extreme cases and outliers
