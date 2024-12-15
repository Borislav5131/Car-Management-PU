from fastapi import APIRouter

router = APIRouter()

@router.get("/maintenance/{id}")
def get_maintenance_by_id():
    return []


@router.get("/maintenance/")
def get_maintenance():
    return [{"id": 1,
             "carId": 1,
             "carName": "test",
             "serviceType": "test",
             "scheduleDate": "2024",
             "garageId": 1,
             "garageName": "test"}]