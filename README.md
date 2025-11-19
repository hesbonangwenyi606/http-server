# HTTP Server _   _ _____ _____   _____                           
| | | |_   _|  __ \ / ____|                          
| |_| | | | | |__) | (___   ___ _ ____   _____ _ __  
|  _  | | | |  ___/ \___ \ / _ \ '__\ \ / / _ \ '__| 
| | | |_| |_| |     ____) |  __/ |   \ V /  __/ |    
|_| |_|_____|_|    |_____/ \___|_|    \_/ \___|_|    

# Simple HTTP Server

A lightweight Python HTTP server supporting **GET** and **POST** requests.

---

## Features

* `GET /hello` → Returns a greeting message.
* `GET /echo?msg=...` → Echoes back a query parameter.
* `POST /echo` → Echoes back request body (`text/plain` or `application/json`).

---

## Getting Started

### Run Locally
```bash
python3 http_server.py
Server will run at: http://127.0.0.1:8080

API Examples
Hello Endpoint

bash
Copy code
curl http://127.0.0.1:8080/hello
Response:

bash
Copy code
Hello! You reached /hello
Echo with Query String (GET)

bash
Copy code
curl "http://127.0.0.1:8080/echo?msg=HiThere"
Response:

makefile
Copy code
Echo: HiThere
Echo with Plain Text (POST)

bash
Copy code
curl -X POST http://127.0.0.1:8080/echo \
     -H "Content-Type: text/plain" \
     -d "Hello Pesapal"
Response:

makefile
Copy code
Echo: Hello Pesapal
Echo with JSON (POST)

bash
curl -X POST http://127.0.0.1:8080/echo \
     -H "Content-Type: application/json" \
     -d '{"msg": "Hello JSON"}'
Response:

json
{"echo": "Hello JSON"}
Run with Docker
Build Image
bash
docker build -t http-server .

## Run Container
docker run -p 8080:8080 http-server
Docker Compose
bash

## docker-compose up
Project Structure
bash
http-server/
│── http_server.py          # Main server implementation
│── Dockerfile              # Docker image definition
│── docker-compose.yml      # Docker Compose configuration
│── README.md
               # Project documentation
## Author
Hesbon Angwenyi
Full Stack Software Engineer | DevOps Enthusiast