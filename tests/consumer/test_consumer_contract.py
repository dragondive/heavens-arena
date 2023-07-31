"""Unit tests for the consumer."""
import pytest
from pact import Consumer as PactConsumer, Provider, Like

from consumer.consumer import Consumer

PACK_MOCK_HOST = "localhost"
PACK_MOCK_PORT = 1234


@pytest.fixture
def consumer():
    return Consumer(base_uri=f"http://{PACK_MOCK_HOST}:{PACK_MOCK_PORT}")


@pytest.fixture
def pact_maker():
    pact_maker = PactConsumer("contract_consumer").has_pact_with(
        Provider("contract_provider"),
        host_name=PACK_MOCK_HOST,
        port=PACK_MOCK_PORT,
        file_write_mode="merge",
    )

    try:
        pact_maker.start_service()
        yield pact_maker
    finally:
        pact_maker.stop_service()


@pytest.mark.parametrize(
    "userid",
    range(1, 10),
)
def test_contract_get_user_info_with_valid_userid_returns_valid_user_info(
    consumer, pact_maker, userid
):
    """Check the user info fetched for the userids.

    Parameters
    ----------
    consumer : consumer.consumer.Consumer
        Fixture for the consumer that connects to the pact mock server.
    pact_maker : pact.Consumer
        Fixture for pact's Consumer that will create the contract file.
    userid : int
        userid for which information is to be fetched.
    """
    expected = {
        "name": Like("Aravind Pai"),
        "email": Like("dragondive@outlook.in"),
    }

    (
        pact_maker.given(f"User with ID {userid} exists")
        .upon_receiving("a request to get user info")
        .with_request("GET", f"/users/{userid}")
        .will_respond_with(200, body=expected)
    )

    with pact_maker:
        user_info = consumer.get_user_info(userid=userid)
        assert user_info is not None
        assert isinstance(user_info.name, str)
        assert isinstance(user_info.email, str)
