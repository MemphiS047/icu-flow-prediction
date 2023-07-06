SET
    search_path TO mimiciii;

CREATE VIEW refined.base_dataset AS
SELECT
    first_day.hadm_id,
    first_day.subject_id,
    patients.first_wardid,
    patients.last_wardid,
    patients.intime,
    patients.outtime,
    patients.los,
    first_day.icustay_id,
    patients.dod,
    patients.los_hospital,
    patients.admission_age,
    patients.hospital_expire_flag,
    patients.hospstay_seq,
    patients.first_hosp_stay,
    patients.los_icu,
    patients.icustay_seq,
    patients.first_icu_stay,
    patients.dob,
    patients.dod_hosp,
    patients.dod_ssn,
    patients.expire_flag,
    patients.row_id,
    patients.admittime,
    patients.dischtime,
    patients.deathtime,
    patients.edregtime,
    patients.edouttime,
    patients.has_chartevents_data,
    patients.gender,
    patients.insurance,
    patients.language,
    patients.religion,
    patients.marital_status,
    patients.ethnicity_grouped,
    patients.diagnosis,
    patients.ethnicity,
    patients.dbsource,
    patients.first_careunit,
    patients.last_careunit,
    patients.admission_type,
    patients.admission_location,
    patients.discharge_location,
    first_day.mingcs,
    first_day.gcsmotor,
    first_day.gcsverbal,
    first_day.gcseyes,
    first_day.endotrachflag,
    first_day.height,
    first_day.height_chart,
    first_day.height_echo,
    first_day.urineoutput,
    first_day.vent,
    first_day.heartrate_min,
    first_day.heartrate_max,
    first_day.heartrate_mean,
    first_day.sysbp_min,
    first_day.sysbp_max,
    first_day.sysbp_mean,
    first_day.diasbp_min,
    first_day.diasbp_max,
    first_day.diasbp_mean,
    first_day.meanbp_min,
    first_day.meanbp_max,
    first_day.meanbp_mean,
    first_day.resprate_min,
    first_day.resprate_max,
    first_day.resprate_mean,
    first_day.tempc_min,
    first_day.tempc_max,
    first_day.tempc_mean,
    first_day.spo2_min,
    first_day.spo2_max,
    first_day.spo2_mean,
    first_day.glucose_min,
    first_day.glucose_max,
    first_day.glucose_mean,
    first_day.weight,
    first_day.weight_admit,
    first_day.weight_daily,
    first_day.weight_echoinhosp,
    first_day.weight_echoprehosp,
    first_day.aniongap_min,
    first_day.aniongap_max,
    first_day.albumin_min,
    first_day.albumin_max,
    first_day.bands_min,
    first_day.bands_max,
    first_day.bicarbonate_min,
    first_day.bicarbonate_max,
    first_day.bilirubin_min,
    first_day.bilirubin_max,
    first_day.creatinine_min,
    first_day.creatinine_max,
    first_day.chloride_min,
    first_day.chloride_max,
    first_day.hematocrit_min,
    first_day.hematocrit_max,
    first_day.hemoglobin_min,
    first_day.hemoglobin_max,
    first_day.lactate_min,
    first_day.lactate_max,
    first_day.platelet_min,
    first_day.platelet_max,
    first_day.potassium_min,
    first_day.potassium_max,
    first_day.ptt_min,
    first_day.ptt_max,
    first_day.inr_min,
    first_day.inr_max,
    first_day.pt_min,
    first_day.pt_max,
    first_day.sodium_min,
    first_day.sodium_max,
    first_day.bun_min,
    first_day.bun_max,
    first_day.wbc_min,
    first_day.wbc_max,
    first_day.rrt
FROM
    patients
    JOIN first_day ON first_day.icustay_id = patients.icustay_id