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

"""Format class."""

import dataclasses
from typing import Optional, Union

import xmile_enums
import xmile_globals

__NAMESPACE__ = "http://docs.oasis-open.org/xmile/ns/XMILE/v1.0"


@dataclasses.dataclass(kw_only=True)
class XmileFormat:
  """Default format when displaying a variable or accepting input."""

  class Meta:
    name = "format"
    namespace = xmile_globals.XMILE_NAMESPACE

  precision: Optional[Union[float, int, str]] = dataclasses.field(
      default=None,
      metadata={
          "type": "Attribute",
      },
  )
  scale_by: Optional[int] = dataclasses.field(
      default=1,
      metadata={
          "type": "Attribute",
      },
  )
  delimit_000s: Optional[bool] = dataclasses.field(
      default=False,
      metadata={
          "type": "Attribute",
      },
  )
  display_as: Optional[str] = dataclasses.field(
      default=None,
      metadata={
          "type": "Attribute",
      },
  )
