# AutoItLibrary
This repository is based on the latest AutoItLibrary-1.1 version, which currently is still available on "Google Code" archive:

https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/robotframework-autoitlibrary/AutoItLibrary-1.1.zip


Introduction
------------
AutoItLibrary is a Python keyword library that extends the Robot Framework (http://code.google.com/p/robotframework/) by providing keywords based on the AutoItX COM object. The AutoItX COM object itself belongs to AutoIt (http://www.autoitscript.com/autoit3/index.shtml), which is a set of freeware tools providing for example a scripting language for automating the Windows GUI.

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
For both AutoItLibrary and AutoItX the documentation is installed by the installation process into

    C:\RobotFramework\Extensions\AutoItLibrary\

- the documentation for the Robot library "AutoItLibrary" is provided as HTML file: AutoItLibrary.html
- the documentation for the COM control "AutoItX" is provided as compiled HTML file: AutoItX.chm


Tests
-----
The AutoItLibrary installer puts a suite of self-tests here:

    C:\RobotFramework\Extensions\AutoItLibrary\tests

To run these tests, which exercise the Windows Calculator GUI, run the RunTests.bat file in the above folder.
