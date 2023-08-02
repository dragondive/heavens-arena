"""Unit tests for the consumer."""
import pytest

from consumer.consumer import Consumer


@pytest.fixture
def consumer():
    return Consumer(base_uri="https://jsonplaceholder.typicode.com")


@pytest.mark.skip("for demo")
@pytest.mark.parametrize(
    "userid",
    range(1, 10),
)
def test_get_user_info_with_valid_userid_returns_valid_user_info(consumer, userid):
    """Check the user info fetched for the userids.

    Parameters
    ----------
    consumer : consumer.consumer.Consumer
        Fixture for the consumer that connects to the pact mock server.
    userid : int
        userid for which information is to be fetched.
    """
    user_info = consumer.get_user_info(userid=userid)
    assert user_info is not None
    assert isinstance(user_info.name, str)
    assert isinstance(user_info.email, str)
