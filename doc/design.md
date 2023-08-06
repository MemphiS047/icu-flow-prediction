# Foreword
The design is conformed of several explanations on the things that are aim to be done in the project the whole project is shaped with this document. Planning is done using Trello/Jira. For more information on things that have been done and things that will be done check out the following [Trello/Jira](https://trello.com/b/x9LWes30/project-management-current-mybs)

# Flow of the Development
The flow of the development is divided into building the ML models, developing backend for easy to deploy with different type of technologies that are used by the hospital systems (an intermediary system) and additional frontend for developed on request of the doctors: Analysis - Preprocessing - Modelling - Evaluation - Hearbeat backend (model deployment - architecture decisions) - Frontend (Case Study - Optional)

# Analysis
**Problem**: There is a cost disparity between ICU payments and Insurance payments due to ineffective application of official ICU regulations. These regulations determine which ICU level will the patient be in. For insurance agency to pay for the ICU spending it is important to know why patient is admitted to that ICU and needs some grounding on that. Reporting and documenting is inefficient since doctors use their own predefined templates hence there is no systematic and automated report generation mechanism exists.

**Solution**: We introduce a supportive machine learning model that will help doctors in the grey areas also model should be flexible for variations in ICU regulatory changes in the future. For the report generation and more suitable ICU management solutions we propose a software system that could be generalized to rest of the ICU wards named "heartbeat" where it includes a set of choices refined for the related regulations this software could be generalized in terms of the UI elements, it should be user friendly and efficient for doctors and healthcare professionals but most importantly it should be "plug-and-run" style such that it should be easily configurable to different hospitals, and regulatory systems.

**Research Questions**
2. What features and data sources can be used to develop a machine learning model that accurately predicts the appropriate ICU level for patients?

3. How can the machine learning model be designed to accommodate potential variations in the number of ICU levels, allowing for future scalability and flexibility?

5. What are the financial implications and cost savings associated with implementing the machine learning model in terms of government insurance payments for hospitals and patients?

6. How can the reporting and documentation process in hospitals, specifically in Hospital A, be optimized through the development of an automated and systematic report generation mechanism?

7. What are the key requirements and functionalities of the "heartbeat" software system that can effectively generate reports and manage ICU admissions according to the specific regulations in Hospital A?

8. How can the "heartbeat" software system be designed to be flexible and scalable, allowing for its potential application and generalization to other ICU wards?

9. What are the user interface (UI) elements and design considerations that need to be incorporated into the "heartbeat" software system to ensure usability and efficiency for doctors and healthcare professionals?

**Additional Included Value**
1.  We can extract additional features from the regulations of UK, US and TR.

2.  If there is such data on the MIMIC-III, using those we can generate target features and then train with the resulted dataset

3.  Comparison between models could be improved. For example, using 4 model or higher we can draw a clear distinction between the models with the score values

4.  We can draw a conclusion from benefits of turning the problem into classification, also need a review on that

5.  Distinction could be made between PICU, NICU and other ICU types as well and benefits of it could be explained in the paper

6. We can some advacned explanability methodologies on the model to help with the insurance reporting

7. More aggregatable measurements such as ICD9 codes and elixhouser records

# Preprocessing
The prerpocessing phase is formed of several steps, first data extraction, we extract related tables from MIMIC-III, these tables are not just randomaly picked but rather finalzied on extensive literature review and from the related features that correpsonds to the features in the MIMIC-III's related tables, once the initial dataset is formed we apply set of exclusion criterias for 3 reasons:

1) To reduce the size of the dataset
2) To focus on specific type of patients
3) To open up possibilites for more refined and reduced feature set

Afterwards the excluded dataset is forwarded to a preprocessing pipeline where missing values, outliers and other preprocessing steps are applied. The outcome of the preprocessing pipeline is the well refined dataset that is ready to be used for modelling.

Preprocessing script could me more moduler with decorators such as we can plug different tasks or forward output to multiple tasks in the pipeline

Might include excluded or removed columns for further insigth in the dataset removed columns are as follows on preprocessing stages

