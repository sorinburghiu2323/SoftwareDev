## Backend guide

Make your migrations whenever necessary with:

```
python manage.py makemigrations
```

### Standards
- Upon endpoint creation, document it in the API.yaml file.
- Use proper python coding conventions and document your code. (e.g: each method should have a docstring)
- Create your utility modules to be used throughout the code in /Utils.
- Create your endpoint controllers in /Controllers.
- Do not make your python files too big - start breaking it down if a module becomes overwhelming.
