from apps.utils.fmt import PrintTable, Println
from apps.utils import login


def main():
    # userinfo = [
    #     {'id': 1, 'name': 'monkey1', 'age': 18, 'tel': '132xxx', 'address': 'beijing'},
    #     {'id': 2, 'name': 'monkey2', 'age': 18, 'tel': '132xxx', 'address': 'beijing'},
    #     {'id': 3, 'name': 'monkey3', 'age': 18, 'tel': '132xxx', 'address': 'beijing'},
    #     {'id': 4, 'name': 'monkey4', 'age': 18, 'tel': '132xxx', 'address': 'beijing'},
    #     {'id': 5, 'name': 'monkey4', 'age': 18, 'tel': '132xxx', 'address': 'beijing'},
    # ]
    # # tablemsg, _ = PrintTable(userinfo)
    # # print(tablemsg)
    # Println(userinfo)
    login.Auth_login_token()


if __name__ == '__main__':
    main()
