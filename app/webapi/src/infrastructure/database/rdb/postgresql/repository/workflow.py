from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine.row import Row, Tuple, Sequence
from src.domain.workflow import Workflow, WorkflowRepository
from src.infrastructure.database.rdb.postgresql.schema.table import WorkflowTable


class WorkflowRepositoryImpl(WorkflowRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    @staticmethod
    def to_table(entity: Workflow) -> WorkflowTable:
        return WorkflowTable(
            **entity.model_dump()
        )
    
    @staticmethod
    def to_entity(obj: WorkflowTable) -> Workflow:
        return Workflow(
            id=str(obj.id),
            account_id=obj.account_id,
            title=obj.title,
            status=obj.status,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
            deleted_at=obj.deleted_at
        )


    def get_exclude_deleted(self, id: str) -> Workflow:
        result = self._session.execute(
            select(
                WorkflowTable
            )
            .filter(
                WorkflowTable.id == id,
                WorkflowTable.deleted_at == None
            )
        )
        row: Row[Tuple[WorkflowTable]] = result.one()
        return self.to_entity(row[0])
    

    def get_all_exclude_deleted(self, account_id: str) -> list[Workflow]:
        result = self._session.execute(
            select(
                WorkflowTable
            )
            .filter(
                WorkflowTable.account_id == account_id,
                WorkflowTable.deleted_at == None
            )
            .order_by(WorkflowTable.created_at.desc())
        )
        rows: Sequence[Row[Tuple[WorkflowTable]]] = result.all()
        return [self.to_entity(row[0]) for row in rows]


    def create(self, entity: Workflow) -> Workflow:
        obj = self.to_table(entity)
        self._session.add(obj)
        self._session.flush()
        return self.to_entity(obj)
    

    def update_status(self, id: str, status: str) -> Workflow:
        result = self._session.execute(
            select(
                WorkflowTable
            )
            .filter(
                WorkflowTable.id == id,
                WorkflowTable.deleted_at == None
            )
        )
        row: Row[Tuple[WorkflowTable]] = result.one()
        _in_db: WorkflowTable = row[0]
        _in_db.status = status
        self._session.flush()

        return self.to_entity(_in_db)
    

    def delete(self, id: str) -> Workflow:
        result = self._session.execute(
            select(
                WorkflowTable
            )
            .filter(
                WorkflowTable.id == id,
                WorkflowTable.deleted_at == None
            )
        )
        row: Row[Tuple[WorkflowTable]] = result.one()
        _in_db: WorkflowTable = row[0]
        _in_db.deleted_at = _in_db.now()
        self._session.flush()

        return self.to_entity(_in_db)
    
    
