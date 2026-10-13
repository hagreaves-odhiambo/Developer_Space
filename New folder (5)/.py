test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
    
    }

def add_setting(settings,settings_tuple):
    key_existing = False
    last_message = ''
    #pass
    for item in settings_tuple:
        if isinstance(item, dict):
            for k,v in item.items():
                if isinstance(k, str):
                    k = k.lower()
                if isinstance(v, str):
                    v = v.lower()
                if k in set(settings):
                    last_message = f"Setting '{k}' already exists! Cannot add a new setting with this name."
                    key_existing = True
                else:
                    settings[k] = v
                    last_message = f"Setting '{k}' added with value '{v}' successfully!"
                    key_existing = False
#                settings[k] = v
                print(k, v)
        elif isinstance(item, tuple) and len(item) == 2:
            k, v = item
            if isinstance(k, str):
                k = k.lower()
            if isinstance(v, str):
                v = v.lower()
            #settings[k] = v
            #print(f"{k} : {v}")
            if k in set(settings):
                last_message = f"Setting '{k}' already exists! Cannot add a new setting with this name."
                key_existing = True
            else:
                settings[k] = v
                last_message = f"Setting '{k}' added with value '{v}' successfully!"
                key_existing = False
    return last_message
def update_setting(settings,settings_tuple):
    #pass
    k, v = settings_tuple
    k = k.lower()
    v = v.lower()
    add_setting(settings, settings_tuple)
    if key_existing:
        settings[k] = v
    else:
        return f"Setting '{k}' does not exist! Cannot update a non-existing setting"

def delete_setting(o,p):
    pass
def view_setting(l):
    pass

"""additional_settings = ({
    'Theme': 'light',
    'language': 'English',
    },
    ('THEME', 'dark'))
#print(add_setting(test_settings,additional_settings))

"""
"""
   for item in settings_tuple:
        if isinstance(item, dict):
            for k, v in item.items():
                key = k.lower()
                value = v.lower()
                print(key, value)
                if key in set(settings):
                    return f"Setting '{key}' already exists! Cannot add a new setting with this name."                    
                else:
                    return 

        elif isinstance(item, tuple):
            k, v = item
            key = k.lower()
            value = v.lower()
            print(key, value)
"""
def delete_setting(settings, settings_key):
    key = str(settings_key.lower())
    if key in set(settings):
        settings.pop(key)
        return settings
        


#print(delete_setting(test_settings, "theme"))
def view_settings(settings):
    if settings =={}:
        return "No settings available"  
    else: 
    #key, value settings.items():
        message = f"Current User Settings:\n"
        for key in set(settings):
            value = settings[key]
            message += f"{key}: {value}\n"
            return message

        
print(view_settings(test_settings))