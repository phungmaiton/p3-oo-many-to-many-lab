class Author:
    all = []

    def __init__(self, name):
        self.name = name

        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(
            [contract.royalties for contract in Contract.all if contract.author == self]
        )


class Book:
    all = []

    def __init__(self, title):
        self.title = title

        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise Exception

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.book = book
        self.author = author
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if book and isinstance(book, Book):
            self._book = book
        else:
            raise Exception

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if author and isinstance(author, Author):
            self._author = author
        else:
            raise Exception

    def contracts_by_date():
        return sorted(Contract.all, key=lambda contract: contract.date)
