import pandas as pd

#Tools that will be used by chatgpt to provide relevant order info from orders.csv
#Not using tool wrapper/property here as it would be impossible to unit test
def fetch_order_by_id(order_id: str):
    """Fetch an order by id from a provided csv table.
    """
    try:
        print("called")
        df = pd.read_csv("order_information/orders.csv", sep=",")
        #Only one order can be associated with order id
        associated_order = df[df["order_id"] == order_id]
        return associated_order.to_dict()
    except Exception as e:
        print(e)
        #if parsing fails or file doesnt exist return an empty dictionary, so the model can say that nothing was found
        return dict()

def fetch_order_by_email(email: str):
    """Fetch an order by email from a provided csv table.
    """
    try:
        print("called")
        df = pd.read_csv("order_information/orders.csv", sep=",")
        associated_order = df[df["email"] == email]
        return associated_order.to_dict()
    except Exception as e:
        #same as method above
        return dict()