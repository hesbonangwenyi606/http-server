# http-server _   _ _____ _____   _____                           
| | | |_   _|  __ \ / ____|                          
| |_| | | | | |__) | (___   ___ _ ____   _____ _ __  
|  _  | | | |  ___/ \___ \ / _ \ '__\ \ / / _ \ '__| 
| | | |_| |_| |     ____) |  __/ |   \ V /  __/ |    
|_| |_|_____|_|    |_____/ \___|_|    \_/ \___|_|    
                                                     

# Simple HTTP Server

A lightweight HTTP server built with Python.
Supports **GET** and **POST** requests with the following features:

* `GET /hello` → Returns a greeting.
* `GET /echo?msg=...` → Echoes back query parameter `msg`.
* `POST /echo` → Echoes back request body (supports `text/plain` and `application/json`).


## 🚀 Getting Started

### Prerequisites

* Python 3.7+
* `curl` (for testing)

### Run the server

```bash
python3 server.py
```

By default, it listens on:
http://127.0.0.1:8080

## 📌 API Usage Examples

### 1. Hello Endpoint

```bash
curl http://127.0.0.1:8080/hello
```

**Response:**

Hello! You requested /hello
### 2. Echo with Query String

```bash
curl "http://127.0.0.1:8080/echo?msg=HiThere"
```

**Response:**
HiThere

### 3. Echo with Plain Text (POST)

```bash
curl -X POST http://127.0.0.1:8080/echo \
     -H "Content-Type: text/plain" \
     -d "Hello Pesapal"
```

**Response:**
Hello Pesapal

### 4. Echo with JSON (POST)
```bash
curl -X POST http://127.0.0.1:8080/echo \
     -H "Content-Type: application/json" \
     -d '{"msg": "Hello JSON"}'
```

**Response:**
Hello JSON

## Project Structure
http-server/
│── server.py        # Main server implementation
│── README.md        # Documentation


## Notes
* Returns `404 Not Found` for unsupported paths.
* Handles both plain text and JSON POST payloads.

## Author

**Hesbon Angwenyi**
Full Stack Software Engineer | DevOps Enthusiast
