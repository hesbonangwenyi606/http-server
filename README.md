# 🌐 HTTP Server

A lightweight **Python HTTP server** supporting **GET** and **POST** requests.  
Main endpoints: `/hello` and `/echo`.

---

## ⚡ Features

- `GET /hello` → Returns a greeting  
- `GET /echo?msg=...` → Echoes back query parameter  
- `POST /echo` → Echoes back request body (`text/plain` or `application/json`)

---

## 🛠️ Prerequisites

- Python 3.7+  
- Docker (optional)  
- `curl` (optional, for testing)

---

## 🚀 Run Locally

```bash
python3 http_server.py
Server runs at: http://127.0.0.1:8080

📝 API Examples
👋 Hello
bash
Copy code
curl http://127.0.0.1:8080/hello
Response:

text
Copy code
Hello! You reached /hello
🔁 Echo GET
bash
Copy code
curl "http://127.0.0.1:8080/echo?msg=HiDocker"
Response:

text
Copy code
Echo: HiDocker
✉️ Echo POST (Plain Text)
bash
Copy code
curl -X POST http://127.0.0.1:8080/echo \
     -H "Content-Type: text/plain" \
     -d "Hello Pesapal"
Response:

text
Copy code
Echo: Hello Pesapal
📦 Echo POST (JSON)
bash
Copy code
curl -X POST http://127.0.0.1:8080/echo \
     -H "Content-Type: application/json" \
     -d '{"msg": "Hello Docker"}'
Response:

json
Copy code
{"echo": "Hello Docker"}
🐳 Run with Docker
Build Image
bash
Copy code
docker build -t http-server .
## Run Container
docker run -d -p 8080:8080 http-server
Access server: http://127.0.0.1:8080

## View Logs
docker logs -f <container_id>

## Stop Container
docker stop <container_id>

## Project Structure
pgsql
http-server/
│── http_server.py
│── Dockerfile
│── docker-compose.yml
│── README.md


## Author
Hesbon Angwenyi – Full Stack Software Engineer | DevOps Enthusiast