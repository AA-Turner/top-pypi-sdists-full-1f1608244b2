# coding: utf-8
# /*##########################################################################
#
# Copyright (C) 2016-2018 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/

from __future__ import absolute_import

__authors__ = ["V. Valls"]
__license__ = "MIT"
__date__ = "31/01/2025"

import os.path

from silx.gui import qt
from silx.gui import icons
import pyFAI.calibrant
from ..model.CalibrantModel import CalibrantModel
from ...utils.decorators import deprecated


class CalibrantSelector(qt.QComboBox):
    """Dropdown widget to select a calibrant.

    It is a view on top of a calibrant model (see :meth:`setCalibrantModel`,
    :meth:`calibrantModel`)

    The calibrant can be selected from a list of calibrant known by pyFAI.

    An extra option to load a calibrant from a file can be enabled with
    :meth:`setFileLoadable`. The widget does not handle the dialog or the IO
    but provides a signal :attr:`sigLoadFileRequested` which has to be connected.
    """

    sigLoadFileRequested = qt.Signal()

    def __init__(self, parent=None):
        super(CalibrantSelector, self).__init__(parent)
        self.setStyleSheet("QComboBox {combobox-popup: 0;}")

        # feed the widget with default calibrants
        items = pyFAI.calibrant.CALIBRANT_FACTORY.items()
        items = sorted(items, key=lambda x: x[0].lower())
        for calibrantName, calibrant in items:
            self.addItem(calibrantName, calibrant)
            icon = icons.getQIcon("pyfai:gui/icons/calibrant")
            self.setItemIcon(self.count() - 1, icon)

        self.__calibrantCount = self.count()
        self.__isFileLoadable = False

        self.__model: CalibrantModel = None
        self.setCalibrantModel(CalibrantModel())
        self.currentIndexChanged[int].connect(self.__currentIndexChanged)

    def __currentIndexChanged(self, index):
        model = self.calibrantModel()
        if model is None:
            return
        if self.__isFileLoadable:
            if index == self.count() - 1:
                # Selection back to the previous location
                calibrant = model.calibrant()
                index = self.findCalibrant(calibrant)
                self.setCurrentIndex(index)
                # Send the request
                self.__loadFileRequested()
                return

        item = self.itemData(index)
        old = self.blockSignals(True)
        model.setCalibrant(item)
        self.blockSignals(old)

    def setFileLoadable(self, isFileLoadable):
        if self.__isFileLoadable == isFileLoadable:
            return

        self.__isFileLoadable = isFileLoadable

        if isFileLoadable:
            self.insertSeparator(self.count())
            self.addItem("Load calibrant file...")
            icon = icons.getQIcon('document-open')
            index = self.count() - 1
            self.setItemIcon(index, icon)
        else:
            self.removeItem(self.count())
            self.removeItem(self.count())

    def __loadFileRequested(self):
        self.sigLoadFileRequested.emit()

    def setCalibrantModel(self, model: CalibrantModel):
        if self.__model is not None:
            self.__model.changed.disconnect(self.__modelChanged)
        self.__model = model
        if self.__model is not None:
            self.__model.changed.connect(self.__modelChanged)
        self.__modelChanged()

    @deprecated(replacement="setCalibrantModel")
    def setModel(self, model: CalibrantModel):
        self.setCalibrantModel(model)

    def findCalibrant(self, calibrant):
        """Returns the first index containing the requested calibrant.
        Else return -1"""
        for index in range(self.__calibrantCount):
            item = self.itemData(index)
            if item == calibrant:
                return index
        return -1

    def __findInsertion(self, name):
        for index in range(self.__calibrantCount):
            itemName = self.itemText(index)
            if name < itemName:
                return index
        return self.__calibrantCount

    def __modelChanged(self):
        value = self.__model.calibrant()
        if value is None:
            self.setCurrentIndex(-1)
        else:
            index = self.currentIndex()
            item = self.itemData(index)
            if item != value:
                # findData is not working
                index = self.findCalibrant(value)
                if index == -1:
                    if value.filename is not None:
                        calibrantName = os.path.basename(value.filename)
                    else:
                        calibrantName = "No name"
                    index = self.__findInsertion(calibrantName)
                    self.insertItem(index, calibrantName, value)
                    icon = icons.getQIcon("pyfai:gui/icons/calibrant-custom")
                    self.setItemIcon(index, icon)
                    self.__calibrantCount += 1
                self.setCurrentIndex(index)

    def calibrantModel(self) -> CalibrantModel:
        return self.__model

    @deprecated(replacement="calibrantModel")
    def model(self) -> CalibrantModel:
        return self.model()
