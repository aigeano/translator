import sys, requests, json

def main():
	
	text = raw_input('Enter text to be translated\n')
	url = "http://api.mymemory.translated.net/get?q="+text+"&langpair=en|it"
	
	
	r = requests.get(url)

        json_data = json.loads(r.text)
	print "Translated text in Italian :"
        print json_data['responseData']['translatedText']

if __name__=='__main__':
  main()
