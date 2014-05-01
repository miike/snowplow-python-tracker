"""
    test_tracker.py

    Copyright (c) 2013-2014 Snowplow Analytics Ltd. All rights reserved.

    This program is licensed to you under the Apache License Version 2.0,
    and you may not use this file except in compliance with the Apache License
    Version 2.0. You may obtain a copy of the Apache License Version 2.0 at
    http://www.apache.org/licenses/LICENSE-2.0.

    Unless required by applicable law or agreed to in writing,
    software distributed under the Apache License Version 2.0 is distributed on
    an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
    express or implied. See the Apache License Version 2.0 for the specific
    language governing permissions and limitations there under.

    Authors: Anuj More, Alex Dean, Fred Blundun
    Copyright: Copyright (c) 2013-2014 Snowplow Analytics Ltd
    License: Apache License Version 2.0
"""


import unittest
from snowplow_tracker.tracker import Tracker


class TestTracker(unittest.TestCase):

    def setUp(self):
        pass

    def test_initialisation(self):
        t = Tracker("d3rkrsqld9gmqf.cloudfront.net", "cloudfront", encode_base64= False, app_id="AF003", context_vendor="com.example")
        self.assertEquals(t.standard_nv_pairs["tna"], "cloudfront")
        self.assertEquals(t.standard_nv_pairs["aid"], "AF003")
        self.assertEquals(t.encode_base64, False)
        self.assertEquals(t.context_vendor, "com.example")
