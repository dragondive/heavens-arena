"""Consumer example for contract testing."""

import requests


class Consumer:
    """Consumer that fetches data using REST API.

    Parameters
    ----------
    base_uri : str
        Base URI to use for the REST API."""

    def __init__(self, base_uri):
        self.base_uri = base_uri

    def get_user_info(self, userid: int):
        """Return user information for the specified userid.

        Parameters
        ----------
        userid : int
            Userid of the user whose information is requested.

        Returns
        -------
        user_info : UserInfo or None
            Information about the user, or None if userid not found.

        """
        uri = f"{self.base_uri}/users/{userid}"
        response = requests.get(uri)
        if response.status_code == 404:
            return None

        json = response.json()
        return UserInfo(json["name"], json["email"], json["userid"])


class UserInfo:
    """Information about a user.

    Attributes
    ----------

    name: str
        User's full name.
    email: str
        User's email address.

    """

    def __init__(self, name: str, email: str, userid: str):
        self.name = name
        self.email = email
        self.userid = userid
