import os
import shutil
import winshell

# Function to create a new Chrome profile
def create_chrome_profile(profile_name, base_dir):
    profile_directory = os.path.join(base_dir, profile_name)
    if not os.path.exists(profile_directory):
        os.makedirs(profile_directory)

    first_run_file = os.path.join(profile_directory, 'First Run')
    open(first_run_file, 'a').close()

    preferences_file = os.path.join(profile_directory, 'Preferences')
    with open(preferences_file, 'w') as prefs:
        prefs.write('{ "created_by_version": "123.45" }')

    return profile_directory

# Function to create a shortcut for a Chrome profile on Windows
def create_shortcut(profile_directory, chrome_exe):
    shortcut_path = os.path.join(profile_directory, 'Chrome_Profile.lnk')

    with winshell.shortcut(shortcut_path) as shortcut:
        shortcut.path = chrome_exe
        shortcut.arguments = '--user-data-dir="{}"'.format(profile_directory)
        shortcut.icon = chrome_exe
        shortcut.working_directory = profile_directory

# Base directory for Chrome profiles
base_profiles_dir = r'D:\NguoiDung\NguoiDung'

# Directory for storing shortcut files
shortcut_files_dir = r'D:\NguoiDung'

# Chrome executable path
chrome_exe_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  # Replace with your Chrome path

# Create multiple Chrome profiles and individual shortcut files

for i in range(1, 101):
   
    profile_name = ""
    if i < 10:
        profile_name = f"NguoiDung-00{i}"
    elif i >= 10 and i < 100:
        profile_name = f"NguoiDung-0{i}"
    else:
        profile_name = f"NguoiDung-{i}"
    profile_dir = create_chrome_profile(profile_name, base_profiles_dir)
    create_shortcut(profile_dir, chrome_exe_path)

    # Create individual shortcut files for each profile
    profile_shortcut_path = os.path.join(shortcut_files_dir, f'{profile_name}.lnk')
    shutil.copy(os.path.join(profile_dir, 'Chrome_Profile.lnk'), profile_shortcut_path)
