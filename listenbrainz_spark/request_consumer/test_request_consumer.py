from unittest.mock import patch, MagicMock

from listenbrainz_spark.request_consumer.request_consumer import RequestConsumer
from listenbrainz_spark.tests import SparkTestCase
from listenbrainz_spark.utils import create_app


class RequestConsumerTestCase(SparkTestCase):

    def setUp(self):
        self.consumer = RequestConsumer()
        self.consumer.rabbitmq = MagicMock()
        self.consumer.request_channel = MagicMock()
        self.consumer.result_channel = MagicMock()

    @patch('listenbrainz_spark.request_consumer.request_consumer.init_rabbitmq')
    def test_connect_to_rabbitmq(self, mock_init_rabbitmq):
        with create_app().app_context():
            self.consumer.connect_to_rabbitmq()
            mock_init_rabbitmq.assert_called_once()


