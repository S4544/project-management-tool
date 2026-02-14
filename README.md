# 📋 Project Management Tool

A full-stack Django web application for efficient project and task management with real-time collaboration features.

## 📑 Table of Contents
- [Features](#-features)
- [Technical Stack](#-technical-stack)
- [Installation & Setup](#-installation--setup)
- [Project Structure](#-project-structure)
- [Usage](#-usage)
- [Contributing](#-contributing)

---

## ✨ Features

### Core Functionality
- **Project Dashboard** - Visual progress tracking with automated progress bars for each project
- **Kanban Board View** - Customizable workflow stages (To Do, In Progress, Done)
- **Priority Color-Coding** - Color-coded task borders based on priority levels
  - 🔴 Red: High Priority
  - 🟡 Yellow: Medium Priority
  - 🟢 Green: Low Priority
- **Full CRUD Operations** - Create, Read, Update, and Delete projects and tasks with confirmation dialogs
- **Collaboration System** - Integrated comment threads for team communication and task tracking

---

## 🛠️ Technical Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python 3.x, Django 5.x (MTV Architecture) |
| **Frontend** | HTML5, CSS3, Bootstrap 5 (Responsive Design) |
| **Database** | SQLite3 (Relational Database) |
| **Authentication** | Django Contrib Auth (Session-based) |

---

## ����️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/S4544/project-management-tool.git
cd project-management-tool
## 🏗️ Installation
1. Clone the repo: `git clone  https://github.com/S4544/project-management-tool.git
cd project-management-tool
2. Install Django: `pip install django`
3. Run migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver`
