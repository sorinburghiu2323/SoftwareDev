# SoftwareDev
ECM2434 Group D Project

## Setup

First set up you python virtual environment.

`python -m venv .venv`

and activate it

`.venv\Scripts\activate.bat` or `.venv/bin/activate`

Then install python dependencies:

```
pip install -r requirements.txt
```

Do your migrations (create your development database):

```
python manage.py migrate
```

Next install the VueJS frontend dependencies:


```shell script
cd frontend
npm install
```
  Note: When you pull changes that others have made, you may want to do `npm install` again to ensure any additional dependencies have been added.

Now to build the frontend, there are two ways:

Watches for any changes in the filetree and recompiles when detects a change
```
npm run watch
```

Compiles and minifies for production
```
npm run build
```
