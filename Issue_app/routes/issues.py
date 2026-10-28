import uuid
from fastapi import APIRouter, HTTPException, status
from routes.schemas import TaskCreate, TaskGet, TaskUpdate, TaskStatus
from routes.storage import load_data, save_data
router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

@router.get("/", response_model=list[TaskGet])
def get_tasks():
    issues = load_data()
    return issues

@router.post("/", response_model=TaskGet, status_code=status.HTTP_201_CREATED)
def create_tasks(paybody: TaskCreate):
    issues = load_data()
    new_issues = {
        "id": str(uuid.uuid4()),
        "title": paybody.title,
        "description": paybody.description,
        "priority": paybody.priority,
        "status": TaskStatus.OPEN,
    }
    issues.append(new_issues)
    save_data(issues)
    return new_issues

@router.get("/{issue_id}", response_model=TaskGet)
def get_ids(issue_id: str):
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            return issue
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.put("/{issue_id}", response_model=TaskGet)
def update_issue(issue_id: str, paybody: TaskUpdate):
    issues = load_data()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            updated_issue = issue.copy()
            if paybody.title is not None:
                updated_issue["title"] = paybody.title
            if paybody.description is not None:
                updated_issue["description"] = paybody.description
            if paybody.priority is not None:
                updated_issue["priority"] = paybody.priority
            if paybody.status is not None:
                updated_issue["status"] = paybody.status
            save_data(issues)
            return updated_issue
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not foud")

@router.delete('/{issue_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(issue_id: str):
    issues = load_data()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            issues.pop(index)
            save_data(issues)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

