from bs4 import BeautifulSoup
import requests    # The requests module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, ...
                   # HTTP requests are messages sent by the client to initiate an action on the server. Their start-line contain three elements: An HTTP method, a verb (like GET , PUT or POST ) or a noun (like HEAD or OPTIONS ), that describes the action to be performed.

content = requests.get("https://www.lipsum.com/").text
soup = BeautifulSoup(content, "lxml")

#print(soup.find('h2'))
#print(soup.find('h2').text)
#print(soup.find('h2').text.replace('Lorem Ipsum', 'python'))  # replace('old_data', 'new_data') 

#print(soup.find(class_='boxed').strong)       #ouput -> <strong>Translations:</strong>
#print(soup.find(class_='boxed').strong.text)  #output -> Translations:

#print(soup.find(id="Translation").h3)         #output -> <h3>The standard Lorem Ipsum passage, used since the 1500s</h3>
#print(soup.find(id="Translation").h3.text)    #output -> The standard Lorem Ipsum passage, used since the 1500s


tag = soup.find(id="Translation").h3
text = soup.find(id="Translation").h3.text

print(f'''
  h3 :  {tag}
  text : {text}
''')

