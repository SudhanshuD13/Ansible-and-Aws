# 🚀 Ansible + AWS Deployment Project

A simple DevOps project demonstrating how to deploy a Flask application using **Ansible automation** on an AWS EC2 instance with Nginx.

---

## 📌 Project Overview

This project showcases:

* Infrastructure automation using **Ansible**
* Application deployment on **AWS EC2**
* Configuration management
* A simple **Flask web app** with a modern UI
* Nginx setup using templates

---

## 🏗️ Project Structure

```
.
├── ansible/
├── ansible-demo/
│   ├── files/
│   │   └── app.py
│   ├── templates/
│   │   └── nginx.conf.j2
│   ├── inventory
│   ├── playbook.yml
│   └── vars.yml
├── aws/
├── script_practice/
├── aws_tracker.sh
```

---

## ⚙️ Technologies Used

* 🐍 Python (Flask)
* ⚙️ Ansible
* ☁️ AWS EC2
* 🌐 Nginx
* 🐧 Linux (Ubuntu)

---

## 🚀 Features

* Automated deployment using Ansible playbooks
* Dynamic Nginx configuration using Jinja2 templates
* Flask app served via EC2 instance
* Clean UI with gradient background
* Infrastructure as Code (IaC) approach

---

## 🧑‍💻 Flask App

A simple Flask application:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "A warm welcome to Ansible deployed app By Sudhanshu!"

app.run(host="0.0.0.0", port=5000)
```

---

## 🛠️ How to Run

### 1. Clone the repository

```
git clone https://github.com/SudhanshuD13/Ansible-and-Aws.git
cd Ansible-and-Aws
```

---

### 2. Update Inventory

Edit the `inventory` file with your EC2 public IP:

```
[web]
<your-ec2-ip>
```

---

### 3. Run Ansible Playbook

```
ansible-playbook -i inventory playbook.yml
```

---

### 4. Access Application

Open in browser:

```
http://<your-ec2-ip>:5000
```

---

## 🔐 Security Notes

* Sensitive files like `.aws/` and `.ssh/` are excluded using `.gitignore`
* AWS credentials should **never be committed**
* Rotate credentials if accidentally exposed

---

## 📈 Future Improvements

* Add CI/CD pipeline (GitHub Actions)
* Dockerize the Flask app
* Use Terraform for infrastructure provisioning
* Add HTTPS (SSL with Nginx)
* Monitoring (Prometheus + Grafana)

---

## 🙌 Author

**Sudhanshu**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!

---
