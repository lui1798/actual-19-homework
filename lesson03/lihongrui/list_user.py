import json

USER_FILE="usejson"
users=[]


try:

    fhandler = open(USER_FILE, "r")
    cxt=fhandler.read()
    fhandler.close()
    users =json.loads(fhandler.read())

    print(fhandler)
except Exception as e:
    pass