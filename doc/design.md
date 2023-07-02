# Foreword
The design is conformed of several explanations on the things that are aim to be done in the project the whole project is shaped with this document. Planning is done using Trello/Jira. For more information on things that have been done and things that will be done check out the following Trello/Jira [link](https://trello.com/b/x9LWes30/project-management-current-mybs)

# Flow of the Development
The flow of the development is divided into building the ML models, developing backend for easy to deploy with different type of technologies that are used by the hospital systems (an intermediary system) and additional frontend for developed on request of the doctors: Analysis - Preprocessing - Modelling - Evaluation - Hearbeat backend (model deployment - architecture decisions) - Frontend (Case Study)


# Additional Included Value
1.  We can extract additional features from the regulations of UK, US and TR.
2.  If there is such data on the MIMIC-III, using those we can generate target features 
    and then train with the resulted dataset
3.  Comparison between models could be improved. For example, using 4 model or higher 
    we can draw a clear distinction between the models with the score values
4.  We can draw a conclusion from benefits of turning the problem into classification, 
    also need a review on that
5.  Distinction could be made between PICU, NICU and other ICU types as well and 
    benefits of it could be explained in the paper
6.  MIMIC-III does not include any target variable for use (ICU level) instead of using supervised learning by
    labeling the data given the mortality rates with a specific ranging for each level, we can use either unsupervised or semi-supervised learning. Furthermore the mortality rate is one of the many factors in the ICU level admission of patients (ther are other features such as age, organ failures, etc.) we can use state of the art unsupervised learning methodologies to construct a model for clustering pateints with the given features
7.  Check out the semi-supervised learning methodologies for the ICU level admission of patients and majority voting
    withgradient boosting algorithms 

<blockquote>
  <h3>🚧 Warning</h3>
  <p>It is important to note that the information related to poisoning in MIMIC-III may not be comprehensive or completely accurate, as it is dependent on how the data was collected and recorded in the electronic health record. Therefore, careful consideration should be given to how this information is used in research studies, and any limitations or potential biases in the data should be taken into account.</p>
</blockquote>

# Analysis
Problem: In Turkey there is a huge imbalance in the admission to ICU such that doctors need to obey regulations indicated by the government and according to those regulations doctors need to place patients into related ICU levels on the other side doctors sometimes couldn't obey there rules hence occurrence of imbalance also causing financial problems for government insurant payments for both hospital and patients. There is a clear distinction between ICU criticality levels however sometimes number of levels might need to be increased or decreased, furthermore reporting and documenting is inefficient since doctors use their own predefined templates hence there is no systematic and automated report generation mechanism exists (in specific hospital A due to usage of these provided hospital management software by third parties)

Solution: We introduce a supportive machine learning model that will help doctors in the grey areas and will be flexible for future increase in the ICU levels (such that the model should be flexible for number of ICU level variations), for the report generation and more suitable ICU management solutions (for that specific hospital A) we propose a software system that could be generalized to rest of the ICU wards named "heartbeat" where it includes a set of choices refined for the related regulations this software could be generalized in terms of the UI elements

Research Questions:

1. How can machine learning models be applied to assist doctors in the decision-making process for ICU admissions, particularly in cases where the regulations are unclear or flexible?
2. What features and data sources can be used to develop a machine learning model that accurately predicts the appropriate ICU level for patients?
3. How can the machine learning model be designed to accommodate potential variations in the number of ICU levels, allowing for future scalability and flexibility?
4. What is the impact of implementing the proposed machine learning model on achieving a more balanced distribution of patients across ICU levels in Turkey?
5. What are the financial implications and cost savings associated with implementing the machine learning model in terms of government insurance payments for hospitals and patients?
6. How can the reporting and documentation process in hospitals, specifically in Hospital A, be optimized through the development of an automated and systematic report generation mechanism?
7. What are the key requirements and functionalities of the "heartbeat" software system that can effectively generate reports and manage ICU admissions according to the specific regulations in Hospital A?
8. How can the "heartbeat" software system be designed to be flexible and scalable, allowing for its potential application and generalization to other ICU wards?
9. What are the user interface (UI) elements and design considerations that need to be incorporated into the "heartbeat" software system to ensure usability and efficiency for doctors and healthcare professionals?

Additional Advanced Methodologies or Solutions:

1. Advanced machine learning algorithms: Explore advanced algorithms such as deep learning models (e.g., convolutional neural networks, recurrent neural networks) or ensemble methods to improve the accuracy and robustness of the ICU level prediction model.
2. Explainable AI: Develop interpretable machine learning models that provide explanations or justifications for the decisions made, enhancing trust and transparency in the system.
3. Real-time monitoring: Implement a real-time monitoring system that continuously tracks ICU occupancy and patient conditions, providing timely alerts and recommendations to doctors for appropriate ICU level assignments.
4. Reinforcement learning: Investigate the use of reinforcement learning techniques to optimize ICU management policies and dynamically adapt to changing regulations or conditions.
5. Natural language processing (NLP): Utilize NLP techniques to automate the extraction of relevant information from doctors' predefined templates and generate standardized reports, improving efficiency and consistency in reporting.
6. Data integration and interoperability: Develop solutions to integrate and exchange data seamlessly between different hospital management software systems, ensuring efficient data flow for report generation and ICU management.
7. Decision support system: Build a comprehensive decision support system that incorporates clinical guidelines, patient-specific data, and machine learning predictions to assist doctors in making informed decisions regarding ICU admissions.
8. User-centered design: Conduct user research and involve healthcare professionals in the design process of the "heartbeat" software system, ensuring that it meets their specific needs and workflows.
9. Cloud-based architecture: Implement a cloud-based infrastructure for the "heartbeat" software system, enabling scalability, accessibility, and efficient data storage and processing.

## Feature Extraction from Regulations
We extracted features from the regulations of UK, US and TR, with text mining techniques, table below shows the extacted features

# Preprocessing
The prerpocessing phase is formed of several steps, first data extraction, we extract related tables from MIMIC-III, these tables are not just randomaly picked but rather finalzied on extensive literature review and from the related features that correpsonds to the features in the MIMIC-III's related tables, once the initial dataset is formed we apply set of exclusion criterias for 3 reasons:

1) To reduce the size of the dataset
2) To focus on specific type of patients
3) To open up possibilites for more refined and reduced feature set

