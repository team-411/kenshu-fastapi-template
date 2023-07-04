from sqlalchemy import Column, Integer, String
from db import Base
from db import ENGINE


# テーブル定義
class TaskTable(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    done = Column(Integer, nullable=False)


def main():
    # マイグレーションなどを記述
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()

