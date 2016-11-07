import random
import string


class RandomGen:
    """ class contain methods generate random char, num, and Emails from pool of data    """
    def Random_char(name):
        "function_docstring"
        RandomChar = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(name)])
        return [RandomChar]

    def Random_Num(no):
        "function_docstring"
        RandomNum = random.sample(range(1100), no)
        return [RandomNum]

    def Random_Email(mail):
        letters = string.ascii_lowercase[:20]
        domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
        random_letter = ''.join(random.choice(letters) for i in range(mail))
        random_domain = random.choice(domains)
        Random_Email = random_letter + '@' + random_domain
        return [Random_Email]