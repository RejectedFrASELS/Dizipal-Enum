import requests

reachable_list = []

def try_func(url):
    try:
        response = requests.get(url, verify=True)
        if response.status_code == 200 and not response.history and response.ok :
            print( url + " is reachable")
            reachable_list.append(url)
        else:
            print(url + " is not reachable")
    except requests.exceptions.RequestException as e:
        print(url + " is not reachable")


url_base = "https://dizipal.com/"
print (url_base)

print("What numbers you want to try between?")
start = int(input("First number:"))
stop = int(input("Last Number:"))


if start > stop:
    print("ERROR, first number must be less than the second one, QUITTING")
    x = input()
    exit()
    
for i in range(start, stop+1):

    url = url_base[:-5] + str(i) + ".com"
    try_func(url)

print("Reachable Addresses: \n" )

#remove_list = ['https://dizipal520.com', 'https://dizipal525.com', 'https://dizipal530.com', 'https://dizipal533.com', 'https://dizipal539.com', 'https://dizipal550.com']

# opening the file in read mode
my_file = open("blacklist.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
remove_list = data.split("\n")
my_file.close()


actual_list = [i for i in reachable_list if i not in remove_list]
print(actual_list)

x = input()
