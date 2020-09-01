# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus

from flask import current_app
from mock import MagicMock

from metadata_service import create_app
from metadata_service.api.badge import BadgeCommon
from metadata_service.entity.resource_type import ResourceType
from tests.unit.api.dashboard.dashboard_test_case import DashboardTestCase

BADGE_NAME = 'foo'
CATEGORY = 'table_status'
BADGE_TYPE = 'neutral'


class TestDashboardBAdgeAPI(DashboardTestCase):
    """
        Test the service if it can standup
        """

    def setUp(self) -> None:
        self.app = create_app(
            config_module_class='metadata_service.config.LocalConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self) -> None:
        self.app_context.pop()

    def test_app_exists(self) -> None:
        self.assertFalse(current_app is None)

    def test_badge_on_reserved_badge_name(self) -> None:
        self.app.config['WHITELIST_BADGES'] = [BADGE_NAME]

        mock_proxy = MagicMock()

        badge_common = BadgeCommon(client=mock_proxy)
        response = badge_common.put(id='',
                                    resource_type=ResourceType.Dashboard,
                                    badge_name=BADGE_NAME,
                                    category=CATEGORY,
                                    badge_type=BADGE_TYPE)

        self.assertEqual(response[1], HTTPStatus.OK)

    def test_badge_on_not_reserved_badge_name(self) -> None:
        self.app.config['WHITELIST_BADGES'] = []

        mock_proxy = MagicMock()
        badge_common = BadgeCommon(client=mock_proxy)
        response = badge_common.put(id='',
                                    resource_type=ResourceType.Dashboard,
                                    badge_name=BADGE_NAME,
                                    category=CATEGORY,
                                    badge_type=BADGE_TYPE)

        self.assertEqual(response[1], HTTPStatus.NOT_FOUND)
