from settings_object.appsettings import SettingsObject, Setting, MergedDictSetting


class AppSettings(SettingsObject):
    """
    Settings for the ``jasmin_oauth_client`` application.
    """
    #: The authorize URL to use
    AUTHORIZE_URL = Setting(default = 'https://accounts.jasmin.ac.uk/oauth/authorize/')
    #: The token URL to use to obtain an access token
    ACCESS_TOKEN_URL = Setting(default = 'https://accounts.jasmin.ac.uk/oauth/token/')
    #: The URL to use to obtain profile information
    PROFILE_URL = Setting(default = 'https://accounts.jasmin.ac.uk/api/profile/')
    #: Indicates whether to perform verification of the SSL certificate
    #: This should be ``True`` in production
    VERIFY_SSL = Setting(default = True)
    #: The oauth client id
    CLIENT_ID = Setting()
    #: The oauth client secret
    CLIENT_SECRET = Setting()
    #: The scopes to ask for
    SCOPES = Setting(default = lambda s: (s.PROFILE_URL, ))
    #: The session key to use for storing the oauth state parameter
    STATE_SESSION_KEY = Setting(default = 'jasmin_auth_state')
    #: The session key to use for the login redirect url
    NEXT_URL_SESSION_KEY = Setting(default = 'jasmin_auth_next_url')
    #: The error message for each error code
    ERROR_MESSAGES = MergedDictSetting(defaults = dict(
        access_denied = 'You did not grant the required access.',
    ))
    #: The default error message if the code is not present
    DEFAULT_ERROR_MESSAGE = Setting(
        default = 'An error occurred during authentication - please try again'
    )


app_settings = AppSettings('JASMIN_AUTH')
