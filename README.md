# Capstone1.4
Learning and testing tool for new joiners in a team 
Design and implement an interactive learning & knowledge testing tool that allows new joiners in a team to learn and test their knowledge before starting to work
The requirements to implement are as follows:
When the program starts, the welcome text should be printed, user should be asked to enter name, surname, email address in order to identify which team lead should be assigned
and afterwards choose between the following modes:

Read theory;
Test mode;
View statistics;
Exit;

Theory mode:
User should be able to select topics for reading/learning by selecting different icons for each topic - Blocked orders, Credit limit assessments and Collections. After
selecting icon it should automatically go the related folder path of selected topic and open documentation;
After reading all the documentation user should go to the test mode.

Test mode:
User should get random 10 questions from data base;
After the test finished, user should be able to select either to repeat the test (if not passed) and get another random 10 quetions, or get results automatically
sent (if passed) to user's email, entered at the beginning and email cc to team lead (automatically identified by user's name which Team lead is assigned to each user).
Each test (passed or not) must be saved in view statistics mode - it must be saved the test date, time, questions given and the result ("correct" or "incorrect");
After each answer should follow confirmation "Correct!" or "Incorrect, please try again" and get the same question;
If user enters/select inncorect answer 3 times, the program should provide the correct answer and user should be able to move to the next question;
Passing score 90%  correct answered questions. After passing the test it should be printed congratulation and confirmation email should be sent automatically
to user's email with copy to cc to assigned team lead.
If test not passed - user should be informed that test is not passed and go back to the main menu to choose mode;

View Statistics mode:
It must print each test's date and time, user's email address;
It should print the list of questions;
It should print statistics with score and percentage;

Exit:
Exits the program with a message ("Goodbye");

Create:
3 user groups for each region (America, EMEA, APAC+MEA) and assign the responsible team lead (name, surname and email address) for each of the region;
Database for questions in a separate folder;
Database for picture icons for each topic in a separate folder;
Database for theory documentation for each topic in separate folders;


Requirements and Libraries
Welcome Screen and User Input:
input() for capturing user information.

Menu Options:
Console-based navigation using a loop and conditions.

Theory Mode:
File handling using os and potentially subprocess for opening files.

Test Mode:
Random question selection using random.
Email sending using smtplib.
Results storing using simple JSON file.

Statistics Mode:
Reading from the .txt and printing results.

Exit:
Simple print and exit.
