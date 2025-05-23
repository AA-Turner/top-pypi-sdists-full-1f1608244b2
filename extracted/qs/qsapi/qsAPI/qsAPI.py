# -*- coding: UTF-8 -*-

'''
@author:     Rafael Sanz
@contact:    rafael.sanz@selab.es
@Copyright 2016 <Rafael Sanz - (R)SELAB>

This software is MIT licensed (see terms below)

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy,
    modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
    LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR 
    IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import sys, os.path
from distutils.version import LooseVersion as Version
import requests as req
import urllib.parse as up
import random, string, json, uuid, re
import logging

__version__ = "1.16"
__updated__ = '20/01/2019'



class _Controller(object):
    """ Handler REST-API QRS"""
       
    _referer='Mozilla/5.0 (Windows NT 6.3; Win64; x64) qsAPI APIREST (QSense)'
    
    try:
        from requests_ntlm import HttpNtlmAuth as _ntlm
    except ImportError:
        _ntlm=None  
    
    def __init__(self, schema, proxy, port, vproxy, certificate, verify, user, verbosity, logName):
        ''' 
            @Function setup: Setup the connection and initialize handlers
            @param schema: http/https
            @param proxy: hostname to connect
            @param port: port number
            @param vproxy: virtual proxy conf. {preffix:'proxy', path: '^/qrs/', template:'/{}/qrs/'})
            @param certificate: path to .pem client certificate
            @param verify: false to trust in self-signed certificates
            @param user: dict with keys {userDirectory:, userID:, password:} or tuple
            @param verbosity: debug level
            @param logger: logger instance name
        '''
        self.proxy    = proxy
        self.port     = str(port)
        self.proxy    = proxy;
        self.vproxy   = None;
        self.baseurl  = None
        self.request  = None
        self.response = None
        self.session  = None
        
        if vproxy:
            self.setVProxy(**vproxy)
        
        self.setUser(**user) if isinstance(user, dict) else self.setUser(*user)
          
        self.chunk_size = 512 #Kb
        
        self.log=logging.getLogger(logName)
        if not self.log.hasHandlers():
            self.log.addHandler(logging.StreamHandler(sys.stdout))
        self.log.setLevel(verbosity)
        
        self.baseurl= '{schema}://{host}:{port}'.format(schema=schema, host=proxy, port=str(port))
        
        if isinstance(certificate, str):
            (base,ext)=os.path.splitext(certificate)
            self.cafile=(base+ext, base+'_key'+ext)
            self.log.debug('CERTKEY: %s%s', base, ext)
        elif isinstance(certificate, tuple):
            self.cafile=certificate
            self.log.debug('CERT: %s',certificate)
        else:
            self.cafile=False
            
        self._verify=bool(verify)
        
        if not self._verify:
            req.packages.urllib3.disable_warnings()
        
        self.session=req.Session()
        
        if self._ntlm and not self.cafile:
            self.log.debug('NTLM authentication enabled')
            self.session.auth = self._ntlm('{domain}\\{user}'.format(domain=self.UserDirectory, user=self.UserId), self.Password)
        
        
    def setVProxy(self, preffix, path, template):
        self.vproxy={}
        self.vproxy['preffix'] =preffix               # proxy
        self.vproxy['path']    =re.compile(path)      # ^/qrs/
        self.vproxy['template']=template              # /{}/qrs/
        self.vproxy['pxpath']  =template.format(preffix)    
 
        
    def setUser(self, userDirectory, userID, password=None):
        self.UserDirectory=userDirectory
        self.UserId = userID
        self.Password=password
            
    
    @staticmethod
    def normalize(schema, proxy, port, certificate):
        
        if '://' in proxy:
            schema, proxy = proxy.split('://')
        if not certificate and isinstance(port, int):
            port=443
        if ':' in proxy:
            proxy, port = proxy.split(':')
        
        return(schema, proxy, port)
    
        
    def _params_prepare(self, param, xhd={}):
                
        par=dict({'Xrfkey': ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))})
        if isinstance(param, dict):
            for p,v in param.items():
                if v is not None:
                    if isinstance(v, bool):
                        par[p]=str(v).lower()
                    else:
                        par[p]=str(v)
                    self.log.debug(" >> %s=>%s",p , par[p])
                else:
                    self.log.debug(" >> %s=>(default)", p)
            
        hd= { 'User-agent': self._referer,
              'Pragma': 'no-cache',
              'X-Qlik-User': 'UserDirectory={directory}; UserId={user}'.format(directory=self.UserDirectory, user=self.UserId),
              'x-Qlik-Xrfkey': par.get('Xrfkey'),
              'Accept': 'application/json',
              'Content-Type': 'application/json'}
        
        if self.vproxy:
            hd['X-Qlik-Virtual-Proxy-Prefix']=self.vproxy['preffix']
                
        hd.update(xhd)
        return(par, hd)  
    
    
    
    def _params_update(self, url, par):
        scheme, netloc, path, query, fragment=up.urlsplit(url)
        if self.vproxy:
            path= self.vproxy['path'].sub(self.vproxy['pxpath'], path)
        p=up.parse_qs(query)
        p.update(par)
        query=up.urlencode(p,doseq=True,quote_via=up.quote)
        return up.urlunsplit((scheme, netloc, path, query, fragment))
        
        
    
       
    def call(self, method, apipath, param=None, data=None, files=None):
        """ initialize control structure """
               
        if str(method).upper() not in ('GET', 'POST', 'PUT', 'DELETE'):
            raise ValueError('invalid method <{0}>'.format(method))
       
        self.log.info('API %s <%s>', method[:3], apipath)
        
        (par,hd)=self._params_prepare(param, {} if files is None else {'Content-Type': 'application/vnd.qlik.sense.app'})
        
        # Build the request        
        self.response= None
            
        url=self._params_update(up.urljoin(self.baseurl,apipath), par)
        self.request=req.Request(method, url, headers=hd, data=data, files=files, auth=self.session.auth)
        pr=self.session.prepare_request(self.request)
                
        self.log.debug('SEND: %s', self.request.url)
                
        # Execute the HTTP request
        self.response = self.session.send(pr, cert=self.cafile, verify=self._verify, allow_redirects=False)
        rc=0
        while self.response.is_redirect:
            rc+=1
            if rc > self.session.max_redirects:
                raise req.HTTPError('Too many redirections')
            self.session.rebuild_auth(self.response.next, self.response)
            self.response.next.prepare_headers(hd)
            self.response.next.prepare_cookies(self.response.cookies)
            self.response.next.url=self._params_update(self.response.next.url, par)
            self.log.debug('REDIR: %s', self.response.next.url)
            self.response = self.session.send(self.response.next, verify=self._verify, allow_redirects=False)
            
        self.log.debug('RECV: %s',self.response.text)
        self.response.raise_for_status()
        
        return(self.response)



    def download(self, apipath, filename, param=None):
        """ initialize control structure """
                   
        self.log.info('API DOWN <%s>', apipath)

        (par,hd)=self._params_prepare(param)
        
        # Build the request        
        self.response= None
        
        url=self._params_update(up.urljoin(self.baseurl,apipath), par)
     
        self.log.debug('__SEND: %s',url)
                
        # Execute the HTTP request 
        self.request = self.session.get(url, headers=hd, cert=self.cafile, verify=self._verify, stream=True, auth=self.session.auth)
            
        with open(filename, 'wb') as f:
            self.log.info('__Downloading (in %sKb blocks): ', str(self.chunk_size))
            
            #download in 512Kb blocks
            for chunk in self.request.iter_content(chunk_size=self.chunk_size << 10): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                        
            self.log.info('__Saved: %s', os.path.abspath(filename))
        
        return(self.request)

    
    
    def upload(self, apipath, filename, param=None):
        """ initialize control structure """
        
        class upload_in_chunks(object):
            def __init__(self, filename, chunksize=512):
                self.filename = filename
                self.chunksize = chunksize << 10
                self.totalsize = os.path.getsize(filename)
                self.readsofar = 0
        
            def __iter__(self):
                with open(self.filename, 'rb') as file:
                    while True:
                        data = file.read(self.chunksize)
                        if not data:
                            break
                        self.readsofar += len(data)
                        yield data
        
            def __len__(self):
                return self.totalsize
                       
        self.log.info('API UPLO <%s>', apipath)

        (par,hd)=self._params_prepare(param, {'Content-Type': 'application/vnd.qlik.sense.app'})
           
        # Build the request        
        self.response= None
        url=self._params_update(up.urljoin(self.baseurl,apipath), par)
        self.log.debug('__SEND: %s', url)

        # Execute the HTTP request 
        self.log.info('__Uploading {:,} bytes'.format(os.path.getsize(filename)))
        self.request = self.session.post(url, headers=hd, cert=self.cafile, verify=self._verify, \
                                data=upload_in_chunks(filename, self.chunk_size), auth=self.session.auth)
            
        self.log.info('__Done.')                
            
        return(self.request)


    
    
    def get(self, apipath, param=None):
        '''
        @Function get: generic purpose call
        @param apipath: uri REST path
        @param param : whatever other param needed in form a dict
                      (example: {'filter': "name eq 'myApp'} )
        '''
        return self.call('GET', apipath, param)
    
    
    
    def post(self, apipath, param=None, data=None, files=None):
        '''
        @Function post: generic purpose call
        @param apipath: uri REST path
        @param param : whatever other param needed in form a dict
                      (example: {'filter': "name eq 'myApp'} )
        @param data : stream data input (native dict/list structures are json formated)
        @param files : metafile input 
        '''
        if isinstance(data,dict) or isinstance(data,list):
            data=json.dumps(data)
        return self.call('POST', apipath, param, data, files)
    
    
    
    def put(self, apipath, param=None, data=None):
        '''
        @Function put: generic purpose call
        @param apipath: uri REST path
        @param param : whatever other param needed in form a dict
                      (example: {'filter': "name eq 'myApp'} )
        @param data : stream data input (native dict/list structures are json formated)
        '''
        if isinstance(data,dict) or isinstance(data,list):
            data=json.dumps(data)
        return self.call('PUT', apipath, param, data)
    
    
    
    def delete(self, apipath, param=None):
        '''
        @Function delete: generic purpose call
        @param apipath: uri REST path
        @param param : whatever other param needed in form a dict
                      (example: {'filter': "name eq 'myApp'} )
        '''
        return self.call('DELETE', apipath, param)

    
    

class QPS(object):
    '''Qlik Sense Proxy Service REST API'''
    
    VERSION_API= Version(__version__)
    
    def __init__(self, schema='https', proxy='localhost', port=4243, vproxy=None, certificate=None, verify=False, \
                 user={'userDirectory':'internal', 'userID':'sa_repository', 'password': None}, \
                 verbosity='INFO', logger='qsapi'):  
        
        schema, proxy, port=_Controller.normalize(schema, proxy, port, certificate) 
        p_vproxy={'preffix': vproxy, 'path': '^/qps/', 'template':'/{}/qps/'} if vproxy else None
        
        self.driver=_Controller(schema, proxy, port, p_vproxy, certificate, verify, user, verbosity, logger)

        

    def GetUser(self, directory, user):
        '''
        @Function: This returns all proxy sessions that a user (identified by {directory} and {user}) has.
        '''
        apipath='/qps/user/{directory}/{id}'.format(directory=directory, id=user)
        return self.driver.get(apipath)

    
    
    def DeleteUser(self, directory, user):
        '''
        @Function: This is part of the Logout API. The directory and ID are the same UserDirectory and UserId as those that were sent in POST /qps/{virtual proxy/}ticket.
                    A list of all proxy sessions that were connected to the deleted user is returned. 
        '''
        apipath='/qps/user/{directory}/{id}'.format(directory=directory, id=user)
        return self.driver.delete(apipath)
    

    
    def GetSession(self, pId):
        '''
        @Function: This returns the proxy session identified by {id}.
        '''
        apipath='/qps/session/{id}'.format(id=pId)
        return self.driver.get(apipath)
    
    
    def DeleteSession(self, pId):
        '''
        @Function: Delete the proxy session identified by {id}.
        '''
        apipath='/qps/session/{id}'.format(virtual_proxy=self.driver.preffix, id=pId)
        return self.driver.delete(apipath)




class QRS(object):
    '''Qlik Sense Repository Service REST API'''
    
    VERSION_API= Version(__version__)
    
    
    def __init__(self, schema='https', proxy='localhost', port=4242, vproxy=None, certificate=None, verify=False, \
                 user={'userDirectory':'internal', 'userID':'sa_repository', 'password': None}, \
                 verbosity='INFO', logger='qsapi'):
        
        schema, proxy, port=_Controller.normalize(schema, proxy, port, certificate)
        p_vproxy={'preffix': vproxy, 'path': '^/qrs/', 'template':'/{}/qrs/'} if vproxy else None
            
        self.driver=_Controller(schema, proxy, port, p_vproxy, certificate, verify, user, verbosity, logger)
        
        self.VERSION_SERVER=self.getServerVersion()
        if self.VERSION_API > self.VERSION_SERVER:
            raise Exception('<server version mismatch, API:{0} > Server:{1}'.format(self.VERSION_API, self.VERSION_SERVER))
        else:
            self.driver.log.info('Server version: {0}'.format(self.VERSION_SERVER))


    
    def _toDict(self, response, uid='full', key='name', attr='id'):
        r={}
        if response.ok:
            j=response.json()
            if uid != "full":
                if isinstance(attr, str):
                    r[j.get(key)]=j.get(attr)
                elif isinstance(attr, list):
                    ra={}
                    for a in attr:
                        ra[a]=(j.get(a))
                    r[j.get(key)]=ra
                else:
                    raise TypeError('attr argument must be a str or list')
            else:               
                for x in j:
                    if isinstance(attr, str):
                        r[x.get(key)]=x.get(attr)
                    elif isinstance(attr, list):
                        ra={}
                        for a in attr:
                            ra[a]=(x.get(a))
                        r[x.get(key)]=ra
                    else:
                        raise TypeError('attr argument must be a str or list')
        
        return(r)
    

        
    def getServerVersion(self):
        '''
        @Function: retrieve the server version
        '''
        return Version(self.driver.get('/qrs/about').json().get('buildVersion'))

 
 
    
    def getAbout(self):
        '''
        @Function: Get information on the Qlik Sense repository, including version, database provider, and whether the node is the central node of the site or not.
        '''
        return self.driver.get('/qrs/about').json()
    
 
    
    def count(self, pType, pFilter=None):
        '''
        @Function: generic purpose call
        @param pType: entity to count
        @param pFilter: filter the entities before calculating the number of entities. 
        @return : integer from json response
        '''
        return self.driver.get('/qrs/{0}/count'.format(pType), param={'filter':pFilter}).json()['value']
 
    
    
    def getDescription(self, extended='False', method=None, outformat='JSON'):
        '''@Function : List all paths available in the Qlik Sense Repository Service (QRS) API. Optionally, return extended information, endpoints that use a specific HTTP verb, or the return values in JSON format.
           @param extended: If true, returns the following:
                The type (if any) that needs to be included in the body.
                The type of return value (if any).
                If the endpoint is automatically generated or not.
           @param method:  If set to an HTTP verb (GET, PUT, POST, or DELETE), only endpoints that use the verb are returned.
           @param outformat:  If set to "JSON", the return value is given in JSON format. 
        '''
            
        param={'extended': extended in ('True', 'true', True),
               'method'  : method,
               'format'  : outformat}
        
        return self.driver.get('/qrs/about/api/description', param).json()



    def getEnum(self):
        '''@Function: Get all enums that are used by the public part of the Qlik Sense Repository Service (QRS) API.
        '''
        return self.driver.get('/qrs/about/api/enums').json()



    #=========================================================================================

    
    
    def AppDictAttributes(self, puid='full', pFilter=None, key='name', attr='id'):
        '''@Function: retrieve a mapping of apps attributes
           @param pId: limmit the scope to the App {UUID}
           @param pFilter: filter the entities before calculating the number of entities.
           @param key: the attribute to be the key
           @param attr: the attribute value to retrieve (single value or list)
           @return: dict(key:attr)
        '''
        apipath='/qrs/app/{puid}'.format(puid=puid)
        return self._toDict(self.driver.get(apipath, param={'filter':pFilter}), puid, key, attr)    
        
    

    def AppCopy(self, pId, name=None):
        '''
        @Function: Copy an existing app, identified by {id}. Optionally, provide a name for the copy.
        @param pId: app identifier
        @param name: Name of the app
        '''
        param={'name':name}
        return self.driver.post('/qrs/app/{id}/copy'.format(id=pId), param).json()


    
    def AppExport(self, pId, filename=None, skipData=False):
        '''
        @Function: Get an export qvf for an existing app, identified by {id}.
        @param pId: app GUI
        @param filename: target path filename
        @param skipData: if True App will be emptied of data
        @return : stored application
        '''
        file= filename if filename else pId+'.qvf'
        if self.VERSION_SERVER < "17.0":
            #DEPRECATED API since November-2017
            self.driver.log.info('Server version: %s, using legacy API', self.VERSION_SERVER)
            r=self.driver.get('/qrs/app/{id}/export'.format(id=pId))
            if r.ok:
                r=self.driver.download('/qrs/download/app/{appId}/{TicketId}/{fileName}'.format(appId=pId, TicketId=r.json()['value'], fileName=file), file)
            return(r)
        
        #Current API method
        param={'skipData':skipData}
        r=self.driver.post('/qrs/app/{id}/export/{token}'.format(id=pId, token=uuid.uuid4()), param)
        if r.ok:
            r=self.driver.download(r.json()['downloadPath'], file)
        return(r)




    def AppUpload(self, filename, pName, keepdata=None):
        '''
        @Function: Upload a filename.qvf into Central Node.
        @param filename: target path filename
        @param name: target app name
        @param keepdata: Exclude the app data when uploading the app (when it is implemented)
        '''
        param ={'name'    :pName,
                'keepdata':keepdata}
        return self.driver.upload('/qrs/app/upload', filename, param)

    
    def AppGet(self, pId='full', pFilter=None):
        '''
        @Function: retrieve App information
        @param pId: App UUID 
        @param pFilter: filter the entities before calculating the number of entities. 
        @return : json response
        '''
        return self.driver.get('/qrs/app/{id}'.format(id=pId), param={'filter':pFilter}).json()
    
    
    
    def AppMigrate(self, pId):
        '''
        @Function: Migrate an app so that it can be used in the currently installed version of Qlik Sense.
                    Normally, this is done automatically
        @param pId: app identifier
        '''
        return self.driver.put('/qrs/app/{id}/migrate'.format(id=pId))
    
            
    
    def AppReload(self, pId):
        '''
        @Function: Reload an app
        @param pId: app identifier
        '''
        return self.driver.post('/qrs/app/{id}/reload'.format(id=pId))


    def AppPublish(self, pId, streamId, name=None):
        '''
        @Function: Publish an existing app, identified by {id}, to the stream identified by {streamid}.
        @param pId: app identifier
        @param streamId: stream identifier
        @param name: optional alternate name
        '''
        param ={'stream' :streamId,
                'name'   :name}
        return self.driver.put('/qrs/app/{id}/publish'.format(id=pId), param)
    
    
    def AppUpdate(self, pId, pData):
        '''
        @Function: update App info referenced 
        @param pId: App UUID 
        '''
        return self.driver.put('/qrs/app/{id}'.format(id=pId), data=pData)
    
    
    def AppReplace(self, pId, pAppId):
        '''
        @Function: Replace an app, identified by {appid}, with the app identified by {id}. 
        @param pId: source App UUID 
        @param pAppId: target App UUID

        If the replaced app is published, only the sheets that were originally published with the app are replaced.
        If the replaced app is not published, the entire app is replaced.
        '''
        param ={'app' :pAppId}
        return self.driver.put('/qrs/app/{id}/replace'.format(id=pId), param)
    
    
    def AppDelete(self, pId):
        '''
        @Function: delete App referenced 
        @param pId: App UUID 
        '''
        return self.driver.delete('/qrs/app/{id}'.format(id=pId))
    
    
    #=========================================================================================
    
    
    def AppObjectGet(self, pId='full', pFilter=None):
        '''
        @Function: retrieve AppObject information
        @param pId: AppObject UUID 
        @param pFilter: filter the entities before calculating the number of entities. 
        @return : json response
        '''
        return self.driver.get('/qrs/app/object/{id}'.format(id=pId), param={'filter':pFilter}).json()
    
    
    def AppObjectCount(self, pFilter=None):
        '''
        @Function: retrieve AppObject count information
        @param pFilter: filter the entities before calculating the number of entities. 
        @return : json response
        '''
        return self.driver.get('/qrs/app/object/count', param={'filter':pFilter}).json()
    
    
    def AppObjectUpdate(self, pId, pData):
        '''
        @Function: retrieve AppObject information
        @param pId: AppObject UUID  
        @param pData: AppObject attributes
        '''
        return self.driver.put('/qrs/app/object/{id}'.format(id=pId), data=pData)
    
    
    def AppObjectApprove(self, pId, pApprove=True):
        '''
        @Function: Set AppObject approve status
        @param pId: AppObject UUID  
        @param pApprove: True / False
        '''
        return self.driver.post('/qrs/app/object/{id}/{status}'.format(id=pId, status='approve' if pApprove else 'unapprove'))
    
    
    def AppObjectPublish(self, pId, pPublish=True):
        '''
        @Function: Set AppObject publish status
        @param pId: AppObject UUID  
        @param pPublish: True / False
        '''
        return self.driver.put('/qrs/app/object/{id}/{status}'.format(id=pId, status='publish' if pPublish else 'unpublish'))
    
    
    def AppObjectDelete(self, pId):
        '''
        @Function: Delete AppObject
        @param pId: AppObject UUID  
        '''
        return self.driver.delete('/qrs/app/object/{id}'.format(id=pId))
    
        
    #=========================================================================================
    
    
    def StreamCreate(self, pName, pProperties=[] , pTags=[], pUUID=None):
        '''
        @Function: create a Stream
        @param pName: Stream Name 
        @param pUID: Stream UUID
        @param pProperties: list of dict with properties definitions.
        @param pTags: list of dict with tag definitions 
        @return : json response
        '''
        param={'name': pName,
               'customProperties': pProperties,
               'tags': pTags}
        
        if pUUID is not None:
            param['id']=pUUID
                 
        return self.driver.post('/qrs/stream', data=param).json()
    
    
    
    def StreamGet(self, pId='full', pFilter=None):
        '''
        @Function: retrieve Stream information
        @param pId: Stream UUID 
        @param pFilter: filter the entities before calculating the number of entities. 
        @return : json response
        '''
        return self.driver.get('/qrs/stream/{id}'.format(id=pId), param={'filter':pFilter}).json()
    
    
    
    def StreamUpdate(self, pId, pData):
        '''
        @Function: update Stream info referenced 
        @param pId: Stream UUID 
        @param pData: stream attributes
        '''
        return self.driver.put('/qrs/stream/{id}'.format(id=pId), data=pData)
    
    
    
    def StreamDelete(self, pId):
        '''
        @Function: delete Stream referenced 
        @param pId: Stream UUID 
        @return : json response
        '''
        return self.driver.delete('/qrs/stream/{id}'.format(id=pId))
    
    
    
    def StreamDictAttributes(self, pStreamID='full', pFilter=None, key='name', attr='id'):
        '''@Function: retrieve a mapping of Stream attributes
           @param pStreamID: limmit the scope to the Stream {UID}
		   @param pFilter: filter the entities before calculating the number of entities.
           @param key: the attribute to be the key
           @param attr: the attribute value to retrieve (single value or list)
           @return: dict(key:attr)
        '''
        apipath='/qrs/stream/{uid}'.format(uid=pStreamID)            
        return self._toDict(self.driver.get(apipath, param={'filter':pFilter}), pStreamID, key, attr) 
    
    
    #=========================================================================================     
    
    
    def UserGet(self, pUserID='full', pFilter=None):
        '''
        @Function: retrieve user information
        @param pUserID: User id 
        @param pFilter: filter the entities before calculating the number of entities. 
        @return : json response
        '''
        return self.driver.get('/qrs/user/{id}'.format(id=pUserID), param={'filter':pFilter}).json()
    
    
    def UserUpdate(self, pUserID, pData):
        '''
        @Function: update user information
        @param pUserID: User id 
        @param pData: json with user information. 
        @return : json response
        '''
        return self.driver.put('/qrs/user/{id}'.format(id=pUserID), data=pData)
    
    
    def UserDelete(self, pUserID):
        '''
        @Function: retrieve user information
        @param pUserID: User id 
        @param pFilter: filter the entities before calculating the number of entities. 
        @return : json response
        '''
        return self.driver.delete('/qrs/user/{id}'.format(id=pUserID))
    
    
    def UserDictAttributes(self, pUserID='full', pFilter=None, key='name', attr='id'):
        '''@Function: retrieve a mapping of user attributes
           @param pUserID: limmit the scope to the User {UID}
		   @param pFilter: filter the entities before calculating the number of entities.
           @param key: the attribute to be the key
           @param attr: the attribute value to retrieve (single value or list)
           @return: dict(key:attr)
        '''
        apipath='/qrs/user/{uid}'.format(uid=pUserID)            
        return self._toDict(self.driver.get(apipath, param={'filter':pFilter}),pUserID,key,attr)
    
    
    #=========================================================================================
    
    def SystemRulesCreate(self, param):
        '''
        @Function: create a SystemRule
        @return : json response
        ''' 
        return self.driver.post('/qrs/systemrule', data=param).json()
    
   
    def SystemRulesGet(self, pFilter=None):
        '''
        @Function: Get the system rules
        '''
        return self.driver.get('/qrs/systemrule/full', {'filter':pFilter}).json()
   
   
    
    def SystemRulesDictAttributes(self, pRuleID='full', pFilter=None, key='name', attr='id'):
        '''@Function: retrieve a mapping of rules attributes
           @param pRuleID: limmit the scope to the Rule {UID}
		   @param pFilter: filter the entities before calculating the number of entities.
           @param key: the attribute to be the key
           @param attr: the attribute value to retrieve (single value or list)
           @return: dict(key:attr)
        '''
        apipath='/qrs/systemrule/{uid}'.format(uid=pRuleID)            
        return self._toDict(self.driver.get(apipath, param={'filter':pFilter}),pRuleID,key,attr)
    
    
    #=========================================================================================
    
    
    
    def ReloadTaskGet(self, pId='full', pFilter=None):
        '''
        @Function: retrieve ReloadTask information
        @param pId: ReloadTask UID 
        @param pFilter: filter the entities before calculating the number of entities. 
        @return : json response
        '''
        return self.driver.get('/qrs/reloadtask/{id}'.format(id=pId), param={'filter':pFilter}).json()
    
    
    
    #=========================================================================================
     
    
    def PropertiesGet(self, pFilter=None):
        '''
        @Function: Get the system rules
        '''
        return self.driver.get('/qrs/custompropertydefinition/full', {'filter':pFilter}).json()


    #=========================================================================================
    
    
    def TagsDictAttributes(self, pTagID='full', pFilter=None, key='name', attr='id'):
        '''@Function: retrieve a mapping of tags attributes
           @param pRuleID: limmit the scope to the Tag {UID}
		   @param pFilter: filter the entities before calculating the number of entities.
           @param key: the attribute to be the key
           @param attr: the attribute value to retrieve (single value or list)
           @return: dict(key:attr)
        '''
        apipath='/qrs/tag/{uid}'.format(uid=pTagID)            
        return self._toDict(self.driver.get(apipath, param={'filter':pFilter}),pTagID,key,attr)

    
    #=========================================================================================
    
    
    class LicenseType:
        UserAccess='useraccesstype'
        LoginAccess='loginaccesstype'
        ProfessionalAccess='professionalaccesstype'
        AnalyzerAccess='analyzeraccesstype'
    
    
    def LicenseUsageSummary(self):
        '''
        @Function: Get the license summary
        '''
        return self.driver.get('qrs/license/accesstypeinfo').json()
    
    
    def LicenseAccessGet(self, licenseType):
        '''
        @Function: Get a user access licenses
        @param licenseType: LicenseType***Access enumeration
        '''
        return self.driver.get('qrs/license/{}/full'.format(licenseType)).json()
    
    
    def LicenseAccessDelete(self, licenseType, pLicID):
        '''
        @Function: Delete a user access license
        @param licenseType: LicenseType***Access enumeration
        @param pLicID: key of license
        '''
        return self.driver.delete('qrs/license/{}/{}'.format(licenseType, pLicID))
    
    
    def LicenseAccessCount(self, licenseType):
        '''
        @Function: Retrieve the number of assigned access license
        @param licenseType: LicenseType***Access enumeration
        @param pLicID: key of licens
        '''
        return self.driver.get('/qrs/license/{}/count'.format(licenseType)).json()['value']


    #=========================================================================================
    

if __name__ == "__main__":
    '''
    Alternative command line invocation, examples:
        python qsAPI.py -s myServer -c dir/client.pem -Q QRS AppDictAttributes
        python qsAPI.py -s myServer -c dir/client.pem -Q QRS -v INFO AppExport d8b120d7-a6e4-42ff-90b2-2ac6a3d92233 
        python qsAPI.py -s myServer -c dir/client.pem -Q QRS -v INFO AppReload d8b120d7-a6e4-42ff-90b2-2ac6a3d92233
        
    '''
    from argparse import ArgumentParser
    import inspect
    from pprint import pprint
    
    parser = ArgumentParser(description='qsAPI for QlikSense')
    parser.add_argument('-s', dest='server', required=True, help='server hostname | hostname:port | https://hostname:port')
    parser.add_argument('-u', dest='user', required=False, default='internal\\sa_repository', help='user in domain\\userid format.')
    parser.add_argument('-p', dest='password', required=False, default=None, help='password credential (NTLM)')
    parser.add_argument('-c', dest='certificate', required=False, help='path to client.pem certificate.')
    parser.add_argument('-P', dest='vproxy', required=False, help='virtual proxy preffix if needed.')
    parser.add_argument("-Q", dest="api", choices=['QPS','QRS'], default='QRS', required=True, help="service API")
    parser.add_argument("-v", dest="verbose", choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'], default='INFO', help="set verbosity level")
    parser.add_argument('--version', action='version', version='tools {}'.format(__version__))
    parser.add_argument(dest='method', nargs='+', help='API method to call and arguments')
    
    # Process arguments
    args = parser.parse_args()
    Q=QPS if args.api == 'QPS' else QRS

    if not (bool(args.password) != bool(args.certificate)):
        print('ERROR: One and only one authentication method must be provided (password or certificate)')
        sys.exit(-1)
        
    user=args.user.replace('\\\\','\\').split('\\')
    user.append(args.password)
    qr=Q(proxy=args.server, vproxy=args.vproxy, certificate=args.certificate, user=user, verbosity=args.verbose)
    m=[x for x,y in inspect.getmembers(Q) if not x.startswith('_') ]
    
    cmd=args.method[0]
    if cmd not in m:
        print('ERROR: "{}" is not a method of {}, expected=> {}'.format(cmd, args.api, m))
        sys.exit(-1)
    
    pprint(getattr(qr, cmd)(*args.method[1:]))
    sys.exit(0)

    
