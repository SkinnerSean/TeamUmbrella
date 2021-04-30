from engine_profile import EngineProfile
from sqlitedict import SqliteDict
import os

class Admin: # in gui have delete user and then prompt for user an key 
    
    def __init__(self,user_pw):
        self._key = '12345'
        self.password = user_pw

    def __verify_password(self):
       
        if self.password == self._key: 
            return True
        return False

    def delete_user_from_database(self,user):
        if not self.__verify_password(): 
            return False
        os.unlink(f'../resources/tmp/users_engine{user}.sqlite')
        return True

class User: # create a new user w name then new_profile in gui
    def __init__(self,user_name):
        self.user_name = user_name
        self.profiles_database = SqliteDict(f'../resources/tmp/users_engine{user_name}.sqlite', autocommit=True)
    
    def get_profiles(self):
        return self.profiles_database.items()


    def new_profile(self,name,location,file_name):
        if name in self.profiles_database.keys():
            print(f'{name} already in use!')
            return
        self.profiles_database[name] = EngineProfile(name,location,file_name).__dict__
        

    def delete_profile(self,name):
        del self.profiles_database[name]
    
    def profile_by_name(self,name):
        pass
    
    def profile_by_loc(self,location):
        pass

    def __del__(self):
        self.profiles_database.close()