import requests
import xmltodict
#Jio Cinema Downloader Bot Created By Aryan Chaudhary
# Request object with Session maintained
session = requests.Session()
#session.proxies.update({'http': "http://bobprakash4646:ivR8gSbjLN@103.172.85.130:49155"})
session.proxies.update({'http': "http://toonrips:xipTsP9H9s@103.171.51.246:50100"})
proxy = {'http':'http://toonrips:xipTsP9H9s@103.171.51.246:50100','https':"http://toonrips:xipTsP9H9s@103.171.51.246:50100"}
# Common Headers for Session
headers = {
    "Origin": "https://www.jiocinema.com",
    "Referer": "https://www.jiocinema.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}

# Content Type Dir Map
contentTypeDir = {
    "CAC": "promos",
    "MOVIE": "movies",
    "SHOW": "series",
    "SERIES": "series",
    "EPISODE": "series"
}

# Language Id Name Map
LANG_MAP = {
    "en": "English",
    "hi": "Hindi",
    "gu": "Gujarati",
    "ta": "Tamil",
    "te": "Telugu",
    "kn": "Kannada",
    "mr": "Marathi",
    "ml": "Malayalam",
    "bn": "Bengali",
    "bho": "Bhojpuri",
    "pa": "Punjabi",
    "or": "Oriya"
}

REV_LANG_MAP = {
    "English": "en",
    "Hindi": "hi",
    "Gujarati": "gu",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Marathi": "mr",
    "Malayalam": "ml",
    "Bengali": "bn",
    "Bhojpuri": "bho",
    "Punjabi": "pa",
    "Oriya": "or"
}

# Audio Codec Decode Map
AUDIO_CODECS = {
    "1": "PCM",
    "mp3": "MP3",
    "mp4a.66": "MPEG2_AAC",
    "mp4a.67": "MPEG2_AAC",
    "mp4a.68": "MPEG2_AAC",
    "mp4a.69": "MP3",
    "mp4a.6B": "MP3",
    "mp4a.40.2": "MPEG4_AAC",
    "mp4a.40.02": "MPEG4_AAC",
    "mp4a.40.5": "MPEG4_AAC",
    "mp4a.40.05": "MPEG4_AAC",
    "mp4a.40.29": "MPEG4_AAC",
    "mp4a.40.42": "MPEG4_XHE_AAC",
    "ac-3": "AC3",
    "mp4a.a5": "AC3",
    "mp4a.A5": "AC3",
    "ec-3": "EAC3",
    "mp4a.a6": "EAC3",
    "mp4a.A6": "EAC3",
    "vorbis": "VORBIS",
    "opus": "OPUS",
    "flac": "FLAC",
    "vp8": "VP8",
    "vp8.0": "VP8",
    "theora": "THEORA",
}


# Request guest token from JioCine Server
def fetchGuestToken():
    # URL to Guest Token Server
    guestTokenUrl = "https://auth-jiocinema.voot.com/tokenservice/apis/v4/guest"

    guestData = {
        "appName": "RJIL_JioCinema",
        "deviceType": "fireTV",
        "os": "android",
        "deviceId": "1464251119",
        "freshLaunch": False,
        "adId": "1464251119",
        "appVersion": "4.1.3"
    }

    r = session.post(guestTokenUrl, json=guestData, headers=headers, proxies=proxy)
    if r.status_code != 200:
        return None

    result = r.json()
    if not result['authToken']:
        return None

    return result['authToken']


# Fetch Content Details from Server
def getContentDetails(content_id):
    assetQueryUrl = "https://content-jiovoot.voot.com/psapi/voot/v1/voot-web//content/query/asset-details?" + \
                    f"&ids=include:{content_id}&responseType=common&devicePlatformType=desktop"

    r = session.get(assetQueryUrl, headers=headers, proxies=proxy)
    if r.status_code != 200:
        return None

    result = r.json()
    if not result['result'] or len(result['result']) < 1:
        return None

    return result['result'][0]


# Fetch Video URl details using Token
def fetchPlaybackData(content_id, token):
    playbackUrl = f"https://apis-jiovoot.voot.com/playback/v1/{content_id}"

    
    playData = {
        "4k": True,
        "ageGroup": "18+",
        "appVersion": "3.4.0",
        "bitrateProfile": "xxhdpi",
        "capability": {
            "drmCapability": {
                "aesSupport": "yes",
                "fairPlayDrmSupport": "none",
                "playreadyDrmSupport": "yes",
                "widevineDRMSupport": "yes"
            },
            "frameRateCapability": [
                {
                    "frameRateSupport": "60fps",
                    "videoQuality": "2160p"
                }
            ]
        },
        "continueWatchingRequired": False,
        "dolby": True,
        "downloadRequest": False,
        "hevc": True,
        "kidsSafe": False,
        "manufacturer": "Android",
        "model": "Android",
        "multiAudioRequired": True,
        "osVersion": "10",
        "parentalPinValid": False,
        "x-apisignatures": "o668nxgzwff",
        "deviceRange": "",
        "networkType": "4g",
        "deviceMemory": 4096  # Web: o668nxgzwff, FTV: 38bb740b55f, JIOSTB: e882582cc55, ATV: d0287ab96d76
    }
    playHeaders = {
        "authority": "apis-jiovoot.voot.com",
        "accesstoken": token,
        "x-platform": "androidweb",
        "x-platform-token": "web",
        "appname": "RJIL_JioCinema",
        "jc-user-agent": "JioCinema/2411044 (web; mweb/10; tablet; Chrome Android)",
        "uniqueid": "0a97cbb8e9a871ba2ae6fde431e24efe",
        "x-apisignatures": "o668nxgzwff",
        "versioncode": "2411044",
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site"
    }
    playHeaders.update(headers)

    r = session.post(playbackUrl, json=playData, headers=playHeaders, proxies = proxy)
    if r.status_code != 200:
        return None
        print("problem in playback")

    result = r.json()
    if not result['data']:
        return None

    return result['data']
    


# Fetch Series Episode List from Server
def getSeriesEpisodes(content_id):
    episodeQueryUrl = "https://content-jiovoot.voot.com/psapi/voot/v1/voot-web//content/generic/series-wise-episode?" + \
                    f"sort=episode:asc&id={content_id}"

    r = session.get(episodeQueryUrl, headers=headers, proxies=proxy)
    if r.status_code != 200:
        return None

    result = r.json()
    if not result['result'] or len(result['result']) < 1:
        return None

    return result['result']



def fetchPlaybackDataold(content_id, token):
    playbackUrl = f"https://apis-jiovoot.voot.com/playbackjv/v5/{content_id}"

    playData = {
        "4k": True,
        "ageGroup": "18+",
        "appVersion": "3.4.0",
        "bitrateProfile": "xxhdpi",
        "capability": {
            "drmCapability": {
                "aesSupport": "yes",
                "fairPlayDrmSupport": "none",
                "playreadyDrmSupport": "yes",
                "widevineDRMSupport": "yes"
            },
            "frameRateCapability": [
                {
                    "frameRateSupport": "50fps",
                    "videoQuality": "2160p"
                }
            ]
        },
        "continueWatchingRequired": False,
        "dolby": True,
        "downloadRequest": False,
        "hevc": True,
        "kidsSafe": False,
        "manufacturer": "Android",
        "model": "Android",
        "multiAudioRequired": True,
        "osVersion": "10",
        "parentalPinValid": False,
        "x-apisignatures": "o668nxgzwff",
        "deviceRange": "",
        "networkType": "4g",
        "deviceMemory": 4096  # Web: o668nxgzwff, FTV: 38bb740b55f, JIOSTB: e882582cc55, ATV: d0287ab96d76
    }
    playHeaders = {
        "authority": "apis-jiovoot.voot.com",
        "accesstoken": token,
        "x-platform": "androidweb",
        "x-platform-token": "web",
        "appname": "RJIL_JioCinema",
        "jc-user-agent": "JioCinema/2411044 (web; mweb/10; tablet; Chrome Android)",
        "uniqueid": "0a97cbb8e9a871ba2ae6fde431e24efe",
        "x-apisignatures": "o668nxgzwff",
        "versioncode": "2411044",
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site"
    }
    playHeaders.update(headers)

    r = session.post(playbackUrl, json=playData, headers=playHeaders, proxies = proxy)
    if r.status_code != 200:
        return None
        print("problem in playback")

    result = r.json()
    if not result['data']:
        return None

    return result['data']



# Fetch Video URl details using Token

def getMPDData(mpd_url,is_hs=False):
    headerhs = {
    "Origin": "https://www.hotstar.com",
    "Referer": "https://www.hotstar.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }
    headerjcs = {
    "Origin": "https://www.jiocinema.com",
    "Referer": "https://www.jiocinema.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }
    if is_hs:
        r = session.get(mpd_url, headers=headerhs, proxies=proxy)
    else:
        r = session.get(mpd_url, headers=headers, proxies=proxy)
    if r.status_code != 200:
        return None

    try:
        import logging
        logging.info(r.content)
        return xmltodict.parse(r.content), r.text
    except Exception as e:
        print(f"[!] getMPDData: {e}")
        return None


# Parse MPD data for PSSH maps
def parseMPDData(mpd_per):
    # Extract PSSH and KID
    rid_kid = {}
    pssh_kid = {}
    import logging
    logging.info("pase mpd data")

    # Store KID to corresponding Widevine PSSH and Representation ID
    def readContentProt(rid, cp):
        _pssh = None
        if cp[1]["@schemeIdUri"].lower() == "urn:uuid:edef8ba9-79d6-4ace-a3c8-27dcd51d21ed":
            logging.info("found pssh")
            _pssh = cp[1]["cenc:pssh"]

        if _pssh:
            if _pssh not in pssh_kid:
                pssh_kid[_pssh] = set()

            if cp[0]['@value'].lower() == "cenc":
                _kid = cp[0]["@cenc:default_KID"].replace("-", "")  # Cleanup
                logging.info("found kid")

                rid_kid[rid] = {
                    "kid": _kid,
                    "pssh": _pssh
                }
                if _kid not in pssh_kid[_pssh]:
                    pssh_kid[_pssh].add(_kid)

    # Search PSSH and KID
    for ad_set in mpd_per['AdaptationSet']:
        resp = ad_set['Representation']
        if isinstance(resp, list):
            for res in resp:
                if 'ContentProtection' in res:
                    readContentProt(res['@id'], res['ContentProtection'])
        else:
            if 'ContentProtection' in resp:
                readContentProt(resp['@id'], resp['ContentProtection'])

    return rid_kid, pssh_kid


# Perform Handshake with Widevine Server for License
def getWidevineLicense(license_url, challenge, token, playback_id=None):
    # Just in case :)
    if not playback_id:
        playback_id = "27349583-b5c0-471b-a95b-1e1010a901cb"

    drmHeaders = {
        "authority": "key-jio.voot.com",
        "accesstoken": token,
        "appname": "RJIL_JioCinema",
        "devicetype": "androidstb",
        "os": "android",
        "uniqueid": "1957805b-8c2a-4110-a5d9-767da377ffce",
        "x-platform": "fireOS",
        "x-feature-code": "ytvjywxwkn",
        "x-playbackid": playback_id
    }
    drmHeaders.update(headers)

    r = session.post(license_url, data=challenge, headers=drmHeaders, proxies=proxy)
    if r.status_code != 200:
        print(f"[!] Error: {r.content}")
        return None

    return r.content



#Jio Cinema Downloader Bot Created By Aryan Chaudhary
