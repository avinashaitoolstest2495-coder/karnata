Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "python """ & CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName) & "\silent_runner.py""", 0, False
