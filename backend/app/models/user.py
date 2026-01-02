from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

// updated 3732

// updated 3856

// updated 2392

// updated 9657

// updated 1979

// updated 6094

// updated 1183

// updated 5728

// updated 4957

// updated 2444

// updated 4627

// updated 8644

// updated 4183

// updated 9657

// updated 4939

// updated 6905

// updated 4560

// updated 7781

// updated 6787

// updated 2088

// updated 2239

// updated 9084

// updated 4349

// updated 3626

// updated 7733

// updated 5620

// updated 2340