- columns_to_remove = ['language', 'religion', 'diagnosis', 'ethnicity']
- columns_to_remove = ['height_echo', 'weight_echoinhosp', 'weight_echoprehosp', 'dbsource']
- columns_to_remove = ['intime', 'outtime', 'dod', 'admittime', 'dischtime', 'deathtime', 'edregtime', 'edouttime']

## Data Extraction Phase
Forming the intial datasets or tables we followed similar practice used in MIMIC-Extract paper

1) Patient data
2) First stay data
3) Severity scores
4) Medication and treatment data
5) Features only included in extracted data from regulations

- Tables that might be useful = ['martin', '']
   
## Exclusion Phase

## Preprocessing Pipeline

  
# Modelling
Depending on the approach there are few models that we can use these models are categorized with the approaches or more specifically learning techniques that we will seperate the problem into and at the same time dataset is also will change accordingly, for example for supervised there will be levels while for unsupervised there won't be any level columns

## Dimensionality Reduction
1. PCA (Principal Component Analysis): PCA is a widely used technique for dimensionality reduction. It projects the data onto a lower-dimensional subspace while preserving the maximum variance. It allows you to visualize the data in 2D by selecting the top two principal components.

2. t-SNE (t-distributed Stochastic Neighbor Embedding): t-SNE is a popular method for visualizing high-dimensional data in a two-dimensional space. It aims to preserve the local structure of the data, making it useful for identifying clusters and patterns.

3. UMAP (Uniform Manifold Approximation and Projection): UMAP is another dimensionality reduction technique that can be used for visualization. It aims to preserve both local and global structure, often providing better separation of clusters than t-SNE.

4. Autoencoders: Autoencoders are neural networks that can be used for unsupervised learning and dimensionality reduction. By training an autoencoder on your data and using the encoder part, you can obtain a lower-dimensional representation for visualization.

5. Spectral Embedding: Spectral embedding is a graph-based dimensionality reduction technique that uses the eigenvectors of a graph Laplacian to create a lower-dimensional representation of the data.

6. LLE (Locally Linear Embedding): LLE is a non-linear dimensionality reduction technique that preserves the local structure of the data. It can be used for visualization when the data has non-linear patterns.

7. Kernel PCA: Kernel PCA is an extension of PCA that uses a kernel function to map the data into a higher-dimensional space, allowing for non-linear dimensionality reduction.

8. MDS (Multi-Dimensional Scaling): MDS is a classical method that aims to preserve the distances between data points in the lower-dimensional space.

9. PCA + t-SNE (or UMAP) Combination: You can first use PCA to reduce the dimensionality to a manageable number of components (e.g., 10-20), and then apply t-SNE or UMAP for further reduction to 2D.

## Unsupervised Approach (Clustering)
Let's go through each of the models and techniques, providing a brief explanation of how they work:

1. **Self-Organizing Maps (SOMs)**:
SOMs are a type of unsupervised neural network that creates a low-dimensional representation (usually 2D) of high-dimensional input data. SOMs use competitive learning to iteratively adjust their weights to map similar input data points closer to each other on the 2D grid. They are often used for data visualization and clustering.

2. **Hierarchical Clustering**:
Hierarchical clustering is a method for grouping similar data points into clusters in a hierarchical structure. It starts with each data point as a separate cluster and then iteratively merges clusters based on their similarity until all data points belong to a single cluster or a specified number of clusters is reached. The result is a tree-like structure called a dendrogram, which can help visualize the hierarchy of clusters.

3. **Transfer Learning**:
Transfer learning is a technique in machine learning where a model pre-trained on one task is reused or adapted to perform a different but related task. By leveraging the knowledge gained from a larger or more general dataset, transfer learning can significantly speed up training and improve performance on smaller or specialized datasets.

4. **Modular Deep Learning**:
Modular deep learning involves building complex neural network architectures by connecting smaller pre-defined modules together. Each module performs a specific function, and by combining them, one can construct more intricate models with reusable components. This approach enhances modularity, flexibility, and interpretability of the overall model.

5. **Tensor Decomposition**:
Tensor decomposition is a mathematical technique used to factorize high-dimensional tensors (multidimensional arrays) into a combination of lower-dimensional tensors. Different tensor decomposition methods provide different trade-offs between interpretability, efficiency, and approximation accuracy. Some common tensor decomposition methods include Canonical Polyadic Decomposition (CPD), Tensor Train Decomposition (TTD), and Tensor Tucker Decomposition.

