import datetime as dt
current = str(dt.datetime.now())
def Thingy(filename):
    file=open(filename, "w+")
    file.write("Today's date and time: " + current)
    file.close()
    file=open(filename, "r")
    print(file.read())
Thingy("today.txt")
