from engine_profile import EngineProfile
from sqlitedict import SqliteDict
import os

class Admin: # in gui have delete user and then prompt for user an key 
    """
        Key can be changed to desired password, must know the key in order to delete user database
    """
    def __init__(self,user_pw):
        self._key = '12345' # private member
        self.password = user_pw

    """
        Used when deleting a user from the database files, will only allow deletion if password is correct
    """
    def __verify_password(self):
        if self.password == self._key: 
            return True
        return False

    """
        Using os lib it deletes the file that corresponds to a certain user, if deleted succesfully return true, if not
            return false
    """
    def delete_user_from_database(self,user):
        if not self.__verify_password(): 
            return False
        os.unlink(f'../resources/tmp/users_engine{user}.sqlite') # deletes user file
        return True

class User: # create a new user w name then new_profile in gui
    '''
        Each user has a local database stored inside the resources/tmp folder with a unique name
        The tmp folder contains the input passed into profiles_database 
        SqliteDict opens the file and sends the file as a key:value pair of {unique car name:engine_profile serialized data}
    '''
    def __init__(self,user_name):
        self.user_name = user_name
        self.profiles_database = SqliteDict(f'../resources/tmp/users_engine{user_name}.sqlite', autocommit=True) # opens the database

    """
        Returns the entire user database as key:value pairs
    """
    def get_profiles(self):
        return self.profiles_database.items() # returns a iterable with key:value pairs

    """
        This adds a new profile into the database as a key:value pair so the data can be easily retrieved
        and sent to the gui for display. Dictionaries are easy to work with in python so we are storing our
        new entries in a key:value database which are fast and efficient 
    """
    def new_profile(self,name,location,file_name):
        if name in self.profiles_database.keys():
            print(f'{name} already in use!')
            return
        self.profiles_database[name] = EngineProfile(name,location,file_name).__dict__ # serliazes the engine profile data and stores in db

    """
        Used in gui in the case where a user wants to delete an entry inside its own database
    """
    def delete_profile(self,name):
        del self.profiles_database[name] # removes entry from db

    """
        Returns a dictionary containing the key:value pair representing the profile with key name
    """
    def profile_by_name(self,name):
        try:
            return {name:self.profiles_database[name]}
        except:
            return {}

    """
        Returns a dictionary containing the database items that match the location specified
    """
    def profile_by_loc(self,location):
        try:
            profiles = {}
            for name,engine_profile_stats in self.profiles_database.iteritems():
                if location in engine_profile_stats.values():
                    profiles[name] = engine_profile_stats
            return profiles
        except:
            return {}
            
    """
        Destrcutor that closes the database after the user object is dereferenced 
    """
    def __del__(self):
        self.profiles_database.close()