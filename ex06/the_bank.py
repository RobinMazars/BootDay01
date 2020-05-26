class Account():

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

    def __repr__(self):
        txt = f"name: {self.name} id: {self.id},value : {self.value}\n"
        txt += f"dir() {self.__dir__()}\n"
        return txt


class Bank():
    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest:
            int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return     True if success, False if an error occured
        """
        if not isinstance(amount, float) or amount < 0:
            raise TypeError(f"{amount} is not a float or < 0")
        if isinstance(origin, int):
            a1 = self.find_account(origin, "int")
        elif isinstance(origin, str):
            a1 = self.find_account(origin, "string")
        else:
            raise TypeError(f"{origin} is not a int or a str")
        if isinstance(dest, int):
            a2 = self.find_account(dest, "int")
        elif isinstance(dest, str):
            a2 = self.find_account(dest, "string")
        else:
            raise TypeError(f"{dest} is not a int or a str")
        if not self.fix_account(a1):
            raise Exception(f"{a1.name} is corrupted and can't be fix.")
        if not self.fix_account(a2):
            raise Exception(f"{a2.name} is corrupted and can't be fix.")
        if a1.value >= amount:
            a1.transfer(-amount)
            a2.transfer(amount)
            print(f"Transfert from {a1.name} to {a2.name} of {amount}$.")
        else:
            print(f"{a1.name} have not enough money $$$")

    def find_account(self, atr, type):
        if type == "string":
            for x in self.account:
                if hasattr(x, "name") and x.name == atr:
                    return x
        else:
            for x in self.account:
                if hasattr(x, "id") and x.id == atr:
                    return x
        raise Exception(f"{atr} ({type}) account not found.")

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return     True if success, False if an error occured
        """
        try:
            di = account.__dir__()
            if not hasattr(account, "name"):
                account.name = "Default"
                print("fix name")
            if not hasattr(account, "value"):
                account.value = 0
                print("fix value")
            if not hasattr(account, "id"):
                vale = account.value
                account.__init__(**account.__dict__)
                account.value = vale
                print("fix id")
            find_addr = False
            find_zip = False
            for x in di:
                if x.startswith("b"):
                    delattr(account, x)
                    print("fix b")
                if x.startswith("zip"):
                    find_zip = True
                if x.startswith("addr"):
                    find_addr = True
            if not find_zip:
                account.zip = None
                print("fix zip")
            if not find_addr:
                account.addr = None
                print("fix addr")
            if len(di) % 2:
                if not hasattr(account, "not_even"):
                    account.not_even = None
                    print(f"fix eveness now len {len(di)} +")
                else:
                    delattr(account, "not_even")
                    print(f"fix eveness now len {len(di)} -")

            return True
        except Exception:
            return False


# rec2 = {'cote1': 4, 'cote2': 8}
# print(rec2.items())
a1 = Account("account 1", value=10, zip=True, addr=5, bar=True, ezfds=8)
a1.value = 1000.0
del a1.addr
a2 = Account("account 2", value="1", zip=True, addr=5)
bank = Bank()
bank.add(a1)
bank.add(a2)
bank.transfer("account 1", 2, 1500.0)
print(repr(a1))
print(repr(a2))
bank.transfer("account 1", 2, 1000.0)
print(repr(a1))
print(repr(a2))
