""" Module containing a front-end to the ElasticSearch-based ElasticJobParametersDB.
    This is a drop-in replacement for MySQL-based table JobDB.JobParameters.

    The reason for switching to a ES-based JobParameters lies in the extended searching
    capabilities of ES.
    This results in higher traceability for DIRAC jobs.

    The following class methods are provided for public usage
      - getJobParameters()
      - setJobParameter()
      - deleteJobParameters()
"""
from collections import defaultdict
from typing import Union

from DIRAC import S_ERROR, S_OK
from DIRAC.ConfigurationSystem.Client.Helpers import CSGlobals
from DIRAC.Core.Base.ElasticDB import ElasticDB
from DIRAC.Core.Utilities import TimeUtilities
from DIRAC.ConfigurationSystem.Client.Config import gConfig
from DIRAC.ConfigurationSystem.Client.PathFinder import getDatabaseSection

try:
    from opensearchpy.exceptions import NotFoundError, RequestError
except ImportError:
    from elasticsearch.exceptions import NotFoundError, RequestError

name = "ElasticJobParametersDB"  # (base for) old index name


mapping = {
    "properties": {
        "JobID": {"type": "long"},
        "timestamp": {"type": "date"},
        "CPUNormalizationFactor": {"type": "long"},
        "NormCPUTime(s)": {"type": "long"},
        "Memory(kB)": {"type": "long"},
        "TotalCPUTime(s)": {"type": "long"},
        "MemoryUsed(kb)": {"type": "long"},
        "HostName": {"type": "keyword"},
        "GridCE": {"type": "keyword"},
        "ModelName": {"type": "keyword"},
        "Status": {"type": "keyword"},
        "JobType": {"type": "keyword"},
    }
}


