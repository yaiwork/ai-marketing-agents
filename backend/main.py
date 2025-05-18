from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from backend.services import run_all_agents, run_agent_by_name
import os

app = FastAPI()

class AgentRequest(BaseModel):
    agent_name: str

# Endpoint to run all agents (optional if not needed)
@app.post("/run-all")
def run_all():
    return {"result": run_all_agents()}

# Endpoint to run a single agent by name
@app.post("/run-agent")
def run_agent(data: AgentRequest):
    return {"result": run_agent_by_name(data.agent_name)}

# Endpoint to download the full output file
@app.get("/download-full-output")
def download_full_output():
    output_file = os.path.join("data", "all_agents_output.txt")
    
    if not os.path.exists(output_file):
        raise HTTPException(status_code=404, detail="Output file not found.")

    return FileResponse(
        path=output_file,
        filename="all_agents_output.txt",
        media_type="text/plain"
    )
