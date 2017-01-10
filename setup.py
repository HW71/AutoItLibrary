"""
Package: robotframework-AutoItLibrary
Module:  AutoItLibrary Installation Module
Purpose: This is a Python "Distutils" setup program used to build installers for and to install the
         robotframework-AutoItLibrary.

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
__author__  = "Erik Fornoff <efornoff@iname.com>"

from distutils.core      import setup
from distutils.sysconfig import get_python_lib
import sys
import os
import shutil
import subprocess

CLASSIFIERS = """
Development Status :: 5 - Production/Stable
License :: OSI Approved :: Apache Software License
Operating System :: Microsoft :: Windows
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

DESCRIPTION = """
AutoItLibrary is a Robot Framework keyword library wrapper for for the
freeware AutoIt tool (http://www.autoitscript.com/autoit3/index.shtml)
using AutoIt's AutoItX.dll COM object. The AutoItLibrary class
provides a proxy for the AutoIt keywords callable on the AutoIt COM
object and provides additional high-level keywords implemented as
methods in this class.
"""[1:-1]

if __name__ == "__main__":
    #
    # Check for non-Windows platform...
    #
    if os.name != "nt" :
        print "AutoItLibrary cannot be installed on non-Windows platforms. os.name == '{}'.".format(os.name)
        sys.exit(2)             

    #
    # Check for valid number of arguments...
    #
    if ((len(sys.argv) != 2) and (len(sys.argv) != 3)) :
        print "Wrong number of arguments!"
        print "For automatic processor architecture detection (recomended) please use:"
        print "'python setup.py install' (without quotes)"
        print "\nIn order to specify processor architecure on your own please use:"
        print "'python setup.py install x32' (for 32 Bit) or 'python setup.py install x64' (for 64 Bit)"
        sys.exit(2)

    #
    # Check processor architecture of currently used Python interpreter...
    #
    if (sys.maxsize > 2**32) :
        isX64Python = True
        print "\nWe seem to run on a 64 Bit Python interpreter..."
    else :
        isX64Python = False
        print "\nWe seem to run on a 32 Bit Python interpreter..."

    passedArguments = ""
    if (len(sys.argv) == 3) :
        passedArguments = sys.argv[2].lower()

        if (passedArguments != "x32") and (passedArguments != "x64") :
            print "Invalid arguments!"
            print "In order to specify processor architecure on your own please use:"
            print "'python setup.py install x32' (for 32 Bit) or 'python setup.py install x64' (for 64 Bit)"
            sys.exit(2)

        if ((passedArguments == "x32") and isX64Python is True) or ((passedArguments == "x64") and isX64Python is False) :
            print "\nWARNING: Requested processor architecture {} doesn't seem to match current Python interpreter!".format(passedArguments)

        # Ugly hack in order to not interfere with call to Distutils setup()
        if (passedArguments == "x32") :
            sys.argv.remove("x32")
        else :
            sys.argv.remove("x64")

    #
    # Distinguish processor architecture to be used for installation...
    #
    if ((passedArguments == "x32") or ((passedArguments == "") and (isX64Python == False))) :
        print "Installing 32 Bit version of AutoItX3 COM object..."
        dllName = "AutoItX3.dll"
        # Use 32 Bit version of Au3Info tool later on in distribution process
        exeName = "Au3Info.exe"
    elif ((passedArguments == "x64") or ((passedArguments == "") and (isX64Python == True))) :
        print "Installing 64 Bit version of AutoItX3 COM object..."
        dllName = "AutoItX3_x64.dll"
        # Use 64 Bit version of Au3Info tool later on in distribution process
        exeName = "Au3Info_x64.exe"
    else :
        print "Error while detecting processor architecture to be used for installation!"
        sys.exit(2)

    #
    # Copy AutoItX COM object
    #
    if os.path.isfile(os.path.join(get_python_lib(), "AutoItLibrary/lib/"+dllName)) :
        print "AutoItX3 COM Dll already present in PythonLib subdir - for now we don't try to unregister a possibly present COM server..."

    instDir = os.path.normpath(os.path.join(get_python_lib(), "AutoItLibrary/lib"))
    if not os.path.isdir(instDir) :
        os.makedirs(instDir)
    instFile = os.path.normpath(os.path.join(instDir, dllName))
    shutil.copyfile("3rdPartyTools/AutoIt/"+dllName, instFile)

    #
    # Register the AutoItX COM object
    # and make its methods known to Python
    #
    cmd = r"%SYSTEMROOT%\system32\regsvr32.exe /S " + instFile
    print "\nRegistering COM object using command:\n{}".format(cmd)
    
    try:
        subprocess.check_call(cmd, shell=True)
        print "Done!"
    except subprocess.CalledProcessError as e:
        print "\nError while registering COM object (maybe admin rights missing?)..."
        print "regsvr32 exited with returncode {0} and error message: {1}".format(e.returncode, e.output)
        sys.exit(2)

    #
    # Make sure we have win32com installed
    #
    makepy = os.path.normpath(os.path.join(get_python_lib(), "win32com/client/makepy.py"))
    if not os.path.isfile(makepy) :
        print "AutoItLibrary requires win32com. See http://starship.python.net/crew/mhammond/win32/."
        sys.exit(2)

    #
    # Generate Python code out of COM object using makepy...
    #
    cmd = "python %s %s" % (makepy, instFile)
    print "\nGenerate Python code out of COM object using command:\n{}".format(cmd)
    subprocess.check_call(cmd)
    print "Done!\n"

    #
    # Figure out the install path
    #
    destPath = os.path.normpath(os.path.join(os.getenv("HOMEDRIVE"), r"\RobotFramework\Extensions\AutoItLibrary"))
    #
    # Do the distutils installation
    #
    setup(name         = "AutoItLibrary",
          version      = "2.0.1",
          description  = "AutoItLibrary for Robot Framework with 64 Bit support",
          author       = "Erik Fornoff",
          author_email = "efornoff@iname.com",
          url          = "https://github.com/HW71/AutoItLibrary",
          license      = "Apache License 2.0",
          platforms    = "Microsoft Windows",
          classifiers  = CLASSIFIERS.splitlines(),
          long_description = DESCRIPTION,
          package_dir  = {'' : "src"},
          packages     = ["AutoItLibrary"],
          data_files   = [(destPath,
                             ["README.md",
                              "LICENSE",
                              "doc/AutoItLibrary.html",
                              "3rdPartyTools/AutoIt/" + exeName,
                              "3rdPartyTools/AutoIt/AutoItX.chm",
                              "3rdPartyTools/AutoIt/AutoIt_License.html",
                             ]),
                           (os.path.join(destPath, "tests"),
                             ["tests/CalculatorGUIMap.py",
                              "tests/__init__.html",
                              "tests/Calculator_Test_Cases.html",
                              "tests/RobotIDE.bat",
                              "tests/RunTests.bat"
                             ]),
                         ]
         )
#
# -------------------------------- End of file --------------------------------
