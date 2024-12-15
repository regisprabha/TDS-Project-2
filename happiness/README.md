# Automated Dataset Analysis

## Dataset Overview

### Basic Information

None

### First Few Rows

|    | Country name   |   year |   Life Ladder |   Log GDP per capita |   Social support |   Healthy life expectancy at birth |   Freedom to make life choices |   Generosity |   Perceptions of corruption |   Positive affect |   Negative affect |
|---:|:---------------|-------:|--------------:|---------------------:|-----------------:|-----------------------------------:|-------------------------------:|-------------:|----------------------------:|------------------:|------------------:|
|  0 | Afghanistan    |   2008 |         3.724 |                7.35  |            0.451 |                               50.5 |                          0.718 |        0.164 |                       0.882 |             0.414 |             0.258 |
|  1 | Afghanistan    |   2009 |         4.402 |                7.509 |            0.552 |                               50.8 |                          0.679 |        0.187 |                       0.85  |             0.481 |             0.237 |
|  2 | Afghanistan    |   2010 |         4.758 |                7.614 |            0.539 |                               51.1 |                          0.6   |        0.118 |                       0.707 |             0.517 |             0.275 |
|  3 | Afghanistan    |   2011 |         3.832 |                7.581 |            0.521 |                               51.4 |                          0.496 |        0.16  |                       0.731 |             0.48  |             0.267 |
|  4 | Afghanistan    |   2012 |         3.783 |                7.661 |            0.521 |                               51.7 |                          0.531 |        0.234 |                       0.776 |             0.614 |             0.268 |

### Summary Statistics

|       |       year |   Life Ladder |   Log GDP per capita |   Social support |   Healthy life expectancy at birth |   Freedom to make life choices |     Generosity |   Perceptions of corruption |   Positive affect |   Negative affect |
|:------|-----------:|--------------:|---------------------:|-----------------:|-----------------------------------:|-------------------------------:|---------------:|----------------------------:|------------------:|------------------:|
| count | 2363       |    2363       |           2335       |      2350        |                         2300       |                    2327        | 2282           |                 2238        |       2339        |      2347         |
| mean  | 2014.76    |       5.48357 |              9.39967 |         0.809369 |                           63.4018  |                       0.750282 |    9.77213e-05 |                    0.743971 |          0.651882 |         0.273151  |
| std   |    5.05944 |       1.12552 |              1.15207 |         0.121212 |                            6.84264 |                       0.139357 |    0.161388    |                    0.184865 |          0.10624  |         0.0871311 |
| min   | 2005       |       1.281   |              5.527   |         0.228    |                            6.72    |                       0.228    |   -0.34        |                    0.035    |          0.179    |         0.083     |
| 25%   | 2011       |       4.647   |              8.5065  |         0.744    |                           59.195   |                       0.661    |   -0.112       |                    0.687    |          0.572    |         0.209     |
| 50%   | 2015       |       5.449   |              9.503   |         0.8345   |                           65.1     |                       0.771    |   -0.022       |                    0.7985   |          0.663    |         0.262     |
| 75%   | 2019       |       6.3235  |             10.3925  |         0.904    |                           68.5525  |                       0.862    |    0.09375     |                    0.86775  |          0.737    |         0.326     |
| max   | 2023       |       8.019   |             11.676   |         0.987    |                           74.6     |                       0.985    |    0.7         |                    0.983    |          0.884    |         0.705     |

### Missing Values

|                                  |   0 |
|:---------------------------------|----:|
| Log GDP per capita               |  28 |
| Social support                   |  13 |
| Healthy life expectancy at birth |  63 |
| Freedom to make life choices     |  36 |
| Generosity                       |  81 |
| Perceptions of corruption        | 125 |
| Positive affect                  |  24 |
| Negative affect                  |  16 |



## Analysis Summary

The dataset has been analyzed for statistical properties, correlations, and outliers. Key insights are visualized in the charts provided.

## Visualizations

![Chart 1](charts/correlation_heatmap.png)
![Chart 2](charts/boxplot_year.png)
![Chart 3](charts/boxplot_Life Ladder.png)
![Chart 4](charts/boxplot_Log GDP per capita.png)