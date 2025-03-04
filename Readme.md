# To-Do List Application

This is a simple To-Do List web application built using **Flask** (for the backend), **HTML, CSS** (for the frontend), and a basic **Python script** for a CLI-based version. The application allows users to add tasks, mark them as done, and delete them.

## **Features**
- Add new tasks
- View pending and completed tasks
- Mark tasks as done
- Delete tasks
- Persistent UI using Flask & HTML/CSS

## **Installation & Setup**
### **1. Clone the repository**
```bash
git clone https://github.com/your-repo/todo-list.git     #your git repo link
cd todo-list
```

### **2. Create a virtual environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3. Install dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the application**
```bash
python app.py
```
The Flask server will start, and you can access the To-Do List at:
```
http://127.0.0.1:5000
```

## **Project Structure**
```
/todo-list
│── /static
│    ├── style.css
│── /templates
│    ├── index.html
│── app.py
│── requirements.txt
│── cli_todo.py   # Command-line version of To-Do List
│── README.md
```

## **CLI Version**
This project also includes a **command-line version** of the To-Do List (`cli_todo.py`).

To use the CLI-based To-Do List:
```bash
python cli_todo.py
```
You can:
- Add tasks
- View tasks
- Mark tasks as done
- Exit the program