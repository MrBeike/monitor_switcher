from monitorcontrol import get_monitors, InputSource
import keyboard
from pystray import Icon, Menu, MenuItem
from PIL import Image
import os

# 分配显示器名称
for monitor in get_monitors():
    with monitor:
        a = monitor.get_vcp_capabilities()
        # 自用机型
        if a["model"] == "272S1AE":
            left = monitor
        else:
            right = monitor


def switch_inner():
    with left:
        left.set_input_source(InputSource.ANALOG1)
    with right:
        right.set_input_source(InputSource.HDMI1)


def switch_outer():
    with left:
        left.set_input_source(InputSource.HDMI1)
    with right:
        right.set_input_source(InputSource.ANALOG1)

def restore():
    with left:
        left.set_input_source(InputSource.ANALOG1)
    with right:
        right.set_input_source(InputSource.ANALOG1)

def quit():
    icon.stop()
    os._exit(1)

# 创建托盘图标
icon = Icon(
    "Monitor Switcher",
    title="Monitor Switcher",
    icon=Image.open("monitor.ico"),
    menu=Menu(
        MenuItem("切换到内网(crtl+f11)", switch_inner),
        MenuItem("切换到外网(crtl+f12)", switch_outer),
        MenuItem("恢复原状(crtl+insert)", restore),
        MenuItem("退出", quit),
    ),
)
# 绑定快捷键
keyboard.add_hotkey("ctrl+f11", switch_inner)
keyboard.add_hotkey("ctrl+f12", switch_outer)
keyboard.add_hotkey("ctrl+insert", restore)

# 运行托盘图标及监听快捷键
icon.run()
keyboard.wait("ctrl+shift+alt+1")