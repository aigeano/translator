import sys, requests, json

def main():
	
	text = raw_input('Enter text to be translated\n')

	lang = {'italian':'it','german':'de','russian':'ru','french':'fr','spanish':'es','swedish':'sv','dutch':'nl','greek':'el','hungarian':'hu','indonesian':'id'}
        

	url = "http://api.mymemory.translated.net/get?q="+text+"&langpair=en|"
	
        for key in lang.keys():

	  r = requests.get(url+lang.get(key))

          json_data = json.loads(r.text)
	  print "Translated text in",key," :" 
          print json_data['responseData']['translatedText']

if __name__=='__main__':
  main()
