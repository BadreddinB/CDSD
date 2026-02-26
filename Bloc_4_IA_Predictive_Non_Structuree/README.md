# SMS Spam Detection using Deep Learning

## Business Context

Telecommunication operators such as AT&T process millions of SMS messages every day. Among them, an increasing proportion consists of unsolicited or potentially malicious messages (spam), which negatively impacts user experience and reduces trust in communication services.

Manual moderation approaches are no longer scalable given the volume of exchanged messages.

Developing an automated system capable of classifying SMS messages based solely on their textual content would allow AT&T to:

- Protect users from unwanted or fraudulent communications

- Improve customer satisfaction

- Reduce manual moderation workload

- Enable real-time filtering at network level

## Project Objective

The objective of this project is to design a deep learning pipeline capable of automatically classifying SMS messages as either:

- Spam — unsolicited or malicious message

- Ham — legitimate message

This task falls under predictive analysis on unstructured textual data, where the final model should generalize effectively to unseen messages.

## Dataset

The dataset contains 5,572 SMS messages, each labeled as either spam or ham.

The class distribution is imbalanced:

- 87% legitimate messages

- 13% spam messages

No missing values were observed in the dataset.

## Modeling Pipeline

### Baseline Deep Learning Model — LSTM

A first LSTM-based neural network was implemented as a baseline model.

Text messages were:

- Lowercased

- Cleaned from punctuation and special characters

- Tokenized

- Stemmed

- Converted into padded numerical sequences

The model architecture includes:

- An embedding layer

- An LSTM layer

- A sigmoid output layer

Although the model achieved high overall accuracy (~98%), the spam recall remained limited (89%), meaning that some spam messages were still incorrectly classified as legitimate.

From a business perspective, these false negatives represent spam messages reaching end users.

### Data Augmentation using GAN

In order to address class imbalance, a Generative Adversarial Network (GAN) was implemented to synthetically generate additional spam messages.

The GAN was trained exclusively on spam sequences in order to enrich the minority class.

This approach allows the construction of an augmented training dataset without relying on simple oversampling techniques.

The enriched dataset improves the model’s exposure to spam-related patterns during training.

### Transfer Learning — GloVe Embeddings

A second LSTM model was trained using pretrained GloVe word embeddings.

A lighter preprocessing pipeline was applied to preserve linguistic structure required by pretrained embeddings.

Despite improving semantic representation of words, the model achieved:

- 97% overall accuracy

- 86% spam recall

Static embeddings showed limitations in capturing semantic variability in short SMS messages.

### Contextual Transfer Learning — DistilBERT

Finally, a transformer-based architecture (DistilBERT) was fine-tuned on the GAN-augmented dataset.

Unlike static embeddings such as GloVe, DistilBERT generates contextual representations where each word’s meaning depends on its surrounding context.

This model achieved:

- 98% accuracy

- 99% spam recall

Out of 252 spam messages in the test set, 249 were correctly identified, with only 3 missed instances.

## Model Comparison

| Model                        | Accuracy | Spam Recall | Spam F1-Score |
| ---------------------------- | -------- | ----------- | ------------- |
| Baseline LSTM                | 98%      | 89%         | 0.94          |
| GloVe + LSTM (GAN-Augmented) | 97%      | 86%         | 0.92          |
| DistilBERT (GAN-Augmented)   | 98%      | 99%         | 0.96          |

DistilBERT provides the best performance in terms of spam detection, which is the most business-critical metric in this context.

## Business Impact

Improving spam recall directly reduces the number of unsolicited or fraudulent messages reaching end users.

At network scale, even a small improvement in spam detection performance may significantly:

- Enhance customer experience

- Reduce exposure to phishing attempts

- Limit user complaints

- Decrease downstream moderation workload

By integrating contextual deep learning models such as DistilBERT into SMS filtering pipelines, telecommunication providers can improve service reliability while maintaining scalable automated content moderation.

## Repository Structure

Bloc_4_IA_Predictive_Non_Structuree/
│
├── AT&T.ipynb
├── spam.csv
├── glove.6B.50d.txt*
├── glove.6B.100d.txt*
├── glove.6B.200d.txt*
├── glove.6B.300d.txt*
└── README.md

* GloVe embedding files are required for the transfer learning section and may not be included in the GitHub repository due to file size limitations.

* How to download Glove:

* Download them manually from the official Stanford NLP repository -> https://nlp.stanford.edu/projects/glove/

  glove.6B.zip

Then extract the following files into the same directory as the notebook:

glove.6B.50d.txt
glove.6B.100d.txt
glove.6B.200d.txt
glove.6B.300d.txt

## Reproductibility

### Clone the repository:

git clone https://github.com/BadreddinB/CDSD.git

### Navigate to the project folder:

cd CDSD/Bloc_4_IA_Predictive_Non_Structuree

### Place the following files in the same directory as the notebook:

- spam.csv

- glove.6B.100d.txt

### Run the notebook:

jupyter notebook AT&T.ipynb

DistilBERT weights will be automatically downloaded on first run.
