filename = "subscribers.txt"


def add_email(input):
    with open(filename, "r") as f:
        for email in f:
            x = email.strip('\r\n')
            print(x)
            if x == input:
                print(x + ' & ' + input)
                return
            x = ''
    with open(filename, "a") as file:
        file.write(input + "\n")