
# Sentiment Analysis Project Documentation

## Overview
This project is an implementation of sentiment analysis using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analyzer from NLTK (Natural Language Toolkit) in Python. The project demonstrates how to analyze sentiment in various types of text data, such as product reviews, movie reviews, social media posts, news headlines, and customer service feedback.

## Requirements
- Python 3.x
- NLTK (Natural Language Toolkit)
- pandas
- matplotlib

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-project.git
   cd sentiment-analysis-project
   ```

2. Install the required dependencies:
   ```bash
   pip install nltk pandas matplotlib
   ```

3. Download the NLTK VADER lexicon:
   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

## Usage
1. Run the `sentiment_analysis.py` script:
   ```bash
   python sentiment_analysis.py
   ```

2. The script will analyze sentiment in the provided datasets and display the results in the console and as a histogram.

## Sample Output
```
Results for product_reviews.csv:
                                              text  compound    neg    neu    pos
0               This phone has an amazing battery!    0.6249  0.000  0.423  0.577
1               The camera quality is very poor.    -0.6249  0.483  0.517  0.000
2                         Great value for money.     0.6249  0.000  0.423  0.577
...

```

## Contributing
Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
