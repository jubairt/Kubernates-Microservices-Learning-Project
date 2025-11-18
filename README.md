# 🚀 FastAPI Microservices – Kubernetes Version

This repository contains a **beginner-friendly microservices setup** using **FastAPI**, **Docker**, and **Kubernetes (k8s)**.  
It is designed purely for **learning** how microservices run independently, scale, and communicate within a Kubernetes cluster.

---

## 📦 What This Project Includes

### **🔹 User Service (Port 5001)**
Returns user details.

### **🔹 Product Service (Port 5002)**
Returns product details.

### **🔹 Order Service (Port 5003)**
Returns order information by internally calling:
- **User Service**
- **Product Service**

Each service:
- Has its own FastAPI app  
- Has its own Dockerfile  
- Has its own Deployment in Kubernetes  
- Has its own Service in Kubernetes  

---

## 🔗 Service Communication Inside Kubernetes

Kubernetes provides **DNS-based service discovery**, so services can talk to each other simply using service names:

- `http://user-service:5001`
- `http://product-service:5002`
- `http://order-service:5003`

No IP addresses needed — Kubernetes handles routing automatically.

---

## ▶️ Step-by-Step: Deploying to Kubernetes

### **1. Build Docker Images**

Build images for each microservice:

```bash
docker build -t <your-dockerhub-username>/user-service ./user-service
docker build -t <your-dockerhub-username>/product-service ./product-service
docker build -t <your-dockerhub-username>/order-service ./order-service
