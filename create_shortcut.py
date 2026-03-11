import os
import subprocess

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
shortcut_path = os.path.join(desktop, "labelme-train.lnk")

target      = r"C:\Windows\System32\cmd.exe"
arguments   = (
    r'/c "cd /d C:\Users\29115\yolov8\labelme && '
    r'uv run labelme C:\Users\29115\yolov8\yolov11-seg\datasets17k_labelme\train"'
)
working_dir = r"C:\Users\29115\yolov8\labelme"
description = "labelme train dataset"
window_style = 7  # minimized

ps_script = f"""
$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut('{shortcut_path}')
$shortcut.TargetPath = '{target}'
$shortcut.Arguments = '{arguments}'
$shortcut.WorkingDirectory = '{working_dir}'
$shortcut.WindowStyle = {window_style}
$shortcut.Description = '{description}'
$shortcut.Save()
"""

subprocess.run(
    ["powershell", "-NoProfile", "-Command", ps_script],
    check=True,
)

print(f"快捷方式已创建: {shortcut_path}")
