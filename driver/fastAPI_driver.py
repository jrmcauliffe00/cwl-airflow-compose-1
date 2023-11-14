from fastapi import FastAPI, UploadFile, File, Body, Query
from fastapi.responses import JSONResponse
import os, requests, json, yaml

app = FastAPI()

upload_folder = "/path/to/dags"

def create_python_file(upload_folder, dag_id):
    python_code = '''#!/usr/bin/env python3
from cwl_airflow.extensions.cwldag import CWLDAG
dag = CWLDAG(
    workflow="/path/to/dags/{}.cwl",
    dag_id="{}"
)
'''.format(dag_id, dag_id)

    python_file_path = os.path.join(upload_folder, dag_id + ".py")
    with open(python_file_path, 'w') as f:
        f.write(python_code)


def json_to_yaml(json_filename):
    #read
    with open(json_filename, 'r') as json_file:
        data = json.load(json_file)
    #write
    with open(json_filename, 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)


@app.post("/create")
async def create(
    dag_id: str = Body(..., description="dag id to identify"), 
    workflow_file: UploadFile = File(...)
    ):

    create_python_file(upload_folder, dag_id=dag_id)

    if(workflow_file.filename.endswith(".json")):
        json_to_yaml(workflow_file.filename)
        #converting the same file?
        #access to the same folder?
        workflow_file.filename = workflow_file.filename.replace(".json", ".cwl")


    if(workflow_file.filename.endswith(".yml")):
        workflow_file.filename = workflow_file.filename.replace(".yml", ".cwl")

    workflow_file_path = os.path.join(upload_folder, workflow_file.filename)

    with open(workflow_file_path, "wb") as f:
        f.write(workflow_file.file.read())

    return JSONResponse(content={
        "message": "Files uploaded successfully",
        "python_file": f"{dag_id}.py",
        "workflow_file": workflow_file.filename
    })


@app.post("/trigger")
async def trigger(
    dag_id: str = Query(..., embeded=True),
    conf: str = Query(..., embed=True),
    run_id: str = Query(..., embed=True)
):

    external_api_url = f"http://localhost:8081/api/experimental/dag_runs?dag_id={dag_id}&run_id={run_id}&conf={conf}"
    
    
    headers = {
        "Accept": "application/json",  
        "Content-Type": "multipart/form-data",  
    }

    try:
        response = requests.post(external_api_url, headers=headers)


        if response.status_code == 200:
            external_data = response.json()

            return {"external_data": external_data}
        else:
            return {"error": "Failed to retrieve data from the external API"}

    except Exception as e:
        return {"error": str(e)}
    

@app.get("/getWorkflowLogs")
async def getWorkflowLogs():
    external_api_url = f"http://localhost:8081/api/experimental/dags"

    try:
        response = requests.get(external_api_url)


        if response.status_code == 200:
            external_data = response.json()

            return {"external_data": external_data}
        else:
            return {"error": "Failed to retrieve data from the external API"}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)