KEY FEATURES
Dynamic Cutoffs: The system uses a dictionary to store branch names and their required percentage, making it easy to update criteria.
Input Validation: The program ensures that the percentage entered is a real number between 0 and 100.
Error Handling: It uses try-except blocks to prevent crashes if the user enters text instead of numbers.
Smart Search: Users can type partial names (e.g., "Mech") to select "Mechanical Engineering."
Unique ID Generation: Upon confirmation, the system generates a random Application ID using Python's random library.

HOW IT WORKS
Input: The system asks for the student's name and 12th-grade percentage.
Validation: It checks if the input is a valid number. If not, it asks the user to retry.
Processing: It loops through the available branches. If Student Marks >= Cutoff, the branch is added to the eligible list.
Selection: The user selects a branch from the list.
Output: The system prints an Admission Receipt with a unique ID and the fee amount.

HOW TO RUN THE PROJECT

Step 1: Ensure Python 3.x is installed on your computer.

Step 2: Save the code file as admission_system.py.

Step 3: Open your terminal or command prompt.

Step 4: Navigate to the folder where the file is saved.

Step 5: Run the command: python admission_system.py

FUTURE SCOPE Currently, the system prints data to the console. Future improvements could include saving admission records to a text file (File Handling) so data isn't lost, or building a graphical user interface (GUI) using Tkinter.