class ElasticJobParametersDB(ElasticDB):
    def __init__(self, parentLogger=None):
        """Standard Constructor"""

        try:
            section = getDatabaseSection("WorkloadManagement/ElasticJobParametersDB")
            indexPrefix = gConfig.getValue(f"{section}/IndexPrefix", CSGlobals.getSetup()).lower()

            # Connecting to the ES cluster
            super().__init__(name, "WorkloadManagement/ElasticJobParametersDB", indexPrefix, parentLogger=parentLogger)
        except Exception as ex:
            self.log.error("Can't connect to ElasticJobParametersDB", repr(ex))
            raise RuntimeError("Can't connect to ElasticJobParametersDB") from ex

        self.oldIndexName = f"{self.getIndexPrefix()}_{name.lower()}"
        self.indexName_base = f"{self.getIndexPrefix()}_elasticjobparameters_index"

        self.dslSearch = self._Search(self.oldIndexName)
        self.dslSearch.extra(track_total_hits=True)

    def _indexName(self, jobID: int) -> str:
        """construct the index name

        :param jobID: Job ID
        """
        indexSplit = int(jobID) // 1e6
        return f"{self.indexName_base}_{indexSplit}m"

    def _createIndex(self, indexName: str) -> None:
        """Create a new index if needed

        :param indexName: index name
        """
        # Verifying if the index is there, and if not create it
        res = self.existingIndex(indexName)
        if not res["OK"] or not res["Value"]:
            result = self.createIndex(indexName, mapping, period=None)
            if not result["OK"]:
                self.log.error(result["Message"])
                raise RuntimeError(result["Message"])
            self.log.always("Index created:", indexName)

    def getJobParameters(self, jobIDs: Union[int, list[int]], paramList=None) -> dict:
        """Get Job Parameters defined for jobID.
          Returns a dictionary with the Job Parameters.
          If paramList is empty - all the parameters are returned.

        :param self: self reference
        :param jobID: Job ID
        :param paramList: list of parameters to be returned (also a string is treated)
        :return: dict with all Job Parameter values
        """
        if isinstance(jobIDs, int):
            jobIDs = [jobIDs]
        if isinstance(paramList, str):
            paramList = paramList.replace(" ", "").split(",")
        self.log.debug(f"JobDB.getParameters: Getting Parameters for jobs {jobIDs}")

        # First search the old index
        result = self._searchInOldIndex(jobIDs, paramList)

        # Next search the new index
        res = self.getDocs(self._indexName, jobIDs)
        if not res["OK"]:
            return res

        # Update result, preferring parameters from the new index
        for job_id, doc in res["Value"].items():
            if job_id not in result:
                result[job_id] = {}
            if paramList:
                result[job_id] |= {k: v for k, v in doc.items() if k in paramList}
            else:
                result[job_id] |= doc

        return S_OK(result)

    def setJobParameter(self, jobID: int, key: str, value: str) -> dict:
        """
        Inserts data into ElasticJobParametersDB index

        :param self: self reference
        :param jobID: Job ID
        :param key: parameter key
        :param value: parameter value
        :returns: S_OK/S_ERROR as result of indexing
        """
        data = {"JobID": jobID, key: value, "timestamp": TimeUtilities.toEpochMilliSeconds()}

        self.log.debug("Inserting data in {self.indexName}:{data}")

        # The _id in ES can't exceed 512 bytes, this is a ES hard-coded limitation.

        # If a record with this jobID update and add parameter, otherwise create a new record
        if self.existsDoc(self._indexName(jobID), docID=str(jobID)):
            self.log.debug("A document for this job already exists, it will now be updated")
            result = self.updateDoc(index=self._indexName(jobID), docID=str(jobID), body={"doc": data})
        else:
            self.log.debug("No document has this job id, creating a new document for this job")
            self._createIndex(self._indexName(jobID))
            result = self.index(indexName=self._indexName(jobID), body=data, docID=str(jobID))
        if not result["OK"]:
            self.log.error("Couldn't insert or update data", result["Message"])
        return result

    def setJobParameters(self, jobID: int, parameters: list) -> dict:
        """
        Inserts data into ElasticJobParametersDB index using bulk indexing

        :param self: self reference
        :param jobID: Job ID
        :param parameters: list of tuples (name, value) pairs
        :returns: S_OK/S_ERROR as result of indexing
        """
        self.log.debug("Inserting parameters", f"in {self._indexName(jobID)}: for job {jobID}: {parameters}")

        parametersDict = dict(parameters)
        parametersDict["JobID"] = jobID
        parametersDict["timestamp"] = int(TimeUtilities.toEpochMilliSeconds())

        if self.existsDoc(self._indexName(jobID), docID=str(jobID)):
            self.log.debug("A document for this job already exists, it will now be updated")
            result = self.updateDoc(index=self._indexName(jobID), docID=str(jobID), body={"doc": parametersDict})
        else:
            self.log.debug("Creating a new document for this job")
            self._createIndex(self._indexName(jobID))
            result = self.index(self._indexName(jobID), body=parametersDict, docID=str(jobID))
        if not result["OK"]:
            self.log.error("Couldn't insert or update data", result["Message"])
        return result

    def deleteJobParameters(self, jobID: int, paramList=None) -> dict:
        """Deletes Job Parameters defined for jobID.
          Returns a dictionary with the Job Parameters.
          If paramList is empty - all the parameters for the job are removed

        :param self: self reference
        :param jobID: Job ID
        :param paramList: list of parameters to be returned (also a string is treated)
        :return: S_OK()/S_ERROR()
        """

        if isinstance(paramList, str):
            paramList = paramList.replace(" ", "").split(",")
        inNewIndex = self.existsDoc(self._indexName(jobID), str(jobID))
        inOldIndex = self._isInOldIndex(self.oldIndexName, jobID)

        # 3 Cases as in GetJobParameters
        if inNewIndex and inOldIndex:
            # Delete first in the old index, then in the new one
            self._deleteInOldIndex(jobID, paramList)
            res = self._deleteInNewIndex(jobID, paramList)
            if not res["OK"]:
                return S_ERROR(res)

        elif inOldIndex:
            self._deleteInOldIndex(jobID, paramList)

        else:
            self.log.debug(
                f"The searched parameters with JobID {jobID} exists in the new index {self._indexName(jobID)}"
            )
            res = self._deleteInNewIndex(jobID, paramList)
            if not res["OK"]:
                return S_ERROR(res)

        return S_OK()

    def _isInOldIndex(self, old_index: str, jobID: int) -> bool:
        """Checks if a document with this jobID exists in the old index"""
        query = {
            "query": {
                "bool": {
                    "filter": {  # no scoring
                        "term": {"JobID": jobID}  # term level query, does not pass through the analyzer
                    }
                }
            }
        }
        try:
            # See a document with this jobID is stored in the old index
            self.query(old_index, query)
            return True
        except (RequestError, NotFoundError):
            return False

    def _searchInOldIndex(self, jobIDs: list[int], paramList: list):
        """Searches for a document with this jobID in the old index"""
        if paramList:
            if isinstance(paramList, str):
                paramList = paramList.replace(" ", "").split(",")
        else:
            paramList = []

        s = self.dslSearch.query("bool", filter=self._Q("terms", JobID=jobIDs))

        res = s.scan()

        resultDict = {}
        try:
            for hit in res:
                jobID = int(hit.JobID)
                pname = hit.Name
                if paramList and pname not in paramList:
                    continue
                resultDict.setdefault(jobID, {})[pname] = hit.Value
        except NotFoundError:
            pass
        return resultDict

    def _deleteInOldIndex(self, jobID: int, paramList: list) -> dict:
        """Deletes a document with this jobID in the old index"""
        self.log.debug(f"A document with JobID {jobID} was found in the old index {self.oldIndexName}")
        jobFilter = self._Q("term", JobID=jobID)

        if not paramList:
            s = self.dslSearch.query("bool", filter=jobFilter)
            s.delete()
            return S_OK()

        # the following should be equivalent to
        # {
        #   "query": {
        #     "bool": {
        #       "filter": [  # no scoring
        #         {"term": {"JobID": jobID}},  # term level query, does not pass through the analyzer
        #         {"term": {"Name": param}},  # term level query, does not pass through the analyzer
        #       ]
        #     }
        #   }
        # }

        for param in paramList:
            paramFilter = self._Q("term", Name=param)
            combinedFilter = jobFilter & paramFilter

            s = self.dslSearch.query("bool", filter=combinedFilter)
            s.delete()

    def _deleteInNewIndex(self, jobID: int, paramList=None) -> dict:
        """Deletes a document with this jobID in the new index"""
        if not paramList:
            # Deleting the whole record
            self.log.debug("Deleting record of job {jobID}")
            result = self.deleteDoc(self._indexName(jobID), docID=str(jobID))
        else:
            # Deleting the specific parameters
            self.log.debug(f"JobDB.getParameters: Deleting Parameters {paramList} for job {jobID}")
            for paramName in paramList:
                result = self.updateDoc(
                    index=self._indexName(jobID),
                    docID=str(jobID),
                    body={"script": "ctx._source.remove('" + paramName + "')"},
                )
                self.log.debug(f"Deleted parameter {paramName}")
        if not result["OK"]:
            return S_ERROR(result)
        self.log.debug("Parameters successfully deleted.")
        return S_OK()

    # TODO: Add query by value (e.g. query which values are in a certain pattern)
