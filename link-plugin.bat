@ECHO OFF
SETLOCAL

SET DIRECTORY_PATH=%~dp0
FOR %%A IN ("%DIRECTORY_PATH:~0,-1%") DO SET PROJECTNAME=%%~nxA

SET DEVLINK=%APPDATA%\FlowLauncher\Plugins\%PROJECTNAME%-dev

IF EXIST %DEVLINK% (
    RMDIR %DEVLINK%
) ELSE (
    MKLINK /D %DEVLINK% %~dp0
)