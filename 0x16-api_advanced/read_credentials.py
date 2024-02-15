"""read login credentials from text file"""

def read_file(path):
    
    credentials = []

    #read file
    with open("credentials.txt") as file:
        for line in file:
            username, password = line.strip().split(",")
            credentials.append((username, password))

    return credentials
