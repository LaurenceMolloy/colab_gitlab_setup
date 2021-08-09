from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='ColabGitlabSetup',
    url='https://github.com/LaurenceMolloy/colab_gitlab_setup',
    author='Laurence Molloy',
    author_email='laurence.molloy@gmail.com',
    # Needed to actually package something
    packages=['colab_gitlab_setup'],
    # Needed for dependencies
    install_requires=['os','subprocess','re','google.colab'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='A simple API for linking Google Colab Notebooks to Gitlab using SSH',
    # We will also need a readme eventually (there will be a warning)
    #long_description=open('README.txt').read(),
)
