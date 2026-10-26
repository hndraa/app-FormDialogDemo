# Form Dialog Studio

**GUI DEVELOPMENT** | **DESKTOP APPLICATION** | **PYTHON ‧ PYQT5**

Form Dialog Studio is a desktop application that demonstrates interactive form input using dialog windows. Users can enter their name and student ID through text dialogs and select their favorite programming language through a selection dialog, all within a modern graphical interface.

## 01. Project Overview

### Description

Form Dialog Studio is a Python desktop application developed with PyQt5. It demonstrates how dialog-based input can be integrated into a form interface without allowing users to type directly into the displayed fields.

The application features a modern dark-themed interface, input validation, a profile summary, and a reset function.

### Objectives

- Demonstrate the use of input dialogs in desktop GUI development.
- Implement interactive form fields using PyQt5.
- Apply input validation before submitting form data.
- Improve user experience through consistent styling and a structured layout.

### Problem Statement

Basic forms often rely on direct text entry, which may not demonstrate how dialog-based input works. A separate dialog for each field provides a simple way to explore different input methods in graphical application development.

### Solution

Form Dialog Studio uses `QInputDialog.getText()` for text input and `QInputDialog.getItem()` for selecting a programming language. The entered information is displayed in read-only fields and summarized after successful submission.

### Key Features

- **Name Input:** Enter a name through a text dialog.
- **Student ID Input:** Enter a student ID through a text dialog.
- **Language Selection:** Choose from Python, Java, C++, JavaScript, and Go.
- **Read-Only Fields:** Prevent direct typing into the displayed form fields.
- **Input Validation:** Ensure all fields are completed before submission.
- **Profile Summary:** Display submitted information in a dedicated result panel.
- **Reset Form:** Clear all fields after confirmation.
- **Modern Interface:** Use a dark theme, styled cards, and interactive buttons.

## 02. Tech Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| GUI Framework | PyQt5 |
| Window and Widget Management | `QWidget`, `QLabel`, `QPushButton`, `QLineEdit`, `QFrame` |
| Form Layout | `QFormLayout`, `QVBoxLayout`, `QHBoxLayout` |
| Dialog Input | `QInputDialog` |
| Validation and Confirmation | `QMessageBox` |
| Interface Styling | Qt Style Sheets (`setStyleSheet()`) |
| Development Environment | Python and a compatible code editor |

## 03. Screenshots / Results

Capture the following application states and save the screenshots in the `screenshots/` directory.

### Main Interface

Displays the application header, personal information form, read-only input fields, action buttons, and profile summary panel.

<img width="1365" height="694" alt="image" src="https://github.com/user-attachments/assets/94f39415-c6be-4bd4-a593-47436ff1b4a5" />


### Name Input Dialog

Demonstrates entering a name through a text input dialog.

<img width="1365" height="700" alt="image" src="https://github.com/user-attachments/assets/d3f51b0b-23f9-4d81-bbb5-dd5988a5f7b1" />


### Student ID Input Dialog

Demonstrates entering a student ID through a text input dialog.

<img width="1365" height="698" alt="image" src="https://github.com/user-attachments/assets/5c35d865-3986-4048-b4b2-c240ddadcc6f" />


### Programming Language Selection

Displays the available programming languages in a selection dialog.

<img width="1365" height="697" alt="image" src="https://github.com/user-attachments/assets/8c4543b5-3e83-4e49-9d93-2e97d48f8f2a" />


### Submitted Profile

Displays the entered name, student ID, and favorite programming language after successful form submission.

<img width="1365" height="694" alt="image" src="https://github.com/user-attachments/assets/5c1c041a-ee76-4a78-af74-553f58d59e27" />


### Form Validation

Demonstrates the warning message displayed when the user submits the form without completing all required fields.

<img width="1365" height="696" alt="image" src="https://github.com/user-attachments/assets/485bff94-e1da-485b-8746-57609da4d024" />


### Reset Form

Demonstrates the confirmation dialog and the cleared form after the user confirms the reset action.

<img width="1365" height="694" alt="image" src="https://github.com/user-attachments/assets/e3faf173-a1f0-4345-a7d1-8e2b9fe361b2" />



## 04. Installation & Usage

### Prerequisites

- Python 3.10 or a compatible Python 3 version.
- pip package manager.
- PyQt5 library.

### Project Structure

```text
app-FormDialogDemo/
├── main.py
└── README.md
```

### Installation

**Step 1. Clone the repository**

```bash
git clone https://github.com/hndraa/app-FormDialogDemo.git
```

**Step 2. Navigate to the project directory**

```bash
cd app-FormDialogDemo
```

**Step 3. Install the dependency**

```bash
python -m pip install PyQt5
```

### Configuration

No additional configuration is required. The application interface is created directly in Python, so no external Qt Designer `.ui` file is needed.

### Run the Application

Execute the following command from the project directory:

```bash
python main.py
```

### Usage Instructions

1. Launch the application.
2. Click the **Full Name** field to open the name input dialog.
3. Enter your name and confirm the dialog.
4. Click the **Student ID** field to enter your student ID.
5. Click the **Favorite Language** field and select a programming language.
6. Click **Submit Profile** to validate and display the information.
7. If a required field is empty, complete it before submitting again.
8. Click **Reset Form** and confirm the action to clear all fields.

### Limitations

- Form data is stored temporarily in application memory.
- Submitted information is not saved to a database or external file.
- The available programming languages are predefined in the source code.

GitHub: [hndraa](https://github.com/hndraa)
