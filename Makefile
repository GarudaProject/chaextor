.PHONY: uic

uic:
	pyuic6 -x designer/*mainwindow.ui -o package/ui/ui_mainwindow.py