Library System Application
==========================

This library management project will create to study with DevOps Tools

Library management project was created to help librarian manage a lot ok book in library.

Features

    Create an account
    Borrow and return book
    Add and remove book
    Borrow and return history

Python is the computer language that use to develops.

How install Application
==========================

This document provides instructions on how to run the build script to create an executable for the Library System application.

Requirements:
-------------
- Python 3.x
- pip (Python package installer)
- pyinstaller (can be installed via pip)

Step-by-Step Instructions:
--------------------------

1. Install Python:
   Ensure that Python 3.x is installed on your system. You can download it from https://www.python.org/.

2. Install pip:
   pip is usually included with Python. To check if pip is installed, run:

If pip is not installed, follow the instructions at https://pip.pypa.io/en/stable/installation/.

3. Install pyinstaller:
Open your terminal or command prompt and run:

4. Save the Script:
Save the provided `library_system.py` script in a directory of your choice.

5. Create the Executable:
Open your terminal or command prompt, navigate to the directory containing `library_system.py`, and run:

This will create a standalone executable file.

6. Locate the Executable:
After running pyinstaller, a `dist` directory will be created in the same directory as `library_system.py`. Inside the `dist` directory, you will find the executable file `library_system`.

7. Run the Executable:
Navigate to the `dist` directory and run the executable:

8. Testing the Application:
To run the test cases, you can run the script directly using Python: