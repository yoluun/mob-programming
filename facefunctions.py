#fbapi
from fbkey import *
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json, sys, ast

def detectFaces(img_url):
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
	body = {'url': img_url}

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
	return 0

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

def applyFace(personGroupId, personId, image):
	return 0

def verifyFace(image, personGroupId=None, personId=None):
	return 0
