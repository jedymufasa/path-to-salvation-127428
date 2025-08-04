from pydantic import BaseModel, EmailStr

# PUBLIC_INTERFACE
class TractSection(BaseModel):
    """
    Represents a section of the digital tract.
    """
    id: int
    title: str
    content: str
    image_url: str | None = None

# PUBLIC_INTERFACE
class SalvationStep(BaseModel):
    """
    Represents a step in the way of salvation walkthrough.
    """
    id: int
    title: str
    summary: str
    details: str
    scripture: str

# PUBLIC_INTERFACE
class ContactRequest(BaseModel):
    """
    Represents a contact request submitted by a user.
    """
    name: str
    email: EmailStr
    message: str | None = None

# PUBLIC_INTERFACE
class ShareInfo(BaseModel):
    """
    Provides metadata for social media sharing.
    """
    title: str
    text: str
    url: str
