from abc import ABC,abstractmethod
import random

class Transaction(ABC):
    def __init__(self,customer_id,teller_id):
        self.customer_id = customer_id
        self.teller_id =teller_id
    
    def get_customer_id(self):
        return self.customer_id

    def get_teller_id(self):
        return self.teller_id

    @abstractmethod
    def get_transaction_description(self):
        pass

class Withdrawal(Transaction):
    def __init__(self,customer_id,teller_id,amount):
        super(Withdrawal, self).__init__(customer_id,teller_id,amount)
        self.amount=amount
    
    def get_transaction_description(self):
        return f"Teller {self.teller_id} withdrew {self.amount} from account {self.customer_id}"

class Deposit(Transaction):
    def __init__(self,customer_id,teller_id,amount):
        super(Withdrawal, self).__init__(customer_id,teller_id,amount)
        self.amount=amount
    
    def get_transaction_description(self):
        return f"Teller {self.teller_id} deposited {self.amount} to account {self.customer_id}"
    
class OpenAccount(Transaction):
    def __init__(self,customer_id,teller_id):
        super(Withdrawal, self).__init__(customer_id,teller_id)
    
    def get_transaction_description(self):
        return f"Teller {self.teller_id} opened account {self.customer_id}"

class BankTeller:
    def __init__(self,id) -> None:
        self.id=id
    
    def get_teller_id(self):
        return self.id

class BankAccount:
    def __init__(self,customer_id,name,balance) -> None:
        self.customer_id=customer_id
        self.name=name
        self.balance=balance
    
    def get_balance(self):
        return self.balance

    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw(self,amount):
        self.balance-=amount

class BankSystem:
    def __init__(self,accounts,transactions) -> None:
        self.accounts=accounts
        self.transactions=transactions
    
    def get_account(self,customer_id):
        return self.accounts[customer_id]

    def get_transactions(self):
        return self.transactions

    def get_accounts(self):
        return self.accounts
    
    def open_account(self,customer_name,teller_id):
        customer_id=len(self.accounts)
        account=BankAccount(customer_id,customer_name,0)
        self.accounts.append(account)

        transaction=OpenAccount(customer_id,teller_id)
        self.transactions.append(transaction)
        return customer_id

    def deposit(self,customer_id,teller_id,amount):
        account=self.get_account[customer_id]
        account.deposit(amount)

        transaction=Deposit(customer_id,teller_id)
        self.transactions.append(transaction)

    def withdraw(self,customer_id,teller_id,amount):
        if amount>self.get_account(customer_id).get_balance():
            raise Exception('Insufficient funds')
        account=self.get_account[customer_id]
        account.withdraw(amount)

        transaction=Withdrawal(customer_id,teller_id)
        self.transactions.append(transaction)
    



class BankBranch:
    def __init__(self,address,cash_on_hand,bank_system) -> None:
        self.address=address
        self.cash_on_hand=cash_on_hand
        self.bank_system=bank_system
        self.tellers=[]
    
    def add_tellers(self,teller):
        self.tellers.append(teller)
    
    def get_available_teller(self):
        index = round(random.random() * (len(self._tellers) - 1))
        return self.tellers[index].get_id()

    def open_account(self,customer_name):
        if not self.tellers:
            raise ValueError('Branch does not have any tellers')

        teller_id=self.get_available_teller()
        return self.bank_system.open_account(customer_name,teller_id)
    
    def deposit(self,customer_id,amount):
        if not self.tellers:
            raise ValueError('Branch does not have any tellers')

        teller_id=self.get_available_teller()
        return self.bank_system.deposit(customer_id,teller_id,amount)

    def withdraw(self,customer_id,amount):
        if not self.tellers:
            raise ValueError('Branch does not have any tellers')

        teller_id=self.get_available_teller()
        return self.bank_system.withdraw(customer_id,teller_id,amount)

    def collect_cash(self, ratio):
        cash_to_collect = round(self.cash_on_hand * ratio)
        self.cash_on_hand -= cash_to_collect
        return cash_to_collect

    def provide_cash(self, amount):
        self.cash_on_hand += amount

class Bank:
    def __init__(self,address,bank_system,total_cash) -> None:
        self.address=address
        self.bank_system=bank_system
        self.total_cash = total_cash
        self.branches=[]
    
    def addBranch(self,address, initial_funds):
        branch=BankBranch(address,initial_funds,self.bank_system)
        branch = BankBranch(address, initial_funds, self.bank_system)
        self.branches.append(branch)
        return branch

    def collect_cash(self,ratio):
        for branch in self.branches:
            cash_collected=branch.collect_cash(ratio)
            self.total_cash+=cash_collected
        return self.total_cash
    
    def print_transactions(self):
        for transaction in self.bank_system.get_transactions():
            print(transaction.get_transaction_description())