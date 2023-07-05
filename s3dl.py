import boto3
import base64
from functools import reduce
from random import choice
from string import digits, ascii_letters, punctuation
import sys
from Crypto.Cipher import AES 

# pip3 install pycryptodome, boto3

ENDPOINT = "ckciUDl0Mmg0TFRFISZqe/cGCySsEkFWdpbioz9KA3cPgJkeTgjk5KUjgE1pwP1Xrvi27Xja+7Jj296SH56tP4mgLXtVXWzk0nC8sYdIHlE="
ACCESS_KEY = 'PjMsfjpUWUJpMXNDUH1qdBkw3dlnNakgwbfTU7Qd1wZ3VfDU1ERf6yoC5+QjnOyynvBeeLCqjrYfUb6Bknpascs1yCMEaXjvPu+HwdMxAFA='
SECRET_KEY = 'Zzk8UWI3WFsjaipvMGlNca/joAbVvMfje14qs/P9q3XbC5zv8lkMSrEg1/vmDEUl0OD4zji+i3461cIJfRY9eyQzgzZxz0fF5WVtdEBcwz3EpVmNKqH3+eLPXyu85xU76r2bf4tqQDLxrtFATUrldA=='
BUCKET = "PS97QlRoSD8kdGpILnpOYinN/PaGukrHH/9mac2Fs43ZynNmi0HN9Mc+9MY89X7h"

U = "N0VIbTFKXHVGd3VNUCwiZ8l5W3Jyan1yuYPBjX7lRDiI18BBjF+ll+tYetbbgpTy"

PP = "Tkk1MCtBRXBWOWlWdXAmUPDmCtlRlDge4F6zfEbB8ZJM13zZ3DKzGl6uQbvQNCxp"
CM = "QV1+VSNDMEIrR1NTTEAtdJchlnJ/Re2YyqZnwwcMsYgpP39jyD86cR3RTFjFRKaxPmB/dDBpaYOGAUS2kdheEVMX37eql00OT0S9bfj7otgeTBIPkoEcDAciLpDSr6ZsRE5PuGvWB2BGOLj7Jr1tEA=="

def cbc_decrypt(ciphertext: str, key: str):
    ciphertext = base64.b64decode(ciphertext)
    mode = AES.new(key.encode(), AES.MODE_CBC, ciphertext[:AES.block_size])
    plaintext = mode.decrypt(ciphertext[AES.block_size:]).decode()
    return plaintext[:-ord(plaintext[-1])]




if __name__ == '__main__':
    key = sys.argv[1]
    obj = sys.argv[2]
    s3 = boto3.client('s3',
        endpoint_url = 'https://{}.{}/{}'.format(cbc_decrypt(ENDPOINT, key), cbc_decrypt(U, key),cbc_decrypt(BUCKET, key)),
        aws_access_key_id = cbc_decrypt(ACCESS_KEY, key),
        aws_secret_access_key = cbc_decrypt(SECRET_KEY, key)
        )
    s3.download_file(cbc_decrypt(BUCKET, key), obj, 'mini.zip')
    print(cbc_decrypt(PP, key))
    print(cbc_decrypt(CM, key))
