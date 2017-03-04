import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
websites_list=["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working hours...")

        # get content of file
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            print(content)

            # Check if websites are already in file
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website)
    else:
        print("Fun hours...")
    time.sleep(5)
