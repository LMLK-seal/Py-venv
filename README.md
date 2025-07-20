# 🐍 Python Virtual Environment Setup Tool

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg?logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows-blue.svg?logo=windows&logoColor=white)](https://microsoft.com/windows)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A simple, user-friendly Python script that automates the creation and activation of Python virtual environments on Windows systems.

## ✨ Features

- 🔧 **Automatic Detection**: Checks if a virtual environment already exists
- 🆕 **Smart Creation**: Creates a new `.venv` directory if none exists
- 🚀 **Easy Activation**: Launches a new Command Prompt with the virtual environment pre-activated
- 🛡️ **Error Handling**: Comprehensive error messages and graceful failure handling
- 💻 **Windows Optimized**: Specifically designed for Windows Command Prompt and PowerShell users

## 📋 Prerequisites

- Python 3.6 or higher installed on your system
- Python added to your system's PATH environment variable
- Windows operating system

## 🚀 Quick Start

1. **Download** the `venv.py` script to your project directory
2. **Run** the script:
   ```cmd
   python venv.py
   ```
3. **Enjoy** your new Command Prompt window with an activated virtual environment!

## 📁 Project Structure

```
your-project/
├── venv.py          # The setup script
├── .venv/           # Virtual environment (created automatically)
│   ├── Scripts/
│   ├── Lib/
│   └── ...
└── your_files...    # Your project files
```

## 🎯 How It Works

1. **Environment Check**: The script first checks if a `.venv` directory exists in your current working directory
2. **Creation Phase**: If no virtual environment is found, it creates one using `python -m venv .venv`
3. **Activation**: Opens a new Command Prompt window with the virtual environment automatically activated
4. **Ready to Use**: You can now install packages and run your Python code in an isolated environment

## 💡 Usage Examples

### First Time Setup
```cmd
C:\MyProject> python venv.py
--- Virtual Environment Setup for Windows ---
Virtual environment '.venv' not found.
Creating a new virtual environment... (This may take a moment)
Virtual environment created successfully!

Launching a new Command Prompt with the virtual environment activated...
This script window will now close.
```

### Subsequent Runs
```cmd
C:\MyProject> python venv.py
--- Virtual Environment Setup for Windows ---
Virtual environment '.venv' already exists. Skipping creation.

Launching a new Command Prompt with the virtual environment activated...
This script window will now close.
```

## ⚡ Benefits of Virtual Environments

- **🔒 Isolation**: Keep project dependencies separate
- **🧹 Clean System**: Avoid cluttering your global Python installation
- **📦 Version Control**: Manage different package versions per project
- **🤝 Team Collaboration**: Ensure consistent development environments

## 🛠️ Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `'python' command not found` | Ensure Python is installed and added to PATH |
| `Permission denied` | Run Command Prompt as Administrator |
| `Virtual environment creation failed` | Check available disk space and permissions |

### Error Messages

- **Python not in PATH**: The script will display a helpful message about adding Python to your system PATH
- **Creation failures**: Detailed error information is provided to help diagnose issues
- **Missing activation script**: The script verifies the virtual environment was created correctly

## 🔧 Customization

You can easily modify the script to suit your needs:

```python
# Change the virtual environment directory name
VENV_DIR = "my_custom_venv"  # Instead of ".venv"
```

## 📝 Requirements

- Windows 7/8/10/11
- Python 3.6+
- Standard Python `venv` module (included with Python 3.3+)

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with Python's built-in `venv` module
- Designed for the Windows development community
- Inspired by the need for simpler virtual environment management

---

**Happy Coding!** 🎉

*Made with ❤️ for Python developers on Windows*
