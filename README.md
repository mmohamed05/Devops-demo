# 🚀 DevOps Demo – FastAPI CI/CD Pipeline

![Build Status](https://github.com/mmohamed05/Devops-demo/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

### 🌍 Live Preview
*(Coming Soon — will display once deployed)*  
For now, you can **run it locally** or pull the **Docker image** below.

---

## 📸 Project Overview

A simple **FastAPI web app** packaged with **Docker** and automated using **GitHub Actions CI/CD**.

This project demonstrates a complete DevOps workflow:  
**Code → Build → Test → Deploy** — all automated in the cloud.

![Preview Screenshot](https://github.com/mmohamed05/Devops-demo/assets/preview-example.png?raw=true)
*(Example Preview – replace with your own screenshot once deployed)*

---

## 🧱 Tech Stack
- **Python 3.11**
- **FastAPI** – lightweight backend web framework
- **Uvicorn** – ASGI server
- **Docker** – for containerization
- **GitHub Actions** – for CI/CD automation
- **GitHub Packages (GHCR)** – for hosting container images

---

## ⚙️ Features
✅ FastAPI microservice (`app.py`)  
✅ Dockerfile for containerization  
✅ GitHub Actions workflow (`ci.yml`)  
✅ Automated build and test pipeline  
✅ GitHub Container Registry publishing  

---

## 🧩 Project Structure
.
├── app.py # FastAPI app entry point
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build configuration
├── .github/workflows/ci.yml # GitHub Actions CI workflow
└── .gitignore

yaml
Copy code

---

## 🐳 Run Locally
```bash
# Clone the repo
git clone https://github.com/mmohamed05/Devops-demo.git
cd Devops-demo

# Build Docker image
docker build -t devops-demo .

# Run the container
docker run -p 8000:8000 devops-demo
Then open:
👉 http://localhost:8000

⚙️ Continuous Integration (CI)
Every push to the main branch triggers GitHub Actions to:

Set up Python environment

Install dependencies

Build Docker image

Run checks

Push image to GitHub Container Registry (GHCR)

📦 GitHub Container Registry (GHCR)
You can pull and run the latest container image directly:

bash
Copy code
docker pull ghcr.io/mmohamed05/devops-demo:latest
🧠 Learning Objectives
This project demonstrates:

CI/CD automation using GitHub Actions

Containerization with Docker

Secure workflow permissions

Version control & deployment best practices

Image publishing via GitHub Packages

🧰 Tools Used
Tool	Purpose
FastAPI	Web API framework
Docker	Containerization
GitHub Actions	CI/CD automation
GitHub Packages	Host container image (GHCR)

📘 About the Developer
👨‍💻 Mohamed Mohamed
Junior @ Georgia State University | Aspiring DevOps & Platform Engineer
Passionate about automation, cloud systems, and infrastructure as code.
🌐 GitHub: mmohamed05
📧 Contact: Available upon request

🔥 Future Improvements
Add Pytest for unit testing

Deploy to AWS / Render / Railway

Add API routes and /health endpoint

Integrate monitoring + logs dashboard

📄 License
This project is open source and available under the MIT License.


### ✅ What You Should Do Now
1. Create a new file in your repo called `README.md`  
2. Paste everything above into it  
3. Commit and push 




