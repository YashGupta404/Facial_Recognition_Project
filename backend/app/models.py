from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, time
from uuid import UUID


class UserBase(BaseModel):
    """Base user model with common fields."""
    student_id: str
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    department: Optional[str] = None
    course: Optional[str] = None
    year: Optional[str] = None
    semester: Optional[str] = None
    division: Optional[str] = None
    roll_no: Optional[str] = None
    gender: Optional[str] = None
    dob: Optional[date] = None
    address: Optional[str] = None
    teacher_name: Optional[str] = None
    photo_sample_status: Optional[str] = "No"


class UserCreate(UserBase):
    """Model for creating a new user."""
    face_encoding: Optional[str] = None


class UserUpdate(BaseModel):
    """Model for updating user details."""
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    department: Optional[str] = None
    course: Optional[str] = None
    year: Optional[str] = None
    semester: Optional[str] = None
    division: Optional[str] = None
    roll_no: Optional[str] = None
    gender: Optional[str] = None
    dob: Optional[date] = None
    address: Optional[str] = None
    teacher_name: Optional[str] = None
    photo_sample_status: Optional[str] = None
    face_encoding: Optional[str] = None


class UserResponse(UserBase):
    """Model for user response."""
    id: UUID
    face_encoding: Optional[str] = None
    
    class Config:
        from_attributes = True


class AttendanceBase(BaseModel):
    """Base attendance model."""
    student_id: str
    name: Optional[str] = None
    roll_no: Optional[str] = None
    department: Optional[str] = None
    attendance_status: Optional[str] = "Present"


class AttendanceCreate(AttendanceBase):
    """Model for creating attendance record."""
    user_id: Optional[UUID] = None
    check_in_time: Optional[time] = None
    attendance_date: Optional[date] = None


class AttendanceResponse(AttendanceBase):
    """Model for attendance response."""
    id: UUID
    user_id: Optional[UUID] = None
    check_in_time: Optional[time] = None
    attendance_date: Optional[date] = None
    
    class Config:
        from_attributes = True


class FaceEncodingRequest(BaseModel):
    """Model for storing face encoding."""
    student_id: str
    face_encoding: str  # JSON string of face landmarks/encoding


class AttendanceMarkRequest(BaseModel):
    """Model for marking attendance via face recognition."""
    student_id: str
    name: str
    roll_no: Optional[str] = None
    department: Optional[str] = None
