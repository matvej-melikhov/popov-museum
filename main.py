from app import application
from app.routes import *

application.run(host="0.0.0.0", port=5000, debug=True)