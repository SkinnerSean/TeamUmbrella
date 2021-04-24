import engine_profile

class Admin:
    def __init__(self):
        pass

class User:
    def __init__(self):
        self.profiles = {} # call load profile, read from json to poplate dict of profile_name,engine_profile objs, empty dict if json is empty

    def load_profiles(self):
        pass

    def save_profiles(self):
        pass

    def new_profile(self,name):
        pass

    def del_profile(self,name):
        pass
    
    def profile_by_name(self,name):
        pass
    
    def profile_by_loc(self,location):
        pass
