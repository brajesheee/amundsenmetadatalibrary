# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

import attr
from marshmallow_annotations.ext.attrs import AttrsSchema
from . import Badge


@attr.s(auto_attribs=True, kw_only=True)
class Badge:
    badge_name: str = attr.ib()
    category: str = attr.ib()
    badge_type: str = attr.ib()

    def equals(self, other: Badge) -> bool:
        return (self.badge_name == other.badge_name) and \
               (self.category == other.category) and (self.badge_type == other.badge_type)


class BadgeSchema(AttrsSchema):
    class Meta:
        target = Badge
        register_as_scheme = True
