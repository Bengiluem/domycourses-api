# DoMyCourses

This repository is a small web application to automate your grocery shopping. Basically, you provide the application a list of recipes (from website urls or manually) you want to do the following week, and the application computes your final grocery list.  
The application relies on a ReactNative front-end & a Django backend.

## Database

To test the database without running the server, you must
add this to your virtual environment :
```bash
DJANGO_SETTINGS_MODULE=domycourses_api.settings
export DJANGO_SETTINGS_MODULE
```

Then cd into domycourses_api & run :
```python
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from api.models import Recipe
...
```
