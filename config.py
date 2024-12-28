import os
from pydrive2.auth import GoogleAuth

currentFile = __file__
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)
dirName = os.path.basename(dirPath)



SIMPLE_CAPTION = '''<code>{}</code>'''

LOG_MESSAGE = "<code>[🙄]</code> <b>{}</b>\n<b><code>[+]</code> <b>{} : </b><code>{}</code>"

class GDRIVE_CONFIG:
    #for Gdrive (Leave it as Empty String if not Gdrive Upload is turned ON)
    root_folder_id = "1dkH1j4naVN0eem7kOSS8sTB3gt4cSdKQ"

    #keep it empty if you don't have index link or don't touch
    indexlink_format = ""

    is_making_drive_files_public = True

class GD_SHARER_CONFIG:

    is_uploading_to_filepress = False

    #Don't add a trailing slash at the end (keep in this format only - https://new5.filepress.store)
    filepress_url = "https://new9.filepress.store"
    
    cookie_path = dirPath + "/cookies/filepress.txt"
    _, dict_cookies = get_cookies(cookie_path)
    
    filepress_connect_sid_cookie_value = dict_cookies.get("connect.sid")


DL_DONE_MSG = """
✅ <b> Task Completed In </b> <code>{}</code>

<b>FileName : </b> <code>{}</code>
<b>OTT : </b> <code>{}</code>
<b>Size : </b> <code>{}</code>
"""

token_file = os.path.join(dirPath, "static", "session")

dl_folder = os.path.join(dirPath, "downloads")  

os.makedirs(dl_folder) if not os.path.exists(dl_folder) else None


gauth = GoogleAuth()
GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = client_secrets_json
