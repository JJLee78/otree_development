from os import environ

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'captcha_quiz',
        'display_name': "CAPTCHA Quiz with Multiple Price List",
        'num_demo_participants': 1,
        'app_sequence': ['captcha_quiz', 'mpl'],
    },

]


# ISO-639 code
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = []

ALLOWED_HOSTS = ['*']
# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'a1234'

# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {'', None, '1'})

DEMO_PAGE_INTRO_HTML = """
 The apps allow conducting the CAPTCHA quiz with MPL.
 """


# don't share this with anybody.
SECRET_KEY = 'ot'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
