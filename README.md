
# 🐛 BugSphere-Bug-Tracker
<img width="901" height="425" alt="image" src="https://github.com/user-attachments/assets/8ffcf3fe-8a6d-4f08-95ab-62eaeb86f182" />

![BugSphere Banner](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

**BugSphere** is a modern, lightweight, and highly responsive bug tracking dashboard built with Python/Flask and vanilla web technologies. It features a stunning UI with live animated backgrounds, glassmorphism elements, and seamless dark/light mode toggling.

---

## ✨ Features

* 🔐 **Secure Admin Portal:** Beautiful login screen with a live animated CSS gradient background and glassmorphism card design.
* 🌓 **Dark / Light Mode:** Fully integrated theme toggler that remembers your preference using browser local storage.
* 📊 **Dashboard Analytics:** Live statistics cards tracking Total, Open, In Progress, and Resolved bugs.
* 🛠️ **Full CRUD Operations:** Seamlessly Create, Read, Update, and Delete bugs via a RESTful API.
* 🔍 **Smart Filtering & Search:** Instantly filter bugs by status, severity, or text-based search.
* 📱 **Modern UI/UX:** Built with a clean `Inter` font layout, dynamic status badges, and interactive modals.
* 📂 **Multi-View Navigation:** Mockup views for Projects, Analytics, and Team management.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3 (CSS Variables, Grid, Flexbox), Vanilla JavaScript
* **Icons:** FontAwesome 6
---

## 🚀 Getting Started

Follow these steps to get BugSphere running on your local machine.

### 1. Prerequisites
Ensure you have Python installed on your system (Python 3.7+ recommended).

### 2. Installation
Clone the repository and navigate into the project directory:
```bash
git clone [https://github.com/yourusername/BugSphere-Bug-Tracker.git](https://github.com/yourusername/BugSphere-Bug-Tracker.git)
cd BugSphere-Bug-Tracker

```

Install the required Python packages:

```bash
pip install Flask

```

### 3. Running the App

Start the Flask server:

```bash
python app.py

```

*The app will be live at: `http://127.0.0.1:5000*`

---

## 🔑 Login Credentials

When you first launch the app, you will be greeted by the secure login screen. Use the default admin credentials:

* **Username:** `admin`
* **Password:** `admin123`

---

## 📡 API Endpoints

BugSphere utilizes a lightweight REST API to manage data:

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/bugs` | Retrieve a list of all bugs |
| `POST` | `/api/bugs` | Create a new bug |
| `PUT` | `/api/bugs/<id>` | Update an existing bug by ID |
| `DELETE` | `/api/bugs/<id>` | Delete a bug by ID |

---

## 📂 Project Structure

```text
BugSphere-Bug-Tracker/
│
├── app.py                  # Main Flask application & API routes
├── requirements.txt        # Python dependencies
└── templates/
    └── index.html          # Frontend UI (Login, Dashboard, JS logic, Styles)

```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://www.google.com/search?q=https://github.com/yourusername/BugSphere-Bug-Tracker/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

*Built with ❤️ for better bug tracking.*

```

```
