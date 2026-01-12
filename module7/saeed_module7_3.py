import requests
import psutil
import datetime

def get_server_health():
    """
    Collects server health information, including CPU, memory, and disk usage.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    
    health_data = {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_info.percent,
        "disk_usage": disk_info.percent,
        "server_time": datetime.datetime.now().isoformat()
    }
    return health_data

def send_health_info(server_url: str):
    """
    Sends the server health information to the FastAPI server via a POST request.
    """
    health_data = get_server_health()
    try:
        response = requests.post(server_url, json=health_data)
        response.raise_for_status()  # Raise an exception for bad status codes
        print("Health information sent successfully.")
        print("Response from server:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error sending health information: {e}")

if __name__ == "__main__":
    # URL of the FastAPI server's health endpoint.
    # To call this from another computer, replace "localhost" with the
    # IP address of the computer running the FastAPI server.
    # For example: "http://192.168.1.100:8000/health"
    server_url = "http://localhost:8000/health"
    send_health_info(server_url)
