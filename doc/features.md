# Foreword
This document provides extracted potential features that can be utilized in training process. It includes three different country UK, USA and Turkey, initially starting with Turkey.

> Note that some of the regulations do have conditions that mostly depends on the severity of condition described in the points

# Turkey
For turkey there are three different ICU type each of the ICU have different levels, maximum number of level is 5 as in NICU (neonatal). Each extracted featuer is described under levels of each ICU types. 

## Adult Intensive Care
Patient who are at the age of 18 or greater this statistic also can be extracted from the MIMIC-III on the <span style="color:#91ff00">DEMOGRAPHICS</span>

### ICU Level 1
-  <span style="color:#91ff00">Tek organ yetmezligi → SAPS</span> <br>
Condition : diyaliz gerektirmeyen, akut veya kronik bobrek yetmezligi, kalp yetmezligi, karaciger yetmezligi (hafif seyreden)

-  <span style="color:#91ff00">2. veya 3. seviyeden cikarilan henuz taburcu edilemeyecek durumdaki hastalar → PREVIOUS_LEVEL or DISCHARGE_PROB</span> <br> 
Condition : There is no previous level stored in the patient data in MIMIC-III so we have to manually detect patients that are lowered to below levels. Using the mapped ICU levels and same patients different ICU stays we can assign PREVIOUS_LEVEL depending on the date of the admission for detecting the antecedence

- <span style="color:#91ff00">Cerrahi sonrasi yakin takip → PROCEDUREEVENTS_MV</span> <br>
Condition : We can by directly include the feature that contains procedure events to training set without any precalculations

- <span style="color:#91ff00"> → </span>