import subprocess
import base64
from hashlib import sha256

def ec(text):
    return sha256(text.encode("ascii")).hexdigest()

current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()

message = current_machine_id
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print("[+] ------------------------------------------------------------------------- [+]")
print("                                   ")
print("                                   ")
print("                                   ")
print("                                   ")
print("                                   ")
print("                                   ")
print("                                   ")
print("                                   ")
print("                                   ")
print("                                   ")
print("                                   ")
print("                        NT MACHINES ONLY          ")
print("                                   ")
print(                      f"SHA256 -> {ec(current_machine_id)}")
print(                          f"Base64 -> {base64_message}")
print(                        f"Normal -> {current_machine_id}")
print("                                   ")
print("                                   ")
print("                        NT MACHINES ONLY          ")
print("                                   ")
print("                                   ")
print("                                   ")
print("                                   ")
print("                                   ")
print("                                   ")
print("                                   ")
print("[+] -------------------------------------------------------------------------- [+]")
