from password_strength import PasswordPolicy
from password_strength import PasswordStats
from hashlib import sha1
# from getpass import getpass
import requests

def passwd_test(policy: PasswordPolicy, password: str) -> bool:
    result = policy.test(password)
    if result:
        # print("Weak Password,", result)
        # stats = PasswordStats(password)
        # print(f"Entropy = {stats.entropy_bits} : strength = {stats.strength()}")
        return False

    passhash = sha1(password.encode("utf-8")).hexdigest().upper()
    first_characters = passhash[0:5]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{first_characters}")
    for header in response.text.splitlines():
        if passhash[6:] in header:
            # print("Password Pwned")
            return False
    return True

if __name__=='__main__':
    policy = PasswordPolicy.from_names(
        entropybits=66,
        strength=(0.66, 30)
    )
    # print(passwd_test(policy, getpass(prompt = "Please type your password: ", stream = None)))