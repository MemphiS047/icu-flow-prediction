SET search_path to mimiciii;
WITH icd9_agg AS (
    SELECT icustay_detail.subject_id,
        STRING_AGG(diagnoses_icd.icd9_code, ',') AS aggregated_icd9_code
    FROM icustay_detail
        JOIN diagnoses_icd ON icustay_detail.subject_id = diagnoses_icd.subject_id
        JOIN rrt_first_day ON icustay_detail.subject_id = rrt_first_day.subject_id
    GROUP BY icustay_detail.subject_id
)
SELECT *
FROM icustay_detail t1
    JOIN icd9_agg t2 ON t1.subject_id = t2.subject_id
    JOIN vitals_first_day t4 ON t1.icustay_id = t4.icustay_id
    JOIN sofa t5 ON t1.icustay_id = t5.icustay_id
    JOIN saps t6 ON t1.icustay_id = t6.icustay_id
    JOIN sirs t7 ON t1.icustay_id = t7.icustay_id
    JOIN ventilation_first_day t8 ON t1.icustay_id = t8.icustay_id
    JOIN rrt_first_day t10 ON t1.icustay_id = t10.icustay_id
    JOIN urine_output_first_day t11 ON t1.icustay_id = t11.icustay_id
    JOIN labs_first_day t12 ON t1.icustay_id = t12.icustay_id
WHERE first_icu_stay = true
    and t1.first_hosp_stay = true;
-- ### Weight is problematic since it hasy only icuadm_id
-- JOIN weight_first_day t9 ON t1.icustay_id=t9.icustay_id
-- ### Tables that could be added
-- ### admissions table could be added as well since it includes NEW BORN or EMERGANCT etc.
-- ### angus table includes organ disfunction, infection etc.
-- ### apsiii table also includes good features
-- ### all first day measurements
-- ### elixhauser could also be inclided
-- ### include most of the scores martin, lods, meld, mlods, oasis, qsofa, saps, sapsii, sirs, sofa, 
-- JOIN base tables, such as