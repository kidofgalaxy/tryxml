#! /usr/bin/python
import os
import codecs
import traceback
import xml.dom.minidom as minidom
from portalocker import *
def covert_to_unicode(msg):
	__re_str=None
	if isinstance(msg,unicode):
		__re_str=msg
	elif isinstance(msg,str):
		try:
			__re_str=msg.decode('utf-8')
		except Exception,errinfo:
			raise Exception,'%s,%s' % (errinfo,str(msg))
	else:
		raise Exception,'%s is need  to be a str or unicode type' % msg
	return __re_str


class CreateXml():
	def __init__(self,xml_path):
		self.__xml_path=xml_path
		self.__dom=None
		self.__root=None
		self.__second=None

	def __covert_code(self,msg):
		return covert_to_unicode(msg)
	def __create_new_node(self,node_name,node_text=None):
		if self.__dom==None:
			raise Exception,'dom is not exist!'
		
		if None==node_text:
			return self.__dom.createElement(self.__covert_code(node_name))
		else:
			newNode=self.__dom.createElement(self.__covert_code(node_name))
			newText=self.__dom.createTextNode(self.__covert_code(node_text))
			newNode.appendChild(newText)
			return newNode
		
	def begin_cov(self):
		try:
			impl=minidom.getDOMImplementation()
			self.__dom=impl.createDocument(None,u'WebTrojanDetectionResult',None)
			self.__root=self.__dom.documentElement
		except:
			#traceback.print_exc()
			raise Exception,'create xml root node failure!'
	def add_header_cov(self,task_id,task_type,module_type,check_time):
		if self.__root==None:
			raise Exception,'Create root node failure!'
		self.__second=self.__create_new_node("WebTrojanDetectionTask")
		self.__second.setAttribute(u'task_id',task_id)
		self.__second.setAttribute(u'task_type',task_type)
		self.__second.setAttribute(u'module_type',module_type)
		check_time_node=self.__create_new_node("TimeStamp",check_time)
		self.__second.appendChild(check_time_node)

	def add_cov(self,iframe_src,start_url,task_target_id,user_id):
		if self.__root==None:
			raise Exception,'create node failure!'

#		url_iframe_node=self.__create_new_node("WebTrojanCheckTask")
#		url_iframe_node.setAttribute(u'start_url',start_url)
#		url_iframe_node.setAttribute(u'task_id',task_id)
#		url_iframe_node.setAttribute(u'check_time',check_time)
#		url_iframe_node.setAttribute(u'module_type',module_type)
#		url_iframe_node.setAttribute(u'task_type',task_type)
		
#		url_timestamp_node=self.__create_new_node("TimeStamp",check_time)
	#	url_starturl_node=self.__create_new_node("StartURL",start_url)
#		self.__second.appendChild(url_timestamp_node)
	#	url_iframe_node.appendChild(url_starturl_node)
		
		url_iframe_check_result=self.__create_new_node("TrojanDetectionResult")
		url_iframe_check_result.setAttribute(u'user_id',user_id)
		url_iframe_check_result.setAttribute(u'start_url',start_url)
		url_iframe_check_result.setAttribute(u'task_target_id',task_target_id)
		totalNumber='0'
		for src in iframe_src:
			url_src_node=self.__create_new_node("trojan_link",src[0])
			url_src_node.setAttribute(u'id',src[1])
			url_src_node.setAttribute(u'src',src[2])
			url_src_node.setAttribute(u'refered_url',src[3])
			url_src_node.setAttribute(u'trojan_type',src[4])
			totalNumber=src[1]
			url_iframe_check_result.appendChild(url_src_node)
			
		url_iframe_check_result.setAttribute('total_number',totalNumber)
		self.__second.appendChild(url_iframe_check_result)
		self.__root.appendChild(self.__second)

	def end_cov(self):
		try:
			f=open(self.__xml_path,'wb')
			lock(f,LOCK_EX)
			w=codecs.lookup('utf-8')[3](f)
			self.__dom.writexml(w,addindent='  ', newl='\n',encoding='utf-8')
			w.close()
		#	self.__dom.writexml(f)
			f.close()
			return True
		except Exception,err:
			traceback.print_exc()
			raise Exception,'failured'

if __name__ == '__main__':
	test=CreateXml('WebTrojanCheckResult1.xml')
	test.begin_cov()
	test.add_header_cov(
			task_id='1',
			task_type='1',
			module_type='1',
			check_time='2014-08-17'
		       )
	test.add_cov(
	#	iframe_src=[[],['2','2','www.gggwi.com','http://wwww.douban.com/explore','script']],
		iframe_src=[],
		start_url='www.douban.com',
		task_target_id='1',
		user_id='1'
	)
	test.end_cov()
	print 'endl'
		
