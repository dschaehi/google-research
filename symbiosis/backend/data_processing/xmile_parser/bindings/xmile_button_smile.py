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
from typing import Optional, Union

import xmile_globals
import xmile_model_view

__NAMESPACE__ = "http://www.systemdynamics.org/XMILE"


@dataclasses.dataclass(kw_only=True)
class XmileButtonSmile:

  class Meta:
    name = "button"
    namespace = xmile_globals.SMILE_NAMESPACE

  text_align: str = dataclasses.field(
      metadata={
          "name": "text-align",
          "type": "Attribute",
          "required": True,
      }
  )
  label: str = dataclasses.field(
      metadata={
          "type": "Attribute",
          "required": True,
      }
  )
  style: str = dataclasses.field(
      metadata={
          "type": "Attribute",
          "required": True,
      }
  )
  appearance: str = dataclasses.field(
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
  background: str = dataclasses.field(
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
  font_family: str = dataclasses.field(
      metadata={
          "name": "font-family",
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
  color: str = dataclasses.field(
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
  font_size: int = dataclasses.field(
      metadata={
          "name": "font-size",
          "type": "Attribute",
          "required": True,
      }
  )
  x: int = dataclasses.field(
      metadata={
          "type": "Attribute",
          "required": True,
      }
  )
  story: xmile_model_view.XmileStory = dataclasses.field(
      metadata={
          "type": "Element",
          "namespace": xmile_globals.ISEE_NAMESPACE,
          "required": True,
      }
  )
