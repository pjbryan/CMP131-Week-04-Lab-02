# CMP 131 – Python Programming


> **Required file location:** Keep every Python file directly in the repository root. Do not create a `src` folder.

## Week 4 – Lab 2: Basic Arithmetic Operations

### Learning Objectives

After completing this lab, students should be able to:

* Accept numeric input from the user.
* Convert user input to an appropriate numeric data type.
* Store values in variables.
* Perform basic arithmetic calculations.
* Calculate the average of two numbers.
* Display results using clear labels.
* Format numeric results to two decimal places.
* Use comments to explain the major parts of a program.

## Assignment Overview

Create a Python program that asks the user to enter two numbers.

The program must use the two numbers to calculate and display:

* Addition
* Subtraction
* Multiplication
* Division
* Power
* Average

The program will display the results of all six operations.

Do not use:

* `if` statements
* `elif` statements
* `else` statements
* Loops
* Functions
* A numbered selection menu

This assignment focuses only on user input, variables, arithmetic operators, comments, and formatted output.

## Required Python File

Create a Python file named:

`arithmetic_operations.py`

Include a comment header at the beginning of the file containing:

* Student name
* Course number
* Week number
* Lab number
* Assignment title
* Date

## Part 1: Program Title

Display a descriptive title when the program begins.

The title should clearly indicate that the program performs basic arithmetic operations.

Use appropriate spacing or decorative characters to make the title easy to identify.

Possible decorative characters include:

* Equal signs
* Hyphens
* Asterisks
* Number signs

## Part 2: User Input

Ask the user to enter:

* The first number
* The second number

The numbers may contain decimal values.

Convert both values to an appropriate numeric data type before using them in calculations.

For this assignment, the user must enter a nonzero value for the second number so the division calculation can be completed.

## Part 3: Addition

Add the first number and the second number.

Display the result using a clear label.

## Part 4: Subtraction

Subtract the second number from the first number.

Use the following relationship:

**Subtraction result = First number − Second number**

Display the result using a clear label.

## Part 5: Multiplication

Multiply the first number by the second number.

Display the result using a clear label.

## Part 6: Division

Divide the first number by the second number.

Use the following relationship:

**Division result = First number ÷ Second number**

The second number must not be zero.

Division-by-zero validation is not required because conditional statements are not used in this assignment.

## Part 7: Power

Raise the first number to the power of the second number.

Use the following relationship:

**Power result = First number raised to the power of the Second number**

Use Python’s exponent operator to perform the calculation.

## Part 8: Average

Calculate the average of the two numbers.

Use the following relationship:

**Average = (First number + Second number) ÷ 2**

Make sure the addition is performed before the division.

## Part 9: Display the Results

Display all six calculation results:

* Addition result
* Subtraction result
* Multiplication result
* Division result
* Power result
* Average

The output must include:

* A descriptive heading.
* The two numbers entered by the user.
* A clear label for every result.
* Blank lines between major sections.
* Consistent capitalization and spacing.
* Results formatted to two decimal places.

Students should create their own output layout. The instructor is not providing completed Python code or an exact output design.

## Part 10: Code Comments

Use comments to identify and explain the major sections of the program.

Include comments for:

* The comment header
* The program title
* The user-input section
* The arithmetic-calculation section
* The output section

Comments should briefly explain the purpose of each section. They do not need to explain every individual statement.

## Required Testing

Test the program using the following values:

* First number: `12`
* Second number: `4`

Confirm that the program displays:

* Addition: `16.00`
* Subtraction: `8.00`
* Multiplication: `48.00`
* Division: `3.00`
* Power: `20736.00`
* Average: `8.00`

Also confirm that:

* All six results are displayed.
* Each result has a clear label.
* Each result displays two decimal places.
* The program runs without errors.

## Functional Requirements

When the program runs, it must:

* Display a descriptive program title.
* Ask the user to enter two numbers.
* Convert both inputs to an appropriate numeric data type.
* Add the two numbers.
* Subtract the second number from the first number.
* Multiply the two numbers.
* Divide the first number by the second number.
* Raise the first number to the power of the second number.
* Calculate the average of the two numbers.
* Display all six results.
* Format the results to two decimal places.
* Include comments explaining the major sections.
* Run completely without errors.

## General Requirements

* Use Python to complete the assignment.
* Save the program as `arithmetic_operations.py`.
* Use meaningful variable names.
* Accept two numeric values from the user.
* Use arithmetic operators to perform the calculations.
* Do not use conditional statements.
* Do not use loops or functions.
* Do not create an operation-selection menu.
* Display all six calculation results.
* Use a nonzero value for the second number.
* Format all results to two decimal places.
* Use clear prompts, headings, and labels.
* Include the required comment header.
* Include comments throughout the program.
* Test the program using the required values.
* Make sure the program runs without errors.
* Follow the course AI-use policy.
* Record any AI assistance in `AI-Use-Report.md`.

## Required Organization

Organize the assignment as follows:

* `Week-04`

  * `Lab-02`

    * `CMP131-Week-04-Lab-0.md2.md`
    * `AI-Use-Report.md`
    * `src`

      * `arithmetic_operations.py`

## Submission Requirements

Submit or push the complete `Lab-02` folder.

The submission must include:

* `arithmetic_operations.py`
* `AI-Use-Report.md`

Before submitting, verify that:

* The filename is exactly `arithmetic_operations.py`.
* The required comment header is included.
* The program asks the user for two numbers.
* Both inputs are converted to an appropriate numeric data type.
* All six calculations are performed.
* All six results are displayed.
* Subtraction uses the first number minus the second number.
* Division uses the first number divided by the second number.
* The power calculation works correctly.
* The average calculation works correctly.
* Results are formatted to two decimal places.
* Comments explain the major sections.
* No conditional statements, loops, or functions are used.
* The program runs without errors.
* The AI-use report is complete.
* The latest work has been committed and pushed to GitHub.

## Suggested Git Commit Messages

* Create Week 4 Lab 2 arithmetic program
* Add user input and variables
* Add arithmetic calculations
* Format calculation results
* Add program comments
* Test Week 4 arithmetic program
* Complete Week 4 Python lab

---

## GitHub Starter Repository

Use the following public starter repository:

[CMP131-Week-04-Lab-02](https://github.com/ahedhli12/CMP131-Week-04-Lab-02)

### Getting Started

1. Open the starter repository using the link above.
2. If **Use this template** is available, select **Use this template → Create a new repository**.
3. Choose your personal GitHub account as the owner.
4. Name your repository `LastName-FirstName-CMP131-Week-04-Lab-02`.
5. Set your repository to **Public**.
6. Clone your own newly created repository—not the instructor’s starter repository.
7. Open the entire cloned folder in Visual Studio Code.
8. Complete and test every required Python file.
9. Commit and push your work to GitHub.
10. Verify that your latest files appear on GitHub.
11. Complete `AI-Use-Report.md`.
12. Submit the required work through Blackboard Ultra and include your public repository link when requested.

### Required Repository Files

- `CMP131-Week-04-Lab-02.md`
- `AI-Use-Policy.md`
- `AI-Use-Report.md`
- `arithmetic_operations.py`

### Before You Submit

- [ ] All required Python files are in the repository root.
- [ ] Every required filename is exact.
- [ ] Each program runs successfully.
- [ ] Required tests and screenshots are complete.
- [ ] `AI-Use-Report.md` is complete and accurate.
- [ ] The latest commit is visible on GitHub.
