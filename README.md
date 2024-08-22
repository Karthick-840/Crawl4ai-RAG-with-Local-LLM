# Sentiment Analysis using Machine Learning

This project performs sentiment analysis on tweets using various machine learning models. The code processes raw tweet text, trains models to classify sentiment, and provides a pipeline for making predictions.

## Table of Contents

- [Installation](#installation)
- [Dataset](#dataset)
- [Preprocessing](#preprocessing)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Pipeline](#pipeline)
- [Prediction](#prediction)
- [Usage](#usage)

## Installation

1. Clone the repository.
2. Install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Download necessary NLTK data:
    ```python
    import nltk
    nltk.download('omw-1.4')
    nltk.download('wordnet')
    ```

## Dataset

The dataset used is a preprocessed version of the Sentiment140 dataset, containing tweets labeled as either positive or negative.

- **Columns**: `["sentiment", "ids", "date", "flag", "user", "text"]`
- **Encoding**: `ISO-8859-1`
- **Location**: The dataset should be in a CSV file located at `C:\Users\gksme\PycharmProjects\Local_Git_Projects\profile\big_investor_pics\archive\training.1600000.processed.noemoticon.csv`.

## Preprocessing

The code preprocesses the tweet text by:

1. Replacing URLs with a placeholder.
2. Replacing user mentions with a placeholder.
3. Handling emojis by replacing them with corresponding text representations.
4. Removing non-alphabetical characters.
5. Reducing sequences of three or more repeating characters to two.
6. Lemmatizing words to their base form.
7. Removing stopwords from the text.

## Model Training

The following machine learning models are trained on the processed tweet text:

1. **Bernoulli Naive Bayes** (`BernoulliNB`)
2. **Linear Support Vector Classifier** (`LinearSVC`)
3. **Logistic Regression** (`LogisticRegression`)

The models are trained using `TfidfVectorizer` to convert the text data into numerical features.

## Evaluation

The models are evaluated on a test set, and the following metrics are used:

- **Precision**
- **Recall**
- **F1-score**
- **Accuracy**

The `model_evaluate()` function prints a classification report for each model.

## Pipeline

The code creates a machine learning pipeline using `sklearn.pipeline.Pipeline`, combining the `TfidfVectorizer` and the trained `BernoulliNB` model. The pipeline is saved as a pickle file (`pipeline.pickle`) for easy reuse.

## Prediction

A `predict()` function is provided to classify new text inputs. The function takes a list of text strings, preprocesses them, and returns the predicted sentiment.

- **Input**: List of text strings.
- **Output**: List of tuples containing the original text, predicted label (0 or 1), and sentiment (`Negative` or `Positive`).

## Usage

To use the sentiment analysis pipeline:

1. Load the pipeline:
    ```python
    with open('pipeline.pickle', 'rb') as f:
        loaded_pipe = pickle.load(f)
    ```

2. Predict sentiment for new text:
    ```python
    text = ["I hate twitter", "May the Force be with you.", "Mr. Stark, I don't feel so good"]
    predictions = predict(loaded_pipe, text)
    print(predictions)
    ```

The output will show the sentiment analysis for each input text.

---

This project demonstrates how to preprocess text data, train machine learning models, and make sentiment predictions using a pipeline approach. The trained models and pipeline are saved for easy reuse in real-world applications.
