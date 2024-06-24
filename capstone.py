import re
import os
import sys
import subprocess
import random
import smtplib
import json
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from datetime import datetime

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
while True:
    email = input("Enter your email: ").lower().strip()
    if re.match(email_pattern, email):
        break
    else:
        print("Invalid email format. Please enter a valid email address.")


load_dotenv()
teams = {
    "America": {"lead": {"name": os.getenv('AMERICA_LEAD'), "email": os.getenv('AMERICA_LEAD_EMAIL')}},
    "EMEA": {"lead": {"name": os.getenv('EMEA_LEAD'), "email": os.getenv('EMEA_LEAD_EMAIL')}},
    "APAC_MEA": {"lead": {"name": os.getenv('APAC_MEA_LEAD'), "email": os.getenv('APAC_MEA_LEAD_EMAIL')}}
}

def load_users_from_csv(filename):
    users = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

def validate_user_input(name, surname, email, users):
    for user in users:
        if user['name'] == name and user['surname'] == surname and user['email'] == email:
            return user['region']
    return None

def main_menu():
    global email
    print("Welcome to the Interactive Learning and Testing Tool")

    users = load_users_from_csv('teams.csv')

    while True:
        name = input("Enter your first name: ").capitalize().strip()
        surname = input("Enter your surname: ").capitalize().strip()

        region = validate_user_input(name, surname, email, users)

        if region:
            team_lead = teams[region]["lead"]
            print(f"Assigned to region: {region}")
            print(f"Team Lead: {team_lead['name']}")

            while True:
                print("\nChoose an option:")
                print("1. Read theory")
                print("2. Test mode")
                print("3. View statistics")
                print("4. Exit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    read_theory()
                elif choice == "2":
                    test_mode(name, surname, email, team_lead)
                elif choice == "3":
                    view_statistics()
                elif choice == "4":
                    print("Thank you for using our tool. Goodbye!")
                    sys.exit()
                else:
                    print("Invalid choice, please try again.")
        else:
            print("No matching user found. Please check your details and try again.")


def read_theory():
    topics = ["Blocked orders", "Credit limit assessments", "Collections", "Go back to the main menu"]

    while True:
        print("\nSelect a topic to read:")
        for i, topic in enumerate(topics):
            print(f"{i + 1}. {topic}")

        try:
            choice = int(input("Enter your choice: ")) - 1

            if 0 <= choice < len(topics):
                topic = topics[choice]
                if topic == "Go back to the main menu":
                    print("Returning to the main menu...")
                    break
                else:
                    file_path = select_file(topic)
                    if file_path:
                        open_file(file_path)
                    else:
                        print("Invalid topic choice. Please select again.")
            else:
                print("Invalid topic choice. Please select again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def select_file(topic):
    while True:
        if topic == "Blocked orders":
            print("\nSelect a file to open:")
            print("1. blocked_orders.docx (Word)")
            print("2. blocked_orders.pptx (PowerPoint)")
        elif topic == "Credit limit assessments":
            print("\nSelect a file to open:")
            print("1. credit_limit_assessment.docx (Word)")
            print("2. credit_limit_assessment.pptx (PowerPoint)")
        elif topic == "Collections":
            print("\nSelect a file to open:")
            print("1. collections.docx (Word)")
        else:
            print("Invalid topic.")
            return None

        try:
            file_choice = int(input("Enter your choice: "))
            main_dir = "capstone1.4"
            if topic == "Blocked orders":
                if file_choice == 1:
                    file_path = os.path.join(main_dir, "blocked_orders", "blocked_orders.docx")
                elif file_choice == 2:
                    file_path = os.path.join(main_dir, "blocked_orders", "blocked_orders.pptx")
                else:
                    print("Invalid choice. Please enter 1 or 2.")
                    continue
            elif topic == "Credit limit assessments":
                if file_choice == 1:
                    file_path = os.path.join(main_dir, "credit_limit_assessment", "credit_limit_assessment.docx")
                elif file_choice == 2:
                    file_path = os.path.join(main_dir, "credit_limit_assessment", "credit_limit_assessment.pptx")
                else:
                    print("Invalid choice. Please enter 1 or 2.")
                    continue
            elif topic == "Collections":
                if file_choice == 1:
                    file_path = os.path.join(main_dir, "collections", "collections.docx")
                else:
                    print("Invalid choice. Please enter 1.")
                    continue
            return file_path
        except ValueError:
            print("Invalid input. Please enter a number.")


def open_file(file_path):
    try:
        if os.path.exists(file_path):
            print(f"Opening file: {file_path}")
            if file_path.endswith('.docx'):
                if sys.platform.startswith('win'):
                    subprocess.Popen(['start', 'winword', file_path], shell=True)
                elif sys.platform.startswith('darwin'):
                    subprocess.Popen(['open', file_path])
                else:
                    subprocess.Popen(['xdg-open', file_path])
            elif file_path.endswith('.pptx'):
                if sys.platform.startswith('win'):
                    subprocess.Popen(['start', 'powerpnt', file_path], shell=True)
                elif sys.platform.startswith('darwin'):
                    subprocess.Popen(['open', file_path])
                else:
                    subprocess.Popen(['xdg-open', file_path])
        else:
            print(f"File does not exist: {file_path}")
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")


def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        questions = json.load(file)
    return questions

def test_mode(name, surname, email, team_lead):
    questions = load_questions('questions.json')
    test_questions = random.sample(questions, 4)
    score = 0
    attempts = {}

    for i, q in enumerate(test_questions):
        attempts[q["text"]] = 0
        options = q["options"]
        while attempts[q["text"]] < 3:
            print(f"\nQuestion {i+1}: {q['text']}")
            for j, option in enumerate(options):
                print(f"{j + 1}. {option}")
            try:
                answer = int(input("Enter your choice: "))
                if 1 <= answer <= len(options):
                    if options[answer - 1] == q['correct_option']:
                        print("Correct!")
                        score += 1
                        break
                    else:
                        print("Incorrect, please try again.")
                        attempts[q["text"]] += 1
                        if attempts[q["text"]] == 3:
                            print(f"The correct answer is: {q['correct_option']}")
                else:
                    print("Invalid choice. Please enter a number corresponding to the options.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    result = (score / 4) * 100
    if result >= 90:
        print("Congratulations! You have passed the test.")
        send_email(email, team_lead['email'], name, surname, result)
    else:
        print("You did not pass the test. Please try again.")
    save_results(name, surname, score, len(test_questions))


def save_results(name, surname, score, num_questions):
    results_path = 'results.txt'
    percentage = (score / num_questions) * 100
    rounded_percentage = round(percentage, 2)

    with open(results_path, 'a') as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Name: {name} {surname} - Email: {email} - Score: {score}/{num_questions} - Percentage: {rounded_percentage}%\n")
        print("Results saved successfully!")

def send_email(user_email, lead_email, name, surname, score):
    sender_email = os.getenv("GMAIL_EMAIL")
    sender_password = os.getenv("GMAIL_PASSWORD")

    subject = "Newjoiner's test results"
    body = f"""
    Hi {name} {surname},

    Your test score is {score}%.

    Regards,
    Learning Team
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = user_email
    msg['Cc'] = lead_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    recipients = [user_email, lead_email]

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipients, text)
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate. Please check your email credentials.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred while sending email: {e}")
    finally:
        server.quit()

def view_statistics():
    global email
    results_path = 'results.txt'

    if not os.path.exists(results_path):
        print("No test results found.")
        return

    results_found = False

    with open(results_path, 'r') as file:
        for line in file:
            if email in line:
                results_found = True
                print(f"\n{line.strip()}")

    if not results_found:
        print("No test results found for this email.")

if __name__ == "__main__":
    main_menu()
