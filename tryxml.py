#coding:utf8
from __future__ import unicode_literals
import xml.dom.minidom as MD
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')

dom = MD.parse('abc.xml')
impl = MD.getDOMImplementation()
dom2 = impl.createDocument(None,"Test",None)
root = dom.documentElement
root2 = dom.documentElement
print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE

name = root.getElementsByTagName('caption')
myele = name
print myele[0].firstChild.data
kid = dom.createElement("kid")
root.appendChild(kid)
kidT = dom.createTextNode("kidfoff")

kid.appendChild(kidT)
# myele[0].firstChild.appendChild(kid)
f = open('abc2.xml','wb')
dom.writexml(f,addindent=' ',encoding="utf-8")
f.close()