Afterwards the excluded dataset is forwarded to a preprocessing pipeline where missing values, outliers and other preprocessing steps are applied. The outcome of the preprocessing pipeline is the well refined dataset that is ready to be used for modelling.

## Data Extraction Phase
Forming the intial datasets or tables we followed similar practice used in MIMIC-Extract paper

1) Patient data
2) First stay data
3) Severity scores
4) Medication and treatment data
5) Features only included in extracted data from regulations
   
## Exclusion Phase

## Preprocessing Phase
1. **Ordinal Regression**: Ordinal regression is a technique specifically designed for predicting ordinal variables, such as ICU levels. It models the relationship between the predictors (including mortality rate) and the ordinal outcome. This approach takes into account the inherent ordering of the ICU levels and can provide more nuanced predictions compared to simple intervals.

2. **Proportional Odds Model**: The proportional odds model is a type of ordinal regression that assumes a proportional odds assumption, meaning the odds of being in a higher ICU level versus a lower one are constant across all values of the predictors. This model can be used to map the mortality rate to ICU levels while considering the ordinal nature of the outcome variable.

3. **Support Vector Machines (SVM)**: SVMs can be used for multi-class classification tasks like mapping the mortality rate to ICU levels. SVMs are powerful models that can handle non-linear relationships. You can train an SVM model to predict ICU levels based on the mortality rate and other features in your dataset.

4. **Threshold-based Binning**: In this method, you define specific thresholds or bins for the continuous variable. The continuous values falling within each bin are assigned corresponding categorical labels or levels. For example, you can divide the range of the variable into intervals and assign labels such as "low," "medium," and "high" based on the bin in which the value falls.

5. **Decision Trees**: Decision trees can be used to map a continuous variable to a categorical variable. The decision tree algorithm automatically learns thresholds and splits based on the values of the continuous variable to form distinct categories. Each leaf node of the tree represents a categorical label. The decision tree can be trained to predict the corresponding categorical label for a given continuous value.

6. **Optimal Binning**: Optimal binning techniques aim to find the best cut-off points or bins for the continuous variable that maximize the predictive power or information gain for the categorical outcome. These techniques use statistical measures such as chi-square, Gini index, or information gain to determine the optimal splits. This approach ensures that the bins are chosen based on their predictive value for the categorical variable.

7.  **Weight of Evidence (WoE)**: Weight of Evidence is a technique commonly used in credit scoring and risk modeling. It transforms a continuous variable into categorical bins by calculating the WoE value for each bin. WoE represents the predictive power of each bin with respect to the categorical outcome. The WoE values are then used as features in a classification model to predict the categorical variable.

8.  **CatBoost Encoding**: CatBoost encoding is a technique used in gradient boosting algorithms. It maps a continuous variable to a categorical variable by encoding each category with a target statistic (e.g., mean, median) calculated over the target variable. This encoding can help capture the relationship between the continuous variable and the categorical outcome, enabling a classification model to learn from the transformed feature.  
  
# Modelling
Depending on the approach there are few models that we can use these models are categorized with the approaches or more specifically learning techniques that we will seperate the problem into and at the same time dataset is also will change accordingly, for example for supervised there will be levels while for unsupervised there won't be any level columns

