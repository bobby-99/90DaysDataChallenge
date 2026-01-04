def add_setting(settings: dict, pairs: tuple):
    if not isinstance(pairs, tuple):
        return f"Please provide a tuple as settings value"
    lowercase = tuple([items.lower() for items in pairs if isinstance(items, str)])
    if lowercase[0] in settings:
        return f"Setting '{lowercase[0]}' already exists! Cannot add a new setting with this name."
    else:
        settings.update([lowercase])
        return f"Setting '{lowercase[0]}' added with value '{lowercase[1]}' successfully!"


def update_setting(settings: dict, pairs: tuple):
    if not isinstance(pairs, tuple):
        return f"Please provide a tuple as settings value"
    lowercase = tuple([items.lower() for items in pairs if isinstance(items, str)])
    if lowercase[0] in settings:
        settings[lowercase[0]] = lowercase[1]
        return f"Setting '{lowercase[0]}' updated to '{lowercase[1]}' successfully!"
    else:
        return f"Setting '{lowercase[0]}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings: dict, key: str):
    lowercase_key = key.lower()
    if lowercase_key in settings:
        del settings[lowercase_key]
        return f"Setting '{lowercase_key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings: dict):
    if not settings:
        return "No settings available."

    lines = ["Current User Settings:"]
    for key, val in settings.items():
        lines.append(f"{key.capitalize()}: {val}")

    return "\n".join(lines) + "\n"

    
test_settings = {
    'theme': 'dark', 
    'notifications': 'enabled', 
    'volume': 'high'
}

