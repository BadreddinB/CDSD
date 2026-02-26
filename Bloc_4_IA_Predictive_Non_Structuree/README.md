# SMS Spam Detection using Deep Learning

## Business Problem

AT&T processes millions of SMS messages every day.

A growing proportion of these messages are unsolicited or malicious (spam), negatively impacting:

- User experience

- Trust in the network

- Customer retention

- Support workload

Manual filtering methods do not scale to this volume.

The objective of this project is therefore to design an automated deep learning pipeline capable of classifying SMS messages as:

- Spam

- Ham (legitimate message)

based solely on their textual content.

This system could ultimately support real-time filtering at network level.

## Analytical Objective

The problem is formulated as a binary text classification task on non-structured data.

Given an SMS message:

Predict whether the message should be filtered as spam before reaching the end user.

A key business constraint is the high cost of false negatives:

-> A spam message incorrectly classified as legitimate directly reaches the user.

Therefore, model selection focuses on:

- Spam Recall
rather than overall accuracy.

## AI Pipeline Architecture

Raw SMS Messages
        ↓
Text Cleaning
(lowercase / punctuation removal)
        ↓
Tokenization
(Keras Tokenizer)
        ↓
Sequence Padding
(maxlen = 100)
        ↓
Label Encoding
(ham = 0 / spam = 1)
        ↓
Class Imbalance Handling
(GAN-based augmentation)
        ↓
Model Training
Baseline LSTM
GloVe + LSTM
DistilBERT
        ↓
Model Evaluation
(F1 / Recall)
        ↓
Final Model Selection
(Business-driven metric)

## Dataset

| Property        | Value              |
| --------------- | ------------------ |
| Dataset size    | 5,572 SMS messages |
| Spam messages   | ~13%               |
| Ham messages    | ~87%               |
| Missing values  | None               |
| Target variable | Spam / Ham         |

The dataset is strongly imbalanced, requiring specific treatment during training.

## Text Preprocessing

A custom cleaning pipeline was applied:

- Lowercasing

- Removal of punctuation and special characters

- Stopwords removal (NLTK)

- Porter stemming

⚠️ A lighter preprocessing pipeline (without stemming) was used for transfer learning models in order to preserve the linguistic structure expected by pretrained embeddings.

## Model Development

### Baseline Model — LSTM

A sequential neural network including:

- Trainable embedding layer

- LSTM layer

- Sigmoid output

Results:

- Accuracy: 98%

- Spam Recall: 89%

- Spam F1-score: 0.94

This provides a strong baseline but remains sensitive to class imbalance.

### Handling Class Imbalance — GAN Augmentation

A Generative Adversarial Network (GAN) was trained on spam messages to generate:

-> 500 synthetic spam samples

These generated messages were added to the training dataset in order to:

- Improve class representation

- Increase model exposure to spam patterns

- Reduce bias towards the majority class

### Transfer Learning — GloVe + LSTM

Pretrained GloVe word embeddings (100-dimensional) were integrated as a frozen embedding layer.

Results:

- Accuracy: 97%

- Spam Recall: 86%

- Spam F1-score: 0.92

Static embeddings show limitations on short informal text messages.

### Transfer Learning — DistilBERT

A fine-tuned DistilBERT transformer model was trained on the GAN-augmented dataset.

Unlike GloVe, DistilBERT generates contextual embeddings where each word representation depends on its surrounding context.

Results:

- Accuracy: 98%

- Spam Recall: 99%

- Spam F1-score: 0.96

249 out of 252 spam messages were correctly identified.

### Model Comparison

| Model         | Accuracy | Spam Recall | Spam F1 |
| ------------- | -------- | ----------- | ------- |
| Baseline LSTM | 98%      | 89%         | 0.94    |
| GloVe + LSTM  | 97%      | 86%         | 0.92    |
| DistilBERT    | 98%      | **99%**     | 0.96    |

-> DistilBERT was selected as the final model

due to its superior spam recall — the most critical business metric.

## Reproducibility

### Clone the repository

git clone https://github.com/BadreddinB/CDSD.git
cd CDSD/Bloc_4_IA_Predictive_Non_Structuree/AT&T

### Install dependencies

pip install -r requirements.txt

### Download required resources

Due to GitHub file size limitations (>100MB), the pretrained GloVe embeddings are not included in this repository.

Download them manually from the official Stanford NLP repository:

👉 https://nlp.stanford.edu/projects/glove/

Download:

glove.6B.zip

Then extract the following files into the same directory as the notebook:

glove.6B.50d.txt
glove.6B.100d.txt
glove.6B.200d.txt
glove.6B.300d.txt

Make sure the project structure matches:

AT&T/
│
├── AT&T.ipynb
├── spam.csv
├── glove.6B.50d.txt
├── glove.6B.100d.txt
├── glove.6B.200d.txt
├── glove.6B.300d.txt
└── README.md

⚠️The notebook loads these files using relative paths.
Moving them to another directory may prevent the code from executing correctly.

### Dataset location
spam.csv

## Run the notebook

AT&T.ipynb

GloVe embeddings and DistilBERT weights will be automatically downloaded during first execution.

## Project Structure on GIT Hub

Bloc_4_IA_Predictive_Non_Structuree/
│
├── AT&T.ipynb
├── spam.csv
└── README.md


