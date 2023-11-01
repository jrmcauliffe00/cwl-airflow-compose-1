from fastapi import Query, FastAPI
import requests

app = FastAPI()

@app.post("/upload")
async def call_external_api(
# Variables that will be passed to this endpoint
    dag_id: str = Query(..., embeded=True),
    run_id: str = Query(..., embeded=True),
    workflow_path: str = Query(..., embeded=True),
    conf: str = Query(..., embed=True)
):

    external_api_url = f"http://localhost:8081/api/experimental/dags/dag_runs?dag_id={dag_id}&run_id={run_id}&conf={conf}"
    
    data = {
        "workflow": f"{workflow_path}"  
    }
    
    headers = {
        "Accept": "application/json",  
        "Content-Type": "multipart/form-data",  
    }

    try:
        response = requests.post(external_api_url, data=data, headers=headers)


        if response.status_code == 200:
            external_data = response.json()

            return {"external_data": external_data}
        else:
            return {"error": "Failed to retrieve data from the external API"}

    except Exception as e:
        return {"error": str(e)}
    


@app.get("/logs")
async def call_external_api():
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
