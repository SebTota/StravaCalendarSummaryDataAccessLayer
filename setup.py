import setuptools

setuptools.setup(
    name='strava_calendar_summary_data_access_layer',
    version='0.0.4',
    author='Sebastian Tota',
    author_email='seb001@protonmail.com',
    description='The Data Access Layer for the Strava Calendar Summary Application',
    url='',
    packages=['strava_calendar_summary_data_access_layer', 
    'strava_calendar_summary_data_access_layer.models', 
    'strava_calendar_summary_data_access_layer.controllers'],
    install_requires=['google-cloud-firestore']
)