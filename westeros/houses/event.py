#
# Copyright 2011 Scott Turnbull
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Founding(object):
    """
    Provides basic information on generating a founding.
    """
    def __init__(self, label, code, rnd):
        """
        Creates a new founding event type.
        :param label:  String represending the short description of the founding period.
        :param code:  INT designating the founding code, used for DB choices.
        :param rnd:  Random event generator code to use.
        """
        self.label = label
        self.code = code
        self.rnd = rnd