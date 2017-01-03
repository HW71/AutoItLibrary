@echo off
::
:: CMD file to run the AutoIt tests in this directory
::
:: Based on AutoItLibrary 1.1 by Texas Instruments, Inc. / Martin Taylor hosted on Google Code.
:: Author: Erik Fornoff <efornoff@iname.com>
::
::  Licensed under the Apache License, Version 2.0 (the "License");
::  you may not use this file except in compliance with the License.
::  You may obtain a copy of the License at
::
::      http://www.apache.org/licenses/LICENSE-2.0
::
::  Unless required by applicable law or agreed to in writing, software
::  distributed under the License is distributed on an "AS IS" BASIS,
::  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
::  See the License for the specific language governing permissions and
::  limitations under the License.
::
::-------------------------------------------------------------------------------
::
call pybot --name "AutoItLibrary Windows Calculator" --noncritical ExpectedFAIL --outputdir .\results .
pause
