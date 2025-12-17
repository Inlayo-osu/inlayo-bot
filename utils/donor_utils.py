class Patreon:
    def __init__(self):
        self.patrons = []
    
    def is_patron(self, user_id):
        return user_id in self.patrons
    
    def add_patron(self, user_id):
        if user_id not in self.patrons:
            self.patrons.append(user_id)
    
    def remove_patron(self, user_id):
        if user_id in self.patrons:
            self.patrons.remove(user_id)
