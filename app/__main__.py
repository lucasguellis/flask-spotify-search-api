from app import logger
from datetime import datetime

from app import create_app

# App start
if __name__ == "__main__":
    logger.info(datetime.today().strftime(" * Running started at [%d/%b/%Y %H:%M:%S]"))

    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
