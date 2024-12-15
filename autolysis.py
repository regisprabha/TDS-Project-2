import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
CHARTS_DIR = "charts"
README_FILE = "README.md"

def generate_analysis_story(data_description, analysis_summary, charts):
    return (
        f"# Automated Dataset Analysis\n\n"
        f"## Dataset Overview\n\n{data_description}\n\n"
        f"## Analysis Summary\n\n{analysis_summary}\n\n"
        f"## Visualizations\n\n"
        + "\n".join([f"![Chart {i + 1}]({chart})" for i, chart in enumerate(charts)])
    )

def save_chart(fig, filename):
    if not os.path.exists(CHARTS_DIR):
        os.makedirs(CHARTS_DIR)
    filepath = os.path.join(CHARTS_DIR, filename)
    fig.savefig(filepath)
    plt.close(fig)
    return filepath

def main():
    if len(sys.argv) != 2:
        print("Usage: python autolysis.py <dataset.csv>")
        return

    # Load dataset
    csv_filename = sys.argv[1]
    try:
        data = pd.read_csv(csv_filename)
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return

    # Initial Dataset Analysis
    data_description = (
        f"### Basic Information\n\n{data.info()}\n\n"
        f"### First Few Rows\n\n{data.head().to_markdown()}\n\n"
        f"### Summary Statistics\n\n{data.describe().to_markdown()}\n\n"
    )

    # Check for missing values
    missing_values = data.isnull().sum()
    if missing_values.sum() > 0:
        data_description += (
            f"### Missing Values\n\n{missing_values[missing_values > 0].to_markdown()}\n\n"
        )
    else:
        data_description += "### Missing Values\n\nNo missing values detected.\n\n"

    # Generate Correlation Heatmap
    if not data.select_dtypes(include=['number']).empty:
        corr_chart = "correlation_heatmap.png"
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        corr_chart_path = save_chart(fig, corr_chart)
    else:
        corr_chart_path = None

    # Outliers Analysis (Boxplots)
    numerical_cols = data.select_dtypes(include=['number']).columns
    outliers_charts = []
    for col in numerical_cols:
        fig, ax = plt.subplots()
        sns.boxplot(data=data[col], ax=ax)
        chart_path = save_chart(fig, f"boxplot_{col}.png")
        outliers_charts.append(chart_path)

    # Simulated LLM Analysis (Placeholder)
    analysis_summary = (
        "The dataset has been analyzed for statistical properties, correlations, and outliers. "
        "Key insights are visualized in the charts provided."
    )

    # Generate Story
    charts_paths = [corr_chart_path] + outliers_charts[:3] if corr_chart_path else outliers_charts[:3]
    story = generate_analysis_story(data_description, analysis_summary, charts_paths)

    # Save Story to README.md
    with open(README_FILE, "w") as readme_file:
        readme_file.write(story)

    print(f"Analysis complete. See {README_FILE} and {CHARTS_DIR}/ for details.")

if __name__ == "__main__":
    main()
