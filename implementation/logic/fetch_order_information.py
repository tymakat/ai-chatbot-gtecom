import pandas as pd
from config import DATASET_PATH
from logs import log_tool_usage

#Tools that will be used by chatgpt to provide relevant order info from orders.csv
#Not using tool wrapper/property here as it would be impossible to unit test
def fetch_order_by_id(order_id: str, session_id: str):
    try:
        df = pd.read_csv(DATASET_PATH, sep=",")
        #Only one order can be associated with order id
        associated_order = df[df["order_id"] == order_id]
        log_tool_usage(session_id=session_id, tool_name="fetch_order_by_order_id", message=f"Order information: {associated_order.to_dict()} ", is_error=False)
        return associated_order.to_dict()
    except Exception as e:
        log_tool_usage(session_id=session_id, tool_name="fetch_order_by_email", message=e, is_error=True)
        #if parsing fails or file doesnt exist return an empty dictionary, so the model can say that nothing was found
        return dict()

def fetch_order_by_email(email: str, session_id: str):
    try:
        df = pd.read_csv(DATASET_PATH, sep=",")
        associated_order = df[df["email"] == email]
        #Not sure if I should log an error if there are no orders associated with the email
        log_tool_usage(session_id=session_id, tool_name="fetch_order_by_email", message=f"Order information: {associated_order.to_dict()} ", is_error=False)
        return associated_order.to_dict()
    except Exception as e:
        log_tool_usage(session_id=session_id, tool_name="fetch_order_by_email", message=e, is_error=True)
        #same as method above
        return dict()