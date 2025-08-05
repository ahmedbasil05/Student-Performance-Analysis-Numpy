
# Student Performance Analysis System Using NumPy

This project implements a comprehensive Student Performance Report system using Python's **NumPy** library. It simulates exam scores for 100 students across five subjects and provides detailed data analysis including subject-wise statistics, student rankings, failure detection, and identification of best/worst performing subjects.

---

## Features

- Dynamic generation of student roll numbers and names  
- Simulation of random exam scores within a realistic range (35-99)  
- Calculation of key statistics per subject: average, standard deviation, maximum, and minimum  
- Ranking students based on total and average scores  
- Identification of students failing in one or more subjects  
- Determination of best and worst performing subjects based on average scores  
- Clean, modular code with clear single-line comments and readable variable names  

---

## NumPy Concepts Covered

- **Array creation and manipulation:** Use of `arange`, list comprehensions, and multidimensional arrays  
- **Indexing and slicing:** Row/column access and Boolean masking for data filtering  
- **Mathematical and statistical functions:** `mean()`, `std()`, `max()`, `min()`, and others for analysis  
- **Sorting and ranking:** Using `argsort()` for ordering students by scores  
- **Boolean logic & filtering:** Conditional filtering to identify failed students  
- **Vectorized operations:** Efficient computations without explicit loops  
- **Real-world data simulation:** Handling student records and performance analytics  

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system.  
- NumPy library installed.

If you do not have NumPy installed, you can install it via pip:

```bash
pip install numpy
```

---

### Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/your-username/student-performance-analysis-numpy.git
```

This command will download the repository to your local machine.

---

### Navigate to the Project Directory

Change directory to the cloned repository folder:

```bash
cd student-performance-analysis-numpy
```

---

### Run the Project

Execute the Python script:

```bash
python student_performance.py
```

This will run the student performance report system and display analysis output in the terminal.

---

## Project Structure

```
student-performance-analysis-numpy/
│
├── student_performance.py    # Main Python script containing all functions and program flow
├── README.md                 # Project overview and instructions (this file)
└── .gitignore                # Git ignore file (optional)
```

---

## Example Output

```
=== Student Performance Report ===
Total Students: 100
Subjects: Math, Physics, Chemistry, English, CS

Subject-wise Statistics:
 Math: Avg = 66.43, Std Dev = 16.81, Max = 98, Min = 35
 Physics: Avg = 67.25, Std Dev = 18.12, Max = 99, Min = 35
 Chemistry: Avg = 67.50, Std Dev = 16.03, Max = 98, Min = 35
 English: Avg = 66.80, Std Dev = 16.99, Max = 98, Min = 35
 CS: Avg = 66.79, Std Dev = 16.99, Max = 98, Min = 35

Top 5 Students:
 1. Student_45 - Total: 460, Average: 92.00
 2. Student_12 - Total: 458, Average: 91.60
 3. Student_78 - Total: 455, Average: 91.00
 4. Student_5 - Total: 450, Average: 90.00
 5. Student_99 - Total: 448, Average: 89.60

Students who failed in at least one subject: 12
 - Student_4
 - Student_23
 - Student_56
 - Student_67
 - Student_88
 ...

Best subject: Chemistry with avg score 67.50
Worst subject: Math with avg score 66.43

=== End of Report ===
```

---

## Author

[Ahmed Basil] – [Your LinkedIn Profile](https://www.linkedin.com/in/ahmed-basil/)  

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Thank you for checking out this project! Feel free to open issues, suggest improvements, or contribute.

