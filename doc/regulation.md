# Feature Extraction from Regulations
We extracted features from the regulations of UK, US and TR, with text mining techniques, table below shows the extacted features

## Preprocessing of the Regulations
All the regulations are generally structured as levels that are divided into sections whereby each level contains different conditions, evaluations etc.

## Information Extraction Methods
Remove any irrelevant information or noise from the text, such as headers, footers, or formatting Tokenize the text into individual words or phrases. Perform stop-word removal to eliminate common words that do not carry much information. 

Named Entity Recognition (NER): Apply a pre-trained NER model to identify medical conditions, such as "late prematurity," "cleft palate/lip," or "maternal drug effect." This can help extract specific features related to these conditions. 

Sentiment Analysis: Perform sentiment analysis on the text to capture any sentiment or emotional context present in the regulations. This may provide additional insights or features for the model. 

Keyword Extraction: Use keyword extraction techniques (e.g., TF-IDF, RAKE) to identify important keywords or phrases in the text. These keywords can be used as features or indicators of specific conditions mentioned in the regulations.

Word Embeddings: Convert the text into word embeddings using techniques like Word2Vec or GloVe. Word embeddings capture semantic relationships between words and can provide useful contextual information for feature extraction.

Rule-based Feature Extraction: Create a set of rules based on the identified conditions in the regulations. For each rule, assign binary values (0 or 1) to indicate the presence or absence of the condition. These rules can be based on explicit mentions of conditions or patterns in the text.


Contextual Analysis: Analyze the context surrounding the conditions mentioned in the regulations. Look for additional information that may provide insights or features for the model. For example, identify the duration of parenteral glucose support for hypoglycemia or severity levels for respiratory distress.

Topic Modeling: Apply topic modeling techniques such as Latent Dirichlet Allocation (LDA) or Non-Negative Matrix Factorization (NMF) to identify latent topics in the text. These topics can serve as higher-level features that capture the underlying themes or concepts in the regulations.

Relation Extraction: Use relation extraction techniques to identify relationships between different conditions or entities mentioned in the text. This can help extract features that describe associations or dependencies between conditions.

Feature Selection: Once you have extracted a wide range of features, employ feature selection methods (e g., mutual information, chi-square test, LASSO regression) to identify the most relevant and informative features for your machine learning model.

Data Encoding: Encode the extracted features into a suitable format for training your machine learning model. This could involve creating binary indicators, one-hot encodings, or numerical representations based on the nature of the features.