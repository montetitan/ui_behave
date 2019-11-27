# -*- coding: utf-8 -*-
"""
    ui-tests.lib.session
    ~~~~~~~~~~~~~~~~~~~~~

    Stores current user session
"""


class Session(object):
    """
    Session holds current username and password that we used to log in to application
    """

    def __init__(self, username, password):
        """
        Creates new Session from provided username and password

        :param username: session username
        :param password: session password
        """

        self.username = username
        self.password = password

    def format_steps(self, steps):
        """
        Formats steps that contain {username} and {password} and replace them with Session data

        :param steps: string containing Behave steps
        :return: formatted steps
        """

        return steps.format(username=self.username, password=self.password)
