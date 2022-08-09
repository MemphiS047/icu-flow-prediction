CREATE TABLE dataset_fpm_icustay_elixhasuer AS 
SELECT
public.dataset_fpm_icustay.icustay_id,
public.dataset_fpm_icustay.age,
public.dataset_fpm_icustay.pulmonary,
public.dataset_fpm_icustay.pao2fio2,
public.dataset_fpm_icustay.mingcs,
public.dataset_fpm_icustay.heartrate_mean,
public.dataset_fpm_icustay.wbc_min,
public.dataset_fpm_icustay.wbc_max,
public.dataset_fpm_icustay.sysbp_mean,
public.dataset_fpm_icustay.urineoutput,
public.dataset_fpm_icustay.pco2,
public.dataset_fpm_icustay.po2,
public.dataset_fpm_icustay.icu_level,

public.icustay_detail_age.subject_id,
public.icustay_detail_age.hadm_id,
public.icustay_detail_age.gender,
public.icustay_detail_age.dod,
public.icustay_detail_age.admittime,
public.icustay_detail_age.dischtime,
public.icustay_detail_age.los_hospital,
public.icustay_detail_age.ethnicity,
public.icustay_detail_age.ethnicity_grouped,
public.icustay_detail_age.admission_type,
public.icustay_detail_age.hospital_expire_flag,
public.icustay_detail_age.hospstay_seq,
public.icustay_detail_age.first_hosp_stay,
public.icustay_detail_age.intime,
public.icustay_detail_age.outtime,
public.icustay_detail_age.los_icu,
public.icustay_detail_age.icustay_seq,
public.icustay_detail_age.first_icu_stay,

public.elixhauser_score_quan.elixhauser_vanwalraven,
public.elixhauser_score_quan.elixhauser_sid29,
public.elixhauser_score_quan.elixhauser_sid30

FROM public.dataset_fpm_icustay, public.icustay_detail_age, public.elixhauser_score_quan
WHERE 
public.dataset_fpm_icustay.icustay_id = public.icustay_detail_age.icustay_id AND
public.dataset_fpm_icustay.icustay_id = public.icustay_detail_age.icustay_id AND
public.dataset_fpm_icustay.hadm_id = public.elixhauser_score_quan.hadm_id