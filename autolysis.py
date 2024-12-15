import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import httpx
import chardet
import zipfile

# Constants
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
AIPROXY_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjMwMDI1MzNAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.qOQLdmOIYMA_bt9IZhXNlYUUI7cYkuaKgMUT6AVLJ4M"
CHARTS_DIR = "charts"
README_FILE = "README.md"

if not AIPROXY_TOKEN:
    print("Error: AIPROXY_TOKEN is not set.")
    exit(1)

def save_chart(fig, filename):
    """Save a Matplotlib figure as a file."""
    if not os.path.exists(CHARTS_DIR):
        os.makedirs(CHARTS_DIR)
    filepath = os.path.join(CHARTS_DIR, filename)
    fig.savefig(filepath)
    plt.close(fig)
    return filepath

def compress_results():
    """Compress the charts directory and README file for download."""
    with zipfile.ZipFile("results.zip", "w") as zipf:
        # Add charts directory
        for root, _, files in os.walk(CHARTS_DIR):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=os.path.join("charts", file))
        # Add README.md
        if os.path.exists(README_FILE):
            zipf.write(README_FILE, arcname=README_FILE)

def load_data(file_path):
    """Load CSV data with encoding detection."""
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    encoding = result['encoding']
    return pd.read_csv(file_path, encoding=encoding)

def analyze_data(df):
    """Perform basic data analysis."""
    numeric_df = df.select_dtypes(include=['number'])
    analysis = {
        'summary': df.describe(include='all').to_dict(),
        'missing_values': df.isnull().sum().to_dict()
    }
    return analysis

def visualize_data(df):
    """Generate and save three visualizations."""
    sns.set(style="whitegrid")
    numeric_df = df.select_dtypes(include=['number'])

    # Heatmap for correlation
    if not numeric_df.empty:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        save_chart(fig, "correlation_heatmap.png")

    # Two histograms for the first two numeric columns
    for column in numeric_df.columns[:2]:
        fig, ax = plt.subplots()
        sns.histplot(numeric_df[column].dropna(), kde=True, bins=20, ax=ax)
        ax.set_title(f"Distribution of {column}")
        save_chart(fig, f"{column}_distribution.png")

def generate_narrative(analysis):
    """Generate narrative using LLM."""
    headers = {
        'Authorization': f'Bearer {AIPROXY_TOKEN}',
        'Content-Type': 'application/json'
    }
    prompt = f"Provide a detailed analysis based on the following data summary: {analysis['summary']}"
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = httpx.post(API_URL, headers=headers, json=data, timeout=30.0)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
    except httpx.RequestError as e:
        print(f"Request error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return "Narrative generation failed due to an error."

def main():
    try:
        print("Please upload your dataset (CSV format).")
        file_path = input("Enter the path to your CSV file: ")
        data = load_data(file_path)

        analysis = analyze_data(data)

        visualize_data(data)

        narrative = generate_narrative(analysis)
        print("\nGenerated Narrative:")
        print(narrative)

        with open(README_FILE, "w") as readme_file:
            readme_file.write("# Automated Data Analysis\n\n")
            readme_file.write("## Summary Statistics\n\n")
            readme_file.write(str(analysis['summary']))
            readme_file.write("\n\n## Narrative\n\n")
            readme_file.write(narrative + "\n")

        compress_results()

        print(f"Analysis complete. Download results.zip for charts and the README file.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()