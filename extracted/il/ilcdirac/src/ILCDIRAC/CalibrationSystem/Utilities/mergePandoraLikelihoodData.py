"""This is the the script for chaining many pandora photon likelihood files into a single likelihood file.

Input: ['InputFile1.xml', 'InputFile2.xml']
Ouput: OutputFile.xml

Tested with Pandora v02-08-02. If photon reconstruction algorithm in LCContent is not changed, then this script should
be valid
"""


# !/usr/bin/python

from __future__ import absolute_import
import xml.etree.ElementTree as ET
from DIRAC import S_OK, S_ERROR
from six.moves import zip


def getFixedXMLTree(inputFile):
  """Get fixed xml files by adding a top element.

  :param str inputFile: a string of input file
  :returns: an elementtree with fixed top element
  """
  content = ""
  with open(inputFile, "r") as f:
    content = f.read()
  # fix xml; Added top element in order to use the xml tree structure
  content = "<HEAD>\n" + content + "</HEAD>\n"
  root = ET.fromstring(content)
  return root


def convertLikelihoodToNum(root):
  """Convert entries from likelihood data to absolute number.

  :param root: an elementtree
  :returns: an elementtree with modified entries
  """
  nSignalVec = [int(i) for i in root.find("NSignalEvents").text.split()]
  nBackgroundVec = [int(i) for i in root.find("NBackgroundEvents").text.split()]

  dataChildrenNodes = [node for node in list(root) if node.tag.find("_") > 0]
  for node in dataChildrenNodes:
    nCurrentEnergyBin = int(node.tag.split("_")[-1])
    nBin = nSignalVec[nCurrentEnergyBin] if node.tag.find("Bkg") < 0 else nBackgroundVec[nCurrentEnergyBin]

    subnode = root.find("./" + node.tag + "/BinContents")
    subnode.text = " ".join([str(int(round(float(i) * nBin))) for i in subnode.text.split()])
  return root


def convertNumToLikelihood(root):
  """Convert entries from absolute number to likelihood number.

  :param root: an elementtree
  :returns: an elementtree with modified entries
  """
  nSignalVec = [int(i) for i in root.find("NSignalEvents").text.split()]
  nBackgroundVec = [int(i) for i in root.find("NBackgroundEvents").text.split()]

  dataChildrenNodes = [node for node in list(root) if node.tag.find("_") > 0]
  for node in dataChildrenNodes:
    nCurrentEnergyBin = int(node.tag.split("_")[-1])
    nBin = nSignalVec[nCurrentEnergyBin] if node.tag.find("Bkg") < 0 else nBackgroundVec[nCurrentEnergyBin]

    subnode = root.find("./" + node.tag + "/BinContents")
    # TODO FIXME treat nBin == 0 case. it was in the original script.
    if nBin == 0:
      nBin = 1
    # same precision as we had in python2
    subnode.text = " ".join([('{0:.12g}'.format(float(i) / nBin) if float(i) else '0.0') for i in subnode.text.split()])
  return root


def addTwoNode(initialRoot, finalRoot, tag):
  """Add entries of a tag of two trees.

  :param initialRoot: an elementtree
  :param finalRoot: an elementtree to be modified
  :param tag: the tag to be operated
  :returns: an elementtree with modified entries
  """
  nVecFinal = [int(i) for i in finalRoot.find(tag).text.split()]
  nVecInitial = [int(i) for i in initialRoot.find(tag).text.split()]
  nVecSim = [sum(x) for x in zip(nVecFinal, nVecInitial)]
  finalRoot.find(tag).text = " ".join(str(i) for i in nVecSim)
  return finalRoot


def mergeLikelihoods(inputFiles, outputFile):
  """Change many pandora photon likelihood files into a single likelihood file.

  This is the the main method.
  :param list str inputFiles: a list of strings with names of input files
  :param str outputFile: a string of output file
  """
  finalRoot = None
  for inputFile in inputFiles:
    root = convertLikelihoodToNum(getFixedXMLTree(inputFile))

    if (finalRoot is None):
      finalRoot = root
    else:
      finalRoot = addTwoNode(root, finalRoot, "NSignalEvents")
      finalRoot = addTwoNode(root, finalRoot, "NBackgroundEvents")

      dataChildrenNodes = [node for node in list(root) if node.tag.find("_") > 0]
      for node in dataChildrenNodes:
        finalRoot = addTwoNode(root, finalRoot, "./" + node.tag + "/BinContents")
  try:
    finalRoot = convertNumToLikelihood(finalRoot)
  except ZeroDivisionError as e:
    return S_ERROR('Division by zero. Not enough events used for photon training - some energy bins have 0 bkg/signal'
                   ' events. Error_msg: %s' % e)

  # fix xml; Strip the top element to revert the change
  finalContent = ET.tostring(finalRoot).decode().strip('</HEAD>').strip('<HEAD>').lstrip()
  with open(outputFile, "w") as f:
    f.write(finalContent)
  return S_OK()
