# 🔐 Access Guard

**A Python-based access control system for managing roles, employees, and access logs.**

Access Guard is a beginner-friendly Python project that demonstrates how an access control system can manage users, assign roles, and maintain records. It uses file handling to store information and provides a simple command-line interface.

## 🚀 Features

- 🔑 **Role-Based Access Control** — Organizes access based on assigned roles.
- 👥 **Employee Management** — Maintains employee records.
- 📋 **Access Logs** — Stores access-related records for reference.
- 💾 **File Handling** — Uses files to persist data between program runs.
- 🎨 **Command-Line Interface** — Includes a customized terminal banner and formatted output.

## 🛠️ Technologies Used

- Python
- File Handling
- Data Management
- Command-Line Interface (CLI)

## 📂 Project Structure

```text
Access-Guard/
├── access_guard.py
├── employees.txt
├── roles.txt
├── logs.txt
└── README.md
```

*Note: The file names and structure above are illustrative. Adjust them to match your actual repository.*

## ⚙️ Getting Started

### Prerequisites

- Python 3.x
- A code editor such as VS Code

### Installation

1. Clone this repository:

   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd Access-Guard
   ```

3. Run the program:

   ```bash
   python access_guard.py
   ```

## 💡 Learning Outcomes

Through this project, I practised:

- Python fundamentals and program structure
- File handling for storing and retrieving data
- Organizing employee and role information
- Maintaining access logs
- Building a user-friendly CLI application

## 🔮 Future Improvements

- Implement stronger authentication mechanisms.
- Add more granular permissions for different roles.
- Introduce improved input validation and error handling.
- Develop a graphical user interface.
- Add more detailed access reports and audit features.

## 👨‍💻 Author

**Shashi Rama Krishna Kadali**

First-Year Computer Engineering Student  
MIT Academy of Engineering (MIT AOE)

---

*Built as a hands-on project to strengthen my Python programming and problem-solving skills.*


# 📚 Library Management System

**A Python-based application to manage books, users, and book issuing records.**

The Library Management System is a command-line application developed using Python. It helps organize library operations by managing book records, user information, and issued books, with data stored in text files for persistence.

## 🚀 Features

- 📖 **Book Management** — Add and manage books with unique Book IDs.
- 👥 **User Management** — Maintain user records with unique User IDs.
- 🔄 **Book Issuing** — Record books issued to library users.
- 💾 **File Handling** — Store and retrieve records using text files.
- 🎨 **CLI Interface** — Provides a customized terminal interface.
- 🧩 **Modular Code** — Organizes functionality into manageable sections.

## 🛠️ Technologies Used

- Python 3
- File Handling
- `colorama` — For colored terminal output
- `ast` — For safely parsing supported Python literal data formats

## 📂 Project Structure

```text
Library-Management-System/
├── library_management.py
├── books.txt
├── users.txt
├── issued.txt
└── README.md
```

*Note: Adjust the file and folder names to match your actual repository.*

## ⚙️ Getting Started

### Prerequisites

- Python 3.x
- VS Code or another Python editor

### Installation

**1. Clone the repository**

```bash
git clone <your-repository-url>
```

**2. Navigate to the project folder**

```bash
cd Library-Management-System
```

**3. Install the required dependency**

```bash
pip install colorama
```

**4. Run the application**

```bash
python library_management.py
```

## 🆔 ID System

The application uses unique identifiers to organize records:

- **Book IDs:** Start from `101`
- **User IDs:** Start from `1001`

These IDs help distinguish books and users within the system.

## 📚 Learning Outcomes

This project helped me practise:

- Python programming and problem-solving
- File handling and persistent data storage
- Working with dictionaries and structured data
- Using Python modules and external libraries
- Organizing records and implementing library workflows
- Creating a more readable command-line interface

## 🔮 Future Improvements

- Add book search and filtering.
- Implement book return and availability tracking.
- Introduce overdue tracking and fine calculation.
- Add authentication for librarians and users.
- Develop a graphical user interface.
- Migrate from text files to an SQL database.

## 👨‍💻 Author

**Shashi Rama Krishna Kadali**

First-Year Computer Engineering Student  
MIT Academy of Engineering (MIT AOE)

---

*Built as a hands-on project to strengthen my Python programming, file handling, and application development skills.*
