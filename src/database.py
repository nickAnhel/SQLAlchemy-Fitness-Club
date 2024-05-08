from sqlalchemy import create_engine

import config


engine = create_engine(
    config.DB_URL,
    echo=True,
)
