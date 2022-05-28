from untity.database import authdb

class UserModel:

    userID = ''
    username = ''
    password = ''
    email = ''
    enable = '1'
    address = ''
    phone = ''
    picture = '' 
    company = ''

    def __init__(self, username, password, email, address, phone, picture, conmpany):
        self.username = username
        self.password = password
        self.email = email
        self.address = address
        self.phone = phone
        self.picture = picture
        self.conmpany = conmpany

    def add_user(self):
        cur = authdb.cursor()
        sql = "insert into user (username,password,email,enable,address,phone,picture,company) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(self.username,self.password,self.email,self.enable,self.address,self.phone,self.picture,self.company)
        cur.execute(sql)
        authdb.commit()
        cur.close()

    def update_user(self):
        cur = authdb.cursor()
        sql = "update user set email='{0}',username='{1}',password='{2}' where userID='{3}'".format(self.email,self.username,self.password,self.userID)
        cur.execute(sql)
        authdb.commit()
        cur.close()

    def delete_user(self):
        cur = authdb.cursor()
        sql = "delete from user where userID='{0}'".format(self.userID)
        cur.execute(sql)
        authdb.commit()
        cur.close()

    def get_user(username):
        user = None
        cur = authdb.cursor()
        sql = "select * from user where username='{0}'".format(username)
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return None
        user = UserModel(result[2],result[1],result[3])
        user.userID = result[0]
        cur.close()
        return user

    def get_email(email):
        user = None
        cur = authdb.cursor()
        sql = "select * from user where email='{0}'".format(email)
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return None
        user = UserModel(result[2],result[1],result[3])
        user.userID = result[0]
        cur.close()
        return user

    def get_all_user(self):

        users = []

        cur = authdb.cursor()
        sql = "select * from user"
        result = cur.execute(sql)
        for item in result:
            user = UserModel(item[1], item[2], item[3])
            user.id = item[0]
            users.append(user)
        cur.close()
        return users