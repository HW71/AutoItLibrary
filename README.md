# AutoItLibrary
This repository is based on the latest AutoItLibrary-1.1 version, which currently is still available on "Google Code" archive:

https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/robotframework-autoitlibrary/AutoItLibrary-1.1.zip


Introduction
------------
AutoItLibrary is a Python keyword library that extends the Robot Framework (http://code.google.com/p/robotframework/) by providing keywords based on the COM interface to AutoIt (http://www.autoitscript.com/autoit3/index.shtml). AutoIt is a freeware tool providing a scripting language for automating the Windows GUI.

In order to do screenshots, the AutoItLibrary uses the Open Source Python Image Library tool PIL (http://www.pythonware.com/products/pil/). Unfortunately this library is not maintained anymore and additionally only available for 32 Bit operating systems. Hence automatically taking screenshots in case of a failed AutoItLibrary keyword is currently not possible on 64 Bit OSs. A possible workaround would be to adapt AutoItLibrary in such a way that the PIL fork "pillow" (https://python-pillow.org/) is used.


Installation
------------
AutoItLibrary installs its own file and, if not already present, the 3rd party AutoIt and PIL tools. In order to install:
- simply download this repository as ZIP (green button "Clone or download" => "Download ZIP")
- then unzip into a temporary directory on your PC
- open DOS box / command window with administrative rights in that directory and type

    python setup.py install

This will create the folder

    C:\RobotFramework\Extensions\AutoItLibrary

on your PC and put various files there.


Documentation
-------------
AutoItLibrary documentation is installed by the installation process into

    C:\RobotFramework\Extensions\AutoItLibrary\AutoItLibrary.html

The AutoItX documentation is also installed into this folder as AutoItX.chm.


Tests
-----
The AutoItLibrary installer puts a suite of self-tests here:

    C:\RobotFramework\Extensions\AutoItLibrary\tests

To run these tests, which exercise the Windows Calculator GUI, run the RunTests.bat file in the above folder.
