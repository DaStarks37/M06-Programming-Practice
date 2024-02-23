#Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between zero and one, print the current time, and then exit.
import datetime as dt
import time
import random as rng
import multiprocessing
import os


def samiam(what):
    print("Process %s says: %s" % (os.getpid(), what))

def noiamthesamiamthatiamthesamiam(what):
    randomnumbah = rng.random()
    time.sleep(randomnumbah)
    print(dt.datetime.now())

if __name__ == "__main__":
    samiam("I am the main program")
    for n in range(3):
        p = multiprocessing.Process(target=noiamthesamiamthatiamthesamiam,
          args=("I'm function %s" % n,))
        p.start()