## Unsupervised Approach
Sure! Let's go through each of the models and techniques, providing a brief explanation of how they work:

1. **Autoencoders**:
Autoencoders are a type of neural network designed to learn efficient representations of input data. They consist of an encoder, which compresses the input data into a lower-dimensional latent representation, and a decoder, which reconstructs the original data from the latent space. By minimizing the reconstruction error, autoencoders learn meaningful features in the data and can be used for data compression, denoising, and anomaly detection.

2. **Variational Autoencoders (VAEs)**:
VAEs are a type of autoencoder that extends the idea by adding a probabilistic element to the latent space. Instead of learning a fixed representation, VAEs learn the parameters of a probability distribution in the latent space. This allows for the generation of new data points by sampling from the learned distribution, enabling the model to generate novel samples.

3. **Weiners VAE**:
I couldn't find any specific information on a model called "Weiners VAE" based on the link you provided. It's possible that it might not be a widely known or recognized model in the community. Please double-check the link or provide more context for me to assist further.

4. **t-SNE (t-Distributed Stochastic Neighbor Embedding)**:
t-SNE is a dimensionality reduction technique used to visualize high-dimensional data in a lower-dimensional space, typically two or three dimensions. It aims to preserve local pairwise similarities in the data by mapping nearby data points in the high-dimensional space to nearby points in the low-dimensional space. It is particularly useful for visualizing complex datasets and identifying patterns or clusters.

5. **UMAP (Uniform Manifold Approximation and Projection)**:
UMAP is another dimensionality reduction technique that preserves both local and global structure in the data. It constructs a high-dimensional fuzzy topological representation of the data and then optimizes a low-dimensional representation that approximates the high-dimensional topology. UMAP is known for its scalability and ability to preserve complex data structures.

6. **Self-Organizing Maps (SOMs)**:
SOMs are a type of unsupervised neural network that creates a low-dimensional representation (usually 2D) of high-dimensional input data. SOMs use competitive learning to iteratively adjust their weights to map similar input data points closer to each other on the 2D grid. They are often used for data visualization and clustering.

7. **Hierarchical Clustering**:
Hierarchical clustering is a method for grouping similar data points into clusters in a hierarchical structure. It starts with each data point as a separate cluster and then iteratively merges clusters based on their similarity until all data points belong to a single cluster or a specified number of clusters is reached. The result is a tree-like structure called a dendrogram, which can help visualize the hierarchy of clusters.

8. **Transfer Learning**:
Transfer learning is a technique in machine learning where a model pre-trained on one task is reused or adapted to perform a different but related task. By leveraging the knowledge gained from a larger or more general dataset, transfer learning can significantly speed up training and improve performance on smaller or specialized datasets.

9. **Modular Deep Learning**:
Modular deep learning involves building complex neural network architectures by connecting smaller pre-defined modules together. Each module performs a specific function, and by combining them, one can construct more intricate models with reusable components. This approach enhances modularity, flexibility, and interpretability of the overall model.

10. **Tensor Decomposition**:
Tensor decomposition is a mathematical technique used to factorize high-dimensional tensors (multidimensional arrays) into a combination of lower-dimensional tensors. Different tensor decomposition methods provide different trade-offs between interpretability, efficiency, and approximation accuracy. Some common tensor decomposition methods include Canonical Polyadic Decomposition (CPD), Tensor Train Decomposition (TTD), and Tensor Tucker Decomposition.

11. **Gaussian Mixture Models (GMMs)**:
GMMs are probabilistic models used for clustering and density estimation. They assume that the data points are generated from a mixture of Gaussian distributions, where each component represents a cluster. GMMs estimate the parameters of the Gaussian components (mean, covariance) and the mixture weights to represent the underlying data distribution.

12. **Ensemble Learning Models (GBM, XGBoost, LightGBM, CatBoost, Random Forest, etc.)**:
Ensemble learning combines multiple individual models (base learners) to create a stronger and more robust predictive model. Each base learner might be trained on different subsets of the data or with different algorithms. Gradient Boosting Machines (GBM), XGBoost, LightGBM, CatBoost, and Random Forest are examples of ensemble learning algorithms widely used for classification and regression tasks. They differ in their underlying algorithms and optimization techniques but share the idea of combining multiple models for improved performance.

## Supervised Approach
1. **Ordinal Regression**: Ordinal regression is a technique specifically designed for predicting ordinal variables, such as ICU levels. It models the relationship between the predictors (including mortality rate) and the ordinal outcome. This approach takes into account the inherent ordering of the ICU levels and can provide more nuanced predictions compared to simple intervals.

# Evaluation

# Heartbeat Backend

# Frontend (Case Study)