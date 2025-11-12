# 🧭 Developers Guide — Student Dashboard Module

Welcome to the **School Management System (SMS)** project under **GoUpTech**.  
This guide explains how backend and frontend developers should collaborate on the `feature/student-dashboard` module efficiently.

---

## 🚀 Module Overview

**Module Name:** Student Dashboard  
**Feature Branch:** `feature/student-dashboard`  

### 🎯 Objective
To build a centralized student dashboard displaying:
- Student profile and attendance summary  
- Upcoming classes & assignments  
- Notifications & announcements  
- Fee status and academic performance overview  

---

## 🚀 Developer Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/GoUpTech/school-management-system.git
cd school-management-system
```

## 🌿 Branch Setup


## 🚀 0. Developer Quick Start

### Clone the Repository

```bash
git clone https://github.com/GoUpTech/school-management-system.git
cd school-management-system
```

Each developer should start from the latest `dev` branch.

```bash
# Switch to dev branch
git checkout dev
git pull origin dev

# Create your own feature branch
git checkout -b yourname-feature/student-dashboard-frontend
git push -u origin yourname-feature/student-dashboard-frontend
```

And make changes or create files and then commit all the changes and push into the github make sure you are into your branch to go your branch (git checkout your-branch-name)
```bash
git checkout your-branch-name
git add .
git commit -m "feat: your commit message"
git push
```

---

## ⚙️ For Backend Developers (Django)

### 🧩 Responsibilities
- Create or update APIs to serve dashboard data (profile, attendance, grades, etc.)
- Ensure authentication & role-based access for students.
- Optimize queries and secure endpoints.
- Write unit tests for your API logic.

### 🪶 Workflow

```bash
# Navigate to backend folder
cd backend

# Activate environment
source venv/bin/activate   # (Mac/Linux)
venv\Scripts\activate      # (Windows)

# Run server locally
python manage.py runserver
```

**Commit Example:**
```
feat(backend/student-dashboard): added API for attendance summary
```

### 📁 Suggested Folder Structure
```
backend/
 ├── student/
 │   ├── views.py
 │   ├── serializers.py
 │   ├── urls.py
 │   └── models.py
```

---

## 🎨 For Frontend Developers (React.js)

### 🧩 Responsibilities
- Build the student dashboard UI (cards, graphs, and sections).
- Integrate APIs from backend.
- Maintain consistent UI/UX with the overall SMS theme.
- Implement error handling and loading states.

### 🪶 Workflow

```bash
# Navigate to frontend folder
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

**Commit Example:**
```
feat(frontend/student-dashboard): added dashboard layout and API integration
```

### 📁 Suggested Folder Structure
```
frontend/
 ├── src/
 │   ├── modules/
 │   │   └── student-dashboard/
 │   │       ├── components/
 │   │       ├── pages/
 │   │       ├── hooks/
 │   │       └── services/
```

---

## 🧑‍💻 Team Workflow

1. **Pull latest dev changes**
   ```bash
   git checkout feature/student-dashboard
   git pull origin dev
   ```

2. **Make your updates**  
   Work only inside your module directories to avoid conflicts.

3. **Commit frequently with clear messages**

4. **Push your changes**
   ```bash
   git push origin feature/student-dashboard
   ```

5. **Create a Pull Request (PR)**  
   - Base branch: `dev`  
   - Compare branch: `feature/student-dashboard`  
   - Add reviewers (team lead + module partner)

---

## 🧩 PR Title Examples

- `feat(student-dashboard): implemented profile section`
- `fix(student-dashboard): API response error handled`
- `ui(student-dashboard): improved layout responsiveness`

---

## ✅ PR Review Checklist

Before submitting your PR:
- [ ] Code runs without errors locally  
- [ ] Followed folder structure and naming conventions  
- [ ] Proper commit messages  
- [ ] Tested APIs or components  
- [ ] Added comments where needed  

---

## 🧹 Merging Rules

- No one merges directly to `dev` or `main`
- PRs must be reviewed by **at least one team member**
- Once approved and tested, merge into `dev`

---

## 🪪 Notes

- Always sync with `dev` before new work.
- Keep commits small and meaningful.
- Communicate blockers early with the team lead.
- Tag your teammate or lead in PR if you need help.

---

### 🧠 Example Summary

| Role | Branch | Work | Example Commit |
|------|--------|------|----------------|
| Backend Dev | feature/student-dashboard | Django API for attendance | `feat(api): added attendance summary endpoint` |
| Frontend Dev | feature/student-dashboard | React Dashboard UI | `feat(ui): added student dashboard layout` |

---

### 🔁 When a Developer Returns to Continue Work

If you’ve already set up your local environment previously, here’s what to do when you come back after a break 👇

1. Navigate to the project
   ```bash
   cd /path/to/school-management-system
   ```

2. Activate your virtual environment
   ```bash
   # For backend (Django)
      cd backend
      source venv/bin/activate   # (Mac/Linux)
   # or
      venv\Scripts\activate      # (Windows)
   ```

3. Update code with latest changes
   ```bash
   git checkout feature/student-dashboard
   git pull origin dev
   ```

4. Ensure dependencies are up to date
   ```bash
   # Backend
   pip install -r requirements.txt

   # Frontend
   cd ../frontend
   npm install
   ```

5. Run your servers
   ```bash
   # Backend
   python manage.py runserver

   # Frontend
   npm start
   ```

✅ You’re now synced and ready to continue development exactly where you left off.

```bash
# move to the dev branch
git checkout dev
git pull origin dev

# if you are working different branch then switch to that branch
git checkout branch-name
git pull origin branch-name

# after changing/creatting/modifying the files commit the code on github by doing these commands
git add .
git commit -m "message for chnages"
git push
```

> 🏁 **Goal:** Smooth and modular development of the feature of School-Managements-System — clean commits, independent work, and seamless integration.

**Organization:** GoUpTech  
