# Preface
The prerpocessing phase is formed of several steps, first data extraction, we extract related tables from MIMIC-III, these tables are not just randomaly picked but rather finalzied on extensive literature review and from the related features that correpsonds to the features in the MIMIC-III's related tables, once the initial dataset is formed we apply set of exclusion criterias for 3 reasons:

1) To reduce the size of the dataset
2) To focus on specific type of patients
3) To open up possibilites for more refined and reduced feature set

Afterwards the excluded dataset is forwarded to a preprocessing pipeline where missing values, outliers and other preprocessing steps are applied. The outcome of the preprocessing pipeline is the well refined dataset that is ready to be used for modelling.

# Data Extraction Phase
For forming the initial dataset different tables are created that each of them have different context
1) Patient table
2) First day measurements
3) Comorbidities 

# Exclusion Phase

# Preprocessing Phase

# Mapping for Supervised / Semi Supervised Approach
1. **Gradient Boosting Machines (GBMs)**: GBMs are powerful ensemble learning methods that combine multiple weak models (typically decision trees) to create a strong predictive model. GBMs have shown excellent performance in various tasks and can handle both numerical and categorical features. You can train a GBM model to predict ICU levels based on the features in your dataset, including the mortality rate intervals.

2. **Random Forest**: Random Forest is another ensemble learning method that combines multiple decision trees. It is known for its ability to handle high-dimensional data and provide robust predictions. Random Forest models can be trained to predict ICU levels, taking into account the mortality rate intervals and other features.

3. **XGBoost or LightGBM**: XGBoost and LightGBM are gradient boosting frameworks known for their efficiency and performance. They are highly optimized and offer additional features and tuning options compared to traditional GBMs. You can use these frameworks to build a model that predicts ICU levels, considering the mortality rate intervals and other features.

4. **Ordinal Regression**: Ordinal regression is a technique specifically designed for predicting ordinal variables, such as ICU levels. It models the relationship between the predictors (including mortality rate) and the ordinal outcome. This approach takes into account the inherent ordering of the ICU levels and can provide more nuanced predictions compared to simple intervals.

5. **Proportional Odds Model**: The proportional odds model is a type of ordinal regression that assumes a proportional odds assumption, meaning the odds of being in a higher ICU level versus a lower one are constant across all values of the predictors. This model can be used to map the mortality rate to ICU levels while considering the ordinal nature of the outcome variable.

6. **Support Vector Machines (SVM)**: SVMs can be used for multi-class classification tasks like mapping the mortality rate to ICU levels. SVMs are powerful models that can handle non-linear relationships. You can train an SVM model to predict ICU levels based on the mortality rate and other features in your dataset.

7. **Threshold-based Binning**: In this method, you define specific thresholds or bins for the continuous variable. The continuous values falling within each bin are assigned corresponding categorical labels or levels. For example, you can divide the range of the variable into intervals and assign labels such as "low," "medium," and "high" based on the bin in which the value falls.

8. **Decision Trees**: Decision trees can be used to map a continuous variable to a categorical variable. The decision tree algorithm automatically learns thresholds and splits based on the values of the continuous variable to form distinct categories. Each leaf node of the tree represents a categorical label. The decision tree can be trained to predict the corresponding categorical label for a given continuous value.

9. **Optimal Binning**: Optimal binning techniques aim to find the best cut-off points or bins for the continuous variable that maximize the predictive power or information gain for the categorical outcome. These techniques use statistical measures such as chi-square, Gini index, or information gain to determine the optimal splits. This approach ensures that the bins are chosen based on their predictive value for the categorical variable.

10. **Weight of Evidence (WoE)**: Weight of Evidence is a technique commonly used in credit scoring and risk modeling. It transforms a continuous variable into categorical bins by calculating the WoE value for each bin. WoE represents the predictive power of each bin with respect to the categorical outcome. The WoE values are then used as features in a classification model to predict the categorical variable.

11. **CatBoost Encoding**: CatBoost encoding is a technique used in gradient boosting algorithms. It maps a continuous variable to a categorical variable by encoding each category with a target statistic (e.g., mean, median) calculated over the target variable. This encoding can help capture the relationship between the continuous variable and the categorical outcome, enabling a classification model to learn from the transformed feature.