"""cehcking versions/path/etc"""

import sys
import boto3

print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)
print("Path to python interpreter")
print(sys.executable)
print("Path to python sys prefix")
print(sys.prefix)

print(boto3.client("sts").get_caller_identity().get("Account"))
