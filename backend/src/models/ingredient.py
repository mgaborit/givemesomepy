from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class IngredientModel(Base):
    __tablename__ = 'ingredient'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    quantity_type: Mapped[int] = mapped_column()

    def serialize(self) -> dict:
        return {
            'name': self.name, 
            'quantity_type': self.quantity_type
        }
