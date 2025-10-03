🍽️ Amazon Food Review NLP Analysis & Parsing Comparison<br>
📊 Overview<br>
This repository contains an extensive Natural Language Processing (NLP) analysis of the Amazon Fine Food Review dataset. The project focuses on performing comprehensive Exploratory Data Analysis (EDA), robust text preprocessing, and a crucial comparative study of different parsing algorithms.

The core analysis, code, and visualizations are detailed within the Amazon_FoodReview.ipynb Jupyter notebook.

✨ Key Features & Results<br>
The project successfully executes the following tasks and yields a key finding on parsing efficiency:

Data Handling: Loading and preprocessing the first 10,000 rows of the Amazon Fine Food Review dataset.

Exploratory Data Analysis (EDA): Comprehensive analysis and visualization of review scores, helpfulness, and key text features.

Part-of-Speech (POS) Tagging: Implementation and display of POS tags on sample text.

Parsing Implementation:

Visualization of Dependency Parsing (using an efficient approach like the Arc-Eager algorithm, likely via spaCy).

Visualization of Statistical Parsing (using an approach like the PCFG model, likely via Stanford Parser/NLTK).

Efficiency Comparison: Detailed comparison of the Time Complexity and Runtime of the two parsing approaches.

Key Finding: Arc-Eager Dependency Parsing (O(n) complexity) was found to be approximately 121 times faster than PCFG Statistical Parsing (O(n<sup>3</sup>)) complexity) for the tested sentences.

🛠️ Setup and Installation<br>
To run the analysis locally, you will need Python 3.x and the necessary NLP libraries.

Install Dependencies:<br>
The notebook relies on common libraries for NLP and data science. You will likely need:

pandas, numpy, matplotlib, seaborn

nltk (for tokenization, POS, and potentially PCFG tools)

spacy (for efficient dependency parsing)
