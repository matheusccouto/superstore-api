""" Unit tests for API. """

import api

client = api.app.test_client()


class TestHome:
    """Test homepage."""

    def test_get(self):
        """Test GET. Response status must be 200 (OK)."""
        assert client.get(r"/").status_code == 200

    def test_post(self):
        """Test POST. Response status must be 405 (method not allowed)."""
        assert client.post(r"/", data={}).status_code == 405

    def test_put(self):
        """Test PUT. Response status must be 405 (method not allowed)."""
        assert client.put(r"/").status_code == 405

    def test_delete(self):
        """Test DELETE. Response status must be 405 (method not allowed)."""
        assert client.delete(r"/").status_code == 405


class TestSales:
    """Test sales endpoint."""

    def test_get(self):
        """Test GET. Response status must be 200 (OK)."""
        assert client.get(r"/v1/sales/?weeks=1").status_code == 200

    def test_length(self):
        """Test length from all players sequence."""
        assert len(client.get(r"/v1/sales/?weeks=52").json) == 52

    def test_post(self):
        """Test POST. Response status must be 405 (method not allowed)."""
        assert client.post(r"/v1/sales/?weeks=1").status_code == 405

    def test_put(self):
        """Test PUT. Response status must be 405 (method not allowed)."""
        assert client.put(r"/v1/sales/?weeks=1").status_code == 405

    def test_delete(self):
        """Test DELETE. Response status must be 405 (method not allowed)."""
        assert client.delete(r"/v1/sales/?weeks=1").status_code == 405
