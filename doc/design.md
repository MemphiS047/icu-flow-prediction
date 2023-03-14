# Things that can be added
1.  We can extract additional features from the regulations of UK, US and TR.
2.  If there is such data on the MIMIC-III, using those we can generate target features 
    and then train with the resulted dataset
3.  Comparison between models could be improved. For example, using 4 model or higher 
    we can draw a clear distinction between the models with the score values
4.  We can draw a conclusion from benefits of turning the problem into classification, 
    also need a review on that
5.  Distinction could be made between PICU, NICU and other ICU types as well and 
    benefits of it could be explained in the paper

# Extracted features from Turkey ICU regulations
1. Adult
   1. **ICU Level 1** - Following features are extracted from the "1. Seviye" section in adult.docx:
      1. <span style="color:#0EAEEE">Akut organ yetmezligi</span> *(diyaliz gerektirmeyen bobrek yetmezligi, stabil kronik bobrek yetzmeligi, kalp yetmezligi, hafif seyreden karaciger yetmezligi, transfuzyon gerektirmeyen kanamalar)* <span style="color:#ff6d59">SOFA score - scoring of organ failure </span>
      2. <span style="color:#ffdd63">Yaşamsal fonksiyonların aniden bozulma olasılığı bulunan ve sürekli gözlemi gereken hastalar,</span>
      3. <span style="color:#0EAEEE">2. veya 3. Seviye yoğun bakım servislerinden çıkarılan henüz taburcu edilemeyecek durumdaki hastalar</span> *(Could be detected via additional analysis on some of the continus measurmenets and categorical features on MIMIC-III)* <span style="color:#ff6d59">We can create a **DISCHARGE_SCORE** depending on some probability and add additional features such as **PREVIOUS_LEVEL** to indicate the previous level of the patient</span> 
      4. <span style="color:#0EAEEE">Cerrahi sonrası yakın takibi gereken hastalar</span> *(Could be extracted via vital signs, lab measurments etc. that are also continues not limited with the first day measurmenets)* <span style="color:#ff6d59">**PROCEDUREEVENTS_MV** shows the procedural events it might be related to surgical events of the patients</span>
      5. <span style="color:#0EAEEE">Psikiyatrik, nörolojik acil vakalar</span> *(There could be some categorical feauters realted to psychoatric features)* <span style="color:#ff6d59">**DIAGNOSES_ICD**, **NOTEEVENTS** and **PROCEDUREEVENTS_MV** could include related diognsis type</span>
   2. **ICU Level 2** - Below is for level 2 ICU features that are more critical and severly ill cases
      1. <span style="color:#0EAEEE">Patients who discharged from ICU level 3</span> *(Could add labels or another feautres that indicates patients who discharged form level 3 and increase the weight of the patients depending on these cases)* <span style="color:#ff6d59">**PREVIOUS_LEVEL** to indicate the previous level of the patient</span>
      2. <span style="color:#0EAEEE">Tek organ yetmezligi acil</span> *(Could create a severity score from few of the measurments and depending on the severity score we can determine if the organ failure is critical or not)* <span style="color:#ff6d59">**SOFA** score might be useful here again</span>
      3. <span style="color:#ffdd63">Patients who will enter surgical operations *(Also there might be categorical features that realtes to, if patient had seen a surgical operation or not)*</span> 
      4. <span style="color:#0EAEEE">Hayati tehtit edici zehirlenmeler</span> *(Again maybe some categorical values or blood measurmenets would be used to label patient as critically posined state)* <span style="color:#ff6d59">Information such as drug overdoses and toxic ingestion can be found in several tables such as **DIAGNOSIS_ICD**, **LABEVENTS**, **PRESCRIPTIONS** and **NOTEEVENTS** </span>
      5. <span style="color:#0EAEEE">Gebelik durumu</span> *(Depending on the pregnenacy categorical varible we can add weight to our predicitve modal)*
      6. <span style="color:#0EAEEE">Hemotoraks, ampiyem,  ağır malnütrisyon ?</span> *(Did not now what these are but might be included in MIMIC-III as categorical variable or lab measurmenets etc.)*
      7. <span style="color:#0EAEEE">Features about nervous system</span> *(There are features related to nervous system diseases that affect wheter patient should be inside level 1 or level 2)*
   3. **ICU Level 3** - Rest of the features here are for critically ill patients which is the lowest ratio among the three levels.
      1. <span style="color:#0EAEEE">Multiple organ failure</span> *(Either from predefined categorical features or previously defined or created score measurmenets depending on a treshold we can determine wheter the patient have multiple organ failures)*
      2. <span style="color:#0EAEEE">HELLP, agir sepsis, septik sok, ARDS</span> *(Could find related critically severe dissases on the database)*
      3. <span style="color:#0EAEEE">Izolasyon gerektiren hastalar</span>  <span style="color:#ff6d59"> There is a categorical feature related name **ISOLATION FLAG**</span>
      4. <span style="color:#0EAEEE">Glasgow coma score is 8 or lesser</span> <span style="color:#ff6d59"> There is definitly a feature ther about **GCS_SCORE** </span>
      5. <span style="color:#0EAEEE">Kalp cerrahisi</span> <span style="color:#ff6d59">**PROCEDUREEVENTS_MV** - there might be a information about the this feature in the procedure events</span>



<blockquote class="callout callout_default">
  <h3>🚧 Warning</h3>
  <p>It is important to note that the information related to poisoning in MIMIC-III may not be comprehensive or completely accurate, as it is dependent on how the data was collected and recorded in the electronic health record. Therefore, careful consideration should be given to how this information is used in research studies, and any limitations or potential biases in the data should be taken into account.</p>
</blockquote>

# Preprocessing
To train the model I have to have a finalized dataset that do not include repetitive patient data. Most of  the features that I need are ordered on the above by type and level <br>
First and foremost obtain a data analysis of the dataset obtained on the finalized merger of over 100+ tables probably. 