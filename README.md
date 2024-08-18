Library System Application
===========================

This is a simple library management system that allows users to create accounts, add books, borrow books, and return books. This application is packaged using PyInstaller.

Prerequisites:
--------------
1. Python 3.x installed on your system.
2. `pip` (Python package installer) installed.

Setup Instructions:
-------------------
1. Clone the repository or download the `main.py` script to your local machine.

2. Open a terminal (Command Prompt, PowerShell, or a terminal emulator on Linux/Mac).

3. Navigate to the directory where `main.py` is located.

4. Create a virtual environment:
   ```
   python -m venv myenv
   ```

   or

   ```
   python3 -m venv myenv
   ```

5. Activate the virtual environment:
   - On Windows:
   ```
   myenv\Scripts\activate
   ```
   - On MacOS/Linux:
   ```
   source myenv/bin/activate
   ```

6. Install the required packages:
   ```
   pip install pyinstaller
   ```

7. Run the PyInstaller to create an executable:
   ```
   pyinstaller --onefile main.py
   ```

8. After the build process completes, you will find the executable file in the `dist` directory.

Running the Application:
------------------------
1. Navigate to the `dist` directory:
   ```
   cd dist
   ```

2. Run the executable:
- On Windows:
  ```
  main.exe
  ```
- On MacOS/Linux:
  ```
  ./main
  ```

3. Follow the on-screen menu to create accounts, add books, borrow books, and return books.

Testing the Application:
------------------------
The `test-library-system.py` script includes unit tests using the `unittest` framework.

1. Ensure the virtual environment is activated.

2. Run the tests:
   ```
   python test-library-system.py
   ```
   or
   ```
   python3 test-library-system.py
   ```

The tests will automatically run, and the results will be displayed in the terminal.

Exiting the Application:
------------------------
To exit the application, simply select the '0' option from the main menu.

Deactivating the Virtual Environment:
-------------------------------------
After you are done, you can deactivate the virtual environment:
   ```
   deactivate
   ```
Using Build script:
-------------------
For Unix-like systems, you need to make the build.sh script executable:
   ```
   chmod +x build.sh
   ```
Run the script
   ```
   ./build.sh
   ```
For Windows systems, simply double-click the build.bat file or run it from the Command Prompt:
   ```
   build.bat
   ```

Enjoy using the Library System Application!
