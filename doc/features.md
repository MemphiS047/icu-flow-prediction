# Foreword

This document provides extracted potential features that can be utilized in training process. It includes three different country UK, USA and Turkey, initially starting with Turkey.

> Note that some of the regulations do have conditions that mostly depends on the severity of condition described in the points

Each country have different number of levels and ICU types but mostly in the basis the structure is similar. The feature extraction from these regulations are limited into the possible smallest number to minimize interpretation, re-definition, and possible missing features in MIMIC-III to avoid formulating calculations that would most probably introduce bias to the modal.

# Turkey

For turkey there are three different ICU type each of the ICU have different levels, maximum number of level is 5 as in NICU (neonatal). Each extracted featuer is described under levels of each ICU types.


## Adult Intensive Care (AdICU)
Patient who are at the age of 18 or greater this statistic also can be extracted from the MIMIC-III on the

### Extraction by Level and MIMIC-III Equivalency
ICU Level 1:

- Patients with uncomplicated single-organ failures (excluding respiratory failure) can be identified from the diagnosis and procedure codes in the ICU-stay table.
- Patients who require close follow-up after surgery can be identified from the surgical procedures recorded in the procedure events table.
- Patients with uncomplicated psychiatric and neurological emergencies can be identified from the diagnosis codes in the diagnosis table.

ICU Level 2:

- Patients who require short-term observation and vital support can be identified from the vital sign measurements recorded in the chart events table.
- Patients who need urgent treatment for single organ failure can be identified from the diagnosis and procedure codes in the ICU-stay table.
- Patients who require respiratory support can be identified from the ventilator settings recorded in the chart events table.
- Patients who require invasive monitoring can be identified from the procedure events table.

ICU Level 3:

- Patients who have developed multiple organ failure can be identified from the organ failure scores recorded in the sofa table.
- Patients who require long-term observation and vital support can be identified from the length of stay in the ICU-stay table.
- Patients with acute problems such as severe sepsis, septic shock, ARDS, and severe preeclampsia/eclampsia can be identified from the diagnosis and procedure codes in the ICU-stay table.
- Patients with bleeding that cannot be controlled or requires massive transfusion can be identified from the transfusion events recorded in the procedure events table.
- Patients with severe central nervous system pathology and surgery can be identified from the diagnosis and procedure codes in the ICU-stay table.

## Neonatal Intensive Care (NICU)

There is no need to utilize logical computation such as AdICU, there is already a feature that provide information whether the patient is NICU or not.

## Pediatric Intensic Care (PICU)

Similar to NICU there is no need to utilize logical computation such as AdICU. Note that levels do not start from 1. Level 1 is assumed as a vard instead of ICU.

# United Kingdom

# United States
