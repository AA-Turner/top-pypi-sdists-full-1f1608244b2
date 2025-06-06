#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from pyspark.ml.param import *
from ai.h2o.sparkling.ml.params.H2OTypeConverters import H2OTypeConverters
from ai.h2o.sparkling.H2ODataFrameConverters import H2ODataFrameConverters
from ai.h2o.sparkling.ml.metrics.H2OCommonMetrics import H2OCommonMetrics


class H2OBinomialMetrics(H2OCommonMetrics):

    def __init__(self, java_obj):
        self._java_obj = java_obj

    def getR2(self):
        """
        The R^2 for this scoring run.
        """
        value = self._java_obj.getR2()
        return value

    def getLogloss(self):
        """
        The logarithmic loss for this scoring run.
        """
        value = self._java_obj.getLogloss()
        return value

    def getLoglikelihood(self):
        """
        The logarithmic likelihood for this scoring run.
        """
        value = self._java_obj.getLoglikelihood()
        return value

    def getAIC(self):
        """
        The AIC for this scoring run.
        """
        value = self._java_obj.getAIC()
        return value

    def getAUC(self):
        """
        The AUC for this scoring run.
        """
        value = self._java_obj.getAUC()
        return value

    def getPRAUC(self):
        """
        The precision-recall AUC for this scoring run.
        """
        value = self._java_obj.getPRAUC()
        return value

    def getGini(self):
        """
        The Gini score for this scoring run.
        """
        value = self._java_obj.getGini()
        return value

    def getMeanPerClassError(self):
        """
        The mean misclassification error per class.
        """
        value = self._java_obj.getMeanPerClassError()
        return value

    def getConfusionMatrix(self):
        """
        The ConfusionMatrix at the threshold for maximum F1.
        """
        value = self._java_obj.getConfusionMatrix()
        return H2ODataFrameConverters.scalaToPythonDataFrame(value)

    def getThresholdsAndMetricScores(self):
        """
        The Metrics for various thresholds.
        """
        value = self._java_obj.getThresholdsAndMetricScores()
        return H2ODataFrameConverters.scalaToPythonDataFrame(value)

    def getMaxCriteriaAndMetricScores(self):
        """
        The Metrics for various criteria.
        """
        value = self._java_obj.getMaxCriteriaAndMetricScores()
        return H2ODataFrameConverters.scalaToPythonDataFrame(value)

    def getGainsLiftTable(self):
        """
        Gains and Lift table.
        """
        value = self._java_obj.getGainsLiftTable()
        return H2ODataFrameConverters.scalaToPythonDataFrame(value)
