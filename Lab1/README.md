# Linux Fundamentals Lab

## Objective
This lab demonstrates basic Linux command-line operations, including file management, text processing, shell scripting, and environment variable handling.

---

## Repository Structure

```
linux_lab/
├── students.txt
├── script.sh
├── output.txt
└── README.md
```

---

## Task 1: Directory and File Operations

Performed the following operations:

- Created a directory named `linux_lab`
- Navigated into the directory
- Created the following files:
  - `students.txt`
  - `script.sh`
  - `output.txt`
- Displayed the current working directory
- Listed all files in the directory

### Commands Used

```bash
mkdir linux_lab
cd linux_lab
touch students.txt script.sh output.txt
pwd
ls
```

---

## Task 2: Create and Edit a File

Added the following student records to `students.txt`:

```
Alice,Python
Bob,Docker
Charlie,Linux
David,Python
Eva,Docker
Frank,Linux
Grace,Python
Henry,Docker
```

### Commands Used

```bash
nano students.txt
cat students.txt
```

---

## Task 3: Text Processing

Performed the following operations:

- Displayed all Python records
- Displayed all Docker records
- Displayed all Linux records
- Counted the number of Python records
- Saved the Python count to `output.txt`
- Displayed the contents of `output.txt`

### Commands Used

```bash
grep "Python" students.txt
grep "Docker" students.txt
grep "Linux" students.txt
grep -c "Python" students.txt > output.txt
cat output.txt
```

---

## Task 4: Shell Scripting

Created a shell script (`script.sh`) to display:

- Welcome message
- Current User
- Current Working Directory
- Current Date and Time

### Example Script

```bash
#!/bin/bash

echo "Welcome to Linux Lab"
echo "Current User: $USER"
echo "Current Working Directory: $(pwd)"
echo "Current Date and Time: $(date)"
```

### Run the Script

```bash
chmod +x script.sh
./script.sh
```

---

## Task 5: Environment Variables

Created and exported an environment variable:

```bash
export COURSE_NAME="Linux Fundamentals"
```

Displayed its value:

```bash
echo $COURSE_NAME
```

Verified the variable:

```bash
printenv | grep COURSE_NAME
```

Updated `script.sh` to include:

```bash
echo "Course Name: $COURSE_NAME"
```

---

## Files Included

- **students.txt** – Student records
- **script.sh** – Linux shell script
- **output.txt** – Count of Python records
- **README.md** – Documentation for the lab

---

## Learning Outcomes

After completing this lab, I learned how to:

- Create and navigate directories
- Create and manage files
- Edit text files using Linux editors
- Process text using `grep`
- Count matching records
- Redirect command output to files
- Write and execute shell scripts
- Create and use environment variables

---

## Author

**Nithiyasri R**
