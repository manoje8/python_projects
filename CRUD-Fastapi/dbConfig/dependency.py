from dbConfig.database import SessionLocal


def db_connect():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
