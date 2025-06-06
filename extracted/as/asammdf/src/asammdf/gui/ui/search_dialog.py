# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDialog, QDoubleSpinBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTreeWidget,
    QTreeWidgetItem, QWidget)

from asammdf.gui.dialogs.advanced_search_helpers import SearchTreeWidget
from . import resource_rc

class Ui_SearchDialog(object):
    def setupUi(self, SearchDialog):
        if not SearchDialog.objectName():
            SearchDialog.setObjectName(u"SearchDialog")
        SearchDialog.resize(829, 679)
        SearchDialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QGridLayout(SearchDialog)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.tabs = QTabWidget(SearchDialog)
        self.tabs.setObjectName(u"tabs")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.search_box = QLineEdit(self.tab)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.search_box, 0, 0, 1, 1)

        self.status = QLabel(self.tab)
        self.status.setObjectName(u"status")
        self.status.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.status, 0, 1, 1, 1)

        self.match_kind = QComboBox(self.tab)
        self.match_kind.addItem("")
        self.match_kind.addItem("")
        self.match_kind.setObjectName(u"match_kind")

        self.gridLayout.addWidget(self.match_kind, 0, 2, 1, 1)

        self.case_sensitivity = QComboBox(self.tab)
        self.case_sensitivity.addItem("")
        self.case_sensitivity.addItem("")
        self.case_sensitivity.setObjectName(u"case_sensitivity")

        self.gridLayout.addWidget(self.case_sensitivity, 0, 3, 1, 1)

        self.extended_search = QCheckBox(self.tab)
        self.extended_search.setObjectName(u"extended_search")

        self.gridLayout.addWidget(self.extended_search, 0, 4, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.matches = SearchTreeWidget(self.tab)
        self.matches.setObjectName(u"matches")
        self.matches.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.matches.setUniformRowHeights(False)
        self.matches.setSortingEnabled(False)
        self.matches.header().setMinimumSectionSize(40)
        self.matches.header().setStretchLastSection(True)

        self.gridLayout.addWidget(self.matches, 2, 0, 1, 5)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.selection = SearchTreeWidget(self.tab)
        self.selection.setObjectName(u"selection")
        self.selection.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.selection.setSortingEnabled(False)
        self.selection.header().setMinimumSectionSize(25)
        self.selection.header().setProperty(u"showSortIndicator", False)

        self.gridLayout.addWidget(self.selection, 5, 0, 1, 5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.add_btn = QPushButton(self.tab)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon()
        icon.addFile(u":/shift_down.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_btn.setIcon(icon)
        self.add_btn.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.add_btn)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.show_alias_btn = QPushButton(self.tab)
        self.show_alias_btn.setObjectName(u"show_alias_btn")
        icon1 = QIcon()
        icon1.addFile(u":/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_alias_btn.setIcon(icon1)
        self.show_alias_btn.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.show_alias_btn)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel_btn = QPushButton(self.tab)
        self.cancel_btn.setObjectName(u"cancel_btn")
        icon2 = QIcon()
        icon2.addFile(u":/erase.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancel_btn.setIcon(icon2)
        self.cancel_btn.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.horizontalSpacer_2 = QSpacerItem(20, 16, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.apply_btn = QPushButton(self.tab)
        self.apply_btn.setObjectName(u"apply_btn")
        icon3 = QIcon()
        icon3.addFile(u":/checkmark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.apply_btn.setIcon(icon3)
        self.apply_btn.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.apply_btn)

        self.horizontalSpacer = QSpacerItem(10, 16, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.add_window_btn = QPushButton(self.tab)
        self.add_window_btn.setObjectName(u"add_window_btn")
        icon4 = QIcon()
        icon4.addFile(u":/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_window_btn.setIcon(icon4)
        self.add_window_btn.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.add_window_btn)

        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 5)

        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(5, 1)
        icon5 = QIcon()
        icon5.addFile(u":/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabs.addTab(self.tab, icon5, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.filter_type = QComboBox(self.tab_2)
        self.filter_type.addItem("")
        self.filter_type.addItem("")
        self.filter_type.addItem("")
        self.filter_type.addItem("")
        self.filter_type.setObjectName(u"filter_type")

        self.gridLayout_3.addWidget(self.filter_type, 4, 2, 1, 1)

        self.name = QLineEdit(self.tab_2)
        self.name.setObjectName(u"name")

        self.gridLayout_3.addWidget(self.name, 0, 2, 1, 1)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 8, 1, 1, 1)

        self.case_sensitivity_pattern = QComboBox(self.tab_2)
        self.case_sensitivity_pattern.addItem("")
        self.case_sensitivity_pattern.addItem("")
        self.case_sensitivity_pattern.setObjectName(u"case_sensitivity_pattern")

        self.gridLayout_3.addWidget(self.case_sensitivity_pattern, 3, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 254, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 10, 1, 1, 1)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 5, 1, 1, 1)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 9, 1, 1, 1)

        self.filter_value = QDoubleSpinBox(self.tab_2)
        self.filter_value.setObjectName(u"filter_value")
        self.filter_value.setDecimals(6)
        self.filter_value.setMinimum(-9999999999999999635896294965248.000000000000000)
        self.filter_value.setMaximum(999999999999999983222784.000000000000000)

        self.gridLayout_3.addWidget(self.filter_value, 5, 2, 1, 1)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 4, 1, 1, 1)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 1, 1, 1)

        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 1, 1, 1)

        self.define_ranges_btn = QPushButton(self.tab_2)
        self.define_ranges_btn.setObjectName(u"define_ranges_btn")
        icon6 = QIcon()
        icon6.addFile(u":/range.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.define_ranges_btn.setIcon(icon6)
        self.define_ranges_btn.setAutoDefault(False)

        self.gridLayout_3.addWidget(self.define_ranges_btn, 7, 2, 1, 1)

        self.pattern_match_type = QComboBox(self.tab_2)
        self.pattern_match_type.addItem("")
        self.pattern_match_type.addItem("")
        self.pattern_match_type.setObjectName(u"pattern_match_type")

        self.gridLayout_3.addWidget(self.pattern_match_type, 2, 2, 1, 1)

        self.raw = QCheckBox(self.tab_2)
        self.raw.setObjectName(u"raw")

        self.gridLayout_3.addWidget(self.raw, 6, 2, 1, 1)

        self.pattern_matches = QTreeWidget(self.tab_2)
        self.pattern_matches.setObjectName(u"pattern_matches")
        self.pattern_matches.setSortingEnabled(True)

        self.gridLayout_3.addWidget(self.pattern_matches, 0, 3, 11, 3)

        self.integer_format = QComboBox(self.tab_2)
        self.integer_format.addItem("")
        self.integer_format.addItem("")
        self.integer_format.addItem("")
        self.integer_format.addItem("")
        self.integer_format.setObjectName(u"integer_format")

        self.gridLayout_3.addWidget(self.integer_format, 8, 2, 1, 1)

        self.pattern = QLineEdit(self.tab_2)
        self.pattern.setObjectName(u"pattern")
        self.pattern.setMinimumSize(QSize(300, 0))

        self.gridLayout_3.addWidget(self.pattern, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(282, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 11, 4, 1, 1)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 1)

        self.apply_pattern_btn = QPushButton(self.tab_2)
        self.apply_pattern_btn.setObjectName(u"apply_pattern_btn")
        self.apply_pattern_btn.setIcon(icon3)
        self.apply_pattern_btn.setAutoDefault(False)

        self.gridLayout_3.addWidget(self.apply_pattern_btn, 11, 5, 1, 1)

        self.cancel_pattern_btn = QPushButton(self.tab_2)
        self.cancel_pattern_btn.setObjectName(u"cancel_pattern_btn")
        self.cancel_pattern_btn.setIcon(icon2)
        self.cancel_pattern_btn.setAutoDefault(False)

        self.gridLayout_3.addWidget(self.cancel_pattern_btn, 11, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.y_range_min = QDoubleSpinBox(self.tab_2)
        self.y_range_min.setObjectName(u"y_range_min")
        self.y_range_min.setDecimals(6)

        self.horizontalLayout_3.addWidget(self.y_range_min)

        self.y_range_max = QDoubleSpinBox(self.tab_2)
        self.y_range_max.setObjectName(u"y_range_max")
        self.y_range_max.setDecimals(6)

        self.horizontalLayout_3.addWidget(self.y_range_max)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 9, 2, 1, 1)

        self.gridLayout_3.setRowStretch(10, 1)
        self.gridLayout_3.setColumnStretch(3, 1)
        self.tabs.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabs, 0, 0, 1, 1)

        QWidget.setTabOrder(self.search_box, self.match_kind)
        QWidget.setTabOrder(self.match_kind, self.case_sensitivity)
        QWidget.setTabOrder(self.case_sensitivity, self.extended_search)
        QWidget.setTabOrder(self.extended_search, self.matches)
        QWidget.setTabOrder(self.matches, self.add_btn)
        QWidget.setTabOrder(self.add_btn, self.selection)
        QWidget.setTabOrder(self.selection, self.add_window_btn)
        QWidget.setTabOrder(self.add_window_btn, self.apply_btn)
        QWidget.setTabOrder(self.apply_btn, self.cancel_btn)
        QWidget.setTabOrder(self.cancel_btn, self.name)
        QWidget.setTabOrder(self.name, self.pattern)
        QWidget.setTabOrder(self.pattern, self.pattern_match_type)
        QWidget.setTabOrder(self.pattern_match_type, self.case_sensitivity_pattern)
        QWidget.setTabOrder(self.case_sensitivity_pattern, self.filter_type)
        QWidget.setTabOrder(self.filter_type, self.filter_value)
        QWidget.setTabOrder(self.filter_value, self.raw)
        QWidget.setTabOrder(self.raw, self.define_ranges_btn)
        QWidget.setTabOrder(self.define_ranges_btn, self.integer_format)
        QWidget.setTabOrder(self.integer_format, self.apply_pattern_btn)
        QWidget.setTabOrder(self.apply_pattern_btn, self.cancel_pattern_btn)

        self.retranslateUi(SearchDialog)

        self.tabs.setCurrentIndex(0)
        self.match_kind.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SearchDialog)
    # setupUi

    def retranslateUi(self, SearchDialog):
        SearchDialog.setWindowTitle(QCoreApplication.translate("SearchDialog", u"Dialog", None))
        self.search_box.setPlaceholderText(QCoreApplication.translate("SearchDialog", u"channel name pattern", None))
        self.status.setText(QCoreApplication.translate("SearchDialog", u"No results", None))
        self.match_kind.setItemText(0, QCoreApplication.translate("SearchDialog", u"Wildcard", None))
        self.match_kind.setItemText(1, QCoreApplication.translate("SearchDialog", u"Regex", None))

        self.case_sensitivity.setItemText(0, QCoreApplication.translate("SearchDialog", u"Case insensitive", None))
        self.case_sensitivity.setItemText(1, QCoreApplication.translate("SearchDialog", u"Case sensitive", None))

        self.extended_search.setText(QCoreApplication.translate("SearchDialog", u"Extended search", None))
        self.label_7.setText(QCoreApplication.translate("SearchDialog", u"Search results", None))
        ___qtreewidgetitem = self.matches.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("SearchDialog", u"Comment", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("SearchDialog", u"Source path", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("SearchDialog", u"Source name", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("SearchDialog", u"Unit", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("SearchDialog", u"Index", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("SearchDialog", u"Group", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("SearchDialog", u"Name", None));
        self.label.setText(QCoreApplication.translate("SearchDialog", u"Final selection", None))
        ___qtreewidgetitem1 = self.selection.headerItem()
        ___qtreewidgetitem1.setText(6, QCoreApplication.translate("SearchDialog", u"Comment", None));
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("SearchDialog", u"Source path", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("SearchDialog", u"Source name", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("SearchDialog", u"Unit", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("SearchDialog", u"Index", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("SearchDialog", u"Group", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("SearchDialog", u"Name", None));
        self.add_btn.setText(QCoreApplication.translate("SearchDialog", u"Add to selection", None))
        self.show_alias_btn.setText(QCoreApplication.translate("SearchDialog", u"Show overlapping alias", None))
        self.cancel_btn.setText(QCoreApplication.translate("SearchDialog", u"Cancel", None))
        self.apply_btn.setText(QCoreApplication.translate("SearchDialog", u"Apply", None))
        self.add_window_btn.setText(QCoreApplication.translate("SearchDialog", u"Add window", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), QCoreApplication.translate("SearchDialog", u"Search", None))
        self.filter_type.setItemText(0, QCoreApplication.translate("SearchDialog", u"Unspecified", None))
        self.filter_type.setItemText(1, QCoreApplication.translate("SearchDialog", u"Contains", None))
        self.filter_type.setItemText(2, QCoreApplication.translate("SearchDialog", u"Do not contain", None))
        self.filter_type.setItemText(3, QCoreApplication.translate("SearchDialog", u"Constant", None))

        self.label_9.setText(QCoreApplication.translate("SearchDialog", u"Integer format", None))
        self.case_sensitivity_pattern.setItemText(0, QCoreApplication.translate("SearchDialog", u"Case insensitive", None))
        self.case_sensitivity_pattern.setItemText(1, QCoreApplication.translate("SearchDialog", u"Case sensitive", None))

        self.label_4.setText(QCoreApplication.translate("SearchDialog", u"Filter value", None))
        self.label_8.setText(QCoreApplication.translate("SearchDialog", u"Y range", None))
        self.label_3.setText(QCoreApplication.translate("SearchDialog", u"Filter type", None))
        self.label_5.setText(QCoreApplication.translate("SearchDialog", u"Match type", None))
        self.label_6.setText(QCoreApplication.translate("SearchDialog", u"Name", None))
        self.define_ranges_btn.setText(QCoreApplication.translate("SearchDialog", u"Define ranges", None))
        self.pattern_match_type.setItemText(0, QCoreApplication.translate("SearchDialog", u"Wildcard", None))
        self.pattern_match_type.setItemText(1, QCoreApplication.translate("SearchDialog", u"Regex", None))

        self.raw.setText(QCoreApplication.translate("SearchDialog", u"Use the raw channel values", None))
        ___qtreewidgetitem2 = self.pattern_matches.headerItem()
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("SearchDialog", u"Channels matching the pattern conditions", None));
        self.integer_format.setItemText(0, QCoreApplication.translate("SearchDialog", u"phys", None))
        self.integer_format.setItemText(1, QCoreApplication.translate("SearchDialog", u"bin", None))
        self.integer_format.setItemText(2, QCoreApplication.translate("SearchDialog", u"hex", None))
        self.integer_format.setItemText(3, QCoreApplication.translate("SearchDialog", u"ascii", None))

        self.pattern.setPlaceholderText(QCoreApplication.translate("SearchDialog", u"channel name pattern", None))
        self.label_2.setText(QCoreApplication.translate("SearchDialog", u"Pattern", None))
        self.apply_pattern_btn.setText(QCoreApplication.translate("SearchDialog", u"Apply", None))
        self.cancel_pattern_btn.setText(QCoreApplication.translate("SearchDialog", u"Cancel", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), QCoreApplication.translate("SearchDialog", u"Pattern definition", None))
    # retranslateUi

