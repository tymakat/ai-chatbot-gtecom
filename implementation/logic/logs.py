import os
from datetime import datetime
from config import LOG_PATH


def get_current_timestamp():
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

def save_to_txt(line: str):

    # Ensure folder exists
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

    # Append line to .txt file
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")
        
def log_tool_usage(session_id = "unknown", tool_name = "unknown_tool", message = "N/a", is_error = False):
    information_to_save = ""
    if is_error:
        information_to_save = f"{get_current_timestamp()} | Error when using the tool function! | 'error': {message} | 'session_nr': {session_id} | 'log_type': 'tool_interaction' | 'tool_name': {tool_name}"
    else:
        information_to_save += f"{get_current_timestamp()} | Tool was called! | 'message': {tool_name} | 'session_nr': {session_id} | 'log_type': 'tool_interaction' | 'tool_name': {tool_name}"
    save_to_txt(information_to_save)

def log_message(role, message, session_id, is_error):
    information_to_save = ""
    if is_error:
        information_to_save = f"{get_current_timestamp()} | Error when sending a message! | 'error': {message} | 'session_nr': {session_id} | 'log_type': 'message' | 'role': {role}"
    else:
        information_to_save = f"{get_current_timestamp()} | Message sent | 'message': {message} | 'session_nr': {session_id} | 'log_type': 'message' | 'role': {role}"
    save_to_txt(information_to_save)
