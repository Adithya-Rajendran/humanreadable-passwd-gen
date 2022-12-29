from password_strength import PasswordPolicy
from hashlib import sha1
import random
import requests

def passwd_test(policy: PasswordPolicy, password: str) -> bool:
    # Test the strength of the password
    result = policy.test(password)
    if result:
        return False

    # Hash the password
    passhash = sha1(password.encode("utf-8")).hexdigest().upper()
    first_characters = passhash[0:5]

    # Check the https://haveibeenpwned.com/ database to check if the password has appeared in the database
    response = requests.get(f"https://api.pwnedpasswords.com/range/{first_characters}")
    for header in response.text.splitlines():
        if passhash[6:] in header:
            return False

    return True

# Generate a random password
def generate_password(policy: PasswordPolicy) -> str:
    good_password = False

    # Loop until we get a good password
    while not good_password:
        with open('google-10000-english-usa-no-swears-medium.txt', 'r') as wordlist:
            words = wordlist.read().splitlines() # Doing it like this instead of wordlist.readline() automatically removes the \n at the end
            password_gen = "-".join(random.sample(words, 4))
            good_password = passwd_test(policy, password_gen)
    return password_gen

if __name__=='__main__':
    policy = PasswordPolicy.from_names(
        length=12,
        entropybits=66,
        strength=(0.66, 30)
    )
    print(generate_password(policy))