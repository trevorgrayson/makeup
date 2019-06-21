import load
from mlf import MlfBase


class Awesomeo(MlfBase):
    
    LOAD_MODULE = load

    def load(self, accounts, purchases):
        accounts2purchases = dict([(user_id, {'email': email, 'purchases': []})
            for (user_id, email) in accounts])

        for (user_id, purchase) in purchases:
            accounts2purchases[user_id]['purchases'].append(purchase)

        return (accounts, purchases) 
        {
            'a2p': accounts2purchases
        }

    def train(self, accounts, purchases):
        # self.cross_validate // 10
        pass
        
    def cross_validate(self, *args):
        pass

    def run(self, accounts, purchases):
        print(accounts)

Awesomeo().execute()

