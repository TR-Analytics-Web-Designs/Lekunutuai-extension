# /user_management/manage_premium_accounts.py

class PremiumAccountManager:
    def __init__(self):
        self.premium_users = set()

    def add_premium_user(self, user_id):
        self.premium_users.add(user_id)

    def is_premium(self, user_id):
        return user_id in self.premium_users

# Usage
premium_manager = PremiumAccountManager()
premium_manager.add_premium_user('user1')
print(premium_manager.is_premium('user1'))
