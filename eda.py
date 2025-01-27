import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
df = pd.read_csv('Iris.csv')


# Dataset preview toggle
st.sidebar.subheader("Dataset Preview")
if st.sidebar.checkbox("Show Dataset"):
    st.dataframe(df)

# Basic statistics toggle
st.sidebar.subheader("Basic Statistics")
if st.sidebar.checkbox("Show Statistics"):
    st.write(df.describe())


# Streamlit app title and introduction


st.markdown(
    """
    <style>
    .title {
        color: #4CAF50;
        font-family: 'Helvetica', sans-serif;
        font-size: 30px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<h1 class="title">Iris Dataset EDA and Outlier Handling</h1>', unsafe_allow_html=True)



st.markdown("""
### Iris Dataset EDA and Outlier Handling

**Introduction:**

This Streamlit application provides an interactive exploratory data analysis (EDA) for the famous Iris dataset. The Iris dataset contains 150 samples of iris flowers, with measurements for:
- Sepal Length (in cm)
- Sepal Width (in cm)
- Petal Length (in cm)
- Petal Width (in cm)

Each sample is classified into one of three species:
1. **Iris-setosa**
2. **Iris-versicolor**
3. **Iris-virginica**

**Objective:**

The goal of this Streamlit app is to:
- Visualize relationships between variables through interactive plots.
- Identify potential patterns, trends, or clusters in the data.
- Handle outliers (if any) and understand the distribution of features.
- Compute and visualize correlations to assess linear relationships.
""")

# Function for scatter plots
def scatter_plot(x, y):
    """
    Function to create a scatter plot for two specified columns, grouped by species.
    """
    fig, ax = plt.subplots()
    sns.scatterplot(x=x, y=y, hue='Species', data=df, ax=ax)
    ax.legend(bbox_to_anchor=(1, 1), loc=2)
    st.pyplot(fig)

# Scatter Plots Section
with st.expander("Scatter Plots"):
    st.subheader("Scatter Plot: SepalLengthCm vs SepalWidthCm")
    st.markdown("Visualizing the relationship between Sepal Length and Sepal Width.")
    scatter_plot('SepalLengthCm', 'SepalWidthCm')

    st.subheader("Scatter Plot: PetalLengthCm vs PetalWidthCm")
    st.markdown("Visualizing the relationship between Petal Length and Petal Width.")
    scatter_plot('PetalLengthCm', 'PetalWidthCm')

# Pair Plot Section
with st.expander("Pair Plot"):
    st.subheader("Pair Plot")
    st.markdown("Exploring pairwise relationships between all variables.")
    try:
        pair_plot_fig = sns.pairplot(df.drop(['Id'], axis=1), hue='Species', height=2)
        st.pyplot(pair_plot_fig)
    except Exception as e:
        st.error(f"Error rendering pair plot: {e}")

# Histograms Section
with st.expander("Histograms"):
    st.subheader("Histograms")
    st.markdown("Exploring the distribution of each variable.")
    try:
        fig, axes = plt.subplots(2, 2, figsize=(10, 10))
        sns.histplot(df['SepalLengthCm'], bins=7, ax=axes[0, 0], color="skyblue")
        axes[0, 0].set_title("Sepal Length")

        sns.histplot(df['SepalWidthCm'], bins=5, ax=axes[0, 1], color="lightgreen")
        axes[0, 1].set_title("Sepal Width")

        sns.histplot(df['PetalLengthCm'], bins=6, ax=axes[1, 0], color="orange")
        axes[1, 0].set_title("Petal Length")

        sns.histplot(df['PetalWidthCm'], bins=6, ax=axes[1, 1], color="purple")
        axes[1, 1].set_title("Petal Width")

        plt.tight_layout()
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error rendering histograms: {e}")

# KDE Plots Section
with st.expander("KDE Plots"):
    st.subheader("KDE Plots")
    st.markdown("Visualizing the smoothed density distributions for each variable.")
    def kde_plot(column):
        try:
            plot = sns.FacetGrid(df, hue="Species", height=4)
            plot.map(sns.kdeplot, column, fill=True, alpha=0.5).add_legend()
            st.pyplot(plot.fig)
        except Exception as e:
            st.error(f"Error rendering KDE plot for {column}: {e}")

    kde_plot("SepalLengthCm")
    kde_plot("SepalWidthCm")
    kde_plot("PetalLengthCm")
    kde_plot("PetalWidthCm")

# Correlation Matrix Section
with st.expander("Correlation Matrix"):
    st.subheader("Correlation Matrix")
    st.markdown("Checking linear relationships between numerical variables.")
    try:
        corr_matrix = df.select_dtypes(include=['number']).drop(['Id'], axis=1).corr(method='pearson')
        st.write(corr_matrix)

        # Heatmap
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error rendering correlation matrix or heatmap: {e}")

# Box Plots Section
with st.expander("Box Plots"):
    st.subheader("Box Plots")
    st.markdown("Box plots highlight distributions and outliers for each variable across species.")
    def box_plot(y):
        try:
            fig, ax = plt.subplots()
            sns.boxplot(x="Species", y=y, data=df, ax=ax)
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error rendering box plot for {y}: {e}")

    box_plot('SepalLengthCm')
    box_plot('SepalWidthCm')
    box_plot('PetalLengthCm')
    box_plot('PetalWidthCm')

st.success("EDA code by Ann Naser Nabil!")
