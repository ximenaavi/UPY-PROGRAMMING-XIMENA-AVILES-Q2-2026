
This repository contains the programming classwork for the second semester at Universidad Politécnica de Yucatán (UPY).

# CLASSWORK08 - Numerical Integration

The Classwork08  folder was added with the program classwork08.py, the pseudocode integration.txt, and the flowchart Flowchart_Classwork08.png.

The program calculates approximations of definite integrals using numerical methods.

Included files:

1. integration.txt
   Contains the complete pseudocode following the class rules:
   - Simple English.
   - Uses `<-` for assignments.
   - Uses `#` for comments.
   - Does not contain Python syntax.

2. Flowchart_Classwork08.png  
   Contains the exported flowchart as an image.  
   The diagram shows:
   - The iteration flow of each method.
   - The decision between the three available modes.

3. classwork08.py
   Functional Python program with comments for:
   - IPO Specification
     
# CLASSWORK09 - Spanish Verb Conjugator

The Classwork-09-Spanish-Verb-Conjugator folder was added with the program spanish_verb_conjugator.py, the pseudocode file cw09PPP.txt, and the corresponding flowchart, cw09flowchart.png. The program conjugates regular Spanish verbs in the present tense.
The program prompts the user for a regular Spanish verb and conjugates it for all pronouns:

Reads the verb entered by the user.
Separates the stem from the ending (-ar, -er, -ir).
Applies the corresponding endings based on the verb type.
Prints the full conjugation.

Included Files

1.spanish_verb_conjugator.py

   Simple program that conjugates the verb and gives you a sentence.

2.cw09PPP.txt

   Contains the complete pseudocode following class rules:
   
   Simple English.
   Uses <- for assignments.
   Uses # for comments.
   Does not contain Python syntax.

3.cw09flowchart.png
  
   Flow diagram showing the program logic: reading the verb, separating the stem and ending, selecting the ending type based on -ar, -er, or -ir, and the print loop for    each pronoun.

# CLASSWORK10 - School Management System

The folder Classwork-10-School-Management-System was added with the program cw10-school-management-system.py, the pseudocode cw10PPP.txt and the corresponding cw10flowchart.png, which simulates a school management system with login and three distinct roles.

The program asks for a username and password, validates access, and displays a different menu depending on the role:

Reads the entered username and password.
Validates the credentials against the list of registered users.
Identifies the user's role (student, teacher, or coordinator).
Displays the menu corresponding to their role.
Executes the action based on the role: view grade report, grade students, or view general lists.

Files included:
1. cw10-school-management-system.py

   Functional Python program that implements the school management system.

2. cw10PPP.txt

   Contains the complete pseudocode following class rules:
   
   Simple English.
   Uses <- for assignments.
   Uses # for comments.
   Contains no Python syntax.


3. cw10flowchart.png

   Flowchart diagram showing the program logic: login validation,
   
   role selection, and the three possible paths (student grade report, teacher grade entry, and coordinator general lists).

Example usage:

Username: jperez
Password: 1234
Welcome, Juan Perez (student)
Grade report for Juan Perez
Mathematics: 8.5
Programming: 9.0
English: 7.5
Passed subjects: {'Mathematics', 'Programming'}
Pending subjects: {'English'}
Authorship statement
The content of this repository was personally developed by its author.

# CLASSWORK 11 - The Mandelbrot Set
The Classwork-11-Mandelbrot-Set folder was added with the program mandelbrot.py, the pseudocode file cw11PPP.txt, and the corresponding flowchart, cw11flowchart.png. The program generates the Mandelbrot set by reading configuration parameters from a file and calculating the number of iterations for each pixel in the image:
Reads the configuration parameters from config.txt (width, height, max iterations, and the real/imaginary bounds). Loops through every row and column of the image grid. Converts each pixel position into a complex number c. Iterates the Mandelbrot formula z = z² + c until the value escapes (abs(z) > 2) or the maximum iteration count is reached. Writes the row, column, and iteration count to a CSV file.
Included Files

1. classwork11-the-mandelbrot-set.py
   
   Program that reads the configuration, computes the Mandelbrot iterations for each pixel, and writes the results to mandelbrot.csv.

2. cw11PPP.txt

   Contains the complete pseudocode following class rules:
   Simple English. Uses <- for assignments. Uses # for comments. Does not contain Python syntax.

3. cw11flowchart.png

   Flow diagram showing the program logic: reading and parsing the config file, looping through rows and columns, calculating the complex number c, running the escape-      time iteration loop, and writing each result to the output file.

# CLASSWORK 12 - The Mandelbrot Set
The Classwork-12-Mandelbrot-Set folder was added with the program Classwork-12-The-Mandelbrot-Set.py, the pseudocode file cw12PPP.txt, a csv file called mandelbrot.py and a config.txt, with two images generated as a demostration, mandelbrot1.png, the "valley of hippocampus" and mandelbrot2.py.

1.Classwork-12-The-Mandelbrot-Set.py
   
   Program that reads the configuration, computes the Mandelbrot iterations for each pixel, and writes the results to mandelbrot.csv.

2. cw12PPP.txt

   Contains the complete pseudocode following class rules:
   Simple English. Uses <- for assignments. Uses # for comments. Does not contain Python syntax.

3. cw12flowchart.png

   Flow diagram showing the program logic based on the PPP.

4. config.txt

   A list of details needed to generate the images.

5. mandelbrot.csv

   The csv file that we created on the past assignment.
   
AI DISCLOSURE - No artificial intelligence tool was used for the generation of code, documentation or any other.

# CLASSWORK 14 & 15 - Error Handling

The pair of folders where added with the .py files of previous assignment to check and correct the code.

# CLASSWORK 15 - Sorting Algorithms
The Classwork-15-Sorting-Algorithms folder was added with the program sorting_algorithms.py, the pseudocode file sorting_algorithms_ppp.txt, and the corresponding flowchart, sorting_algorithms_flowchart.png. The program implements the bubble sort algorithm with a step-by-step visualization of the sorting process:
Generates a list of random numbers. Prints the list before sorting. Runs the bubble sort algorithm, comparing and swapping adjacent elements when out of order. Draws the bars on a canvas after each comparison, highlighting the pair being checked. Displays the final sorted list once the algorithm finishes.
Included Files

1.sorting_algorithms.py

   Functional Python program that implements bubble sort with animated bar visualization.

2.sorting_algorithms_ppp.txt

   Contains the complete pseudocode following class rules: Simple English. Uses <- for assignments. Uses # for comments. Does not contain Python syntax.

3.sorting_algorithms_flowchart.png

   Flow diagram showing the program logic: generating the list, the sweep and pair comparison loops, the swap condition, drawing the bars, and displaying the final          sorted result.
