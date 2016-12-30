# -*- coding: utf-8 -*-
import re
import os
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import jieba
import jieba.analyse
import subprocess

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(620, 606)
		MainWindow.setMinimumSize(QtCore.QSize(620, 606))
		MainWindow.setMaximumSize(QtCore.QSize(620, 606))
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.tabWidget = QtGui.QTabWidget(self.centralwidget)
		self.tabWidget.setGeometry(QtCore.QRect(0, 0, 611, 601))
		self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
		self.tab_jieba = QtGui.QWidget()
		self.tab_jieba.setObjectName(_fromUtf8("tab_jieba"))
		self.verticalLayoutWidget = QtGui.QWidget(self.tab_jieba)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 601, 231))
		self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
		self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.textEdit_input = QtGui.QTextEdit(self.verticalLayoutWidget)
		self.textEdit_input.setObjectName(_fromUtf8("textEdit_input"))
		self.verticalLayout.addWidget(self.textEdit_input)
		self.verticalLayoutWidget_2 = QtGui.QWidget(self.tab_jieba)
		self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 340, 601, 241))
		self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.textEdit_output = QtGui.QTextEdit(self.verticalLayoutWidget_2)
		self.textEdit_output.setObjectName(_fromUtf8("textEdit_output"))
		self.verticalLayout_2.addWidget(self.textEdit_output)
		self.pushButton = QtGui.QPushButton(self.tab_jieba)
		self.pushButton.setGeometry(QtCore.QRect(504, 248, 85, 84))
		self.pushButton.setAutoFillBackground(False)
		self.pushButton.setStyleSheet(_fromUtf8("background-image: url(backgroud.png);"))
		self.pushButton.setText(_fromUtf8(""))
		self.pushButton.setFlat(False)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.groupBox = QtGui.QGroupBox(self.tab_jieba)
		self.groupBox.setGeometry(QtCore.QRect(130, 240, 341, 95))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Agency FB"))
		font.setPointSize(14)
		self.groupBox.setFont(font)
		self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.groupBox.setObjectName(_fromUtf8("groupBox"))
		self.layoutWidget = QtGui.QWidget(self.groupBox)
		self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 321, 51))
		self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.radioButton_default = QtGui.QRadioButton(self.layoutWidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.radioButton_default.setFont(font)
		self.radioButton_default.setChecked(True)
		self.radioButton_default.setObjectName(_fromUtf8("radioButton_default"))
		self.horizontalLayout.addWidget(self.radioButton_default)
		self.radioButton_full = QtGui.QRadioButton(self.layoutWidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.radioButton_full.setFont(font)
		self.radioButton_full.setObjectName(_fromUtf8("radioButton_full"))
		self.horizontalLayout.addWidget(self.radioButton_full)
		self.radioButton_search = QtGui.QRadioButton(self.layoutWidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.radioButton_search.setFont(font)
		self.radioButton_search.setObjectName(_fromUtf8("radioButton_search"))
		self.horizontalLayout.addWidget(self.radioButton_search)
		self.groupBox_2 = QtGui.QGroupBox(self.tab_jieba)
		self.groupBox_2.setGeometry(QtCore.QRect(0, 240, 121, 95))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Agency FB"))
		font.setPointSize(14)
		self.groupBox_2.setFont(font)
		self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
		self.layoutWidget_2 = QtGui.QWidget(self.groupBox_2)
		self.layoutWidget_2.setGeometry(QtCore.QRect(10, 30, 91, 51))
		self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.radioButton_HMM_Y = QtGui.QRadioButton(self.layoutWidget_2)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.radioButton_HMM_Y.setFont(font)
		self.radioButton_HMM_Y.setChecked(True)
		self.radioButton_HMM_Y.setObjectName(_fromUtf8("radioButton_HMM_Y"))
		self.horizontalLayout_2.addWidget(self.radioButton_HMM_Y)
		self.radioButton_HMM_N = QtGui.QRadioButton(self.layoutWidget_2)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.radioButton_HMM_N.setFont(font)
		self.radioButton_HMM_N.setObjectName(_fromUtf8("radioButton_HMM_N"))
		self.horizontalLayout_2.addWidget(self.radioButton_HMM_N)
		self.tabWidget.addTab(self.tab_jieba, _fromUtf8(""))
		self.tab = QtGui.QWidget()
		self.tab.setObjectName(_fromUtf8("tab"))
		self.verticalLayoutWidget_5 = QtGui.QWidget(self.tab)
		self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 342, 601, 241))
		self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
		self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
		self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
		self.textEdit_keywords_output = QtGui.QTextEdit(self.verticalLayoutWidget_5)
		self.textEdit_keywords_output.setObjectName(_fromUtf8("textEdit_keywords_output"))
		self.verticalLayout_5.addWidget(self.textEdit_keywords_output)
		self.groupBox_5 = QtGui.QGroupBox(self.tab)
		self.groupBox_5.setGeometry(QtCore.QRect(36, 240, 121, 95))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Agency FB"))
		font.setPointSize(14)
		self.groupBox_5.setFont(font)
		self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
		self.layoutWidget_7 = QtGui.QWidget(self.groupBox_5)
		self.layoutWidget_7.setGeometry(QtCore.QRect(10, 30, 91, 51))
		self.layoutWidget_7.setObjectName(_fromUtf8("layoutWidget_7"))
		self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget_7)
		self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
		self.topK = QtGui.QSpinBox(self.layoutWidget_7)
		self.topK.setProperty("value", 20)
		self.topK.setObjectName(_fromUtf8("topK"))
		self.horizontalLayout_7.addWidget(self.topK)
		self.groupBox_6 = QtGui.QGroupBox(self.tab)
		self.groupBox_6.setGeometry(QtCore.QRect(186, 240, 201, 95))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Agency FB"))
		font.setPointSize(14)
		self.groupBox_6.setFont(font)
		self.groupBox_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
		self.layoutWidget_8 = QtGui.QWidget(self.groupBox_6)
		self.layoutWidget_8.setGeometry(QtCore.QRect(10, 30, 181, 51))
		self.layoutWidget_8.setObjectName(_fromUtf8("layoutWidget_8"))
		self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutWidget_8)
		self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
		self.radioButton_withWeight_true = QtGui.QRadioButton(self.layoutWidget_8)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.radioButton_withWeight_true.setFont(font)
		self.radioButton_withWeight_true.setChecked(True)
		self.radioButton_withWeight_true.setObjectName(_fromUtf8("radioButton_withWeight_true"))
		self.horizontalLayout_8.addWidget(self.radioButton_withWeight_true)
		self.radioButton_withWeight_false = QtGui.QRadioButton(self.layoutWidget_8)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.radioButton_withWeight_false.setFont(font)
		self.radioButton_withWeight_false.setObjectName(_fromUtf8("radioButton_withWeight_false"))
		self.horizontalLayout_8.addWidget(self.radioButton_withWeight_false)
		self.verticalLayoutWidget_6 = QtGui.QWidget(self.tab)
		self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 2, 601, 231))
		self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
		self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
		self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
		self.textEdit_keywords_input = QtGui.QTextEdit(self.verticalLayoutWidget_6)
		self.textEdit_keywords_input.setObjectName(_fromUtf8("textEdit_keywords_input"))
		self.verticalLayout_6.addWidget(self.textEdit_keywords_input)
		self.pushButton_keywords = QtGui.QPushButton(self.tab)
		self.pushButton_keywords.setGeometry(QtCore.QRect(470, 250, 85, 84))
		self.pushButton_keywords.setAutoFillBackground(False)
		self.pushButton_keywords.setStyleSheet(_fromUtf8("background-image: url(backgroud.png);"))
		self.pushButton_keywords.setText(_fromUtf8(""))
		self.pushButton_keywords.setFlat(False)
		self.pushButton_keywords.setObjectName(_fromUtf8("pushButton_keywords"))
		self.tabWidget.addTab(self.tab, _fromUtf8(""))
		self.tab_endecode = QtGui.QWidget()
		self.tab_endecode.setObjectName(_fromUtf8("tab_endecode"))
		self.textEdit_encode_input = QtGui.QTextEdit(self.tab_endecode)
		self.textEdit_encode_input.setGeometry(QtCore.QRect(0, 0, 601, 231))
		self.textEdit_encode_input.setObjectName(_fromUtf8("textEdit_encode_input"))
		self.textEdit_encode_output = QtGui.QTextEdit(self.tab_endecode)
		self.textEdit_encode_output.setGeometry(QtCore.QRect(0, 314, 601, 257))
		self.textEdit_encode_output.setObjectName(_fromUtf8("textEdit_encode_output"))
		self.pushButton_encode = QtGui.QPushButton(self.tab_endecode)
		self.pushButton_encode.setGeometry(QtCore.QRect(417, 230, 85, 84))
		self.pushButton_encode.setAutoFillBackground(False)
		self.pushButton_encode.setStyleSheet(_fromUtf8("background-image: url(backgroud.png);"))
		self.pushButton_encode.setText(_fromUtf8(""))
		self.pushButton_encode.setFlat(False)
		self.pushButton_encode.setObjectName(_fromUtf8("pushButton_encode"))
		self.layoutWidget_3 = QtGui.QWidget(self.tab_endecode)
		self.layoutWidget_3.setGeometry(QtCore.QRect(30, 230, 381, 81))
		self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
		self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_3)
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.radioButton_unicode = QtGui.QRadioButton(self.layoutWidget_3)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.radioButton_unicode.setFont(font)
		self.radioButton_unicode.setChecked(True)
		self.radioButton_unicode.setObjectName(_fromUtf8("radioButton_unicode"))
		self.horizontalLayout_3.addWidget(self.radioButton_unicode)
		self.radioButton_url = QtGui.QRadioButton(self.layoutWidget_3)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.radioButton_url.setFont(font)
		self.radioButton_url.setObjectName(_fromUtf8("radioButton_url"))
		self.horizontalLayout_3.addWidget(self.radioButton_url)
		self.radioButton_js = QtGui.QRadioButton(self.layoutWidget_3)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.radioButton_js.setFont(font)
		self.radioButton_js.setObjectName(_fromUtf8("radioButton_js"))
		self.horizontalLayout_3.addWidget(self.radioButton_js)
		self.tabWidget.addTab(self.tab_endecode, _fromUtf8(""))
		self.tab_cmd = QtGui.QWidget()
		self.tab_cmd.setObjectName(_fromUtf8("tab_cmd"))
		self.textEdit_cmd_input = QtGui.QTextEdit(self.tab_cmd)
		self.textEdit_cmd_input.setGeometry(QtCore.QRect(3, 0, 601, 231))
		self.textEdit_cmd_input.setObjectName(_fromUtf8("textEdit_cmd_input"))
		self.textEdit_cmd_output = QtGui.QTextEdit(self.tab_cmd)
		self.textEdit_cmd_output.setGeometry(QtCore.QRect(3, 314, 601, 257))
		self.textEdit_cmd_output.setObjectName(_fromUtf8("textEdit_cmd_output"))
		self.pushButton_cmd = QtGui.QPushButton(self.tab_cmd)
		self.pushButton_cmd.setGeometry(QtCore.QRect(250, 230, 85, 84))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Agency FB"))
		font.setPointSize(14)
		self.pushButton_cmd.setFont(font)
		self.pushButton_cmd.setAutoFillBackground(False)
		self.pushButton_cmd.setFlat(False)
		self.pushButton_cmd.setObjectName(_fromUtf8("pushButton_cmd"))
		self.tabWidget.addTab(self.tab_cmd, _fromUtf8(""))
		self.tab_apache = QtGui.QWidget()
		self.tab_apache.setObjectName(_fromUtf8("tab_apache"))
		self.tableView_apache_vhosts = QtGui.QTableWidget(self.tab_apache)
		self.tableView_apache_vhosts.setGeometry(QtCore.QRect(5, 40, 591, 401))
		self.tableView_apache_vhosts.setObjectName(_fromUtf8("tableView_apache_vhosts"))
		self.plainTextEdit_apache_conf_path = QtGui.QPlainTextEdit(self.tab_apache)
		self.plainTextEdit_apache_conf_path.setGeometry(QtCore.QRect(130, 4, 361, 31))
		self.plainTextEdit_apache_conf_path.setObjectName(_fromUtf8("plainTextEdit_apache_conf_path"))
		self.pushButton_apache_conf_search = QtGui.QPushButton(self.tab_apache)
		self.pushButton_apache_conf_search.setGeometry(QtCore.QRect(500, 4, 96, 31))
		self.pushButton_apache_conf_search.setObjectName(_fromUtf8("pushButton_apache_conf_search"))
		self.label = QtGui.QLabel(self.tab_apache)
		self.label.setGeometry(QtCore.QRect(10, 10, 121, 21))
		self.label.setObjectName(_fromUtf8("label"))
		self.plainTextEdit_vhost_path = QtGui.QPlainTextEdit(self.tab_apache)
		self.plainTextEdit_vhost_path.setGeometry(QtCore.QRect(130, 455, 361, 31))
		self.plainTextEdit_vhost_path.setObjectName(_fromUtf8("plainTextEdit_vhost_path"))
		self.label_2 = QtGui.QLabel(self.tab_apache)
		self.label_2.setGeometry(QtCore.QRect(10, 460, 111, 21))
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.pushButton_vhosts_path_search = QtGui.QPushButton(self.tab_apache)
		self.pushButton_vhosts_path_search.setGeometry(QtCore.QRect(500, 455, 96, 31))
		self.pushButton_vhosts_path_search.setObjectName(_fromUtf8("pushButton_vhosts_path_search"))
		self.label_3 = QtGui.QLabel(self.tab_apache)
		self.label_3.setGeometry(QtCore.QRect(10, 502, 111, 21))
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.plainTextEdit_vhost_port = QtGui.QPlainTextEdit(self.tab_apache)
		self.plainTextEdit_vhost_port.setGeometry(QtCore.QRect(130, 500, 361, 31))
		self.plainTextEdit_vhost_port.setObjectName(_fromUtf8("plainTextEdit_vhost_port"))
		self.pushButton_add_vhost = QtGui.QPushButton(self.tab_apache)
		self.pushButton_add_vhost.setGeometry(QtCore.QRect(130, 540, 96, 31))
		self.pushButton_add_vhost.setObjectName(_fromUtf8("pushButton_add_vhost"))
		self.tabWidget.addTab(self.tab_apache, _fromUtf8(""))
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(4)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.groupBox.setTitle(_translate("MainWindow", "分词模式", None))
		self.radioButton_default.setText(_translate("MainWindow", "精确模式", None))
		self.radioButton_full.setText(_translate("MainWindow", "全模式", None))
		self.radioButton_search.setText(_translate("MainWindow", "搜索引擎模式", None))
		self.groupBox_2.setTitle(_translate("MainWindow", "HMM模型", None))
		self.radioButton_HMM_Y.setText(_translate("MainWindow", "Y", None))
		self.radioButton_HMM_N.setText(_translate("MainWindow", "N", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_jieba), _translate("MainWindow", "结巴分词", None))
		self.groupBox_5.setTitle(_translate("MainWindow", "TopK", None))
		self.groupBox_6.setTitle(_translate("MainWindow", "withWeight", None))
		self.radioButton_withWeight_true.setText(_translate("MainWindow", "True", None))
		self.radioButton_withWeight_false.setText(_translate("MainWindow", "False", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "关键词提取", None))
		self.textEdit_encode_input.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
		self.textEdit_encode_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
		self.radioButton_unicode.setText(_translate("MainWindow", "UNICODE", None))
		self.radioButton_url.setText(_translate("MainWindow", "URL", None))
		self.radioButton_js.setText(_translate("MainWindow", "JS", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_endecode), _translate("MainWindow", "编码解码", None))
		self.textEdit_cmd_input.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
		self.textEdit_cmd_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
		self.pushButton_cmd.setText(_translate("MainWindow", "RUN", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cmd), _translate("MainWindow", "命令行", None))
		self.plainTextEdit_apache_conf_path.setPlainText(_translate("MainWindow", "F:\\www\\httpd\\conf\\extra\\httpd-vhosts.conf", None))
		self.pushButton_apache_conf_search.setText(_translate("MainWindow", "加载", None))
		self.label.setText(_translate("MainWindow", "Apache配置文件路径：", None))
		self.plainTextEdit_vhost_path.setPlainText(_translate("MainWindow", "", None))
		self.label_2.setText(_translate("MainWindow", "虚拟主机网页路径：", None))
		self.pushButton_vhosts_path_search.setText(_translate("MainWindow", "加载", None))
		self.label_3.setText(_translate("MainWindow", "虚拟主机监听端口：", None))
		self.plainTextEdit_vhost_port.setPlainText(_translate("MainWindow", "", None))
		self.pushButton_add_vhost.setText(_translate("MainWindow", "添加", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_apache), _translate("MainWindow", "Apache配置", None))

		self.pushButton.clicked.connect(self.word_segment)
		self.pushButton_encode.clicked.connect(self.encoding_func)
		self.pushButton_cmd.clicked.connect(self.do_cmd)
		self.pushButton_keywords.clicked.connect(self.extract_keywords)
		self.pushButton_apache_conf_search.clicked.connect(self.apache_conf_search)
		self.pushButton_add_vhost.clicked.connect(self.add_vhost)
		self.pushButton_vhosts_path_search.clicked.connect(self.vhosts_path_search)

	def word_segment(self):
		self.textEdit_output.setText(u"")

		sentence = self.textEdit_input.toPlainText()
		sentence = unicode(sentence).encode("utf8")
		cut_full_mode = self.radioButton_full.isChecked()
		cut_search_mode = self.radioButton_search.isChecked()
		hmm_mode = self.radioButton_HMM_Y.isChecked()
		# print "=" *5
		# print cut_full_mode
		# print cut_search_mode
		# print hmm_mode
		if cut_search_mode:
			result = jieba.cut_for_search(sentence, HMM=hmm_mode)
		else:
			result = jieba.cut(sentence, cut_all=cut_full_mode, HMM=hmm_mode)

		sentence_seg = list(result)
		sentence_seg = " / ".join(sentence_seg)
		self.textEdit_output.setText(sentence_seg)

	def extract_keywords(self):
		self.textEdit_keywords_output.setText(u"")

		sentence = self.textEdit_keywords_input.toPlainText()
		sentence = unicode(sentence).encode("utf8")
		withWeight = self.radioButton_withWeight_true.isChecked()
		topK = self.topK.value()
		topK = int(topK)
		result = jieba.analyse.extract_tags(sentence, topK=topK, withWeight=withWeight)
		data = u""
		for i in result:
			if withWeight:
				data += u"%s  %f<br>" %(i[0], i[1])
			else:
				data += u"%s<br>" % (i)

		self.textEdit_keywords_output.setText(data)

	def encoding_func(self):
		self.textEdit_encode_output.setText(u"")
		text = self.textEdit_encode_input.toPlainText()
		text = unicode(text)

		rb_unicode = self.radioButton_unicode.isChecked()
		rb_url = self.radioButton_url.isChecked()
		rb_js = self.radioButton_js.isChecked()

		if rb_unicode:
			text = text.replace(r"u'\u", r"'\u")
			text = eval('u"""' + text + '"""')
			self.textEdit_encode_output.setText(text)
		elif rb_url:
			text = text.encode("utf8")
			import urllib
			text = urllib.unquote(text)
			text = text.decode("utf8")
			self.textEdit_encode_output.setText(text)
		elif rb_js:
			import PyV8
			ctx = PyV8.JSContext()
			ctx.enter()
			code = open("js/base.js").read()
			code += open("js/jsformat.js").read()
			code += open("js/htmlformat.js").read()
			code += open("js/functions-v8.js").read()
			code += """;var content='%s'""" %(text.replace(r"'", r"\'").replace("\n", "").replace("\r", ""))
			code += """;do_js_beautify(content);"""
			# print code
			result = ctx.eval(code)
			result = result.decode("utf8")
			# print result
			# self.textEdit_encode_output.setText(result)
			self.textEdit_encode_output.setPlainText (result)

	def do_cmd(self):
		self.textEdit_cmd_output.setText(u"")
		text = self.textEdit_cmd_input.toPlainText()
		text = unicode(text)
		cmd = text.encode("utf8")
		if "ping " in cmd:
			cmd = cmd.replace("http://", "")
			cmd = cmd.replace("https://", "")
			cmd = cmd.split("/", 1)[0]
		p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		output = p.communicate()
		# print output
		self.textEdit_cmd_output.setText(output[0].decode("gbk"))

	def apache_conf_search(self):
		file_path = self.plainTextEdit_apache_conf_path.toPlainText()
		file_path = unicode(file_path)
		file_path = file_path.encode("utf8").strip()
		if not file_path:
			file_path = QtGui.QFileDialog.getOpenFileName(self, "Apache Vhosts conf")
		print file_path

		self.apache_vhost_conf_path = file_path

		data = open(file_path).read()
		vhost_port = re.findall("[Ll]isten\s+(\d+)", data, re.M)
		vhost_path = re.findall("DocumentRoot\s+\"(.+?)\"", data, re.M)
		vhost_list = zip(vhost_port, vhost_path)

		self.vhost_list = vhost_list

		self.tableView_apache_vhosts.setColumnCount(2)
		self.tableView_apache_vhosts.setRowCount(len(vhost_list))
		self.tableView_apache_vhosts.setSortingEnabled(True)
		self.tableView_apache_vhosts.setShowGrid(True)

		self.tableView_apache_vhosts.setHorizontalHeaderLabels([u"端口", u"路径"])
		for index, vhost in enumerate(vhost_list):
			cellItem = QtGui.QTableWidgetItem(vhost[0])
			cellItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
			self.tableView_apache_vhosts.setItem(index, 0, cellItem)

			cellItem = QtGui.QTableWidgetItem(vhost[1])
			self.tableView_apache_vhosts.setItem(index, 1, cellItem)

		self.tableView_apache_vhosts.horizontalHeader().setStretchLastSection(True)

	def vhosts_path_search(self):
		vhost_path = QtGui.QFileDialog.getExistingDirectory(self, "vhost file dir path")
		vhost_path = unicode(vhost_path)
		vhost_path = vhost_path.encode("utf8").strip()
		vhost_path = vhost_path.replace("\\", "/")
		vhost_path = vhost_path[:-1] if vhost_path.endswith("/") else vhost_path
		print vhost_path
		self.plainTextEdit_vhost_path.setPlainText(vhost_path)
		return vhost_path

	def add_vhost(self):
		if not os.path.exists(self.apache_vhost_conf_path):
			return False

		vhost_path = self.plainTextEdit_vhost_path.toPlainText()
		vhost_path = unicode(vhost_path)
		vhost_path = vhost_path.encode("utf8").strip()
		if not vhost_path:
			vhost_path = self.pushButton_vhosts_path_search.click()

		vhost_port = self.plainTextEdit_vhost_port.toPlainText()
		vhost_port = unicode(vhost_port)
		vhost_port = vhost_port.encode("utf8").strip()

		print vhost_path, vhost_port

		if vhost_port in [port for port, host in self.vhost_list]:
			QtGui.QMessageBox("PORT Exists!")
			return False

		f = open(self.apache_vhost_conf_path, "a")
		new_vhost = """listen %s
<VirtualHost *:%s>
    DocumentRoot "%s"
	<Directory "%s">
		Options Indexes FollowSymLinks
		AllowOverride None
		Require all granted
	</Directory>

	<IfModule dir_module>
		DirectoryIndex index.php index.html index.htm
	</IfModule>
</VirtualHost>""" %(vhost_port, vhost_port, vhost_path, vhost_path)

		f.write("\n"+new_vhost)
		f.close()

#===============================================================================
class TOOLS(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

app = QtGui.QApplication(sys.argv)
win = TOOLS()
win.show()
sys.exit(app.exec_())
