#fbapi
from fbkey import *
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json, sys, ast

def detectFaces(imageUrl):
	# Request headers.
	headers = {
		'Content-Type': 'application/json',
		'Ocp-Apim-Subscription-Key': subscription_key,
	}

	# Request parameters.
	params = {
		'returnFaceId': 'true',
		'returnFaceLandmarks': 'false',
		'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
	}

	# Body. The URL of a JPEG image to analyze.
	body = {'url': imageUrl}

	try:
		# Execute the REST API call and get the response.
		response = requests.request('POST', uri_base + '/face/v1.0/detect', json=body, data=None, headers=headers, params=params)

		parsed = json.loads(response.text)

	except Exception as e:
		print('Error:')
		print(e)
		return None

	return parsed

def createPersonGroup(personGroupId, name, userData=None):
	# Replace 'examplegroupid' with an ID you haven't used for creating a group before.
	# The valid characters for the ID include numbers, English letters in lower case, '-' and '_'. 
	# The maximum length of the ID is 64.
	#personGroupId = 'georgesung'

	# The userData field is optional. The size limit for it is 16KB.
	#body = "{ 'name':'GeorgeTan', 'userData':'abcdefg' }"
	body = "{'name':'" + name +"', 'userData':'" + userData + "'}"

	try:
	    # NOTE: You must use the same location in your REST call as you used to obtain your subscription keys.
	    #   For example, if you obtained your subscription keys from westus, replace "westcentralus" in the 
	    #   URL below with "westus".
	    conn = http.client.HTTPSConnection(uri_base.strip('https://'))
	    conn.request("PUT", "/face/v1.0/persongroups/%s" % personGroupId, body, headers)
	    response = conn.getresponse()

	    # 'OK' indicates success. 'Conflict' means a group with this ID already exists.
	    # If you get 'Conflict', change the value of personGroupId above and try again.
	    # If you get 'Access Denied', verify the validity of the subscription key above and try again.
	    return response.reason

	    conn.close()
	except Exception as e:
	    return(e.args)

def createPerson(personGroupId, name, userData=None):
	params = urllib.parse.urlencode({'personGroupId': personGroupId})
	body = "{'name': 'George Sung', 'userData': 'hello world'}"
	if userData is None:
		body = "{'name': '%s'}" % (name,)
	else:
		body = "{'name': '%s', 'userData': '%s'}" % (name, userData)

	try:
		conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
		conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons?%s" % params, body, headers)
		response = conn.getresponse()
		data = str(response.read())[2:-1]
		conn.close()
	except Exception as e:
		print("[Errno {0}] {1}".format(e.errno, e.strerror))
		return None

	data = ast.literal_eval(data)
	return data['personId']

def applyFace(personGroupId, personId, imageUrl):
	#PUT FACE ONTO PERSON
	params = urllib.parse.urlencode({'personGroupId':personGroupId, 'personId':personId})

	body = '{"url":"%s"}' % imageUrl
	try:
		conn = http.client.HTTPSConnection(uri_base.strip('https://'))
		conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons/{personId}/persistedFaces?%s" % params, body, headers)
		response = conn.getresponse()
		data = response.read()
		conn.close()
	except Exception as e:
		print("[Errno {0}] {1}".format(e.errno, e.strerror))
		return None

	return data

def verifyFaceId(faceId, personGroupId=None, personId=None):
	params = urllib.parse.urlencode({ })
	body = "{'faceId':'%s', 'personGroupId':'%s', 'personId':'%s'}" % (faceId, personGroupId, personId)
	try:
		conn = http.client.HTTPSConnection(uri_base.strip('https://'))
		conn.request("POST", "/face/v1.0/verify?%s" % params, body, headers)
		response = conn.getresponse()
		data = response.read()
		conn.close()
	except Exception as e:
		print("[Errno {0}] {1}".format(e.errno, e.strerror))
		return None

	return data

def verifyFaceImage(imageUrl, personGroupId=None, personId=None):
	parsed = detectFaces(imageUrl)
	if 'error' in parsed:
		print('Error with detectFaces()')
		print(parsed)
		return None

	faceId = parsed['faceId']
	data = verifyFaceId(faceId, personGroupId, personId)

	return data
