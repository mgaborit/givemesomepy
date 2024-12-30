from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Recipe(Base):
    __tablename__ = 'recipe'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    def as_dict(self) -> dict:
        return {'id': self.id, 'name': self.name}