

### Installation:

```
pip install -r requirements.txt
```


Open vs_buildtools.exe and install "Visual C++ build tools" and uninstall any versions of Visual Studio or Build Tools except for Build Tools 2017


then run ```python3 helper.py help```. You should see something like:


```vcvarsall.bat x64 && cd "C:\Users\Garrett McParrot\Desktop\fuzzers\hg-winafl\winafl\bin64" && cmake -G"Visual Studio 15 2017 Win64" .. -DDynamoRIO_DIR="C:\Users\Garrett McParrot\Desktop\fuzzers\hg-winafl\winafl\dynamrio\cmake" && cmake --build "C:\Users\Garrett McParrot\Desktop\fuzzers\hg-winafl\winafl\bin64" --config Release
**********************************************************************
** Visual Studio 2017 Developer Command Prompt v15.0
** Copyright (c) 2017 Microsoft Corporation
**********************************************************************
[vcvarsall.bat] Environment initialized for: 'x64'
-- Selecting Windows SDK version 10.0.17763.0 to target Windows 10.0.18363.
-- The C compiler identification is MSVC 19.16.27043.0
-- The CXX compiler identification is MSVC 19.16.27043.0
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/BuildTools/VC/Tools/MSVC/14.16.27023/bin/Hostx86/x64/cl.exe
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/BuildTools/VC/Tools/MSVC/14.16.27023/bin/Hostx86/x64/cl.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/BuildTools/VC/Tools/MSVC/14.16.27023/bin/Hostx86/x64/cl.exe
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/BuildTools/VC/Tools/MSVC/14.16.27023/bin/Hostx86/x64/cl.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: C:/Users/Garrett McParrot/Desktop/fuzzers/hg-winafl/winafl/bin64
Microsoft (R) Build Engine version 15.9.21+g9802d43bc3 for .NET Framework
Copyright (C) Microsoft Corporation. All rights reserved.
```
If you get an error saying no C compiler found you likely have several version of Visual Studio/Build Tools installed. We don't know why this is happening yet, but the easiest solution is just uninstall everything except for 2017 (feel free to reinstall after).

### Usage:

##### Build winafl:

```
python3 helper.py build
```
##### Generate corpus:
```
python3 helper.py generate
```
*Note* https://en.wikipedia.org/wiki/List_of_file_signatures can be used to find the right file signatures to search for

##### Run winafl:
```
python3 helper.py run
```

##### Get usage information:
```
python3 helper.py help
```

##### Check out the winafl/ directory for more details on winafl itself


### Special thanks:

* Nightmare Fuzzing Project samples finder(https://github.com/joxeankoret/nightmare/blob/master/runtime/find_samples.py)
    * @author: Joxean Koret, @joxeankoret
    * @author: Hardik Shah, @hardik05
* winafl with mopt mutators and afl fast power schedulers(https://github.com/hardik05/winafl-powermopt)
    * @author: Hardik Shah, @hardik05
    * Michal Zalewski <lcamtuf@google.com>
    * Ivan Fratric <ifratric@google.com>
* https://symeonp.github.io/2017/09/17/fuzzing-winafl.html
    * @author: simospar@gmail.com
