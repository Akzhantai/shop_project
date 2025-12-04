from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, Datetime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    image_url = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    created_at = Column(Datetime, default=datetime.utcnow)

    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"