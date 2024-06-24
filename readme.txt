Interactive Learning and Testing Tool
This program is designed to provide an interactive learning and testing experience. Users can authenticate using their email address, access learning materials,
take tests, view statistics, and receive results via email.

Features
*Email Authentication: Users authenticate using their email address, validated against a standard email pattern.
*User Validation: User details (name, surname, email) are validated against a CSV file (teams.csv) to assign them to a specific region and team lead.*
*Main Menu Options:
    1. Read Theory: Users can select from various topics and open corresponding theory documents (Word or PowerPoint).
    2. Test Mode: Users can take a random set of test questions, with multiple attempts allowed per question.
    3. View Statistics: Users can view their test results and percentages.
    4. Exit: Users can exit the program.
*Email Notification: Upon completing a test with a passing score (90% or higher), users receive an email with their results.

Components
*Modules and Libraries:
    1. re, os, sys, subprocess, random: Standard Python libraries for regular expressions, system operations, subprocess handling, and randomization.
    2. smtplib, email.mime: Libraries for sending email notifications.
    3. json, csv: Libraries for handling JSON and CSV files.
    4. dotenv: Library for loading environment variables from a .env file.
    5. datetime: Library for handling date and time operations.

*Functionality:
    1. File Handling: Opening and reading Word (.docx) and PowerPoint (.pptx) files using platform-specific subprocess calls (subprocess.Popen).
    2. Test Mode: Random selection of test questions, scoring, and saving results to a text file (results.txt).
    3. Email Integration: Sending test results via email using SMTP, with error handling for authentication and connection issues.
    4. Statistics: Viewing test results based on the user's email address.

Setup and Usage
*Environment Setup:
    1. Ensure Python and required libraries (dotenv, email, json, csv) are installed.
    2. Create a .env file with necessary environment variables (e.g., email credentials, region_lead name, surname and email address):

            GMAIL_EMAIL=name.surname@gmail.com
            GMAIL_PASSWORD=password
            AMERICA_LEAD = Name Surname
            AMERICA_LEAD_EMAIL = email
            EMEA_LEAD = Name Surname
            EMEA_LEAD_EMAIL = email
            APAC_MEA_LEAD = Name Surname
            APAC_MEA_LEAD_EMAIL = email

*Data Files:
    1. Prepare teams.csv with user details including name, surname, email, and region (EMEA, MEA_APAC or America):

            name,surname,email,region
            name,surname,name.surname@example.com,EMEA
            name,surname,name.surname@example.com,MEA_APAC
            name,surname,name.surname@example.com,America

    2. Ensure document files (*.docx, *.pptx) are structured as per the specified folder paths (capstone1.4).

*Execution:
    1. Run the Python script (capstone.py).
    2. Follow on-screen prompts to authenticate, select options from the main menu, and interact with the tool.

Error Handling
*Invalid Inputs: Checks and prompts users for correct inputs (e.g., email format, menu choices, file selections).
*File Existence: Verifies the existence of specified document files before attempting to open them.
*SMTP Errors: Handles SMTP authentication errors and exceptions during email sending.

Notes
*Ensure all necessary files (teams.csv, document files) are correctly structured and accessible.
*Customize email templates and content in send_email function as per organizational requirements.

Author
Developed by Renata Šapokienė
Date: 24.06.2024
