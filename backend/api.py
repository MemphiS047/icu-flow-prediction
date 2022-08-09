from asyncio import constants
from asyncore import read
from flask import Flask, request
from flask_cors import CORS, cross_origin
from mysql.connector import connect, Error
import json

json_file = open("config.json")
db_config = json.load(json_file)["db"]

app = Flask("Medipolmobileappbackend")

CORS(app, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def add_header(response):
     response.headers['Access-Control-Allow-Origin'] = '*'
     response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
     response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE, OPTIONS, HEAD'
     response.headers['Access-Control-Expose-Headers'] = '*'
     return response

def _connect(host=db_config["host"], database=db_config["name"], user=db_config["user"], password=db_config["password"]):
    try:
        conn = connect(host=host, database=database, user=user, password=password)
    except Error as e:
        print(e)
    return conn

@app.route("/addpatient", methods=['POST'])
def add_patient():
    conn = _connect()
    data = request.get_data()
    data.decode('utf-8')
    data = json.loads(data.decode('utf-8'))
    addPatientQuery = f"""INSERT INTO patient (tc, fName, lName, level, type)
    VALUES ('{data["tc"]}', '{data["firstName"]}',  '{data["lastName"]}', {data["level"]}, '{data["type"]}')"""
    print("PATIENT QUERY ", addPatientQuery)
    with conn.cursor() as cursor:
        cursor.execute(addPatientQuery)
        conn.commit()
    return {"message" : "Success"}, 200, {'Access-Control-Allow-Origin': '*'}

@app.route("/getpatientbyname", methods=['POST'])
def _get_patient_by_name():
    conn = _connect()
    data = request.get_data()
    data.decode('ascii')
    data = json.loads(data.decode('ascii'))
    getPatientQuery = f"""SELECT * FROM patient WHERE fName='{data["name"]}'"""
    queryResult = { "data" : [

    ]}
    with conn.cursor() as cursor:
        cursor.execute(getPatientQuery)
        result = cursor.fetchall()
        for row in result:
            queryResult["data"].append({
                "id" : row[0],
                "tc" : row[1],
                "firstName" : row[2],
                "lastName" : row[3],
                "level" : row[4],
                "type" : row[5],
            })
        return queryResult, 200, {'Access-Control-Allow-Origin': '*'}

@app.route("/getpatientlikequery", methods=['POST'])
def _get_patient_like():
    conn = _connect()
    data = request.get_data()
    data.decode('ascii')
    data = json.loads(data.decode('ascii'))
    getPatientLikeQuery = f"""
    SELECT * FROM patient WHERE tc LIKE '{data["searchQuery"]}%' OR fName LIKE '{data["searchQuery"]}%'
    """
    queryResult = { "data" : [

    ]}
    with conn.cursor() as cursor:
        cursor.execute(getPatientLikeQuery)
        result = cursor.fetchall()
        for row in result:
            queryResult["data"].append({
                "id" : row[0],
                "tc" : row[1],
                "firstName" : row[2],
                "lastName" : row[3],
                "bDate": row[4],
                "gender": row[5],
                "type": row[6],
                "level": row[7],
            })
    return queryResult

@app.route("/getpatientbytc", methods=['POST'])
def _get_patient_by_tc():
    conn = _connect()
    data = request.get_data()
    data.decode('ascii')
    data = json.loads(data.decode('ascii'))
    getPatientQuery = f"""SELECT * FROM patient WHERE tc='{data["tc"]}'"""
    queryResult = { "data" : [

    ]}
    with conn.cursor() as cursor:
        cursor.execute(getPatientQuery)
        result = cursor.fetchall()
        for row in result:
            queryResult["data"].append({
                "id" : row[0],
                "tc" : row[1],
                "firstName" : row[2],
                "lastName" : row[3],
                "bDate": row[4],
                "gender": row[5],
                "type": row[6],
                "level": row[7],
            })
        return queryResult, 200, {'Access-Control-Allow-Origin': '*'}

@app.route("/getdata", methods=['POST'])
def _get_data():
    conn = _connect()
    data = request.get_data()
    data.decode('ascii')
    data = json.loads(data.decode('ascii'))
    getNICUdataQuery = f"""
    SELECT * FROM {data["type"]}data;
    """
    queryResult = { "data" : [

    ]}
    with conn.cursor() as cursor:
        cursor.execute(getNICUdataQuery)
        result = cursor.fetchall()
        for row in result:
            queryResult["data"].append({
                "id" : row[0],
                "name" : row[1],
                "description" : row[2],
                "count" : row[3],
            })
        return queryResult, 200, {'Access-Control-Allow-Origin': '*'}

@app.route("/updatecount", methods=['POST'])
def _update_count():
    conn = _connect()
    data = request.get_data()
    data.decode('ascii')
    data = json.loads(data.decode('ascii'))
    updateCountQuery = f"""
    UPDATE {data["type"]}data SET count = count + 1
    WHERE name = '{data["name"]}'
    """
    with conn.cursor() as cursor:
        cursor.execute(updateCountQuery)
        conn.commit()
        return {"message": "Success"}, 200, {'Access-Control-Allow-Origin': '*'}

@app.route("/getlatestadmission", methods=['POST'])
@cross_origin(supports_credentials=True)
def _get_latest_admission():
    last_admission_id = 0
    conn = connect(host=db_config["host"], database=db_config["name"], user=db_config["user"], password=db_config["password"])
    data = request.get_data()
    data.decode('ascii')
    data = json.loads(data.decode('ascii'))
    getLatestAdmissionIDQuery = f"""SELECT max(admission.id)
    FROM admission, patient WHERE patient.id=admission.patientId AND patient.id={data["id"]};
    """
    queryResult = { "data" : [

    ]}
    if(data["type"] == "icu"):
        getColumnNames = """
        SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS`  WHERE `TABLE_SCHEMA`='medipol_backend' AND `TABLE_NAME`='icupatient';`"""
        getLatestTSList = """SELECT *
            FROM icupatient WHERE {} IS NOT NULL"""
    if(data["type"] == "picu"):
        getColumnNames = """
        SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS`  WHERE `TABLE_SCHEMA`='medipol_backend' AND `TABLE_NAME`='picupatient';`"""
        getLatestTSList = """SELECT *
            FROM picupatient WHERE {} IS NOT NULL"""
    if(data["type"] == "nicu"):
        getColumnNames = """
        SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS`  WHERE `TABLE_SCHEMA`='medipol_backend' AND `TABLE_NAME`='nicupatient';`"""
        getLatestTSList = """SELECT *
            FROM nicupatient WHERE {} IS NOT NULL"""
    cur = conn.cursor()
    cur.execute(getLatestAdmissionIDQuery)
    result = cur.fetchall()
    
    if(result[0][0] == None):
        return {"message": "No admission found"}, 200, {'Access-Control-Allow-Origin': '*'}
    
    cur.execute(getColumnNames)
    listOfColumnNames = cur.fetchall()
    
    for rowColumn in listOfColumnNames[3:]:
        conn = connect(host=db_config["host"], database=db_config["name"], user=db_config["user"], password=db_config["password"])
        cur = conn.cursor()
        cur.execute(getLatestTSList.format(rowColumn[0]))
        result = cur.fetchall()
        if(result != [] and rowColumn[0] != "level" and rowColumn[0] != "id" and rowColumn[0] != "patientId" and rowColumn[0] != "admissionId"):
            queryResult["data"].append({
                "name" : rowColumn[0],
                "value" : "true"
                })
    return queryResult, {'Access-Control-Allow-Origin': '*'}

@app.route("/addnewtslist", methods=['POST'])
def _add_new_tslist():
    conn = _connect()
    data = request.get_data()
    data.decode('ascii')
    data = json.loads(data.decode('ascii'))
    updateLevel = f"""
    update patient set level={data["level"]} where id={data["id"]};
    """

    addNewAdmissionQuery = f"""
    insert into admission(patientId, admDate) values({data["id"]}, NOW());
    """

    setVariableQuery = f"""
    set @lastID = @@identity;
    """
    if(data["type"] == "icu"):
        addNewTSListQuery = """
            insert into icupatient(patientId, {} level, admissionId) values({}, {} {}, @lastID);
            """
    if(data["type"] == "picu"):
        addNewTSListQuery = """
            insert into picupatient(patientId, {} level, admissionId) values({}, {} {}, @lastID);
            """
    if(data["type"] == "nicu"):
        addNewTSListQuery = """
            insert into nicupatient(patientId, {} level, admissionId) values({}, {} {}, @lastID);
            """
    with conn.cursor() as cursor:
        cursor.execute(updateLevel)
        cursor.execute(addNewAdmissionQuery)
        cursor.execute(setVariableQuery)
        queryStringColumn = ""
        queryStringColumnValue = ""
        for obj in data["TSList"]:
            queryStringColumn = queryStringColumn + f"{obj['name']}, "
            queryStringColumnValue = queryStringColumnValue +  "1, "
        print(addNewTSListQuery.format(queryStringColumn, data["id"], queryStringColumnValue, data["level"]))
        cursor.execute(addNewTSListQuery.format(queryStringColumn, data["id"], queryStringColumnValue, data["level"]))
        conn.commit()
        return {"message": "Success"}, 200, {'Access-Control-Allow-Origin': '*'}

app.run()