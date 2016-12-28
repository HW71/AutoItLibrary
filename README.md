# AutoItLibrary
This repository is based on the latest AutoItLibrary-1.1 version, which currently is still available on "Google Code" archive:

https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/robotframework-autoitlibrary/AutoItLibrary-1.1.zip


Introduction
------------
AutoItLibrary is a Python keyword library that extends the [Robot Framework](http://code.google.com/p/robotframework/) by providing keywords based on the AutoItX COM object. The AutoItX COM object itself belongs to [AutoIt](http://www.autoitscript.com/autoit3/index.shtml), which is a set of freeware tools providing for example a scripting language for automating the Windows GUI.

In order to do screenshots, the AutoItLibrary uses the PIL fork ["Pillow"](https://github.com/python-pillow/Pillow), which supports both 32 Bit and 64 Bit Windows versions.

Prerequisites
-------------
- download and install correct version of [Python](https://www.python.org/downloads/) (i.e. 32 Bit or 64 Bit)
- download and install Robot Framework by either using "pip install robotframework" or using [official website](http://robotframework.org/)
- download and install [Python for Windows](https://sourceforge.net/projects/pywin32/files/) extension
- in order to be able to automatically take screenshots in case a AutoItLibrary keyword fails, you need to additionally install the PIL fork "pillow" by using "pip" (see below)


Installation
------------
The installation of AutoItLibrary is done using the setup.py Python script, which itself uses the Python distutils mechanism for the setup. 

As a prerequisite the correct version of Python (i.e. either 32 Bit or 64 Bit) should have already been installed. Afterwards the PIL fork 'pillow' needs to be installed using pip. Hence, open a DOS box / command window and enter 

    pip install pillow

TAfterwards use the following steps to install AutoItLibrary depending on the processor architecture (32 Bit or 64 Bit) of the currently used Python interpreter:
- simply download this GitHub repository as ZIP (green button "Clone or download" => "Download ZIP")
- then unzip into a temporary directory on your PC
- open DOS box / command window with administrative rights in that directory and type

    python setup.py install

This will create the folder

    C:\RobotFramework\Extensions\AutoItLibrary

on your PC and put various files there.

Additionally it is possible to override the automatic detection of the correct processor architecture by passing either "x32" or "x64" as an additional parameter to setup.py:

    python setup.py install x32

This will install the 32 Bit version of AutoItLibrary by registering the 32 Bit AutoItX COM object in the system. Additionally the 32 Bit version of the Au3Info.exe tool will be copied.

In order to "force" installation of the 64 Bit version use:

    python setup.py install x64

In case you pass a processor architecture to be used for installation, and this one doesn't match the one of the current Python interpreter, a warning will be displayed, because it has not been verified if things work as expected in such cases...


Usage
-----
In order to use the AutoItLibrary simply add the Library as "Import" to your Robot test, for example by doing like this:

     *** Settings ***
     Library           AutoItLibrary    OutputDir=${OUTPUTDIR}    CaptureScreenOnError=true

As you can see there are two additional parameters which can be passed to the library:

1. the output directory used to specify the location of screenshots taken in case a keyword fails. If you don't specify this then the screenshots will be located in the directory where the Robot test resides. If you set OutputDir to ${OUTPUTDIR} as shown above then the screenshot files will be located in the same directory where the Robot report / log file will be stored. This is in most cases what you want to do, because otherwise the screenshots will not be shown when you view the Robot reports in your browser.
2. a Boolean flag which enables or disables the automatic capture of screenshots. If not specified it will default to "False".

After importing the Library to your Robot test it should be ready to use. In RIDE the library should be written in black color. If it is shown in red then something went wrong with the import. Sometimes the console gives at least a hint regarding the root cause of the problem.


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
