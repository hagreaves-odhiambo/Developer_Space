
def add_setting(settings, settings_tuple):
    key, value = settings_tuple
    key = key.lower()
    value = value.lower()
    if key in set(settings):
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, settings_tuple):
    key, value = settings_tuple
    key = key.lower()
    value = value.lower()
    if key in set(settings):
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, settings_key):
    key = str(settings_key.lower())
    if key in set(settings):
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    if key not in set(settings):
        return "Setting not found!"


def view_settings(settings):
    if settings =={}:
        return "No settings available."  
    else: 
        message = "Current User Settings:\n"
        for key, value in settings.items():
            capitalized_key = str(key).capitalize()
            message += f"{capitalized_key}: {value}\n"
        return message

        
