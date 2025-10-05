import os
import webbrowser
import datetime
import shutil # <--- ADD THIS IMPORT

def handle_open_app(app_name):
    """Opens an application using a secure whitelist and shutil.which to find it."""
    app_map = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": "chrome.exe" # We can simplify this now
    }
    
    simple_name = app_map.get(app_name.lower())
    
    if not simple_name:
        return f"Sorry, I don't know how to open '{app_name}'."

    # Use shutil.which() to find the full path of the program
    full_path = shutil.which(simple_name)

    if full_path:
        os.startfile(full_path)
        return f"Okay, opening {app_name}."
    else:
        # This message now means the program truly isn't found or installed
        return f"I know what {app_name} is, but I can't find it on your system."

def handle_web_search(query):
    """Opens the default web browser and searches Google."""
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Here are the search results for '{query}'."

def handle_get_time():
    """Returns the current time."""
    now = datetime.datetime.now()
    # It is currently 2:42 PM on Thursday
    return f"The current time is {now.strftime('%I:%M %p')}."