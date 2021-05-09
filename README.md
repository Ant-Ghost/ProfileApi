# Mini-Blog


## Set Up

  Vagrant is app to create a vm box.

  ubuntu.. is my vm box.

  Vagrantfile (ruby file) is the settings needed to create the box.



## Django (python)

  ### Requirements:-
  
    1. 'python3'
    2. 'pip'
    3. 'django'
    4. 'djangorestframework'


## Basic Django Terminology

  Models :
    
    Django has object-relational database. Models are blueprint of your database.
    Object (instance of Model class) is used to create the database.
    
  Views :

	Accepts a request and returns a response.

	Remember: the include() strips the previous contents of the url and send the rest.
				if the rest is nothing , denote it by  - '' .

			: the trailing '/' is recommended as this let chopping after the '/' and decrease
			  the confusion of writing the succeeding urls.

	render(request, 'path/', 'data'): 

		This function renders a html file. The path name is starts from '<app_name>/templates' and seperated by '/'.
		'data' is optional and it is a list {'name': value} or json.
    
    
  Serializers :

	  Similar to form. It has a python code which acts on the given model and convert to frontend friendly data.
	  Helps in serializing data and data transfer.


#### Inspired by : https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
