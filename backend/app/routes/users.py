from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from ..database import supabase
from ..models import UserCreate, UserUpdate, UserResponse, FaceEncodingRequest
from datetime import datetime

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[UserResponse])
async def get_all_users():
    """Get all registered users."""
    try:
        response = supabase.table("users").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{student_id}", response_model=UserResponse)
async def get_user(student_id: str):
    """Get a specific user by student ID."""
    try:
        response = supabase.table("users").select("*").eq("student_id", student_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="User not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Create a new user."""
    try:
        # Check if user already exists
        existing = supabase.table("users").select("id").eq("student_id", user.student_id).execute()
        if existing.data:
            raise HTTPException(status_code=400, detail="User with this student ID already exists")
        
        # Convert date to string if present
        user_data = user.model_dump()
        if user_data.get("dob"):
            user_data["dob"] = user_data["dob"].isoformat()
        
        response = supabase.table("users").insert(user_data).execute()
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{student_id}", response_model=UserResponse)
async def update_user(student_id: str, user: UserUpdate):
    """Update an existing user."""
    try:
        # Check if user exists
        existing = supabase.table("users").select("id").eq("student_id", student_id).execute()
        if not existing.data:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Filter out None values
        update_data = {k: v for k, v in user.model_dump().items() if v is not None}
        
        # Convert date to string if present
        if update_data.get("dob"):
            update_data["dob"] = update_data["dob"].isoformat()
        
        update_data["updated_at"] = datetime.now().isoformat()
        
        response = supabase.table("users").update(update_data).eq("student_id", student_id).execute()
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(student_id: str):
    """Delete a user."""
    try:
        # Check if user exists
        existing = supabase.table("users").select("id").eq("student_id", student_id).execute()
        if not existing.data:
            raise HTTPException(status_code=404, detail="User not found")
        
        supabase.table("users").delete().eq("student_id", student_id).execute()
        return None
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/{student_id}/face-encoding")
async def save_face_encoding(student_id: str, data: FaceEncodingRequest):
    """Save face encoding for a user."""
    try:
        # Check if user exists
        existing = supabase.table("users").select("id").eq("student_id", student_id).execute()
        if not existing.data:
            raise HTTPException(status_code=404, detail="User not found")
        
        response = supabase.table("users").update({
            "face_encoding": data.face_encoding,
            "photo_sample_status": "Yes",
            "updated_at": datetime.now().isoformat()
        }).eq("student_id", student_id).execute()
        
        return {"message": "Face encoding saved successfully", "data": response.data[0]}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/with-face/all")
async def get_users_with_face():
    """Get all users who have face encodings (for recognition matching)."""
    try:
        response = supabase.table("users").select("student_id, name, roll_no, department, face_encoding").eq("photo_sample_status", "Yes").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
