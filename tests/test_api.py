""" Unit tests for API. """

import api


class TestSales:
    """Test sales endpoint."""

    @classmethod
    def setup_class(cls):
        """Setup class."""
        cls.client = api.app.test_client()

    def test_get(self):
        """Test GET. Response status must be 200 (OK)."""
        assert self.client.get(r"/v1/sales/?weeks=1").status_code == 200

    def test_length(self):
        """Test length from all players sequence."""
        assert len(self.client.get(r"/v1/sales/?weeks=52").json) == 52

    def test_post(self):
        """Test POST. Response status must be 405 (method not allowed)."""
        assert self.client.post(r"/v1/sales/", data={}).status_code == 405

    def test_put(self):
        """Test PUT. Response status must be 405 (method not allowed)."""
        assert self.client.put(r"/v1/sales/").status_code == 405

    def test_delete(self):
        """Test DELETE. Response status must be 405 (method not allowed)."""
        assert self.client.delete(r"/v1/sales/").status_code == 405
