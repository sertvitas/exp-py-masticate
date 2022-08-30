import json
import subprocess


# whoami = subprocess.Popen('aws sts get-caller-identity')
whoami = subprocess.Popen(
    "aws sts get-caller-identity", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
).communicate()[0]
print (whoami)
whoami_text = whoami.decode('utf8')
print(whoami_text)

whoamij = json.loads(whoami_text)
print(whoamij)

account = whoamij.get("Account")
print(account)

if account == "<redacted>>":
    print("You're in sandbox")
else:
    print("Double check your settings.....")

#whoamij = whoami_text.json()


#print(whoami)