#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id: test_md5sums.py 12717 2010-12-31 21:15:44Z kwc $

import roslib; roslib.load_manifest('test_roslib_comm')

import unittest
import rosunit
from test_roslib_comm.msg import *


class TestMd5sums(unittest.TestCase):
    
    def test_field_name_change(self):
        self.assertNotEquals(FieldNameChange1._md5sum, FieldNameChange2._md5sum)

    def test_type_name_change(self):
        self.assertEquals(TypeNameChange1._md5sum, TypeNameChange2._md5sum)

    def test_type_name_change_array(self):
        self.assertEquals(TypeNameChangeArray1._md5sum, TypeNameChangeArray2._md5sum)

    def test_type_name_change_complex(self):
        self.assertEquals(TypeNameChangeComplex1._md5sum, TypeNameChangeComplex2._md5sum)

if __name__ == '__main__':
    rosunit.unitrun('test_roslib_comm', 'test_md5sums', TestMd5sums, coverage_packages=[])
