# 🧮 BMI Calculator (Tkinter GUI)

A simple and colorful GUI-based BMI Calculator built using Python Tkinter.  
This application calculates Body Mass Index (BMI) using user-entered weight and height, displays the BMI category with color coding, and stores the results in a text file.

---

## 🚀 Features

- Calculate BMI using weight and height
- Color-coded BMI result display
- Automatic saving of BMI records
- Clear input fields with one click
- Simple, beginner-friendly Tkinter interface

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI Library)
- File Handling

---

## 📂 Project Structure

OIBSIP-Task1/
│
├── bmi_calculator.py
├── bmi_records.txt   (auto-created after first calculation)
└── README.md

---

## ⚙️ Installation & Running

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/OIBSIP-Task1.git  
cd OIBSIP-Task1

### 2️⃣ Run the Program

python bmi_calculator.py

---

## 📊 BMI Formula

BMI = weight (kg) / height (m²)

---

## 📌 BMI Categories

| BMI Range | Category |
|-----------|----------|
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal |
| 25 – 29.9 | Overweight |
| 30 and above | Obese |

---

## 📁 Data Storage

After each calculation, the result is saved automatically in:

bmi_records.txt

Each record contains:

Weight: value, Height: value, BMI: value, Category: value

---

## 🖥️ Interface Overview

- Input fields for weight and height
- Calculate button to compute BMI
- Clear button to reset inputs
- Color-coded result display
- “Stay Healthy!” footer message

---

## 🔮 Future Enhancements

- Unit conversion (kg/lb, meters/feet)
- BMI history viewer
- Graphical BMI chart
- Dark mode interface

---

## 👩‍💻 Author

Harshitha V

---

## 📜 License

This project is licensed under the MIT License.
