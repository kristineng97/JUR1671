#Compulsory exercise
#Exercise 1 - Article 15 ECHR

def run_program():
    """Function running the program."""
    print("This program tells the user if the requirements in ECHR Article 15 are met, so that a lockdown can be started or ended. If a lockdown can be started or ended, the Council of Europe needs to be notified.")
    msg = "Do you want to start a lockdown or end a lockdown? Please write <<start>> or <<end>>."
    start_up = input(msg)
    if (start_up == "start"):
        start_lockdown()
    elif (start_up == "end"):
        end_lockdown()
    else:
        invalid_input()

def start_lockdown():
    """Function (with questions about requirements) regarding starting a lockdown."""
    question(msg["public_emergency"])
    question(msg["threatening_life"])
    question(msg["required"])
    question(msg["consistent"])
    question(msg["article"], 1)

def end_lockdown():
    """Function regarding ending a lockdown."""
    notice()

def question(msg, stop=0):
    """Function for yes/no questions.

    Args:
        msg (string): message displayed before user input
        stop (int): takes on value 0 (default) or 1 (defining the last question)
    """
    tmp = input(msg)
    if tmp == "yes":
        if stop == 0:
            pass
        elif stop == 1:
            notice()
        else:
            invalid_input()
    elif tmp == "no":
        no_notice()
    else:
        invalid_input()

def invalid_input():
    """Function called on when the user writes invalid input"""
    print("Invalid input. Try running the program again. The input needs to be exactly like described.")
    exit()

def no_notice():
    """Function called on when the user does not need to notify the Council of Europe."""
    print("The requirements in ECHR Article 15 are not met. You do not need to notify the Council of Europe.")
    exit()

def notice():
    """Function called on when the user needs to notify the Council of Europe."""
    print("The requirements in ECHR Article 15 are met. You need to notify the Council of Europe.")

msg = { "public_emergency": "Is there a public emergency? Please answer <<yes>> or <<no>>.",
        "threatening_life": "Is the public emergency threatening the life of the nation? Please answer <<yes>> or <<no>>.",
        "required": "Is a lockdown strictly required by the exigencies of the situation? Please answer <<yes>> or <<no>>.",
        "consistent": "Is a lockdown consistent with the obligations under international law? Please answer <<yes>> or <<no>>.",
        "article": "Is a lockdown consistent with article 2, article 3, article 4 paragraph 1 and article 7 in the European Convention of Human Rights? Please answer <<yes>> or <<no>>.",
        }

if __name__ == "__main__":
    run_program()
    
