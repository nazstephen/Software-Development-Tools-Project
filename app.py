import pandas as pd
import streamlit as st
import plotly.express as px

#---------------------------------------------

# reading the file
try:
    # Try to read the CSV file from the local path.
    vehicles_df = pd.read_csv('/Users/benjaminstephen/Documents/TripleTen/Sprint_4/Software-Development-Tools-Project/notebooks/vehicles_us.csv')
except FileNotFoundError:
    try:
        # Try to read the CSV file from the server path
        vehicles_df = pd.read_csv('vehicles_us.csv')
    except FileNotFoundError:
        print("CSV file not found. Please check the file paths.")

#---------------------------------------------

# cleaning up 'model_year' column
# filling in the missing values in 'model_year' with a median for a group based on 'model'
vehicles_df['model_year'] = vehicles_df['model_year'].fillna(vehicles_df.groupby(['model'])['model_year'].transform('median'))
vehicles_df['model_year'] = vehicles_df['model_year'].astype(int)
vehicles_df['model_year'] = vehicles_df['model_year'].astype(str)

#---------------------------------------------

# cleaning up 'cylinders' column
# filling in the missing values in 'cylinders' with a median for a group based on 'model'
vehicles_df['cylinders'] = vehicles_df['cylinders'].fillna(vehicles_df.groupby(['model'])['cylinders'].transform('median'))
vehicles_df['cylinders'] = vehicles_df['cylinders'].astype(int)

#---------------------------------------------

# cleaning up 'odometer' column
# filling in the missing values in 'odometer' with a median for a group based on 'model'
vehicles_df['odometer'] = vehicles_df['odometer'].fillna(vehicles_df.groupby(['model'])['odometer'].transform('median'))

#---------------------------------------------

# cleaning up 'paint_color' column
vehicles_df['paint_color'].fillna('unknown', inplace=True)

#---------------------------------------------

# cleaning up 'is_4wd' column
vehicles_df['is_4wd'].fillna('no', inplace=True)
vehicles_df['is_4wd'].replace(1.0, 'yes', inplace=True)

#---------------------------------------------

st.header("Data Viewer")
st.write("""
###### Check out car listings here!
""")

# Display car listings
st.dataframe(vehicles_df, height=300)

#---------------------------------------------

st.header("Condition vs Model Year")
st.write("""
###### Check the distribution of car conditions across model years.
""")

# Filter out model years equal to 0
filtered_df = vehicles_df[vehicles_df['model_year'] != '0']

# Group by manufacturer and vehicle type, and count the number of vehicles
grouped_df = filtered_df.groupby(['model_year', 'condition']).size().reset_index(name='count')

# Create bar chart
fig1 = px.histogram(grouped_df, x="model_year", y="count", color="condition")

st.plotly_chart(fig1)

#---------------------------------------------

# defining age category of car
vehicles_df['age']= 2024 - (pd.to_numeric(filtered_df['model_year'], errors='coerce'))
def age_category(x):
    if x < 10: return '<10 yrs old'
    elif 10 <= x < 20: return '10-20 yrs old'
    else: return '20+ yrs old'

vehicles_df['age_category'] = vehicles_df['age'].apply(age_category)

#---------------------------------------------

st.header('Price vs Mileage')
st.write("""
###### Check how price is affected by a car's mileage.
""")

# Checkbox to enable/disable visual distinction between ages
show_age_category = st.checkbox("Show Age Categories")

# Distribution of price depending on odometer_value, engine_capacity, number_of_photos
if show_age_category:
    fig2 = px.scatter(vehicles_df, x="price", y="odometer", color="age_category")
else:
    fig2 = px.scatter(vehicles_df, x="price", y="odometer")

st.plotly_chart(fig2)
