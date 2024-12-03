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

import dataclasses
from typing import List
import xmile_globals
import xmile_graph_smile

__NAMESPACE__ = "http://www.systemdynamics.org/XMILE"


@dataclasses.dataclass(kw_only=True)
class XmileStackedContainerSmile:

  class Meta:
    name = "stacked_container"
    namespace = xmile_globals.SMILE_NAMESPACE

  x: int = dataclasses.field(
      metadata={
          "type": "Attribute",
          "required": True,
      }
  )
  y: int = dataclasses.field(
      metadata={
          "type": "Attribute",
          "required": True,
      }
  )
  height: int = dataclasses.field(
      metadata={
          "type": "Attribute",
          "required": True,
      }
  )
  width: int = dataclasses.field(
      metadata={
          "type": "Attribute",
          "required": True,
      }
  )
  uid: int = dataclasses.field(
      metadata={
          "type": "Attribute",
          "required": True,
      }
  )
  graph: List[xmile_graph_smile.XmileGraphSmile] = dataclasses.field(
      default_factory=list,
      metadata={
          "type": "Element",
          "min_occurs": 1,
      },
  )
