from fastapi import FastAPI
from pydantic import BaseModel
import datetime

# Define the data model for the health information
class HealthInfo(BaseModel):
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    server_time: str

# Create a FastAPI app instance
app = FastAPI()

# Define the /health endpoint to receive health information
@app.post("/health")
async def receive_health_info(health_info: HealthInfo):
    """
    Receives server health information and prints it to the console.
    """
    print("Received health information:")
    print(f"  CPU Usage: {health_info.cpu_usage}%")
    print(f"  Memory Usage: {health_info.memory_usage}%")
    print(f"  Disk Usage: {health_info.disk_usage}%")
    print(f"  Server Time: {health_info.server_time}")
    return {"status": "Health information received successfully"}

# Define a root endpoint to confirm the server is running
@app.get("/")
def read_root():
    """
    A simple endpoint to confirm that the server is running.
    """
    return {"message": "FastAPI server is running"}

if __name__ == "__main__":
    import uvicorn
    # To run this application from another computer, you need to bind it to 0.0.0.0
    # This makes the server accessible from any IP address on the network.
    # The default port is 8000, but you can change it if needed.
    uvicorn.run(app, host="0.0.0.0", port=8000)
