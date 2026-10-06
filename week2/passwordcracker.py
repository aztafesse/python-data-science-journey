import time
import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = input("Set a password: ")

print("\nAccessing Database...........\n")
guess = ""
start_time = time.time()
while guess != password:
    guess = ""

    for i in range (len(password)):
        guess +=random.choice(chars)

    print("\nTrying...!", guess)
    time.sleep(0.01)

print(f"\nPASSWORD CRACKED: {password} in {(time.time()-start_time):.4f} s")

