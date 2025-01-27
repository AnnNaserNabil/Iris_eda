# Iris Dataset Exploratory Data Analysis (EDA) and Outlier Handling

This repository contains a Streamlit application for performing exploratory data analysis (EDA) and outlier handling on the famous Iris dataset. The application provides interactive visualizations, statistical summaries, and tools to explore and understand the Iris dataset.

## Table of Contents
- [Project Overview](#project-overview)
- [Iris Dataset](#iris-dataset)
- [Features](#features)


## Project Overview
The Iris dataset is a classic dataset in the field of machine learning and statistics. It consists of 150 samples of iris flowers, with measurements for sepal length, sepal width, petal length, and petal width. Each sample is classified into one of three species:
- Iris-setosa
- Iris-versicolor
- Iris-virginica

The goal of this Streamlit application is to provide an interactive platform for visualizing relationships between variables, identifying patterns, handling outliers, and computing correlations in the Iris dataset.

## Iris Dataset
The Iris dataset (`Iris.csv`) contains the following columns:
- `Id`: Unique identifier for each sample
- `SepalLengthCm`: Sepal length in centimeters
- `SepalWidthCm`: Sepal width in centimeters
- `PetalLengthCm`: Petal length in centimeters
- `PetalWidthCm`: Petal width in centimeters
- `Species`: Species of the iris flower (`Iris-setosa`, `Iris-versicolor`, `Iris-virginica`)

## Features
- **Dataset Preview**: View the entire dataset in a table format.
- **Basic Statistics**: Display basic statistical summaries (mean, median, standard deviation, etc.) for each column.
- **Scatter Plots**: Visualize relationships between pairs of variables grouped by species.
- **Pair Plots**: Explore pairwise relationships between all variables.
- **Histograms**: Analyze the distribution of each variable.
- **KDE Plots**: Visualize smoothed density distributions for each variable.
- **Correlation Matrix**: Compute and visualize the correlation matrix to assess linear relationships.
- **Box Plots**: Highlight distributions and outliers for each variable across species.

