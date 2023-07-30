"""Unit tests for the consumer."""
import pytest

from consumer.consumer import Consumer


@pytest.mark.parametrize(
    "userid",
    range(1, 10),
)
def test_get_user_info_with_valid_userid_returns_valid_user_info(userid):
    """Check the user info fetched for the userids.

    Parameters
    ----------
    userid : int
        userid for which information is to be fetched.
    """
    consumer = Consumer(base_uri="https://jsonplaceholder.typicode.com")
    user_info = consumer.get_user_info(userid=userid)
    assert user_info is not None
    assert isinstance(user_info.name, str)
    assert isinstance(user_info.email, str)
