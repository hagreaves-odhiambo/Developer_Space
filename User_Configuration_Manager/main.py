from Config_Manager import add_setting, delete_setting, update_setting, view_settings
def run_user_config_manager():
    user_settings = {
        'background':'violet',
        'volume':'low',
        'brightness':'medium',
        'Cursor size':'normal',
        
    }
    print("==============================================================")
    print("===⚙️      Welcom to the configuration manager   ⚙️==========")
    print("==================Developed by Hagreaves==========================")
    while True:
        print("\n1. View Settings")
        print("2. Add a Setting")
        print("3. Update a Setting")
        print("4. Delete a Setting")
        print("5. Exit Application")
        try:
            choice = int(input("\nEnter your choice (1-5): \n"))
        except ValueError:
            print("\nPlease enter only a number of choice between 1 to 5")
            #choice = int(input("\nEnter your choice (1-5): "))
            continue    
       # if not isinstance(choice, int):
        #    choice = input("\nEnter your choice must be an integer only (1-5): ")
        if choice == 1 :
            print(f"\n{view_settings(user_settings)}")
        elif choice == 2 :
            key = input("\nEnter the name of the setting to be added: ")
            value = input("\nEnter the value of th value of the setting:")
            if key != '' or value!= '':
                setting =(key, value)
                print(add_setting(user_settings,setting))
            else:
                print("❌ Error: Key and value cannot be empty!")
    
        elif choice == 3:
                key = input("\nEnter the name of setting you want to update:")
                value = input("\nEnter the setting to be updated to :")
                if key !='' and value!='':
                    setting =(key, value)
                    print(f"{update_setting(user_settings,setting)}")
                else: 
                    print("❌ Error: setting name and it's value cannot be empty!")
        elif choice==4:
            key = input("\nEnter name of the setting you want to delete: ")
            if key !='':
                print(delete_setting(user_settings, key))
            else:
                print("❌ Error: Setting name cannot be empty!")
        elif choice == 5:
            print("👋 Exiting Configuration Manager. Goodbye!")  
            break
        
if __name__ == "__main__":
    run_user_config_manager()