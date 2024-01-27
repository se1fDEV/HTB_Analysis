HTB_Analysis
HTB_Analysis is a Python script designed for testing LDAP injections and similar vulnerabilities through fuzzing LDAP with a specified wordlist or charset.

Getting Started
These instructions will guide you on how to set up and run HTB_Analysis on your local machine for development and testing purposes.

Prerequisites
Ensure you have the following installed before proceeding:

Python 3
pip (Python package manager)
Ability to modify your system's /etc/hosts file (for host resolution)
Installation
Clone the Repository

Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/se1fDEV/HTB_Analysis.git
Install Required Python Libraries

Change to the cloned directory and install necessary Python libraries:

bash
Copy code
cd HTB_Analysis
pip install -r requirements.txt
Configure Hosts File

Modify your /etc/hosts file to include the IP address of the target machine. This is required for domain resolution for internal.analysis.htb. Add the following line:

csharp
Copy code
10.129.10.10    analysis.htb internal.analysis.htb
Note: Editing /etc/hosts typically requires administrator privileges.

Running the Script
Execute the script with the following command:

Copy code
python ldap_fuzzer.py
Upon prompt, enter the path to your wordlist or charset. Press Enter to use the default wordlist provided.

License
This project is licensed under the MIT License. 
#writeup
#hackthebox-season-4
#linux
#hard
![HTB_Analysis_s](https://github.com/se1fDEV/HTB_Analysis/assets/154564062/774a1fd6-0fcb-4c4f-8c1d-6f61b6796654)
