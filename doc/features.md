# Foreword

This document provides extracted potential features that can be utilized in training process. It includes three different country UK, USA and Turkey, initially starting with Turkey.

> Note that some of the regulations do have conditions that mostly depends on the severity of condition described in the points

Each country have different number of levels and ICU types but mostly in the basis the structure is similar. The feature extraction from these regulations are limited into the possible smallest number to minimize interpretation, re-definition, and possible missing features in MIMIC-III to avoid formulating calculations that would most probably introduce bias to the modal.

# Turkey

For turkey there are three different ICU type each of the ICU have different levels, maximum number of level is 5 as in NICU (neonatal). Each extracted featuer is described under levels of each ICU types.

## Extracted Features by ICU Level and MIMIC-III Equivalency 

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

## Adult Intensive Care (AdICU)

Patient who are at the age of 18 or greater this statistic also can be extracted from the MIMIC-III on the

<b><u>Type of organ failure or medical condition:</b></u> This could be extracted from the diagnosis codes (ICD-9 or ICD-10 codes) in the MIMIC-III dataset. MIMIC-III contains both primary and secondary diagnosis codes for each patient.

<b><u>Vital signs:</b></u> MIMIC-III contains a wealth of information on vital signs, including blood pressure, heart rate, respiratory rate, oxygen saturation, and more. These values are often recorded at regular intervals during a patient's ICU stay and could be extracted from the continuous vital sign monitoring data.

<b><u>Laboratory values:</b></u> MIMIC-III contains laboratory values for a wide range of tests, including electrolytes, liver function tests, kidney function tests, coagulation profile, and more. These values are often recorded at regular intervals during a patient's ICU stay and could be extracted from the laboratory data.

<b><u>Use of invasive monitoring or mechanical ventilation:</b></u> This information is available in the MIMIC-III database and could be extracted from the electronic medical record. MIMIC-III contains detailed information on the type and duration of invasive monitoring (such as central venous catheters, arterial lines, and pulmonary artery catheters) as well as the use of mechanical ventilation.

<b><u>Presence of sepsis or other infections:</b></u> MIMIC-III contains information on the presence of infections and sepsis, as well as the type of infection and the organism responsible.

<b><u>Need for isolation precautions:</b></u> This information is available in the MIMIC-III database and could be extracted from the electronic medical record.

<b><u>Glasgow coma score:</b></u> MIMIC-III contains information on the Glasgow coma score, which is typically recorded on admission to the ICU.

<b><u>History of recent surgery or trauma:</b></u> This information is available in the MIMIC-III database and could be extracted from the electronic medical record.

<b><u>Pregnancy status and complications:</b></u> MIMIC-III contains information on pregnancy status and complications, as well as the use of medications and procedures related to pregnancy.

<b><u>Type of poisoning or overdose:</b></u> This information is available in the MIMIC-III database and could be extracted from the electronic medical record.

<b><u>Age and gender:</b></u> MIMIC-III contains demographic information for each patient, including age and gender.

<b><u>Medical history and comorbidities:</b></u> MIMIC-III contains information on medical history and comorbidities, including chronic conditions and prior hospitalizations. This information is typically recorded in the electronic medical record.


## Neonatal Intensive Care (NICU)

There is no need to utilize logical computation such as AdICU, there is already a feature that provide information whether the patient is NICU or not.

## Pediatric Intensic Care (PICU)

Similar to NICU there is no need to utilize logical computation such as AdICU. Note that levels do not start from 1. Level 1 is assumed as a vard instead of ICU.

# United Kingdom

# United States
