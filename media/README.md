# Automated Dataset Analysis

## Dataset Overview

### Basic Information

None

### First Few Rows

|    | date      | language   | type   | title       | by                            |   overall |   quality |   repeatability |
|---:|:----------|:-----------|:-------|:------------|:------------------------------|----------:|----------:|----------------:|
|  0 | 15-Nov-24 | Tamil      | movie  | Meiyazhagan | Arvind Swamy, Karthi          |         4 |         5 |               1 |
|  1 | 10-Nov-24 | Tamil      | movie  | Vettaiyan   | Rajnikanth, Fahad Fazil       |         2 |         2 |               1 |
|  2 | 09-Nov-24 | Tamil      | movie  | Amaran      | Siva Karthikeyan, Sai Pallavi |         4 |         4 |               1 |
|  3 | 11-Oct-24 | Telugu     | movie  | Kushi       | Vijay Devarakonda, Samantha   |         3 |         3 |               1 |
|  4 | 05-Oct-24 | Tamil      | movie  | GOAT        | Vijay                         |         3 |         3 |               1 |

### Summary Statistics

|       |    overall |     quality |   repeatability |
|:------|-----------:|------------:|----------------:|
| count | 2652       | 2652        |     2652        |
| mean  |    3.04751 |    3.20928  |        1.49472  |
| std   |    0.76218 |    0.796743 |        0.598289 |
| min   |    1       |    1        |        1        |
| 25%   |    3       |    3        |        1        |
| 50%   |    3       |    3        |        1        |
| 75%   |    3       |    4        |        2        |
| max   |    5       |    5        |        3        |

### Missing Values

|      |   0 |
|:-----|----:|
| date |  99 |
| by   | 262 |



## Analysis Summary

The dataset has been analyzed for statistical properties, correlations, and outliers. Key insights are visualized in the charts provided.

## Visualizations

![Chart 1](charts/correlation_heatmap.png)
![Chart 2](charts/boxplot_overall.png)
![Chart 3](charts/boxplot_quality.png)
![Chart 4](charts/boxplot_repeatability.png)