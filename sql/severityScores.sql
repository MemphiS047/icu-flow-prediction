SET search_path TO mimiciii;
CREATE TABLE refined.scores AS (
    SELECT sapsii.subject_id,
        sapsii.hadm_id,
        sapsii.icustay_id,
        sapsii.sapsii,
        sapsii.sapsii_prob,
        sapsii.age_score,
        sapsii.hr_score,
        sapsii.sysbp_score,
        sapsii.temp_score,
        sapsii.pao2fio2_score,
        sapsii.uo_score,
        sapsii.bun_score,
        sapsii.wbc_score,
        sapsii.potassium_score,
        sapsii.sodium_score,
        sapsii.bicarbonate_score,
        sapsii.bilirubin_score,
        sapsii.gcs_score,
        sapsii.comorbidity_score,
        sapsii.admissiontype_score,
        sirs.sirs,
        sirs.heartrate_score,
        sirs.resp_score,
        sofa.sofa,
        sofa.respiration,
        sofa.coagulation,
        sofa.liver,
        sofa.cardiovascular,
        sofa.cns,
        sofa.renal,
        angus.infection,
        angus.explicit_sepsis,
        angus.organ_dysfunction,
        angus.mech_vent,
        angus.angus,
        explicit.severe_sepsis,
        explicit.septic_shock,
        explicit.sepsis,
        martin.organ_failure,
        martin.respiratory,
        martin.hepatic,
        martin.hematologic,
        martin.metabolic,
        martin.neurologic,
        apsiii.apsiii,
        apsiii.apsiii_prob,
        apsiii.meanbp_score,
        apsiii.resprate_score,
        apsiii.pao2_aado2_score,
        apsiii.hematocrit_score,
        apsiii.creatinine_score,
        apsiii.albumin_score,
        apsiii.glucose_score,
        apsiii.acidbase_score,
        lods.lods,
        lods.pulmonary,
        mlods.mlods,
        oasis.icustay_age_group,
        oasis.hospital_expire_flag,
        oasis.icustay_expire_flag,
        oasis.oasis,
        oasis.oasis_prob,
        oasis.age,
        oasis.preiculos,
        oasis.preiculos_score,
        oasis.gcs,
        oasis.heartrate,
        oasis.meanbp,
        oasis.resprate,
        oasis.temp,
        oasis.urineoutput,
        oasis.urineoutput_score,
        oasis.mechvent,
        oasis.mechvent_score,
        oasis.electivesurgery,
        oasis.electivesurgery_score,
        qsofa.qsofa,
        saps.saps,
        saps.vent_score,
        meld.meld_initial,
        meld.meld,
        meld.rrt,
        meld.creatinine_max,
        meld.bilirubin_max,
        meld.inr_max,
        meld.sodium_min
    FROM sapsii
        JOIN sirs ON sirs.hadm_id = sapsii.hadm_id
        JOIN sofa ON sofa.hadm_id = sapsii.hadm_id
        JOIN angus ON angus.hadm_id = sapsii.hadm_id
        JOIN explicit ON explicit.hadm_id = sapsii.hadm_id
        JOIN martin ON martin.hadm_id = sapsii.hadm_id
        JOIN apsiii ON apsiii.hadm_id = sapsii.hadm_id
        JOIN lods ON lods.hadm_id = sapsii.hadm_id
        JOIN mlods ON mlods.icustay_id = sapsii.icustay_id
        JOIN oasis ON oasis.hadm_id = sapsii.hadm_id
        JOIN qsofa ON qsofa.hadm_id = sapsii.hadm_id
        JOIN saps ON saps.hadm_id = sapsii.hadm_id
        JOIN meld ON meld.hadm_id = sapsii.hadm_id
);
-- CREATE TABLE comorbidity_score AS (
--     SELECT
--     FROM elixhauser_ahrq_v37
--         JOIN elixhauser_ahrq_v37_no_drg ON elixhauser_ahrq_v37_no_drg.hadm_id = elixhauser_ahrq_v37.hadm_id
--         JOIN elixhauser_quan ON elixhauser_quan.hadm_id = elixhauser_ahrq_v37.hadm_id
--         JOIN elixhauser_score_ahrq ON elixhauser_score_ahrq.hadm_id = elixhauser_ahrq_v37.hadm_id
--         JOIN elixhauser_score_quan ON elixhauser_score_quan.hadm_id = elixhauser_ahrq_v37.hadm_id
-- )