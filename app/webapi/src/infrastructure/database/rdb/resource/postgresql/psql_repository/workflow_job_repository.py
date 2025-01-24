from ..psql_table import WorkflowJobTable
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine.row import Row, Tuple, Sequence
from src.domain.workflow import WorkflowJob, WorkflowJobRepository



class WorkflowJobRepositoryImpl(WorkflowJobRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    @staticmethod
    def to_table(entity: WorkflowJob) -> WorkflowJobTable:
        return WorkflowJobTable(
            **entity.model_dump()
        )
    
    @staticmethod
    def to_entity(obj: WorkflowJobTable) -> WorkflowJob:
        return WorkflowJob(
            id=str(obj.id),
            workflow_id=obj.workflow_id,
            on_success=obj.on_success,
            on_failure=obj.on_failure,
            title=obj.title,
            status=obj.status,
            task=obj.task,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
            deleted_at=obj.deleted_at
        )


    def get_exclude_deleted(self, id: str) -> WorkflowJob:
        result = self._session.execute(
            select(
                WorkflowJobTable
            )
            .filter(
                WorkflowJobTable.id == id,
                WorkflowJobTable.deleted_at == None
            )
        )
        row: Row[Tuple[WorkflowJobTable]] = result.one()
        return self.to_entity(row[0])
    

    def get_all_exclude_deleted(self, workflow_id: str) -> list[WorkflowJob]:
        result = self._session.execute(
            select(
                WorkflowJobTable
            )
            .filter(
                WorkflowJobTable.workflow_id == workflow_id,
                WorkflowJobTable.deleted_at == None
            )
            .order_by(WorkflowJobTable.created_at.desc())
        )
        rows: Sequence[Row[Tuple[WorkflowJobTable]]] = result.all()
        return [self.to_entity(row[0]) for row in rows]
    

    def get_latest_list_exclude_deleted(self, workflow_id: str, limit: int) -> list[WorkflowJob]:
        result = self._session.execute(
            select(
                WorkflowJobTable
            )
            .filter(
                WorkflowJobTable.workflow_id == workflow_id,
                WorkflowJobTable.deleted_at == None
            )
            .order_by(WorkflowJobTable.created_at.desc())
            .limit(limit)
        )
        rows: Sequence[Row[Tuple[WorkflowJobTable]]] = result.all()
        return [self.to_entity(row[0]) for row in rows]
    


    def create(self, entity: WorkflowJob) -> WorkflowJob:
        obj = self.to_table(entity)
        self._session.add(obj)
        self._session.flush()
        return self.to_entity(obj)
    

    def update_status(self, id: str, status: str) -> WorkflowJob:
        result = self._session.execute(
            select(
                WorkflowJobTable
            )
            .filter(
                WorkflowJobTable.id == id,
                WorkflowJobTable.deleted_at == None
            )
        )
        row: Row[Tuple[WorkflowJobTable]] = result.one()
        _in_db: WorkflowJobTable = row[0]
        _in_db.status = status
        self._session.flush()

        return self.to_entity(_in_db)
    

    def delete(self, id: str) -> WorkflowJob:
        result = self._session.execute(
            select(
                WorkflowJobTable
            )
            .filter(
                WorkflowJobTable.id == id,
                WorkflowJobTable.deleted_at == None
            )
        )
        row: Row[Tuple[WorkflowJobTable]] = result.one()
        _in_db: WorkflowJobTable = row[0]
        _in_db.deleted_at = _in_db.now()
        self._session.flush()

        return self.to_entity(_in_db)
    
    
