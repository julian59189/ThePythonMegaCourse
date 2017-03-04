import time
from datetime import datetime as dt

working_hours_start = 9
working_hours_end = 14
hosts_temp="hosts"
hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
websites_list=["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, working_hours_start) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, working_hours_end):
        print("Working hours...")

        # get content of file
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            #print(content)

            # Check if websites are already in file
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)

            file.truncate()
        print("Fun hours...")
    time.sleep(5)
