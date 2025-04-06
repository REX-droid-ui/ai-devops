# 🧠 ai-devops

[![CI](https://github.com/REX-droid-ui/ai-devops/actions/workflows/docker-image.yml/badge.svg)](https://github.com/REX-droid-ui/ai-devops/actions)

[![Docker Image](https://img.shields.io/docker/pulls/rexdroid/sentiment-app.svg?style=flat&logo=docker)](https://hub.docker.com/r/rexdroid/sentiment-app)

A lightweight DevOps pipeline for deploying a pre-trained sentiment analysis model. This project showcases containerization with Docker and automated CI/CD using GitHub Actions to build and push the application to Docker Hub. Built with Python and scikit-learn, it’s perfect for beginners learning how to integrate DevOps practices into AI workflows.

---

## 🚀 Key Features

- 🐳 Dockerized sentiment analysis app  
- 🔁 Continuous integration & deployment via GitHub Actions  
- 🔧 Simple, reproducible setup for local and cloud-based environments  
- 💡 Beginner-friendly DevOps + AI example  

---

## 📦 What's Inside?

- `app/`: Python scripts including `main.py` and saved `.pkl` model/vectorizer  
- `train_model.py`: Script to train the sentiment model  
- `Dockerfile`: Builds the image and runs training during build  
- `.github/workflows/`: GitHub Actions workflow for CI/CD  

---

## 🛠 Setup Instructions

### ✅ Prerequisites (All Platforms)

- [Docker](https://www.docker.com/products/docker-desktop/) installed and running  
- [Git](https://git-scm.com/downloads) installed (optional but recommended)  

---

### 🪟 Windows

```bash
git clone https://github.com/your-username/ai-devops.git
cd ai-devops

docker build -t sentiment-app .
docker run -it sentiment-app
```
---

### 🍎 macOS

```bash
git clone https://github.com/your-username/ai-devops.git
cd ai-devops

docker build -t sentiment-app .
docker run -it sentiment-app
```
---

### 🐧 Linux

```bash
git clone https://github.com/your-username/ai-devops.git
cd ai-devops

docker build -t sentiment-app .
docker run -it sentiment-app
```
