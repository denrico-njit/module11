import enum
import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, Float, String
from sqlalchemy.dialects.postgresql import UUID

from app.models.user import Base

# Adds an extra touch of validation using an Enum to ensure that only valid operations are stored in the database.
class OperationType(enum.Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    operand1 = Column(Float, nullable=False)
    operand2 = Column(Float, nullable=False)
    operation = Column(Enum(OperationType), nullable=False)
    result = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Calculation(id={self.id}, user_id={self.user_id}, operation={self.operation}, result={self.result})>"
