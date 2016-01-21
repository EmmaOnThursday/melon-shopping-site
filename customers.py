"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    # __init__ method:
        # can be passed first name, last name, email, password
    # __repr__ method
        # prints useful info about the customer (probably not password)

    #create function to read in customers.txt to a dictionary; key is email

    #get_by_email function: retrieves customer info given email address

    def __init__(self, first_name, 
                 last_name, 
                 email, 
                 password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password


    def __repr__(self):
        """Returns info about customer into console. """
        return "<Customer: %s, %s, %s>" % (
            self.first_name, self.last_name, self.email) 



def build_customer_dictionary(filename):
    """Read through txt file and build customer dictionary. """

    customer_dictionary = {}

    for line in open(filename):
        (first_name, last_name, email, password) = line.strip().split("|")
        customer_dictionary[email] = Customer(first_name, 
                                            last_name,
                                            email,
                                            password)

    return customer_dictionary



def get_by_email(email):
    """Given an email, returns customer data from customer dictionary."""

    return customer_dictionary[email]


customer_dictionary = build_customer_dictionary('customers.txt')

