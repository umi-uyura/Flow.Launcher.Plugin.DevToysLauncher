@echo off
setlocal enabledelayedexpansion
chcp 65001

set DEVTOYS_SRC=DevToys

where rg >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo rg ^(ripgrep^) command not found.
    exit /b
)

where csvtk >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo csvtk command not found.
    exit /b
)

cd "%~dp0"

if not exist "%DEVTOYS_SRC%" (
    git clone git@github.com:veler/DevToys.git
)

pushd %DEVTOYS_SRC%
git pull
popd

rem ECHO Extract protocol name
rg "ProtocolName" --glob "*.cs" --no-heading --trim -N %DEVTOYS_SRC%\src\dev\impl\DevToys\ViewModels\Tools > protocols.txt

echo toolname,protocol > tool-protocols.csv
for /f %%a in (protocols.txt) do (
    set inputPath=%%a

    for %%b in ("!inputPath!\..") do (
        set "toolName=%%~nb"
    )

    for /f "tokens=2 delims=()" %%c in ("!inputPath!") do (
        set "protocol=%%~c"
    )

    if "!toolName!"=="CronParser" (
        set "toolName=CRONParser"
    )
    if "!toolName!"=="Base64TextEncoderDecoder" (
        set "toolName=Base64EncoderDecoder"
    )

    echo !toolName!,!protocol! >> tool-protocols.csv
)

del protocols.txt

rem ECHO Extract Accessible Name (en-US)
rg "data name=\"SearchDisplayName\"" --glob "*.resw" --no-heading --trim -N -A 1 ^
   %DEVTOYS_SRC%\src\dev\impl\DevToys\Strings\en-US ^
   | rg value | rg "\-<value>" -r "" | rg "</value>" -r "" | rg ".resw" -r "," ^
   | rg "&lt;&gt;" -r "ltgt" --passthru | rg "&amp;" -r "aammpp" --passthru | rg " " -r "#" --passthru | rg "#/#" -r "#_#" --passthru > strings.txt

echo toolname,displayname(en-us) > tool-displayname-en_us.csv
for /f %%a in (strings.txt) do (
    set inputPath=%%a

    for /f "tokens=1 delims=," %%b in ("!inputPath!") do (
        set "toolName=%%~nb"
    )

    for /f "tokens=2 delims=," %%c in ("echo !inputPath!") do (
        set "displayName=%%~nc"

        for /f "usebackq delims=" %%d in (`echo !displayName! ^| rg "#_#" -r " / " --passthru ^| rg "#" -r " " --passthru ^| rg "ltgt" -r "<>" --passthru ^| rg "aammpp" -r "&" --passthru`) do (
            set "displayName=%%d"
        )
    )

    echo !toolName!,!displayName! >> tool-displayname-en_us.csv
)

del strings.txt

rem ECHO Extract Accessible Name (ja-JP)
rg "data name=\"SearchDisplayName\"" --glob "*.resw" --no-heading --trim -N -A 1 ^
   %DEVTOYS_SRC%\src\dev\impl\DevToys\Strings\ja-JP ^
   | rg value | rg "\-<value>" -r "" | rg "</value>" -r "" | rg ".resw" -r "," ^
   | rg "&lt;&gt;" -r "ltgt" --passthru | rg "&amp;" -r "aammpp" --passthru | rg " " -r "#" --passthru | rg "#/#" -r "#_#" --passthru > strings.txt

echo toolname,displayname(ja_jp) > tool-displayname-ja_jp.csv
for /f %%a in (strings.txt) do (
    set inputPath=%%a

    for /f "tokens=1 delims=," %%b in ("!inputPath!") do (
        set "toolName=%%~nb"
    )

    for /f "tokens=2 delims=," %%c in ("echo !inputPath!") do (
        set "displayName=%%~nc"

        for /f "usebackq delims=" %%d in (`echo !displayName! ^| rg "#_#" -r " / " --passthru ^| rg "#" -r " " --passthru ^| rg "ltgt" -r "<>" --passthru ^| rg "aammpp" -r "&" --passthru`) do (
            set "displayName=%%d"
        )
    )

    echo !toolName!,!displayName! >> tool-displayname-ja_jp.csv
)

del strings.txt

csvtk join --outer-join tool-protocols.csv tool-displayname-ja_jp.csv tool-displayname-en_us.csv | csvtk sort -k 1 > tool-strings.csv

endlocal
