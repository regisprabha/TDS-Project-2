# Automated Dataset Analysis

## Dataset Overview

### Basic Information

None

### First Few Rows

|    |   book_id |   goodreads_book_id |   best_book_id |   work_id |   books_count |      isbn |      isbn13 | authors                     |   original_publication_year | original_title                           | title                                                    | language_code   |   average_rating |   ratings_count |   work_ratings_count |   work_text_reviews_count |   ratings_1 |   ratings_2 |   ratings_3 |   ratings_4 |   ratings_5 | image_url                                                  | small_image_url                                            |
|---:|----------:|--------------------:|---------------:|----------:|--------------:|----------:|------------:|:----------------------------|----------------------------:|:-----------------------------------------|:---------------------------------------------------------|:----------------|-----------------:|----------------:|---------------------:|--------------------------:|------------:|------------:|------------:|------------:|------------:|:-----------------------------------------------------------|:-----------------------------------------------------------|
|  0 |         1 |             2767052 |        2767052 |   2792775 |           272 | 439023483 | 9.78044e+12 | Suzanne Collins             |                        2008 | The Hunger Games                         | The Hunger Games (The Hunger Games, #1)                  | eng             |             4.34 |         4780653 |              4942365 |                    155254 |       66715 |      127936 |      560092 |     1481305 |     2706317 | https://images.gr-assets.com/books/1447303603m/2767052.jpg | https://images.gr-assets.com/books/1447303603s/2767052.jpg |
|  1 |         2 |                   3 |              3 |   4640799 |           491 | 439554934 | 9.78044e+12 | J.K. Rowling, Mary GrandPré |                        1997 | Harry Potter and the Philosopher's Stone | Harry Potter and the Sorcerer's Stone (Harry Potter, #1) | eng             |             4.44 |         4602479 |              4800065 |                     75867 |       75504 |      101676 |      455024 |     1156318 |     3011543 | https://images.gr-assets.com/books/1474154022m/3.jpg       | https://images.gr-assets.com/books/1474154022s/3.jpg       |
|  2 |         3 |               41865 |          41865 |   3212258 |           226 | 316015849 | 9.78032e+12 | Stephenie Meyer             |                        2005 | Twilight                                 | Twilight (Twilight, #1)                                  | en-US           |             3.57 |         3866839 |              3916824 |                     95009 |      456191 |      436802 |      793319 |      875073 |     1355439 | https://images.gr-assets.com/books/1361039443m/41865.jpg   | https://images.gr-assets.com/books/1361039443s/41865.jpg   |
|  3 |         4 |                2657 |           2657 |   3275794 |           487 |  61120081 | 9.78006e+12 | Harper Lee                  |                        1960 | To Kill a Mockingbird                    | To Kill a Mockingbird                                    | eng             |             4.25 |         3198671 |              3340896 |                     72586 |       60427 |      117415 |      446835 |     1001952 |     1714267 | https://images.gr-assets.com/books/1361975680m/2657.jpg    | https://images.gr-assets.com/books/1361975680s/2657.jpg    |
|  4 |         5 |                4671 |           4671 |    245494 |          1356 | 743273567 | 9.78074e+12 | F. Scott Fitzgerald         |                        1925 | The Great Gatsby                         | The Great Gatsby                                         | eng             |             3.89 |         2683664 |              2773745 |                     51992 |       86236 |      197621 |      606158 |      936012 |      947718 | https://images.gr-assets.com/books/1490528560m/4671.jpg    | https://images.gr-assets.com/books/1490528560s/4671.jpg    |

### Summary Statistics

|       |   book_id |   goodreads_book_id |     best_book_id |         work_id |   books_count |         isbn13 |   original_publication_year |   average_rating |    ratings_count |   work_ratings_count |   work_text_reviews_count |   ratings_1 |   ratings_2 |   ratings_3 |      ratings_4 |       ratings_5 |
|:------|----------:|--------------------:|-----------------:|----------------:|--------------:|---------------:|----------------------------:|-----------------:|-----------------:|---------------------:|--------------------------:|------------:|------------:|------------:|---------------:|----------------:|
| count |  10000    |     10000           |  10000           | 10000           |    10000      | 9415           |                    9979     |     10000        |  10000           |      10000           |                  10000    |    10000    |    10000    |     10000   | 10000          | 10000           |
| mean  |   5000.5  |         5.2647e+06  |      5.47121e+06 |     8.64618e+06 |       75.7127 |    9.75504e+12 |                    1981.99  |         4.00219  |  54001.2         |      59687.3         |                   2919.96 |     1345.04 |     3110.89 |     11475.9 | 19965.7        | 23789.8         |
| std   |   2886.9  |         7.57546e+06 |      7.82733e+06 |     1.17511e+07 |      170.471  |    4.42862e+11 |                     152.577 |         0.254427 | 157370           |     167804           |                   6124.38 |     6635.63 |     9717.12 |     28546.4 | 51447.4        | 79768.9         |
| min   |      1    |         1           |      1           |    87           |        1      |    1.9517e+08  |                   -1750     |         2.47     |   2716           |       5510           |                      3    |       11    |       30    |       323   |   750          |   754           |
| 25%   |   2500.75 |     46275.8         |  47911.8         |     1.00884e+06 |       23      |    9.78032e+12 |                    1990     |         3.85     |  13568.8         |      15438.8         |                    694    |      196    |      656    |      3112   |  5405.75       |  5334           |
| 50%   |   5000.5  |    394966           | 425124           |     2.71952e+06 |       40      |    9.78045e+12 |                    2004     |         4.02     |  21155.5         |      23832.5         |                   1402    |      391    |     1163    |      4894   |  8269.5        |  8836           |
| 75%   |   7500.25 |         9.38223e+06 |      9.63611e+06 |     1.45177e+07 |       67      |    9.78083e+12 |                    2011     |         4.18     |  41053.5         |      45915           |                   2744.25 |      885    |     2353.25 |      9287   | 16023.5        | 17304.5         |
| max   |  10000    |         3.32886e+07 |      3.55342e+07 |     5.63996e+07 |     3455      |    9.79001e+12 |                    2017     |         4.82     |      4.78065e+06 |          4.94236e+06 |                 155254    |   456191    |   436802    |    793319   |     1.4813e+06 |     3.01154e+06 |

### Missing Values

|                           |    0 |
|:--------------------------|-----:|
| isbn                      |  700 |
| isbn13                    |  585 |
| original_publication_year |   21 |
| original_title            |  585 |
| language_code             | 1084 |



## Analysis Summary

The dataset has been analyzed for statistical properties, correlations, and outliers. Key insights are visualized in the charts provided.

## Visualizations

![Chart 1](charts/correlation_heatmap.png)
![Chart 2](charts/boxplot_book_id.png)
![Chart 3](charts/boxplot_goodreads_book_id.png)
![Chart 4](charts/boxplot_best_book_id.png)