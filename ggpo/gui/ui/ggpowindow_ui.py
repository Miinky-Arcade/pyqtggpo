# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ggpo/gui/ui/ggpowindow.ui'
#
# Created: Sat Mar 22 12:07:05 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(810, 708)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("assets/icon-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.uiSplitter = QtGui.QSplitter(self.centralwidget)
        self.uiSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.uiSplitter.setObjectName(_fromUtf8("uiSplitter"))
        self.uiChannelsList = QtGui.QListWidget(self.uiSplitter)
        self.uiChannelsList.setObjectName(_fromUtf8("uiChannelsList"))
        self.layoutWidget = QtGui.QWidget(self.uiSplitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.uiChatHistoryTxtB = QtGui.QTextBrowser(self.layoutWidget)
        self.uiChatHistoryTxtB.setAcceptDrops(False)
        self.uiChatHistoryTxtB.setReadOnly(True)
        self.uiChatHistoryTxtB.setOpenExternalLinks(False)
        self.uiChatHistoryTxtB.setOpenLinks(False)
        self.uiChatHistoryTxtB.setObjectName(_fromUtf8("uiChatHistoryTxtB"))
        self.verticalLayout.addWidget(self.uiChatHistoryTxtB)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.uiChatInputEdit = CompletionLineEdit(self.layoutWidget)
        self.uiChatInputEdit.setObjectName(_fromUtf8("uiChatInputEdit"))
        self.horizontalLayout.addWidget(self.uiChatInputEdit)
        self.uiEmoticonTbtn = QtGui.QToolButton(self.layoutWidget)
        self.uiEmoticonTbtn.setObjectName(_fromUtf8("uiEmoticonTbtn"))
        self.horizontalLayout.addWidget(self.uiEmoticonTbtn)
        self.uiAfkChk = QtGui.QCheckBox(self.layoutWidget)
        self.uiAfkChk.setObjectName(_fromUtf8("uiAfkChk"))
        self.horizontalLayout.addWidget(self.uiAfkChk)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.uiPlayersTableV = QtGui.QTableView(self.uiSplitter)
        self.uiPlayersTableV.setObjectName(_fromUtf8("uiPlayersTableV"))
        self.horizontalLayout_2.addWidget(self.uiSplitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAction = QtGui.QMenu(self.menubar)
        self.menuAction.setObjectName(_fromUtf8("menuAction"))
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        self.uiMenuTheme = QtGui.QMenu(self.menuSetting)
        self.uiMenuTheme.setObjectName(_fromUtf8("uiMenuTheme"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.uiStatusbar = QtGui.QStatusBar(MainWindow)
        self.uiStatusbar.setObjectName(_fromUtf8("uiStatusbar"))
        MainWindow.setStatusBar(self.uiStatusbar)
        self.uiClearChatHistoryAct = QtGui.QAction(MainWindow)
        self.uiClearChatHistoryAct.setObjectName(_fromUtf8("uiClearChatHistoryAct"))
        self.uiAwayAct = QtGui.QAction(MainWindow)
        self.uiAwayAct.setCheckable(True)
        self.uiAwayAct.setObjectName(_fromUtf8("uiAwayAct"))
        self.uiQuitAct = QtGui.QAction(MainWindow)
        self.uiQuitAct.setObjectName(_fromUtf8("uiQuitAct"))
        self.uiMuteChallengeSoundAct = QtGui.QAction(MainWindow)
        self.uiMuteChallengeSoundAct.setCheckable(True)
        self.uiMuteChallengeSoundAct.setObjectName(_fromUtf8("uiMuteChallengeSoundAct"))
        self.uiFontAct = QtGui.QAction(MainWindow)
        self.uiFontAct.setObjectName(_fromUtf8("uiFontAct"))
        self.uiAboutAct = QtGui.QAction(MainWindow)
        self.uiAboutAct.setObjectName(_fromUtf8("uiAboutAct"))
        self.uiStrevivalAct = QtGui.QAction(MainWindow)
        self.uiStrevivalAct.setObjectName(_fromUtf8("uiStrevivalAct"))
        self.uiHitboxViewerAct = QtGui.QAction(MainWindow)
        self.uiHitboxViewerAct.setObjectName(_fromUtf8("uiHitboxViewerAct"))
        self.uiSafejumpGuideAct = QtGui.QAction(MainWindow)
        self.uiSafejumpGuideAct.setObjectName(_fromUtf8("uiSafejumpGuideAct"))
        self.uiMatchVideosAct = QtGui.QAction(MainWindow)
        self.uiMatchVideosAct.setObjectName(_fromUtf8("uiMatchVideosAct"))
        self.uiSRKForumAct = QtGui.QAction(MainWindow)
        self.uiSRKForumAct.setObjectName(_fromUtf8("uiSRKForumAct"))
        self.uiSRKWikiAct = QtGui.QAction(MainWindow)
        self.uiSRKWikiAct.setObjectName(_fromUtf8("uiSRKWikiAct"))
        self.uiJPWikiAct = QtGui.QAction(MainWindow)
        self.uiJPWikiAct.setObjectName(_fromUtf8("uiJPWikiAct"))
        self.uiDarkThemeAct = QtGui.QAction(MainWindow)
        self.uiDarkThemeAct.setCheckable(True)
        self.uiDarkThemeAct.setObjectName(_fromUtf8("uiDarkThemeAct"))
        self.uiDebugLogAct = QtGui.QAction(MainWindow)
        self.uiDebugLogAct.setCheckable(True)
        self.uiDebugLogAct.setObjectName(_fromUtf8("uiDebugLogAct"))
        self.uiEmoticonAct = QtGui.QAction(MainWindow)
        self.uiEmoticonAct.setObjectName(_fromUtf8("uiEmoticonAct"))
        self.uiLocateGgpofbaAct = QtGui.QAction(MainWindow)
        self.uiLocateGgpofbaAct.setObjectName(_fromUtf8("uiLocateGgpofbaAct"))
        self.uiLocateWineAct = QtGui.QAction(MainWindow)
        self.uiLocateWineAct.setObjectName(_fromUtf8("uiLocateWineAct"))
        self.uiLocateGeommdbAct = QtGui.QAction(MainWindow)
        self.uiLocateGeommdbAct.setObjectName(_fromUtf8("uiLocateGeommdbAct"))
        self.uiNotifyPlayerStateChangeAct = QtGui.QAction(MainWindow)
        self.uiNotifyPlayerStateChangeAct.setCheckable(True)
        self.uiNotifyPlayerStateChangeAct.setObjectName(_fromUtf8("uiNotifyPlayerStateChangeAct"))
        self.uiFocusOnChatAct = QtGui.QAction(MainWindow)
        self.uiFocusOnChatAct.setObjectName(_fromUtf8("uiFocusOnChatAct"))
        self.uiToggleSidebarAction = QtGui.QAction(MainWindow)
        self.uiToggleSidebarAction.setObjectName(_fromUtf8("uiToggleSidebarAction"))
        self.uiExpandChannelSidebarAct = QtGui.QAction(MainWindow)
        self.uiExpandChannelSidebarAct.setObjectName(_fromUtf8("uiExpandChannelSidebarAct"))
        self.uiContractChannelSidebarAct = QtGui.QAction(MainWindow)
        self.uiContractChannelSidebarAct.setObjectName(_fromUtf8("uiContractChannelSidebarAct"))
        self.uiContractPlayerListAct = QtGui.QAction(MainWindow)
        self.uiContractPlayerListAct.setObjectName(_fromUtf8("uiContractPlayerListAct"))
        self.uiExpandPlayerListAct = QtGui.QAction(MainWindow)
        self.uiExpandPlayerListAct.setObjectName(_fromUtf8("uiExpandPlayerListAct"))
        self.uiLocateUnsupportedSavestatesDirAct = QtGui.QAction(MainWindow)
        self.uiLocateUnsupportedSavestatesDirAct.setObjectName(_fromUtf8("uiLocateUnsupportedSavestatesDirAct"))
        self.uiSyncUnsupportedSavestatesAct = QtGui.QAction(MainWindow)
        self.uiSyncUnsupportedSavestatesAct.setObjectName(_fromUtf8("uiSyncUnsupportedSavestatesAct"))
        self.uiSelectUnsupportedSavestateAct = QtGui.QAction(MainWindow)
        self.uiSelectUnsupportedSavestateAct.setObjectName(_fromUtf8("uiSelectUnsupportedSavestateAct"))
        self.uiFireThemeAct = QtGui.QAction(MainWindow)
        self.uiFireThemeAct.setCheckable(True)
        self.uiFireThemeAct.setObjectName(_fromUtf8("uiFireThemeAct"))
        self.uiCustomQssFileAct = QtGui.QAction(MainWindow)
        self.uiCustomQssFileAct.setCheckable(True)
        self.uiCustomQssFileAct.setObjectName(_fromUtf8("uiCustomQssFileAct"))
        self.uiNormalThemeAct = QtGui.QAction(MainWindow)
        self.uiNormalThemeAct.setCheckable(True)
        self.uiNormalThemeAct.setObjectName(_fromUtf8("uiNormalThemeAct"))
        self.menuAction.addAction(self.uiAwayAct)
        self.menuAction.addAction(self.uiFocusOnChatAct)
        self.menuAction.addAction(self.uiEmoticonAct)
        self.menuAction.addAction(self.uiClearChatHistoryAct)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.uiToggleSidebarAction)
        self.menuAction.addAction(self.uiContractChannelSidebarAct)
        self.menuAction.addAction(self.uiExpandChannelSidebarAct)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.uiContractPlayerListAct)
        self.menuAction.addAction(self.uiExpandPlayerListAct)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.uiSelectUnsupportedSavestateAct)
        self.menuAction.addAction(self.uiSyncUnsupportedSavestatesAct)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.uiQuitAct)
        self.menuSetting.addAction(self.uiMuteChallengeSoundAct)
        self.menuSetting.addAction(self.uiFontAct)
        self.menuSetting.addAction(self.uiMenuTheme.menuAction())
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.uiLocateGgpofbaAct)
        self.menuSetting.addAction(self.uiLocateWineAct)
        self.menuSetting.addAction(self.uiLocateUnsupportedSavestatesDirAct)
        self.menuSetting.addAction(self.uiLocateGeommdbAct)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.uiNotifyPlayerStateChangeAct)
        self.menuSetting.addAction(self.uiDebugLogAct)
        self.menuAbout.addAction(self.uiSRKForumAct)
        self.menuAbout.addAction(self.uiSRKWikiAct)
        self.menuAbout.addAction(self.uiJPWikiAct)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.uiStrevivalAct)
        self.menuAbout.addAction(self.uiHitboxViewerAct)
        self.menuAbout.addAction(self.uiSafejumpGuideAct)
        self.menuAbout.addAction(self.uiMatchVideosAct)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.uiAboutAct)
        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.uiQuitAct, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.uiClearChatHistoryAct, QtCore.SIGNAL(_fromUtf8("triggered()")), self.uiChatHistoryTxtB.clear)
        QtCore.QObject.connect(self.uiAwayAct, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.uiAfkChk.setChecked)
        QtCore.QObject.connect(self.uiAfkChk, QtCore.SIGNAL(_fromUtf8("clicked()")), self.uiAwayAct.trigger)
        QtCore.QObject.connect(self.uiFocusOnChatAct, QtCore.SIGNAL(_fromUtf8("triggered()")), self.uiChatInputEdit.setFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GGPO", None, QtGui.QApplication.UnicodeUTF8))
        self.uiEmoticonTbtn.setText(QtGui.QApplication.translate("MainWindow", ":)", None, QtGui.QApplication.UnicodeUTF8))
        self.uiAfkChk.setText(QtGui.QApplication.translate("MainWindow", "away", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAction.setTitle(QtGui.QApplication.translate("MainWindow", "&Action", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSetting.setTitle(QtGui.QApplication.translate("MainWindow", "S&ettings", None, QtGui.QApplication.UnicodeUTF8))
        self.uiMenuTheme.setTitle(QtGui.QApplication.translate("MainWindow", "&Theme", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.uiClearChatHistoryAct.setText(QtGui.QApplication.translate("MainWindow", "Clear chat his&tory", None, QtGui.QApplication.UnicodeUTF8))
        self.uiClearChatHistoryAct.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        self.uiAwayAct.setText(QtGui.QApplication.translate("MainWindow", "Away from k&eyboard", None, QtGui.QApplication.UnicodeUTF8))
        self.uiAwayAct.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.uiQuitAct.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.uiQuitAct.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.uiMuteChallengeSoundAct.setText(QtGui.QApplication.translate("MainWindow", "&Mute Challenge Sound", None, QtGui.QApplication.UnicodeUTF8))
        self.uiMuteChallengeSoundAct.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+M", None, QtGui.QApplication.UnicodeUTF8))
        self.uiFontAct.setText(QtGui.QApplication.translate("MainWindow", "&Font", None, QtGui.QApplication.UnicodeUTF8))
        self.uiAboutAct.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.uiStrevivalAct.setText(QtGui.QApplication.translate("MainWindow", "Strategy && &News", None, QtGui.QApplication.UnicodeUTF8))
        self.uiHitboxViewerAct.setText(QtGui.QApplication.translate("MainWindow", "Hitbox &Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.uiSafejumpGuideAct.setText(QtGui.QApplication.translate("MainWindow", "&Safejump Guide", None, QtGui.QApplication.UnicodeUTF8))
        self.uiMatchVideosAct.setText(QtGui.QApplication.translate("MainWindow", "&Match Videos", None, QtGui.QApplication.UnicodeUTF8))
        self.uiSRKForumAct.setText(QtGui.QApplication.translate("MainWindow", "Shoryuken &Forum", None, QtGui.QApplication.UnicodeUTF8))
        self.uiSRKWikiAct.setText(QtGui.QApplication.translate("MainWindow", "Wiki (English)", None, QtGui.QApplication.UnicodeUTF8))
        self.uiJPWikiAct.setText(QtGui.QApplication.translate("MainWindow", "Wiki (Japanese)", None, QtGui.QApplication.UnicodeUTF8))
        self.uiDarkThemeAct.setText(QtGui.QApplication.translate("MainWindow", "&Dark Orange", None, QtGui.QApplication.UnicodeUTF8))
        self.uiDebugLogAct.setText(QtGui.QApplication.translate("MainWindow", "Debug &Log", None, QtGui.QApplication.UnicodeUTF8))
        self.uiEmoticonAct.setText(QtGui.QApplication.translate("MainWindow", "&Insert Emoticon", None, QtGui.QApplication.UnicodeUTF8))
        self.uiEmoticonAct.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.uiLocateGgpofbaAct.setText(QtGui.QApplication.translate("MainWindow", "&Locate ggpofba.exe", None, QtGui.QApplication.UnicodeUTF8))
        self.uiLocateWineAct.setText(QtGui.QApplication.translate("MainWindow", "Locate &Wine", None, QtGui.QApplication.UnicodeUTF8))
        self.uiLocateGeommdbAct.setText(QtGui.QApplication.translate("MainWindow", "Locate &GeoIP mmdb", None, QtGui.QApplication.UnicodeUTF8))
        self.uiNotifyPlayerStateChangeAct.setText(QtGui.QApplication.translate("MainWindow", "&Notify Player State Change", None, QtGui.QApplication.UnicodeUTF8))
        self.uiFocusOnChatAct.setText(QtGui.QApplication.translate("MainWindow", "Foc&us on chat", None, QtGui.QApplication.UnicodeUTF8))
        self.uiFocusOnChatAct.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+U", None, QtGui.QApplication.UnicodeUTF8))
        self.uiToggleSidebarAction.setText(QtGui.QApplication.translate("MainWindow", "To&ggle Channel Sidebar", None, QtGui.QApplication.UnicodeUTF8))
        self.uiToggleSidebarAction.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+G", None, QtGui.QApplication.UnicodeUTF8))
        self.uiExpandChannelSidebarAct.setText(QtGui.QApplication.translate("MainWindow", "&+ Expand Channel Sidebar", None, QtGui.QApplication.UnicodeUTF8))
        self.uiExpandChannelSidebarAct.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.uiContractChannelSidebarAct.setText(QtGui.QApplication.translate("MainWindow", "&- Contract Channel Sidebar", None, QtGui.QApplication.UnicodeUTF8))
        self.uiContractChannelSidebarAct.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.uiContractPlayerListAct.setText(QtGui.QApplication.translate("MainWindow", "&> Contract Player List", None, QtGui.QApplication.UnicodeUTF8))
        self.uiContractPlayerListAct.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+.", None, QtGui.QApplication.UnicodeUTF8))
        self.uiExpandPlayerListAct.setText(QtGui.QApplication.translate("MainWindow", "&< Expand Player List", None, QtGui.QApplication.UnicodeUTF8))
        self.uiExpandPlayerListAct.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+,", None, QtGui.QApplication.UnicodeUTF8))
        self.uiLocateUnsupportedSavestatesDirAct.setText(QtGui.QApplication.translate("MainWindow", "Locate &Unsupported Savestates Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.uiSyncUnsupportedSavestatesAct.setText(QtGui.QApplication.translate("MainWindow", "S&ync Unsupported Savestates", None, QtGui.QApplication.UnicodeUTF8))
        self.uiSelectUnsupportedSavestateAct.setText(QtGui.QApplication.translate("MainWindow", "&Select Unsupported Savestate", None, QtGui.QApplication.UnicodeUTF8))
        self.uiSelectUnsupportedSavestateAct.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.uiFireThemeAct.setText(QtGui.QApplication.translate("MainWindow", "&Fire", None, QtGui.QApplication.UnicodeUTF8))
        self.uiCustomQssFileAct.setText(QtGui.QApplication.translate("MainWindow", "Custom Qss File", None, QtGui.QApplication.UnicodeUTF8))
        self.uiNormalThemeAct.setText(QtGui.QApplication.translate("MainWindow", "&Normal", None, QtGui.QApplication.UnicodeUTF8))

from ggpo.gui.completionlineedit import CompletionLineEdit
