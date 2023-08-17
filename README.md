# Automated CME Password Spraying

![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue)
![License](https://img.shields.io/github/license/GabrielDuschl/Automated-CME-Password-Spraying)
![Last Commit](https://img.shields.io/github/last-commit/GabrielDuschl/Automated-CME-Password-Spraying)

## Overview

Automated CME Password Spraying is a Python script designed for efficient and targeted password spraying attacks using CrackMapExec (CME). It allows you to automate the process of testing a list of passwords against a large number of users in a Windows Active Directory environment. This script is intended for legitimate testing purposes only and should not be used for any illegal activities or unauthorized access.

## Features

- Password spraying against user accounts in a Windows Active Directory.
- Efficient use of CrackMapExec for password spraying attacks.
- Automated handling of user and password lists.
- Adjustable lockout threshold and lockout reset timer.
- Clear reporting of successful password matches.
- Graceful script termination with KeyboardInterrupt handling.

## Prerequisites

- Python 3.6 or higher
- CrackMapExec tool installed

## Usage

1. Clone this repository: `git clone https://github.com/GabrielDuschl/Automated-CME-Password-Spraying.git`
2. Navigate to the repository: `cd Automated-CME-Password-Spraying`
3. Install required Python libraries: `pip install -r requirements.txt`
4. Modify the script parameters in the `main()` function to match your environment.
5. Run the script: `python automated_password_spraying.py`

## Configuration

- `--user` or `-u`: File containing user IDs.
- `--password` or `-p`: File containing passwords to be tested.
- `--treshold` or `-t`: Account Lockout Threshold (default: 5).
- `--lockout` or `-l`: Reset Account Lockout Counter in minutes (default: 15).
- `--domain` or `-d`: Domain name for testing.
- `--pass-length` or `-pl`: Minimum password length.

## Example

```shell
python3 automated_password_spraying.py -u users.txt -p passwords.txt -t 3 -l 10 -d example.com -pl 8
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out:

- LinkedIn: [Gabriel Duschl](https://www.linkedin.com/in/gabrielduschl)
