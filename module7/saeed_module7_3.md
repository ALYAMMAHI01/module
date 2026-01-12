# FastAPI Server Health Monitoring

This project consists of a FastAPI server that listens for server health information and a client that sends this information.

## How to Run the Applications

### 1. Install Dependencies
First, you need to install the required Python libraries. You can do this using `pip`:
```bash
pip install fastapi uvicorn psutil requests
```

### 2. Run the FastAPI Server
To start the FastAPI server, navigate to the `fastapi_health_check` directory and run the following command:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
The server will start and listen for incoming requests on port 8000.

### 3. Run the Client Application
To send the server's health information, open a new terminal and run the client script:
```bash
python fastapi_health_check/client.py
```
The client will collect the current CPU, memory, and disk usage and send it to the server.

## How to Call the API from Another Computer
To call the API from another computer, you need to know the IP address of the computer running the FastAPI server.

1. **Find the server's IP address.**
   - On Linux/macOS, you can use the `ifconfig` or `ip addr` command.
   - On Windows, you can use the `ipconfig` command.

2. **Update the client's server URL.**
   - Open the `fastapi_health_check/client.py` file.
   - Change the `server_url` from `"http://localhost:8000/health"` to the server's IP address. For example:
     ```python
     server_url = "http://192.168.1.100:8000/health"
     ```

3. **Run the client.**
   - Run the client application from the other computer, and it will send the health information to the server.
