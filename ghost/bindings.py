# -*- coding: utf-8 -*-
import sys

PY3 = sys.version > '3'

if PY3:
    unicode = str
    long = int


bindings = ["PySide", "PySide2", "PyQt4"]
binding = None


for name in bindings:
    try:
        binding = __import__(name)
        if name == 'PyQt4':
            import sip
            sip.setapi('QVariant', 2)

    except ImportError:
        continue
    break


class LazyBinding(object):
    class __metaclass__(type):
        def __getattr__(self, name):
            return self.__class__

    def __getattr__(self, name):
        return self.__class__


def _import(name):
    if binding is None:
        return LazyBinding()

    name = "%s.%s" % (binding.__name__, name)
    module = __import__(name)
    for n in name.split(".")[1:]:
        module = getattr(module, n)
    return module


QtCore = _import("QtCore")
QSize = QtCore.QSize
QByteArray = QtCore.QByteArray
QUrl = QtCore.QUrl
QDateTime = QtCore.QDateTime
QtCriticalMsg = QtCore.QtCriticalMsg
QtDebugMsg = QtCore.QtDebugMsg
QtFatalMsg = QtCore.QtFatalMsg
QtWarningMsg = QtCore.QtWarningMsg
if name == "PySide2":
    qInstallMsgHandler = QtCore.qInstallMessageHandler
else:
    qInstallMsgHandler = QtCore.qInstallMsgHandler

QtGui = _import("QtGui")
if name == "PySide2":

    QtWidgets = _import("QtWidgets")
    QtPrintSupport = _import("QtPrintSupport")

    QApplication = QtWidgets.QApplication
    QImage = QtGui.QImage
    QPainter = QtGui.QPainter
    QPrinter = QtPrintSupport.QPrinter
    QRegion = QtGui.QRegion

else:

    QApplication = QtGui.QApplication
    QImage = QtGui.QImage
    QPainter = QtGui.QPainter
    QPrinter = QtGui.QPrinter
    QRegion = QtGui.QRegion

QtNetwork = _import("QtNetwork")
QNetworkRequest = QtNetwork.QNetworkRequest
QNetworkAccessManager = QtNetwork.QNetworkAccessManager
QNetworkCookieJar = QtNetwork.QNetworkCookieJar
QNetworkProxy = QtNetwork.QNetworkProxy
QNetworkCookie = QtNetwork.QNetworkCookie
QSsl = QtNetwork.QSsl

QtWebKit = _import('QtWebKit')
if name == "PySide2":
    QtWebKitWidgets = _import("QtWebKitWidgets")
    QWebPage = QtWebKitWidgets.QWebPage
    QWebView = QtWebKitWidgets.QWebView

else:
    QWebPage = QtWebKit.QWebPage
    QWebView = QtWebKit.QWebView