6. **Gaussian Mixture Models (GMMs)**:
GMMs are probabilistic models used for clustering and density estimation. They assume that the data points are generated from a mixture of Gaussian distributions, where each component represents a cluster. GMMs estimate the parameters of the Gaussian components (mean, covariance) and the mixture weights to represent the underlying data distribution.

7. **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**: DBSCAN is a density-based clustering algorithm that can discover clusters of varying shapes and sizes. It is particularly useful when dealing with noisy datasets and does not require specifying the number of clusters beforehand.

8. **HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise)**: HDBSCAN is an extension of DBSCAN that allows for varying density levels within clusters. It can automatically determine the number of clusters and handle clusters of different densities.

9. **Spectral Clustering**: Spectral Clustering uses the eigenvalues and eigenvectors of a similarity matrix to perform clustering. It can capture complex relationships between data points and works well when the data is not linearly separable.

10. **Birch (Balanced Iterative Reducing and Clustering using Hierarchies)**: Birch is a hierarchical clustering algorithm that can efficiently handle large datasets. It constructs a tree-based representation of the data to perform clustering.

## Supervised Approach (Classification)
1. **Ordinal Regression**: Ordinal regression is a technique specifically designed for predicting ordinal variables, such as ICU levels. It models the relationship between the predictors (including mortality rate) and the ordinal outcome. This approach takes into account the inherent ordering of the ICU levels and can provide more nuanced predictions compared to simple intervals.

2. **Ensemble Learning Models (GBM, XGBoost, LightGBM, CatBoost, Random Forest, etc.)**:
Ensemble learning combines multiple individual models (base learners) to create a stronger and more robust predictive model. Each base learner might be trained on different subsets of the data or with different algorithms. Gradient Boosting Machines (GBM), XGBoost, LightGBM, CatBoost, and Random Forest are examples of ensemble learning algorithms widely used for classification and regression tasks. They differ in their underlying algorithms and optimization techniques but share the idea of combining multiple models for improved performance.

3. **Voting Based Approach**

## Post-Modeling Phase
Once the clustering and supervised based approaches are done, first of all compare results of each of them within each category then comapre the clustring results with the labeling methodology, below steps could be followed

1. Calculate Mortality Rates: First, calculate the mortality rate for each patient in your dataset. The mortality rate is typically the percentage of patients who died in the ICU.

2. Assign Labels based on Mortality Rate: Define the ICU level labels based on mortality rates. For example, you can create different ICU levels such as "Low Risk," "Medium Risk," and "High Risk" based on certain mortality rate thresholds.

3. Map Patients to Clusters: Map each patient to the corresponding cluster obtained from your clustering algorithm. You should have cluster labels for each patient after performing the clustering.

4. Aggregate Mortality Rates within Clusters: Calculate the average or median mortality rate for each cluster. This will give you an idea of the overall mortality rate within each cluster.

5. Assign ICU Level Labels to Clusters: Based on the mortality rates calculated in step 4, assign the appropriate ICU level label to each cluster. For example, if a cluster has a high mortality rate, you can assign it the "High Risk" ICU level label.

6. Relate ICU Level Labels to Patients: Finally, relate the ICU level labels assigned to clusters back to the individual patients within those clusters. This will give you the ICU level prediction for each patient based on their clustering assignment and the corresponding mortality rates.

# Evaluation
## Evaluation Metrics
## Evaluation Techniques
## Evaluation Results

# Heartbeat Backend
Main objective of the heartbeat backend is to find solution for easly deployment of the system to any other hospital IT infrastructure assuming the hospital is not using standarized systems such as HL7, FHIR. To accomplish this we implemented a standarized module based middleware layer that provides easy adaptation to our system and translation of different soruces.

## Architecture
Below is the proposed architecture for the defined main objective of the Heartbeat Backend above, it consists of layers, .....
...
...
...
...
...
+-------------------------------------------------------------------------------------+
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
|                                                                                     |
+-------------------------------------------------------------------------------------+



## Proposed Standarized Middleware Framework Specifically Tailored for ICU Systems


# Frontend (Case Study)