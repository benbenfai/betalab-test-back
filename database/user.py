from untity.database import authdb
from dataclasses import dataclass

@dataclass
class UserModel:

    userID: int
    username: str
    password: str
    email: str
    enable: int
    address: str
    phone: str
    picture: str
    company: str

class UserTool:

    # should a try except there for error catch and a final stage ensure to close the connection
    # a db connection pool would be better

    def add_user(self, username, password, email, address, phone, picture, company):
        try:
            cur = authdb.cursor()
            try:
                sql = "insert into user (username,password,email,enable,address,phone,picture,company) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(username,password,email,1,address,phone,picture,company)
                cur.execute(sql)
            except:
                authdb.rollback()
            authdb.commit()
        finally:
            cur.close()

    def update_user(self):
        cur = authdb.cursor()
        sql = "update user set email='{0}',username='{1}',password='{2}' where userID='{3}'".format(self.email,self.username,self.password,self.userID)
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

        user = UserModel(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8])

        cur.close()
        return user

    """
    def get_email(email):
        user = None
        cur = authdb.cursor()
        sql = "select * from user where email='{0}'".format(email)
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return None
        #user = UserTool(result[2],result[1],result[3])
        user = UserTool()
        user.userID = result[0]
        cur.close()
        return user
    """

    def get_all_user():

        users = []

        cur = authdb.cursor()
        sql = "select username, enable from user"
        cur.execute(sql)
        result = cur.fetchall()
        for item in result:
            #user = UserTool(item[1], item[2], item[3])
            #user = UserTool()
            #user.id = item[0]
            users.append(item)
        cur.close()
        return users