from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from datetime import datetime, date
from ..database import supabase
from ..models import AttendanceCreate, AttendanceResponse, AttendanceMarkRequest

router = APIRouter(prefix="/attendance", tags=["Attendance"])


@router.get("/", response_model=List[AttendanceResponse])
async def get_all_attendance(
    date_filter: Optional[date] = None,
    student_id: Optional[str] = None
):
    """Get attendance records with optional filtering."""
    try:
        query = supabase.table("attendance").select("*")
        
        if date_filter:
            query = query.eq("attendance_date", date_filter.isoformat())
        if student_id:
            query = query.eq("student_id", student_id)
        
        response = query.order("created_at", desc=True).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/today")
async def get_today_attendance():
    """Get today's attendance records."""
    try:
        today = date.today().isoformat()
        response = supabase.table("attendance").select("*").eq("attendance_date", today).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/mark", response_model=AttendanceResponse, status_code=status.HTTP_201_CREATED)
async def mark_attendance(data: AttendanceMarkRequest):
    """Mark attendance for a user (called after face recognition)."""
    try:
        # Get user details
        user_response = supabase.table("users").select("id, name, roll_no, department").eq("student_id", data.student_id).execute()
        
        user_id = None
        if user_response.data:
            user_id = user_response.data[0]["id"]
        
        # Check if already marked today
        today = date.today().isoformat()
        existing = supabase.table("attendance").select("id").eq("student_id", data.student_id).eq("attendance_date", today).execute()
        
        if existing.data:
            raise HTTPException(status_code=400, detail="Attendance already marked for today")
        
        # Create attendance record
        attendance_data = {
            "student_id": data.student_id,
            "name": data.name,
            "roll_no": data.roll_no,
            "department": data.department,
            "user_id": user_id,
            "attendance_status": "Present",
            "check_in_time": datetime.now().time().isoformat(),
            "attendance_date": today
        }
        
        response = supabase.table("attendance").insert(attendance_data).execute()
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=AttendanceResponse, status_code=status.HTTP_201_CREATED)
async def create_attendance(attendance: AttendanceCreate):
    """Create a manual attendance record."""
    try:
        attendance_data = attendance.model_dump()
        
        # Convert date and time to strings
        if attendance_data.get("attendance_date"):
            attendance_data["attendance_date"] = attendance_data["attendance_date"].isoformat()
        else:
            attendance_data["attendance_date"] = date.today().isoformat()
            
        if attendance_data.get("check_in_time"):
            attendance_data["check_in_time"] = attendance_data["check_in_time"].isoformat()
        
        # Convert UUID to string if present
        if attendance_data.get("user_id"):
            attendance_data["user_id"] = str(attendance_data["user_id"])
        
        response = supabase.table("attendance").insert(attendance_data).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{attendance_id}")
async def update_attendance(attendance_id: str, status_update: str):
    """Update attendance status."""
    try:
        response = supabase.table("attendance").update({
            "attendance_status": status_update
        }).eq("id", attendance_id).execute()
        
        if not response.data:
            raise HTTPException(status_code=404, detail="Attendance record not found")
        
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{attendance_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_attendance(attendance_id: str):
    """Delete an attendance record."""
    try:
        supabase.table("attendance").delete().eq("id", attendance_id).execute()
        return None
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stats/today")
async def get_today_stats():
    """Get attendance statistics for today."""
    try:
        today = date.today().isoformat()
        
        # Get today's attendance
        attendance = supabase.table("attendance").select("*").eq("attendance_date", today).execute()
        
        # Get total registered users
        users = supabase.table("users").select("id", count="exact").execute()
        
        total_users = users.count if users.count else len(users.data)
        present_count = len(attendance.data)
        
        return {
            "date": today,
            "total_registered": total_users,
            "present": present_count,
            "absent": total_users - present_count,
            "attendance_percentage": round((present_count / total_users * 100), 2) if total_users > 0 else 0
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
