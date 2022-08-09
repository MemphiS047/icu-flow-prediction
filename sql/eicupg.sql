SET SEARCH_PATH TO eicucrd;

-- drop the table if it already exists
DROP TABLE IF EXISTS apacheApsVar;

-- create the table
CREATE TABLE apacheApsVar
(
	patientUnitStayID	int,
	apacheApsVarID	int,
	intubated	int,
	vent	int,
	dialysis	int,
	eyes	int,
	motor	int,
	verbal	int,
	meds	int,
	urine	float(53),
	wbc	float(53),
	temperature	float(53),
	respiratoryRate	float(53),
	sodium	float(53),
	heartRate	float(53),
	meanBp	float(53),
	ph	float(53),
	hematocrit	float(53),
	creatinine	float(53),
	albumin	float(53),
	pao2	float(53),
	pco2	float(53),
	bun	float(53),
	glucose	float(53),
	bilirubin	float(53),
	fio2	float(53)
) ;


-- drop the table if it already exists
DROP TABLE IF EXISTS apachePatientResult;

-- create the table
CREATE TABLE apachePatientResult
(
	patientUnitStayID	int,
	apachePatientsResultsID	int,
	physicianSpeciality	varchar(50),
	physicianInterventionCategory	varchar(50),
	acutePhysiologyScore	int,
	apacheScore	int,
	apacheVersion	int,
	predictedICUMortality	varchar(50),
	actualICUMortality	varchar(50),
	predictedICULOS	float(53),
	actualICULOS	float(53),
	predictedHospitalMortality	varchar(50),
	actualHospitalMortality	varchar(50),
	predictedHospitalLOS	float(53),
	actualHospitalLOS	float(53),
	preopMI	int,
	preopCardiacCath	int,
	PTCAwithin24h	int,
	unabridgedUnitLOS	float(53),
	unabridgedHospLOS	float(53),
	actualVentdays	float(53),
	predVentdays	float(53),
	unabridgedActualVentdays	float(53)
);

-- drop the table if it already exists
DROP TABLE IF EXISTS apachePredVar;

-- create the table
CREATE TABLE apachePredVar
(
	patientUnitStayID	int,
	apachePredVarID	int,
	sicuDay	int,
	saps3Day1	int,
	saps3Today	int,
	saps3Yesterday	int,
	gender	int,
	teachType	int,
	region	int,
	bedcount	int,
	admitSource	int,
	graftCount	int,
	meds	int,
	verbal	int,
	motor	int,
	eyes	int,
	age	int,
	admitDiagnosis	varchar(11),
	thrombolytics	int,
	diedInHospital	int,
	aids	int,
	hepaticFailure	int,
	lymphoma	int,
	metastaticCancer	int,
	leukemia	int,
	immunosuppression	int,
	cirrhosis	int,
	electiveSurgery	int,
	activeTx	int,
	readmit	int,
	ima	int,
	midur	int,
	ventDay1	int,
	oOBVentDay1	int,
	oOBIntubDay1	int,
	diabetes	int,
	managementSystem	int,
	var03HspXlos	float(53),
	pao2	float(53),
	fio2	float(53),
	ejectFx	float(53),
	creatinine	float(53),
	dischargelocation	int,
	visitNumber	int,
	amilocation	int,
	day1meds	int,
	day1verbal	int,
	day1motor	int,
	day1eyes	int,
	day1pao2	float(53),
	day1fio2	float(53)
) ;

-- drop the table if it already exists
DROP TABLE IF EXISTS lab;

-- create the table
CREATE TABLE lab
(
	patientUnitStayID	int,
	labID	int,
	labResultOffset	int,
	labTypeID	int,
	labName	varchar(255),
	labResult	decimal(11,4),
	labResultText	varchar(255),
	labMeasureNameSystem	varchar(255),
	labMeasureNameInterface	varchar(255),
	labResultRevisedOffset	int
) ;

-- drop the table if it already exists
DROP TABLE IF EXISTS vitalPeriodic;

-- create the table
CREATE TABLE vitalPeriodic
(
	patientUnitStayID	int,
	vitalPeriodicID	int,
	observationOffset	int,
	temperature	decimal(11,4),
	saO2	int,
	heartRate	int,
	respiration	int,
	cvp	int,
	etCo2	int,
	systemicSystolic	int,
	systemicDiastolic	int,
	systemicMean	int,
	paSystolic	int,
	paDiastolic	int,
	paMean	int,
	st1	real,
	st2	real,
	st3	real,
	ICP	int
) ;