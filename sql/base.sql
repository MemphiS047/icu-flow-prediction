SET search_path TO mimiciii;

CREATE TABLE refined.base AS (
    SELECT admissions.row_id,
        admissions.subject_id,
        admissions.hadm_id,
        admissions.admittime,
        admissions.dischtime,
        admissions.deathtime,
        admissions.admission_type,
        admissions.admission_location,
        admissions.discharge_location,
        admissions.insurance,
        admissions.language,
        admissions.religion,
        admissions.marital_status,
        admissions.edregtime,
        admissions.edouttime,
        admissions.diagnosis,
        admissions.has_chartevents_data,
        icustays.dbsource,
        icustays.first_careunit,
        icustays.last_careunit,
        icustays.first_wardid,
        icustays.last_wardid,
        icustays.intime,
        icustays.outtime,
        icustays.los,
        icustay_detail.gender,
        icustay_detail.dod,
        icustay_detail.los_hospital,
        icustay_detail.admission_age,
        icustay_detail.ethnicity,
        icustay_detail.ethnicity_grouped,
        icustay_detail.hospital_expire_flag,
        icustay_detail.hospstay_seq,
        icustay_detail.first_hosp_stay,
        icustay_detail.los_icu,
        icustay_detail.icustay_seq,
        icustay_detail.first_icu_stay
    FROM admissions
        JOIN icustays ON admissions.hadm_id = icustays.hadm_id
        JOIN icustay_detail ON icustays.icustay_id = icustay_detail.icustay_id
)