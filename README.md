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

## 1. Delete Old Resources

Delete everything:

```bash
kubectl delete -f k8s/
```

## 2. Build Docker Images Locally

Run these from your project root:

```bash
docker build -t user-service:latest ./user-service
docker build -t product-service:latest ./product-service
docker build -t order-service:latest ./order-service
```

## 3. Deploy to Kubernetes

Delete everything:

```bash
kubectl apply -f k8s/
```

## 4. Check Everything is Running

Check pods:

```bash
kubectl get pods
```

Check services:

```bash
kubectl get svc
```

## ✅ Conclusion

This project shows how to build Docker images, load them into a kind cluster, and deploy FastAPI microservices on Kubernetes.  
It provides a simple foundation for understanding microservice deployment and can be extended as you learn more. 


