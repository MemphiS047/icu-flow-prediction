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