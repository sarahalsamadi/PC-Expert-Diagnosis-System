# 💻 Computer Diagnosis Expert System

A Python-based **Knowledge-Based System (KBS)** designed to act as a technical assistant for diagnosing computer problems. The system uses a rule-based approach to match symptoms with proven solutions.

## 🚀 Overview
This system simulates an expert's logic by:
- **Diagnosing Issues:** Analyzing user-described symptoms to provide troubleshooting steps.
- **Dynamic Learning:** Allowing users to expand the knowledge base by adding new problems and solutions during runtime.
- **Persistent Memory:** Saving all data to a `knowledge_base.json` file to maintain intelligence across sessions.

## 🛠️ Tech Stack
- **Language:** Python 
- **Data Format:** JSON (for the Knowledge Base)
- **Logic:** Rule-based matching & Inference.

## 📊 Project Workflow
1. **Loading Knowledge:** On startup, the system reads from `knowledge_base.json`.
2. **User Interaction:** A CLI menu offers options to diagnose, add, or view symptoms.
3. **Inference Engine:** The system searches for keywords in the user's description to find the most relevant fix.
4. **Data Management:** New entries are automatically formatted and appended to the local database.

## ⚙️ Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/PC-Expert-Diagnosis-System.git](https://github.com/YourUsername/PC-Expert-Diagnosis-System.git)

2. **Run the system:**
   ```bash
   python knowledge_system.py

3. **Interact:**
   Follow the on-screen menu to start diagnosing or updating the system.

## 📝 Key Features
. **Smart Matching:** Can identify potential issues even if the user's description isn't an exact match.
. **Extensible:** The "Add Symptom" feature allows the system to grow its intelligence over time.
. **Zero Dependencies:** Runs on pure Python without needing external installations, making it highly portable.
