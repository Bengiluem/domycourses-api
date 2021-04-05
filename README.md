# domycourses-api
Api for DoMyCourses

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
