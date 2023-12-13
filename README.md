# Website-blocker

The website blocker script aims to modify the system's hosts file to either block or unblock specific websites based on a predefined list of URLs. Here's an overview of its functionalities:

Operating System Detection and Hosts File Path:

Determines the operating system using the platform module.
Sets the path to the hosts file based on the detected operating system:
For Windows: C:\Windows\System32\drivers\etc\hosts
For other systems: /etc/hosts
List of Blocked Websites:

Contains URLs of websites that the script intends to either block or unblock (blocked_websites list).
Block Websites Function (block_websites()):

Opens the hosts file in read-write mode.
Reads the current content of the file and checks if each website in blocked_websites is already present in the file.
If any website is not present, it adds an entry in the format 127.0.0.1 www.website.com to redirect these sites to the localhost IP (127.0.0.1).
Notifies whether each website has been successfully blocked or if it's already blocked.
Unblock Websites Function (unblock_websites()):

Opens the hosts file in read mode.
Reads all lines of the file and writes back those lines that do not contain any of the blocked websites. This effectively removes the entries for these websites from the hosts file, unblocking them.
Execution:

By default, the script is set to unblock websites. It calls the unblock_websites() function and comments out the block_websites() function.
To block websites, you would comment out the unblock_websites() line and uncomment the block_websites() line.
Error Handling:

Utilizes try-except blocks to catch any IOError that might occur while accessing the hosts file, providing an error message if such an issue arises.
