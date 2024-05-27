# Software Development Tools: Project

## Project description
This project is an interactive web application built with Streamlit, designed for analyzing a car advertisement dataset. It provides users with a platform to explore various attributes of cars, including condition, model year, price, and mileage. Through features like histograms and scatter plots, users can gain insights into relationships between these attributes, such as understanding the distribution of car conditions across model years and the impact of mileage on car prices.

## Features
- Histogram of Car Conditions: A histogram to visualize the distribution of car conditions across different model years.
- Scatter Plot of Price vs. Mileage: A scatter plot to examine how the price of a car is influenced by its mileage.
- Interactive Checkbox: A feature that allows users to toggle the distribution of different ages of cars in the scatter plot.

## Technologies Used
- Python: The main programming language used for the project.
- Pandas: For data manipulation and analysis.
- Streamlit: For building the interactive web application.
- Plotly Express: For creating interactive visualizations.
- Altair: Optionally used for additional visualizations.

## Files in the Repository
- README.md: This file.
- .gitignore: Specifies files and directories to be ignored by git.
- app.py: The main application file for the Streamlit app.
- vehicles_us.csv: The dataset file (to be downloaded separately).
- notebooks/EDA.ipynb: Jupyter notebook for exploratory data analysis.
- requirements.txt: List of dependencies required by the project.
- .streamlit/config.toml: Configuration file for Streamlit deployment.

  ## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/nazstephen/Software-Development-Tools-Project.git
    cd <repository-directory>
    ```

2. Install the required Python packages:
    ```bash
    pip install streamlit scipy pandas
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit r

## Access the Application
You can access the deployed application at the following link: https://software-development-tools-project-ia76.onrender.com
