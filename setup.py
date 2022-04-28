import setuptools

setuptools.setup(
    name='strava_calendar_summary_data_access_layer',
    version='0.0.23',
    author='Sebastian Tota',
    author_email='seb001@protonmail.com',
    description='The Data Access Layer for the Strava Calendar Summary Application',
    url='',
    packages=setuptools.find_packages(),
    install_requires=['google-cloud-firestore', 'google-auth']
)