# /user_management/manage_free_accounts.py

class FreeAccountManager:
    def __init__(self):
        self.user_credits = {}

    def set_credits(self, user_id, credits):
        self.user_credits[user_id] = credits

    def get_credits(self, user_id):
        return self.user_credits.get(user_id, 0)

    def deduct_credit(self, user_id):
        if self.user_credits.get(user_id, 0) > 0:
            self.user_credits[user_id] -= 1

# Usage
free_manager = FreeAccountManager()
free_manager.set_credits('user1', 10)
free_manager.deduct_credit('user1')
print(free_manager.get_credits('user1'))
