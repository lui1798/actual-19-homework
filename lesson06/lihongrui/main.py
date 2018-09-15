import fre

def main():
    if fre.is_unlock():
        if fre.login():
            users=fre.get_user()