import os

def days():
    return 30


if __name__ == '__main__':

    #--------Find game articles--------
    print("From past" ,days() ,"days:")

    os.system("python a16z.py")
    os.system("python Newzoo.py")
    os.system("python Esportobserver.py")
    os.system("python try2.py")
    os.system("python Techcrunch.py")

    #--------Find popular memes------

    # os.system("python IG.py")
    # os.system("python Dcard.py")

    #--------Play Flow music------
    #
    #os.system("python YT_flow.py")
    #
    # #--------Play 神人演講 ------

    #os.system("python YT_god.py")
    #
    # #--------Find 固定Youtuber的最新影片 ------
    #
    #os.system("python Youtubers.py")




