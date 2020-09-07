#!/usr/bin/env python3
import shutil as sh
import psutil as ps
from pyfiglet import Figlet as fig

ft = fig(font='slant')
print(ft.renderText("Health Checkup"))

def disk_use(d):
	du = sh.disk_usage(d)
	f = du.free/du.total * 100
	print(f,"% free space")
	return f > 25

def cpu_use():
	u = ps.cpu_percent(1)
	print(u,"% CPU usage")
	return u < 70

def ram_use():
	ru = ps.virtual_memory()
	print(ru.percent,"% RAM usage")
	return ru.percent < 70

def battery():
	bu = ps.sensors_battery()
	p = bu.percent
	e = bu.power_plugged
	e = "Plugged In" if e else "Not Plugged In"
	print(p,"% battery left")
	print(e)
	return p > 30

if not disk_use("/") or not cpu_use() or not ram_use() or not battery():
	print("Unhealthy!")
else:
	print("Healthy!")
