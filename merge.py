import os

def days():
    return 30


if __name__ == '__main__':

    #--------Find gaming articles--------
    print("From past" ,days() ,"days:")

    os.system("python a16z.py")
    os.system("python Newzoo.py")
    os.system("python Esportobserver.py")
    os.system("python try2.py")
    os.system("python Techcrunch.py")
