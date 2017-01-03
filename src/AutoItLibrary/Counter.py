"""
Package: AutoItLibrary
Module:  Counter
Purpose: Defines a Counter class from which other classes can inherit the ability to initialize a
         counter at class instantiation and get the next number in the sequence with a _next method.

         Based on AutoItLibrary 1.1 by Texas Instruments, Inc. / Martin Taylor hosted on Google Code.

         Licensed under the Apache License, Version 2.0 (the "License");
         you may not use this file except in compliance with the License.
         You may obtain a copy of the License at

             http://www.apache.org/licenses/LICENSE-2.0

         Unless required by applicable law or agreed to in writing, software
         distributed under the License is distributed on an "AS IS" BASIS,
         WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         See the License for the specific language governing permissions and
         limitations under the License.
"""
__author__ = "Erik Fornoff <erik.fornoff@gmail.com>"
__version__ = "2.0.0"

class Counter:
    def __init__(self):
        self._counter = 0

    def _next(self):
        self._counter += 1
        return self._counter
#
# -------------------------------- End of file --------------------------------
