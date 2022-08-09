-- Obtains admission and transfer detail of patients (first admission, trasnfer, discharge etc.)
SET SCHEMA 'mimiciii';
SELECT * FROM admissions INNER JOIN transfers ON admissions.subject_id=transfers.subject_id LIMIT 10;