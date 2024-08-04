from setuptools import setup

APP = ['login.py']  # The entry point of your application
DATA_FILES = [
    'my_database.db',
    'pngimg.com - boxing_gloves_PNG102613.png',
    'users.db'
]
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter', 'PIL'],
    'includes': ['boxing_app', 'calorie_counter', 'database', 'practice', 'stats'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
