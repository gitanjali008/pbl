# 🧠 NLP_COMPILER

**NLP_COMPILER** is a Natural Language Processing–based compiler that takes English instructions and generates working code. The goal is to allow users to write programming logic using plain English, and the system understands and converts it into Python or LLVM IR code.

---

## 📌 What This Project Does

This system allows a user to:
- Type a natural language instruction (e.g., "Create a function that calculates the factorial of a number")
- Process the instruction using **NLP**
- Generate Python code or low-level LLVM IR
- Display the output code in a web-based interface

---

## 🌟 Features

✅ Converts plain English into code  
✅ Supports Python and LLVM IR  
✅ Flask-based web interface  
✅ Organized backend and frontend  
✅ Uses modern NLP libraries like spaCy and transformers

---

## 🗂️ Project Directory Structure

Below is the full structure of the **NLP_COMPILER** project:

```plaintext
NLP_COMPILER/
├── 📁 code_generator/         → 🔧 Creates code based on logic (Python/LLVM)
│   ├── __init__.py
│   └── python_generator.py    → Python code generation logic

├── 📁 compiler/              → 🧮 Compiler backend – handles LLVM logic
│   ├── __init__.py
│   └── llvm_compiler.py       → LLVM IR generation module

├── 📁 compiler_ui/           → 🖥️ Frontend + Flask backend
│   ├── __init__.py
│   ├── server.py              → Flask server handling API requests
│   ├── index.html             → HTML web interface
│   ├── script.js              → JavaScript to send/receive data from server
│   └── style.css              → Styling for the webpage

├── 📁 nlp_processing/        → 🧠 Natural Language Understanding
│   ├── __init__.py
│   └── parser.py              → Main NLP logic to interpret user input

├── main.py                   → 🚀 Entry point if running the project directly
├── temp.py                   → 🧪 Temporary or testing code
├── README.md                 → 📘 This file with full documentation
└── requirements.txt          → 📦 List of all required Python libraries
