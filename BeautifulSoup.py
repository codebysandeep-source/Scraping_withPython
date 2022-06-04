from bs4 import BeautifulSoup  #Beautiful Soup is a Python library for pulling data out of HTML and XML files.

with open("index.html", "r") as san:  # where san is a variable and you can give any other variable
  content = san.read() # to read the file using read() method

  # without BeautifulSoup
  # print(content)

  # With BeautifulSoup
  soup = BeautifulSoup(content, "lxml") # combination of HTML and XML
  # print(soup.prettify())

  h2_tag = soup.find('h2') # to find a HTML tag using find() method.
  #print(h2_tag)

  p_tag = soup.find('p')
  #print(p_tag)

  #print(f'{h2_tag}  and  {p_tag}') # where f is a formate
  #print(f'{h2_tag.text}  and  {p_tag.text}') 

  h2_all_tag = soup.find_all('h2') # to find all HTML tags just by giving the HTML tag name like we are finding all <h2>...</h2> tags
  #print(h2_all_tag)  # all data are comes in list formate like [something, something, ..., ..., ...]

  # for i in h2_all_tag:
  #   print(i.text)

  # we can find tags by classname
  blue = soup.find_all("p", class_="blue")  # in HTMl we write class like this class="" but in this scenario we have to write class_="" because in python class is pre-defined keyword...
  # print(blue)
  # or 
  blue1 = soup.find_all(class_="blue")
  # print(blue1)


  div = soup.find_all(id="mydiv")
  #for j in div:                    
    #print(j.h3)                   # output ->  <h3>Hi, I am Header3 </h3>
    #print(j.h3.text)              # output ->  Hi, I am Header3
    #print(j.h3.text.split())      # output ->  ['Hi,', 'I', 'am', 'Header3']
    #print(j.h3.text.split()[3])   # output ->  Header3
    #print(j.h3.text.split()[1:3]) # output ->  ['I', 'am']



