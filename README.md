<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
</head>
<body>
  <header>
    <h1>Python and Bash Scripts Repository</h1>
  </header>
  <div class="container">
    <h1>GitHub - M-Hamza-dost/Python-Bash-Scripts</h1>
    <p>This repository contains a collection of Python and Bash scripts that I have written to practice and implement what i've learned so far.</p>
    <h2>Scripts</h2>
    <ul>
        <li>
            <h4>Python Script to retrieve creation and modification time of file for Windows and Linux</h4>
                <pre>
import os
import time
import sys
import platform
#Check if the script has the required number of arguments
if len(sys.argv) != 2: 
    print(f"Script needs 1 argument\nEx: python {sys.argv[0]} filename")
    sys.exit()
else:
    #Get the filename from the command line argument
    file_name = sys.argv[1]
    print(file_name)
    from datetime import datetime as dt
    found = False
    # Set the directory path based on the operating system
    if platform.system() == 'Windows':
        dir_path = "C:\\Users\\sc\\Desktop\\python\\day3"
    else:
        dir_path = "/home/hamza/bash"
    # Recursively search for the file in the directory
    for root, directories, files in os.walk(dir_path):
        for file in files:
            if file == file_name:
                # Get the creation and modification times of the file
                creation_time = dt.fromtimestamp(os.path.getctime(os.path.join(root, file))).strftime('%I:%M %p  %d/%m/%Y')
                modified_time = dt.fromtimestamp(os.path.getmtime(os.path.join(root, file))).strftime('%I:%M %p  %d/%m/%Y')
                # Print the file path and its creation and modification times
                print(f"Here is your file with complete path: {os.path.join(root, file)}")
                print(f"{file} was created at {creation_time} and last modified at {modified_time}")   
                found = True
                break
    # If the file is not found, print a message
    if not found:
        print('File not found')</pre>
        </li>
        <br>
        <li>
            <h4>Service Status Checker and Notification Script</h4>
                <pre>
#!/bin/bash
# Prompt the user to enter the service name
echo "Enter service Name: "
read service_n
# Check the status of the service using the 'ps' command
stat=$(ps -ax | grep $service_n | wc -l)
# If the service is running (i.e., the 'grep' command returns more than 1 result)
if [[ $stat > "1" ]]
then
    # Print a message indicating that the service is running
    echo "$service_n is Running"
else
    # Print a message indicating that the service is not running, and suggest contacting the admin
    echo -e "$service_n is not running \nPlease Contact your admin"
    # Prompt the user to send an email to the admin
    echo "Send Mail to your admin [y/n]"
    read input
    if [[ $input == "y" ]]
    then
        # Send email & Print a message indicating that the email has been sent
        mail -s "Service Down $service_n | ALRET" abc@xyz.com
        echo "Mail has been sent!"
    else
        # Exit the script
        exit
    fi
fi</pre>
        </li>
        <br>
        <li>
            <h4>Bash Script to Manage System Processes</h4>
                <pre>
import sys
import os
# Check if the script has the required number of arguments
if len(sys.argv) != 3:
    # If not, print a usage message and exit
    print(f"Script requires two arguments\nFor example {sys.argv[0]} process action\nActions: start/stop/restart/status/enable/disable")
    sys.exit()
else:
    # Get the action and process name from the command-line arguments
    action = sys.argv[2]
    processname = sys.argv[1]  
    # Execute the systemctl command with the provided action and process name
    os.system(f"systemctl {action} {processname}") 
    # Exit the script
    sys.exit()</pre>
        </li>
      <li>
            <h4>Python Script to Send Email with Attachment</h4>
                <pre>
import smtplib
from email.message import EmailMessage
# Set email details
my_mail = "abc@gmail.com"
passwd = "**********"
# Create SMTP connection and start TLS session
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
# Create email message
msg = EmailMessage()
msg['Subject'] = "test mail 2"
msg['From'] = my_mail
msg['To'] = "dosth499@gmail.com"
msg['Cc'] = my_mail
msg.set_content("This is test mail 2")
# Attach a file to the email
with open("simple.csv", "rb") as csvfile:
    data = csvfile.read()
    file_name = csvfile.name
msg.add_attachment(data, maintype='application', subtype='octet-stream', filename=file_name)
# Log in to email account and send the message
connection.login(user=my_mail, password=passwd)
connection.send_message(msg)
connection.close()</pre>
        </li>
        <br>
    </ul>               
    <h2>Contributing</h2>
    <p>If you have any suggestions or improvements for the scripts, feel free to fork the repository and submit a pull request. I'm always happy to collaborate and improve the scripts.</p>
  </div>
</body>
</html>
