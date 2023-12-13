import platform

# Define the path to the hosts file based on the operating system
if platform.system() == 'Windows':
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
else:
    hosts_path = '/etc/hosts'

# Websites to block
blocked_websites = ['www.facebook.com', 'www.twitter.com', 'www.instagram.com']

def block_websites():
    try:
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in blocked_websites:
                if website in content:
                    print(f"{website} is already blocked.")
                else:
                    file.write(f"\n127.0.0.1\t{website}")
                    print(f"{website} has been blocked.")
    except IOError as e:
        print("Error occurred while accessing the hosts file:", e)

def unblock_websites():
    try:
        with open(hosts_path, 'r') as file:
            lines = file.readlines()
        with open(hosts_path, 'w') as file:
            for line in lines:
                if not any(website in line for website in blocked_websites):
                    file.write(line)
            print("Websites unblocked.")
    except IOError as e:
        print("Error occurred while accessing the hosts file:", e)

# Blocking and unblocking websites
# block_websites()  # Comment this line if you want to unblock websites
unblock_websites()  # Uncomment this line if you want to unblock websites
