## Instagram
This project was generated using python version 3.6.and the Django framework. This is an instagram  clone. It allows a user to create an account, add images with captions and tags. Other users can view the images and search for images based on tags. They can also add comments and like.

## SETUP INSTRUCTIONS:

### Installation
1.Python 3.6.5
2.Django 1.11

### Cloning the repository

`git clone https://github.com/yontiii/Instagram.git && cd My-Gallery`

### Creating a virtual environment
`sudo apt-get install python3.6-venv`
`python3.6 -m venv --without-pip virtual`
`source virtual/bin/activate`

### Installing dependencies
`pip install -r requirements.txt`

### Running tests
`python3.6 manage.py test instapic` 

### Running the Development server
`python3.6 manage.py runserver`



## BEHAVIOUR DRIVEN DEVELOPMENT
| GENERAL BEHAVIOUR | INPUT | OUTPUT|
|:------------------|:--------|:-----------|
|User wants to search for a profile| They enter the profile name on the search bar |all relevant profiles are displayed|
|User wants to view the image descriptions|They click on the image |Image descriptions are displayed|
|User wants to upload an image| They navigate to the admin route and upload the image along with its caption,tag.|Image is uploaded|


## Further help
To get more help on the Python CLI use ng help or go check out the Python CLI README and Python documentation. You may also read the news API documentation on the news API website.

## CONTACT INFORMATION
For more information or clarification reach me through my email address : muasajohn01@gmail.com