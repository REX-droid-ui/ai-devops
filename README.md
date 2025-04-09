
# ai-devops 🚀

[![Docker Build Status](https://github.com/REX-droid-ui/ai-devops/actions/workflows/docker-image.yml/badge.svg)](https://github.com/REX-droid-ui/ai-devops/actions)
[![Docker Image](https://img.shields.io/docker/pulls/rexdroid/sentiment-app.svg?style=flat&logo=docker)](https://hub.docker.com/r/rexdroid/sentiment-app)

A simple and production-ready **Sentiment Analysis Web App** powered by **Machine Learning**, built with **Python**, **scikit-learn**, and packaged using **Docker**. This project also includes **CI/CD integration with GitHub Actions** for seamless development workflows.

## 🔍 Features

- ✅ IMDB 50K movie reviews dataset used for model training  
- ✅ Sentiment analysis using a Logistic Regression pipeline  
- ✅ Command-line interactive text input  
- ✅ Pre-trained model stored and used in Dockerized app  
- ✅ GitHub Actions CI/CD pipeline (build & test)  
- ✅ Lightweight and portable via Docker  

## 🧠 Model Info

The model is a **Pipeline**:
- `TfidfVectorizer`: Text vectorization  
- `LogisticRegression`: Classification into positive/negative sentiment  

Trained on the [IMDB 50K Movie Reviews dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews).

## 🐳 Docker Instructions

### 🏗️ Build the Docker image:
```bash
docker build -t sentiment-app .
```

### 🚀 Run the sentiment app:
```bash
docker run -it --rm sentiment-app
```

> You will be prompted to enter a review, and it will return the sentiment (Positive/Negative).

## 🤖 GitHub Actions (CI/CD)

- Automatically builds and checks your app on every push to `main`.
- Define your workflow in `.github/workflows/ci.yml`.

## ✅ Requirements

For local development (without Docker):

```bash
pip install -r requirements.txt
```

## 📌 Example

```text
Enter a movie review: The plot was amazing and I loved the characters!
Predicted Sentiment: Positive 👍
```

## ⚠️ Note on Large Files

The dataset (`IMDB Dataset.csv`) is over 60 MB. Consider using [Git LFS](https://git-lfs.github.com/) to manage large files if you plan on frequent changes.

## 👤 Author

**REX-droid-ui**  
GitHub: [@REX-droid-ui](https://github.com/REX-droid-ui)

---

## 📄 License

MIT License
