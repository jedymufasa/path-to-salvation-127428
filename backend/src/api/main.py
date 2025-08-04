from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .models import TractSection, SalvationStep, ContactRequest, ShareInfo

# In-memory data stores (replace with a database in a real application)
tract_data: List[TractSection] = [
    TractSection(id=1, title="God's Perfect Love", content="God loves you and has a wonderful plan for your life. 'For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life.' - John 3:16", image_url="https://images.unsplash.com/photo-1488345979593-09db0f85545f?q=80&w=2070&auto=format&fit=crop"),
    TractSection(id=2, title="The Problem of Sin", content="All of us have sinned and fallen short of God's glory. This sin separates us from God. 'For all have sinned and fall short of the glory of God.' - Romans 3:23", image_url="https://images.unsplash.com/photo-1508921340878-ba53e1f416ec?q=80&w=1887&auto=format&fit=crop"),
    TractSection(id=3, title="God's Solution: Jesus Christ", content="God sent His Son, Jesus, to die for our sins. He is the bridge back to God. 'But God shows his love for us in that while we were still sinners, Christ died for us.' - Romans 5:8", image_url="https://images.unsplash.com/photo-1594791343049-5987341076b4?q=80&w=1964&auto=format&fit=crop"),
    TractSection(id=4, title="Your Response: Receive Christ", content="You must personally receive Jesus Christ as your Savior and Lord. 'But to all who did receive him, who believed in his name, he gave the right to become children of God.' - John 1:12", image_url="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=2070&auto=format&fit=crop"),
]

salvation_steps_data: List[SalvationStep] = [
    SalvationStep(id=1, title="Acknowledge", summary="Recognize that you are a sinner.", details="Admit to God that you have sinned and that your sin has separated you from Him. True repentance starts with acknowledging the problem.", scripture="Romans 3:23 - 'For all have sinned and fall short of the glory of God.'"),
    SalvationStep(id=2, title="Believe", summary="Believe in your heart that Jesus Christ died for your sins and was raised from the dead.", details="Faith is more than just mental agreement; it's trusting in Jesus alone for your salvation.", scripture="Romans 10:9 - '...if you confess with your mouth that Jesus is Lord and believe in your heart that God raised him from the dead, you will be saved.'"),
    SalvationStep(id=3, title="Confess", summary="Confess with your mouth that Jesus is Lord.", details="Publicly declare your faith in Jesus. This is an outward expression of the change that has happened in your heart.", scripture="Romans 10:10 - 'For with the heart one believes and is justified, and with the mouth one confesses and is saved.'"),
    SalvationStep(id=4, title="Repent and Turn", summary="Turn away from your sin and turn to God.", details="Repentance is a change of mind that leads to a change of action. It means turning from your self-ruled life to a life ruled by God.", scripture="Acts 3:19 - 'Repent, then, and turn to God, so that your sins may be wiped out...'"),
]

contact_requests_db: List[ContactRequest] = []

share_info_data = ShareInfo(
    title="Path to Salvation",
    text="Discover the path to salvation through Jesus Christ.",
    url="https://path-to-salvation.example.com" # Placeholder URL
)


app = FastAPI(
    title="Path to Salvation API",
    description="API for the digital tract evangelism application. This API provides content for the gospel tract, steps to salvation, and a way for users to submit contact requests.",
    version="1.0.0",
    openapi_tags=[
        {"name": "Tract", "description": "Operations related to the gospel tract."},
        {"name": "Salvation Steps", "description": "Operations related to the way of salvation."},
        {"name": "Contact", "description": "Operations for user contact requests."},
        {"name": "Sharing", "description": "Operations for social media sharing."},
        {"name": "Health Check", "description": "API health check."},
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# PUBLIC_INTERFACE
@app.get("/", tags=["Health Check"])
def health_check():
    """
    Health check endpoint to confirm the API is running.
    """
    return {"message": "API is healthy and running."}

# PUBLIC_INTERFACE
@app.get("/tract", response_model=List[TractSection], tags=["Tract"], summary="Get Digital Tract Content")
def get_tract():
    """
    Retrieves the sections of the digital gospel tract. Each section includes a title, content, and an optional image URL.
    """
    return tract_data

# PUBLIC_INTERFACE
@app.get("/salvation-steps", response_model=List[SalvationStep], tags=["Salvation Steps"], summary="Get Way of Salvation Steps")
def get_salvation_steps():
    """
    Retrieves the step-by-step guide to salvation. Each step includes a title, summary, detailed explanation, and a relevant scripture.
    """
    return salvation_steps_data

# PUBLIC_INTERFACE
@app.get("/share-info", response_model=ShareInfo, tags=["Sharing"], summary="Get Social Share Information")
def get_share_info():
    """
    Provides default text, title, and URL for sharing the application on social media. The URL should be updated to point to the deployed frontend application.
    """
    return share_info_data

# PUBLIC_INTERFACE
@app.post("/contact", response_model=ContactRequest, status_code=201, tags=["Contact"], summary="Submit a Contact Request")
def submit_contact_request(request: ContactRequest):
    """
    Accepts a contact request from a user who wants to know more or has made a decision.
    The request should contain the user's name and email, and an optional message.

    - **name**: User's name.
    - **email**: User's email address.
    - **message**: Optional message from the user.
    """
    print(f"Received contact request: {request.dict()}")
    contact_requests_db.append(request)
    # In a real-world application, this is where you would:
    # 1. Save the contact request to a persistent database.
    # 2. Trigger an email notification to an administrator.
    # 3. Send a confirmation email to the user.
    return request
