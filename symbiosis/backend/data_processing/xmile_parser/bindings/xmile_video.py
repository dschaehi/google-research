# coding=utf-8
# Copyright 2024 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Video class."""

import dataclasses
from typing import Optional
import xmile_globals

__NAMESPACE__ = "http://docs.oasis-open.org/xmile/ns/XMILE/v1.0"


@dataclasses.dataclass(kw_only=True)
class XmileVideo:
  """Video class."""

  class Meta:
    name = "video"
    namespace = xmile_globals.XMILE_NAMESPACE

  value: str = dataclasses.field(
      default="",
      metadata={
          "required": True,
      },
  )
  resource: Optional[str] = dataclasses.field(
      default=None,
      metadata={
          "type": "Attribute",
      },
  )
  size_to_parent: bool = dataclasses.field(
      default=False,
      metadata={
          "type": "Attribute",
      },
  )
  width: Optional[int] = dataclasses.field(
      default=None,
      metadata={
          "type": "Attribute",
      },
  )
  height: Optional[int] = dataclasses.field(
      default=None,
      metadata={
          "type": "Attribute",
      },
  )
