from fastapi import FastAPI, HTTPException, Response, status, Depends
import psycopg2
from typing import Optional, List
from psycopg2.extras import RealDictCursor
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session
import time


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

""" CONNECTING TO DATABASE """
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='festo', user='postgres', password='password', 
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error", error)
        time.sleep(2)

@app.get("/")
def root():
    return {"message": "Hello World"}




""" ADMISSION API """
#Create Admission
@app.post("/admission", status_code=status.HTTP_201_CREATED)
def create_admission(admission: schemas.AdmissionCreate, db: Session = Depends(get_db)):
    new_admission = models.Admission(**admission.dict())
    db.add(new_admission)
    db.commit()
    db.refresh(new_admission)
    return new_admission

#Read One Admission
@app.get("/admission/{id}", response_model=schemas.AdmissionResponse)
def get_one_admission(id: int, db: Session = Depends(get_db)):
    admission = db.query(models.Admission).filter(models.Admission.id == id).first()

    if not admission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Admission with id: {id} was not found")
    return  admission

#Read All Admission
@app.get("/admission", response_model=List[schemas.AdmissionResponse])
def get_admission(db: Session = Depends(get_db)):
    admission = db.query(models.Admission).all()
    return admission

#Update Admission
@app.put("/admission/{id}", response_model=schemas.AdmissionResponse)
def update_admission(id: int, updated_admission: schemas.AdmissionCreate, db: Session = Depends(get_db)):

    admission_query = db.query(models.Admission).filter(models.Admission.id == id)

    admission = admission_query.first()

    if admission == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Admission with allergy_id: {id} does not exist")
    
    admission_query.update(updated_admission.dict(), synchronize_session=False)
    db.commit()
    return admission_query.first()


#Delete Admission
@app.delete("/admission/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_admission(id: int, db: Session = Depends(get_db)):

    admission = db.query(models.Admission).filter(models.Admission.id == id)

    if admission.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Admission with id: {id} does not exist")
    
    admission.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" ADVERSE REACTIONS API """
#Create Adverse Reaction
@app.post("/adverse_reaction", status_code=status.HTTP_201_CREATED)
def create_adverse_reaction(adverse_reaction: schemas.AdverseReactionCreate, db: Session = Depends(get_db)):
    new_adverse_reaction = models.AdverseReaction(**adverse_reaction.dict())
    db.add(new_adverse_reaction)
    db.commit()
    db.refresh(new_adverse_reaction)
    return new_adverse_reaction

#Read One Adverse Reaction
@app.get("/adverse_reaction/{id}", response_model=schemas.AdverseReactionResponse)
def get_one_adverse_reaction(id: int, db: Session = Depends(get_db)):
    adverse_reaction = db.query(models.AdverseReaction).filter(models.AdverseReaction.id == id).first()

    if not adverse_reaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Adverse reaction with id: {id} was not found")
    return  adverse_reaction

#Read All Adverse Reaction
@app.get("/adverse_reaction", response_model=List[schemas.AdverseReactionResponse])
def get_adverse_reactions(db: Session = Depends(get_db)):
    adverse_reactions = db.query(models.AdverseReaction).all()
    return adverse_reactions

#Update Adverse Reaction
@app.put("/adverse_reaction/{id}", response_model=schemas.AdverseReactionResponse)
def update_adverse_reaction(id: int, updated_adverse_reaction: schemas.AdverseReactionCreate, db: Session = Depends(get_db)):

    adverse_reaction_query = db.query(models.AdverseReaction).filter(models.AdverseReaction.id == id)

    adverse_reaction = adverse_reaction_query.first()

    if adverse_reaction == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"allergy with id: {id} does not exist")
    
    adverse_reaction_query.update(updated_adverse_reaction.dict(), synchronize_session=False)
    db.commit()
    return adverse_reaction_query.first()


#Delete Adverse Reaction 
@app.delete("/adverse_reaction/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_allergy(id: int, db: Session = Depends(get_db)):

    allergy = db.query(models.Allergies).filter(models.Allergies.id == id)

    if allergy.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"allergy with id: {id} does not exist")
    
    allergy.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

""" ADVERSE REACTION TYPE API """
#Create Adverse Reaction Type
@app.post("/adverse_reaction_type", status_code=status.HTTP_201_CREATED)
def create_adverse_reaction_type(adverse_reaction_type: schemas.AdverseReactionTypeCreate, db: Session = Depends(get_db)):
    new_adverse_reaction_type = models.AdverseReactionType(**adverse_reaction_type.dict())
    db.add(new_adverse_reaction_type)
    db.commit()
    db.refresh(new_adverse_reaction_type)
    return new_adverse_reaction_type

#Read One Adverse Reaction Type
@app.get("/adverse_reaction_type/{id}", response_model=schemas.AdverseReactionTypeResponse)
def get_one_adverse_reaction_type(id: int, db: Session = Depends(get_db)):
    adverse_reaction_type = db.query(models.AdverseReactionType).filter(models.AdverseReactionType.id == id).first()

    if not adverse_reaction_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Adverse reaction type with id: {id} was not found")
    return  adverse_reaction_type

#Read All Adverse Reaction Type
@app.get("/adverse_reaction_type", response_model=List[schemas.AdverseReactionTypeResponse])
def get_adverse_reaction_types(db: Session = Depends(get_db)):
    adverse_reaction_types = db.query(models.AdverseReactionType).all()
    return adverse_reaction_types

#Update Adverse Reaction Type
@app.put("/adverse_reaction_type/{id}", response_model=schemas.AdverseReactionTypeResponse)
def update_adverse_reaction_type(id: int, updated_adverse_reaction_type: schemas.AdverseReactionTypeCreate, db: Session = Depends(get_db)):

    adverse_reaction_type_query = db.query(models.AdverseReactionType).filter(models.AdverseReactionType.id == id)

    adverse_reaction = adverse_reaction_type_query.first()

    if adverse_reaction == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Adverse reaction type with id: {id} does not exist")
    
    adverse_reaction_type_query.update(updated_adverse_reaction_type.dict(), synchronize_session=False)
    db.commit()
    return adverse_reaction_type_query.first()


#Delete Adverse Reaction Type
@app.delete("/adverse_reaction_type/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_adverse_reaction_type(id: int, db: Session = Depends(get_db)):

    adverse_reaction_type = db.query(models.AdverseReactionType).filter(models.AdverseReactionType.id == id)

    if adverse_reaction_type.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Adverse Reaction type with id: {id} does not exist")
    
    adverse_reaction_type.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" ALLERGY API """
#Create Allergy
@app.post("/allergy", status_code=status.HTTP_201_CREATED)
def create_allergy(allergy: schemas.AllergyCreate, db: Session = Depends(get_db)):
    new_allergy = models.Allergy(**allergy.dict())
    db.add(new_allergy)
    db.commit()
    db.refresh(new_allergy)
    return new_allergy

#Read One Allergy
@app.get("/allergy/{id}", response_model=schemas.AllergyResponse)
def get_one_allergy(id: int, db: Session = Depends(get_db)):
    allergy = db.query(models.Allergy).filter(models.Allergy.id == id).first()

    if not allergy:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Allergy with id: {id} was not found")
    return  allergy

#Read All Allergies
@app.get("/allergy", response_model=List[schemas.AllergyResponse])
def get_allergy(db: Session = Depends(get_db)):
    allergy = db.query(models.Allergy).all()
    return allergy

#Update Allergy
@app.put("/allergy/{id}", response_model=schemas.AllergyResponse)
def update_allergy(id: int, updated_allergy: schemas.AllergyCreate, db: Session = Depends(get_db)):

    allergy_query = db.query(models.Allergy).filter(models.Allergy.id == id)

    allergy = allergy_query.first()

    if allergy == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Allergy with id: {id} does not exist")
    
    allergy_query.update(updated_allergy.dict(), synchronize_session=False)
    db.commit()
    return allergy_query.first()


#Delete Allergy
@app.delete("/allergy/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_allergy(id: int, db: Session = Depends(get_db)):

    allergy = db.query(models.Allergy).filter(models.Allergy.id == id)

    if allergy.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Allergy with id: {id} does not exist")
    
    allergy.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



""" APPOINTMENT REMINDERS API """
#Create Appointment Reminder
@app.post("/appointment_reminder", status_code=status.HTTP_201_CREATED)
def create_appointment_reminder(appointment_reminder: schemas.AppointmentReminderCreate, db: Session = Depends(get_db)):
    new_appointment_reminder = models.AppointmentReminder(**appointment_reminder.dict())
    db.add(new_appointment_reminder)
    db.commit()
    db.refresh(new_appointment_reminder)
    return new_appointment_reminder

#Read One Appointment Reminder
@app.get("/appointment_reminder/{id}", response_model=schemas.AppointmentReminderResponse)
def get_single_appointment_reminder(id: int, db: Session = Depends(get_db)):
    appointment_reminder = db.query(models.AppointmentReminder).filter(models.AppointmentReminder.id == id).first()

    if not appointment_reminder:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment Reminder with id: {id} was not found")
    return  appointment_reminder

#Read All Appointment Reminder
@app.get("/appointment_reminder", response_model=List[schemas.AppointmentReminderResponse])
def get_appointment_reminders(db: Session = Depends(get_db)):
    appointment_reminder = db.query(models.AppointmentReminder).all()
    return appointment_reminder

#Update Appointment Reminder
@app.put("/appointment_reminder/{id}", response_model=schemas.AppointmentReminderResponse)
def update_appointment_reminder(id: int, updated_appointment_reminder: schemas.AppointmentReminderCreate, db: Session = Depends(get_db)):

    appointment_reminder_query = db.query(models.AppointmentReminder).filter(models.AppointmentReminder.id == id)

    appointment_reminder = appointment_reminder_query.first()

    if appointment_reminder == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment Reminder with reminder_id: {id} does not exist")
    
    appointment_reminder_query.update(updated_appointment_reminder.dict(), synchronize_session=False)
    db.commit()
    return appointment_reminder_query.first()


#Delete Appointment Reminder
@app.delete("/appointment_reminder/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appointment_reminder(id: int, db: Session = Depends(get_db)):

    appointment_reminder = db.query(models.AppointmentReminder).filter(models.AppointmentReminder.id == id)

    if appointment_reminder.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment Reminder with reminder_id: {id} does not exist")
    
    appointment_reminder.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" APPOINTMENTS API """
#Create Appointment
@app.post("/appointment", status_code=status.HTTP_201_CREATED)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    new_appointment = models.Appointment(**appointment.dict())
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment

#Read One Appointment
@app.get("/appointment/{id}", response_model=schemas.AppointmentResponse)
def get_single_appointment(id: int, db: Session = Depends(get_db)):
    appointment = db.query(models.Appointment).filter(models.Appointment.id == id).first()

    if not appointment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment with appointment_id: {id} was not found")
    return  appointment

#Read All Appointments
@app.get("/appointment", response_model=List[schemas.AppointmentResponse])
def get_appointment(db: Session = Depends(get_db)):
    appointment = db.query(models.Appointment).all()
    return appointment

#Update Appointment
@app.put("/appointment/{id}", response_model=schemas.AppointmentResponse)
def update_appointment(id: int, updated_appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):

    appointment_query = db.query(models.Appointment).filter(models.Appointment.id == id)

    appointment_reminder = appointment_query.first()

    if appointment_reminder == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment with id: {id} does not exist")
    
    appointment_query.update(updated_appointment.dict(), synchronize_session=False)
    db.commit()
    return appointment_query.first()


#Delete Appointment 
@app.delete("/appointment/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appointment(id: int, db: Session = Depends(get_db)):

    appointment = db.query(models.Appointment).filter(models.Appointment.id == id)

    if appointment.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment with id: {id} does not exist")
    
    appointment.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" BED APIs"""
#Create Bed
@app.post("/bed", status_code=status.HTTP_201_CREATED)
def create_bed(bed: schemas.BedCreate, db: Session = Depends(get_db)):
    new_bed = models.Bed(**bed.dict())
    db.add(new_bed)
    db.commit()
    db.refresh(new_bed)
    return new_bed

#Read One Bed
@app.get("/bed/{id}", response_model=schemas.BedResponse)
def get_bed(id: int, db: Session = Depends(get_db)):
    bed = db.query(models.Bed).filter(models.Bed.id == id).first()

    if not bed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bed with id: {id} was not found")
    return  bed

#Read All Bed
@app.get("/bed", response_model=List[schemas.BedResponse])
def get_beds(db: Session = Depends(get_db)):
    bed = db.query(models.Bed).all()
    return bed

#Update Bed
@app.put("/bed/{id}", response_model=schemas.BedResponse)
def update_bed(id: int, updated_bed: schemas.BedCreate, db: Session = Depends(get_db)):

    bed_query = db.query(models.Bed).filter(models.Bed.id == id)

    bed = bed_query.first()

    if bed == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bed with bed_reminder: {id} does not exist")
    
    bed_query.update(updated_bed.dict(), synchronize_session=False)
    db.commit()
    return bed_query.first()


#Delete Bed 
@app.delete("/bed/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bed(id: int, db: Session = Depends(get_db)):

    bed = db.query(models.Bed).filter(models.Bed.id == id)

    if bed.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bed with id: {id} does not exist")
    
    bed.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" BED ASSIGNMENT APIs"""
#Create Bed assignment
@app.post("/bed_assignment", status_code=status.HTTP_201_CREATED)
def create_bed_assignment(bed_assignment: schemas.BedAssignmentCreate, db: Session = Depends(get_db)):
    new_bed_assignment = models.BedAssignment(**bed_assignment.dict())
    db.add(new_bed_assignment)
    db.commit()
    db.refresh(new_bed_assignment)
    return new_bed_assignment

#Read One Bed Assignment
@app.get("/bed_assignment/{id}", response_model=schemas.BedAssignmentResponse)
def get_bed_assignment(id: int, db: Session = Depends(get_db)):
    bed_assignment = db.query(models.BedAssignment).filter(models.BedAssignment.id == id).first()

    if not bed_assignment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bed with id: {id} was not found")
    return  bed_assignment

#Read All Bed Assignment
@app.get("/bed_assignment", response_model=List[schemas.BedAssignmentResponse])
def get_bed_assignment(db: Session = Depends(get_db)):
    bed_assignment = db.query(models.BedAssignment).all()
    return bed_assignment

#Update Bed Assignment
@app.put("/bed_assignment/{id}", response_model=schemas.BedAssignmentResponse)
def update_bed_assignment(id: int, updated_bed_assignment: schemas.BedAssignmentCreate, db: Session = Depends(get_db)):

    bed_assignment_query = db.query(models.BedAssignment).filter(models.BedAssignment.id == id)

    bed_assignment = bed_assignment_query.first()

    if bed_assignment == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bed assignment with id: {id} does not exist")
    
    bed_assignment_query.update(updated_bed_assignment.dict(), synchronize_session=False)
    db.commit()
    return bed_assignment_query.first()


#Delete Bed Assignment
@app.delete("/bed_assignment/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bed(id: int, db: Session = Depends(get_db)):

    bed_assignment = db.query(models.BedAssignment).filter(models.BedAssignment.id == id)

    if bed_assignment.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bed assignment with id: {id} does not exist")
    
    bed_assignment.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" BILLING APIs""" 
#Create Billing
@app.post("/billing", status_code=status.HTTP_201_CREATED)
def create_billing(billing: schemas.BillingCreate, db: Session = Depends(get_db)):
    new_billing = models.Billing(**billing.dict())
    db.add(new_billing)
    db.commit()
    db.refresh(new_billing)
    return new_billing

#Read One Billing
@app.get("/billing/{id}", response_model=schemas.BillingResponse)
def get_billing(id: int, db: Session = Depends(get_db)):
    billing = db.query(models.Billing).filter(models.Billing.id == id).first()

    if not billing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Billing with id: {id} was not found")
    return  billing

#Read All Billings
@app.get("/billing", response_model=List[schemas.BillingResponse])
def get_billing(db: Session = Depends(get_db)):
    billing = db.query(models.Billing).all()
    return billing

#Update Billing
@app.put("/billing/{id}", response_model=schemas.BillingResponse)
def update_billing(id: int, updated_billing: schemas.BillingCreate, db: Session = Depends(get_db)):

    billing_query = db.query(models.Billing).filter(models.Billing.id == id)

    billing = billing_query.first()

    if billing == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Billing with id: {id} does not exist")
    
    billing_query.update(updated_billing.dict(), synchronize_session=False)
    db.commit()
    return billing_query.first()


#Delete Billing
@app.delete("/billing/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bill(id: int, db: Session = Depends(get_db)):

    billing = db.query(models.Billing).filter(models.Billing.id == id)

    if billing.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Billing with id: {id} does not exist")
    
    billing.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" CARE TEAM APIs"""
#Create Care Team Member
@app.post("/care_team", status_code=status.HTTP_201_CREATED)
def create_care_team(care_team: schemas.CareTeamCreate, db: Session = Depends(get_db)):
    new_care_team = models.CareTeam(**care_team.dict())
    db.add(new_care_team)
    db.commit()
    db.refresh(new_care_team)
    return new_care_team

#Read One Care Team Member
@app.get("/care_team/{id}", response_model=schemas.CareTeamResponse)
def get_care_team(id: int, db: Session = Depends(get_db)):
    care_team = db.query(models.CareTeam).filter(models.CareTeam.id == id).first()

    if not care_team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Care Team Member with id: {id} was not found")
    return  care_team

#Read All care team members
@app.get("/care_team", response_model=List[schemas.CareTeamResponse])
def get_care_team_members(db: Session = Depends(get_db)):
    care_team_members = db.query(models.CareTeam).all()
    return care_team_members

#Update care team member
@app.put("/care_team/{id}", response_model=schemas.CareTeamResponse)
def update_care_team(id: int, updated_care_team: schemas.CareTeamCreate, db: Session = Depends(get_db)):

    care_team_member_query = db.query(models.CareTeam).filter(models.CareTeam.id == id)

    care_team_member = care_team_member_query.first()

    if care_team_member == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Care team member with id: {id} does not exist")
    
    care_team_member_query.update(updated_care_team.dict(), synchronize_session=False)
    db.commit()
    return care_team_member_query.first()


#Delete care team member 
@app.delete("/care_team/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_care_team_member(id: int, db: Session = Depends(get_db)):

    care_team_member = db.query(models.CareTeam).filter(models.CareTeam.id == id)

    if care_team_member.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Care team member with id: {id} does not exist")
    
    care_team_member.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" CHRONIC CONDITION APIs"""
#Create Chronic condition
@app.post("/chronic_condition", status_code=status.HTTP_201_CREATED)
def create_chronic_condition(chronic_condition: schemas.ChronicConditionCreate, db: Session = Depends(get_db)):
    new_chronic_condition = models.ChronicCondition(**chronic_condition.dict())
    db.add(new_chronic_condition)
    db.commit()
    db.refresh(new_chronic_condition)
    return new_chronic_condition

#Read One Chronic condition
@app.get("/chronic_condition/{id}", response_model=schemas.ChronicConditionResponse)
def get_chronic_condition(id: int, db: Session = Depends(get_db)):
    chronic_condition = db.query(models.ChronicCondition).filter(models.ChronicCondition.id == id).first()

    if not chronic_condition:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Chronic condition with id: {id} was not found")
    return  chronic_condition

#Read All chronic conditions
@app.get("/chronic_condition", response_model=List[schemas.ChronicConditionResponse])
def get_chronic_conditions(db: Session = Depends(get_db)):
    chronic_condition = db.query(models.ChronicCondition).all()
    return chronic_condition

#Update chronic condition
@app.put("/chronic_condition/{id}", response_model=schemas.ChronicConditionResponse)
def update_chronic_condition(id: int, updated_chronic_condition: schemas.ChronicConditionCreate, db: Session = Depends(get_db)):

    chronic_condition_query = db.query(models.ChronicCondition).filter(models.ChronicCondition.id == id)

    chronic_condition = chronic_condition_query.first()

    if chronic_condition == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Chronic condition with id: {id} does not exist")
    
    chronic_condition_query.update(updated_chronic_condition.dict(), synchronize_session=False)
    db.commit()
    return chronic_condition_query.first()


#Delete chronic condition 
@app.delete("/chronic_condition/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_chronic_condition(id: int, db: Session = Depends(get_db)):

    chronic_condition = db.query(models.ChronicCondition).filter(models.ChronicCondition.id == id)

    if chronic_condition.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Chronic condition with id: {id} does not exist")
    
    chronic_condition.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" COUNTRY APIs"""
#Create Country
@app.post("/country", status_code=status.HTTP_201_CREATED)
def create_country(country: schemas.CountryCreate, db: Session = Depends(get_db)):
    new_country = models.Country(**country.dict())
    db.add(new_country)
    db.commit()
    db.refresh(new_country)
    return new_country

#Read One Country
@app.get("/country/{id}", response_model=schemas.CountryResponse)
def get_country(id: int, db: Session = Depends(get_db)):
    country = db.query(models.Country).filter(models.Country.id == id).first()

    if not country:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Country with id: {id} was not found")
    return  country

#Read All Countries
@app.get("/country", response_model=List[schemas.CountryResponse])
def get_country(db: Session = Depends(get_db)):
    country = db.query(models.Country).all()
    return country

#Update Country
@app.put("/country/{id}", response_model=schemas.CountryResponse)
def update_country(id: int, updated_country: schemas.CountryCreate, db: Session = Depends(get_db)):

    country_query = db.query(models.Country).filter(models.Country.id == id)

    country = country_query.first()

    if country == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Country with id: {id} does not exist")
    
    country_query.update(updated_country.dict(), synchronize_session=False)
    db.commit()
    return country_query.first()


#Delete country 
@app.delete("/country/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_country(id: int, db: Session = Depends(get_db)):

    country = db.query(models.Country).filter(models.Country.id == id)

    if country.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Country with id: {id} does not exist")
    
    country.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" DEPARTMENT APIs"""
#Create Department
@app.post("/department", status_code=status.HTTP_201_CREATED)
def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    new_department = models.Department(**department.dict())
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return new_department

#Read One Department
@app.get("/department/{id}", response_model=schemas.DepartmentResponse)
def get_department(id: int, db: Session = Depends(get_db)):
    department = db.query(models.Department).filter(models.Department.id == id).first()

    if not department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department with id: {id} was not found")
    return  department

#Read All Department
@app.get("/department", response_model=List[schemas.DepartmentResponse])
def get_department(db: Session = Depends(get_db)):
    department = db.query(models.Department).all()
    return department

#Update Department
@app.put("/department/{id}", response_model=schemas.DepartmentResponse)
def update_department(id: int, updated_department: schemas.DepartmentCreate, db: Session = Depends(get_db)):

    department_query = db.query(models.Department).filter(models.Department.id == id)

    department = department_query.first()

    if department == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department with id: {id} does not exist")
    
    department_query.update(updated_department.dict(), synchronize_session=False)
    db.commit()
    return department_query.first()


#Delete Department
@app.delete("/department/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_department(id: int, db: Session = Depends(get_db)):

    department = db.query(models.Department).filter(models.Department.id == id)

    if department.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department with id: {id} does not exist")
    
    department.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" DIAGNOSIS APIs """ #API ERROR
#Create diagnosis
@app.post("/diagnosis", status_code=status.HTTP_201_CREATED)
def create_diagnosis(diagnosis: schemas.DiagnosisCreate, db: Session = Depends(get_db)):
    new_diagnosis = models.Diagnosis(**diagnosis.dict())
    db.add(new_diagnosis)
    db.commit()
    db.refresh(new_diagnosis)
    return new_diagnosis

#Read One diagnosis
@app.get("/diagnosis/{id}", response_model=schemas.DiagnosisResponse)
def get_diagnosis(id: int, db: Session = Depends(get_db)):
    diagnosis = db.query(models.Diagnosis).filter(models.Diagnosis.id == id).first()

    if not diagnosis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Diagnosis with id: {id} was not found")
    return  diagnosis

#Read All diagnosis
@app.get("/diagnosis", response_model=List[schemas.DiagnosisResponse])
def get_diagnosis(db: Session = Depends(get_db)):
    diagnosis = db.query(models.Diagnosis).all()
    return diagnosis

#Update diagnosis
@app.put("/diagnosis/{id}", response_model=schemas.DiagnosisResponse)
def update_diagnosis(id: int, updated_diagnosis: schemas.DiagnosisCreate, db: Session = Depends(get_db)):

    diagnosis_query = db.query(models.Diagnosis).filter(models.Diagnosis.id == id)

    diagnosis = diagnosis_query.first()

    if diagnosis == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Diagnosis with id: {id} does not exist")
    
    diagnosis_query.update(updated_diagnosis.dict(), synchronize_session=False)
    db.commit()
    return diagnosis_query.first()


#Delete diagnosis 
@app.delete("/diagnosis/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_diagnosis(id: int, db: Session = Depends(get_db)):

    diagnosis = db.query(models.Diagnosis).filter(models.Diagnosis.id == id)

    if diagnosis.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Diagnosis with id: {id} does not exist")
    
    diagnosis.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" DISEASES APIs """
#Create diseases
@app.post("/disease", status_code=status.HTTP_201_CREATED)
def create_disease(disease: schemas.DiseaseCreate, db: Session = Depends(get_db)):
    new_disease = models.Disease(**disease.dict())
    db.add(new_disease)
    db.commit()
    db.refresh(new_disease)
    return new_disease

#Read One disease
@app.get("/disease/{id}", response_model=schemas.DiseaseResponse)
def get_disease(id: int, db: Session = Depends(get_db)):
    disease = db.query(models.Disease).filter(models.Disease.id == id).first()

    if not disease:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Disease with id: {id} was not found")
    return  disease

#Read All disease
@app.get("/disease", response_model=List[schemas.DiseaseResponse])
def get_disease(db: Session = Depends(get_db)):
    disease = db.query(models.Disease).all()
    return disease

#Update disease
@app.put("/disease/{id}", response_model=schemas.DiseaseResponse)
def update_disease(id: int, updated_disease: schemas.DiseaseCreate, db: Session = Depends(get_db)):

    disease_query = db.query(models.Disease).filter(models.Disease.id == id)

    disease = disease_query.first()

    if disease == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Disease with id: {id} does not exist")
    
    disease_query.update(updated_disease.dict(), synchronize_session=False)
    db.commit()
    return disease_query.first()


#Delete disease 
@app.delete("/disease/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_disease(id: int, db: Session = Depends(get_db)):

    disease = db.query(models.Disease).filter(models.Disease.id == id)

    if disease.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Disease with id: {id} does not exist")
    
    disease.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" DOCTOR APIs """
#Create doctor
@app.post("/doctor", status_code=status.HTTP_201_CREATED)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    new_doctor = models.Doctor(**doctor.dict())
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor

#Read One doctor
@app.get("/doctor/{id}", response_model=schemas.DoctorResponse)
def get_doctor(id: int, db: Session = Depends(get_db)):
    doctor = db.query(models.Doctor).filter(models.Doctor.id == id).first()

    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor with id: {id} was not found")
    return  doctor

#Read All doctor
@app.get("/doctor", response_model=List[schemas.DoctorResponse])
def get_doctor(db: Session = Depends(get_db)):
    doctor = db.query(models.Doctor).all()
    return doctor

#Update doctor
@app.put("/doctor/{id}", response_model=schemas.DoctorResponse)
def update_doctor(id: int, updated_doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):

    doctor_query = db.query(models.Doctor).filter(models.Doctor.id == id)

    doctor = doctor_query.first()

    if doctor == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor with id: {id} does not exist")
    
    doctor_query.update(updated_doctor.dict(), synchronize_session=False)
    db.commit()
    return doctor_query.first()


#Delete doctor 
@app.delete("/doctor/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_doctor(id: int, db: Session = Depends(get_db)):

    doctor = db.query(models.Doctor).filter(models.Doctor.id == id)

    if doctor.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor with id: {id} does not exist")
    
    doctor.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" DOCTOR  SCHEDULES APIs """
#Create doctor schedule
@app.post("/doctor_schedule", status_code=status.HTTP_201_CREATED)
def create_doctor_schedule(doctor_schedule: schemas.DoctorScheduleCreate, db: Session = Depends(get_db)):
    new_doctor_schedule = models.DoctorSchedule(**doctor_schedule.dict())
    db.add(new_doctor_schedule)
    db.commit()
    db.refresh(new_doctor_schedule)
    return new_doctor_schedule

#Read One doctor schedule
@app.get("/doctor_schedule/{id}", response_model=schemas.DoctorScheduleResponse)
def get_doctor_schedule(id: int, db: Session = Depends(get_db)):
    doctor_schedule = db.query(models.DoctorSchedule).filter(models.DoctorSchedule.id == id).first()

    if not doctor_schedule:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor schedule with id: {id} was not found")
    return  doctor_schedule

#Read All doctor schedules
@app.get("/doctor_schedule", response_model=List[schemas.DoctorScheduleResponse])
def get_doctor_schedule(db: Session = Depends(get_db)):
    doctor_schedule = db.query(models.DoctorSchedule).all()
    return doctor_schedule

#Update doctor schedule
@app.put("/doctor_schedule/{id}", response_model=schemas.DoctorScheduleResponse)
def update_doctor_schedule(id: int, updated_doctor_schedule: schemas.DoctorScheduleCreate, db: Session = Depends(get_db)):

    doctor_schedule_query = db.query(models.DoctorSchedule).filter(models.DoctorSchedule.id == id)

    doctor_schedule = doctor_schedule_query.first()

    if doctor_schedule == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor schedule with id: {id} does not exist")
    
    doctor_schedule_query.update(updated_doctor_schedule.dict(), synchronize_session=False)
    db.commit()
    return doctor_schedule_query.first()


#Delete doctor schedule
@app.delete("/doctor_schedule/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_doctor_schedule(id: int, db: Session = Depends(get_db)):

    doctor_schedule = db.query(models.DoctorSchedule).filter(models.DoctorSchedule.id == id)

    if doctor_schedule.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor schedule with id: {id} does not exist")
    
    doctor_schedule.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" GENETIC CONDITION APIs """
#Create genetic condition
@app.post("/genetic_condition", status_code=status.HTTP_201_CREATED)
def create_genetic_condition(genetic_condition: schemas.GeneticConditionCreate, db: Session = Depends(get_db)):
    new_genetic_condition = models.GeneticCondition(**genetic_condition.dict())
    db.add(new_genetic_condition)
    db.commit()
    db.refresh(new_genetic_condition)
    return new_genetic_condition

#Read One genetic condition
@app.get("/genetic_condition/{id}", response_model=schemas.GeneticConditionResponse)
def get_genetic_condition(id: int, db: Session = Depends(get_db)):
    genetic_condition = db.query(models.GeneticCondition).filter(models.GeneticCondition.id == id).first()

    if not genetic_condition:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Genetic condition with id: {id} was not found")
    return  genetic_condition

#Read All genetic conditions
@app.get("/genetic_condition", response_model=List[schemas.GeneticConditionResponse])
def get_genetic_condition(db: Session = Depends(get_db)):
    genetic_condition = db.query(models.GeneticCondition).all()
    return genetic_condition

#Update genetic condition
@app.put("/genetic_condition/{id}", response_model=schemas.GeneticConditionResponse)
def update_genetic_condition(id: int, updated_genetic_condition: schemas.GeneticConditionCreate, db: Session = Depends(get_db)):

    genetic_condition_query = db.query(models.GeneticCondition).filter(models.GeneticCondition.id == id)

    genetic_condition = genetic_condition_query.first()

    if genetic_condition == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Genetic condition with id: {id} does not exist")
    
    genetic_condition_query.update(updated_genetic_condition.dict(), synchronize_session=False)
    db.commit()
    return genetic_condition_query.first()


#Delete genetic condition
@app.delete("/genetic_condition/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_genetic_condition(id: int, db: Session = Depends(get_db)):

    genetic_condition = db.query(models.GeneticCondition).filter(models.GeneticCondition.id == id)

    if genetic_condition.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Genetic condition with id: {id} does not exist")
    
    genetic_condition.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" HOSPITAL APIs """
#Create hospital 
@app.post("/hospital", status_code=status.HTTP_201_CREATED)
def create_hospital(hospital: schemas.HospitalCreate, db: Session = Depends(get_db)):
    new_hospital = models.Hospital(**hospital.dict())
    db.add(new_hospital)
    db.commit()
    db.refresh(new_hospital)
    return new_hospital

#Read One hospital 
@app.get("/hospital/{id}", response_model=schemas.HospitalResponse)
def get_hospital(id: int, db: Session = Depends(get_db)):
    hospital = db.query(models.Hospital).filter(models.Hospital.id == id).first()

    if not hospital:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Hospital with id: {id} was not found")
    return  hospital

#Read All hospitals
@app.get("/hospital", response_model=List[schemas.HospitalResponse])
def get_hospital(db: Session = Depends(get_db)):
    hospital = db.query(models.Hospital).all()
    return hospital

#Update hospital 
@app.put("/hospital/{id}", response_model=schemas.HospitalResponse)
def update_hospital(id: int, updated_hospital: schemas.HospitalCreate, db: Session = Depends(get_db)):

    hospital_query = db.query(models.Hospital).filter(models.Hospital.id == id)

    hospital = hospital_query.first()

    if hospital == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Hospital with id: {id} does not exist")
    
    hospital_query.update(updated_hospital.dict(), synchronize_session=False)
    db.commit()
    return hospital_query.first()


#Delete hospital 
@app.delete("/hospital/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hospital(id: int, db: Session = Depends(get_db)):

    hospital = db.query(models.Hospital).filter(models.Hospital.id == id)

    if hospital.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Hospital with id: {id} does not exist")
    
    hospital.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



""" IMMUNIZATION APIs """
#Create immunization 
@app.post("/immunization", status_code=status.HTTP_201_CREATED)
def create_immunization(immunization: schemas.ImmunizationCreate, db: Session = Depends(get_db)):
    new_immunization = models.Immunization(**immunization.dict())
    db.add(new_immunization)
    db.commit()
    db.refresh(new_immunization)
    return new_immunization

#Read One immunization 
@app.get("/immunization/{id}", response_model=schemas.ImmunizationResponse)
def get_immunization(id: int, db: Session = Depends(get_db)):
    immunization = db.query(models.Immunization).filter(models.Immunization.id == id).first()

    if not immunization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Immunization with id: {id} was not found")
    return  immunization

#Read All immunization
@app.get("/immunization", response_model=List[schemas.ImmunizationResponse])
def get_immunization(db: Session = Depends(get_db)):
    immunization = db.query(models.Immunization).all()
    return immunization

#Update immunization 
@app.put("/immunization/{id}", response_model=schemas.ImmunizationResponse)
def update_immunization(id: int, updated_immunization: schemas.ImmunizationCreate, db: Session = Depends(get_db)):

    immunization_query = db.query(models.Immunization).filter(models.Immunization.id == id)

    immunization = immunization_query.first()

    if immunization == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Immunization with id: {id} does not exist")
    
    immunization_query.update(updated_immunization.dict(), synchronize_session=False)
    db.commit()
    return immunization_query.first()


#Delete immunization 
@app.delete("/immunization/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_immunization(id: int, db: Session = Depends(get_db)):

    immunization = db.query(models.Immunization).filter(models.Immunization.id == id)

    if immunization.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Immunization with id: {id} does not exist")
    
    immunization.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" INSURANCE CLAIM APIs """
#Create insurance claims 
@app.post("/insurance_claim", status_code=status.HTTP_201_CREATED)
def create_insurance_claim(insurance_claim: schemas.InsuranceClaimCreate, db: Session = Depends(get_db)):
    new_insurance_claim = models.InsuranceClaim(**insurance_claim.dict())
    db.add(new_insurance_claim)
    db.commit()
    db.refresh(new_insurance_claim)
    return new_insurance_claim

#Read one insurance claim 
@app.get("/insurance_claim/{id}", response_model=schemas.InsuranceClaimResponse)
def get_insurance_claim(id: int, db: Session = Depends(get_db)):
    insurance_claim = db.query(models.InsuranceClaim).filter(models.InsuranceClaim.id == id).first()

    if not insurance_claim:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance claim with id: {id} was not found")
    return  insurance_claim

#Read All insurance claim
@app.get("/insurance_claim", response_model=List[schemas.InsuranceClaimResponse])
def get_insurance_claim(db: Session = Depends(get_db)):
    insurance_claim = db.query(models.InsuranceClaim).all()
    return insurance_claim

#Update insurance claim 
@app.put("/insurance_claim/{id}", response_model=schemas.InsuranceClaimResponse)
def update_insurance_claim(id: int, updated_insurance_claim: schemas.InsuranceClaimCreate, db: Session = Depends(get_db)):

    insurance_claim_query = db.query(models.InsuranceClaim).filter(models.InsuranceClaim.id == id)

    insurance_claim = insurance_claim_query.first()

    if insurance_claim == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance claim with id: {id} does not exist")
    
    insurance_claim_query.update(updated_insurance_claim.dict(), synchronize_session=False)
    db.commit()
    return insurance_claim_query.first()


#Delete insurance claim 
@app.delete("/insurance_claim/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_insurance_claim(id: int, db: Session = Depends(get_db)):

    insurance_claim = db.query(models.InsuranceClaim).filter(models.InsuranceClaim.id == id)

    if insurance_claim.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance claim with id: {id} does not exist")
    
    insurance_claim.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

""" INSURANCE PROVIDER APIs """
#Create insurance providers 
@app.post("/insurance_provider", status_code=status.HTTP_201_CREATED)
def create_insurance_provider(insurance_provider: schemas.InsuranceProviderCreate, db: Session = Depends(get_db)):
    new_insurance_provider = models.InsuranceProvider(**insurance_provider.dict())
    db.add(new_insurance_provider)
    db.commit()
    db.refresh(new_insurance_provider)
    return new_insurance_provider

#Read one insurance provider 
@app.get("/insurance_provider/{id}", response_model=schemas.InsuranceProviderResponse)
def get_insurance_provider(id: int, db: Session = Depends(get_db)):
    insurance_provider = db.query(models.InsuranceProvider).filter(models.InsuranceProvider.id == id).first()

    if not insurance_provider:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance provider with id: {id} was not found")
    return  insurance_provider

#Read All insurance providers
@app.get("/insurance_provider", response_model=List[schemas.InsuranceProviderResponse])
def get_insurance_provider(db: Session = Depends(get_db)):
    insurance_provider = db.query(models.InsuranceProvider).all()
    return insurance_provider

#Update insurance provider 
@app.put("/insurance_provider/{id}", response_model=schemas.InsuranceProviderResponse)
def update_insurance_provider(id: int, updated_insurance_company: schemas.InsuranceProviderCreate, db: Session = Depends(get_db)):

    insurance_provider_query = db.query(models.InsuranceProvider).filter(models.InsuranceProvider.id == id)

    insurance_provider = insurance_provider_query.first()

    if insurance_provider == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance company with id: {id} does not exist")
    
    insurance_provider_query.update(updated_insurance_company.dict(), synchronize_session=False)
    db.commit()
    return insurance_provider_query.first()


#Delete insurance provider 
@app.delete("/insurance_provider/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_insurance_provider(id: int, db: Session = Depends(get_db)):

    insurance_provider = db.query(models.InsuranceProvider).filter(models.InsuranceProvider.id == id)

    if insurance_provider.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance provider with id: {id} does not exist")
    
    insurance_provider.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" INSURANCE INFORMATION APIs """
#Create insurance information 
@app.post("/insurance_information", status_code=status.HTTP_201_CREATED)
def create_insurance_information(insurance_information: schemas.InsuranceInformationCreate, db: Session = Depends(get_db)):
    new_insurance_information = models.InsuranceInformation(**insurance_information.dict())
    db.add(new_insurance_information)
    db.commit()
    db.refresh(new_insurance_information)
    return new_insurance_information

#Read single insurance information 
@app.get("/insurance_information/{id}", response_model=schemas.InsuranceInformationResponse)
def get_insurance_information(id: int, db: Session = Depends(get_db)):
    insurance_information = db.query(models.InsuranceInformation).filter(models.InsuranceInformation.id == id).first()

    if not insurance_information:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance information with id: {id} was not found")
    return  insurance_information

#Read All insurance information
@app.get("/insurance_information", response_model=List[schemas.InsuranceInformationResponse])
def get_insurance_information(db: Session = Depends(get_db)):
    insurance_information = db.query(models.InsuranceInformation).all()
    return insurance_information

#Update insurance information 
@app.put("/insurance_information/{id}", response_model=schemas.InsuranceInformationResponse)
def update_insurance_information(id: int, updated_insurance_information: schemas.InsuranceInformationCreate, db: Session = Depends(get_db)):

    insurance_information_query = db.query(models.InsuranceInformation).filter(models.InsuranceInformation.id == id)

    insurance_information = insurance_information_query.first()

    if insurance_information == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance information with id: {id} does not exist")
    
    insurance_information_query.update(updated_insurance_information.dict(), synchronize_session=False)
    db.commit()
    return insurance_information_query.first()


#Delete insurance information 
@app.delete("/insurance_information/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_insurance_information(id: int, db: Session = Depends(get_db)):

    insurance_information = db.query(models.InsuranceInformation).filter(models.InsuranceInformation.id == id)

    if insurance_information.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance information with id: {id} does not exist")
    
    insurance_information.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" LAB TEST APIs """
#Create lab test 
@app.post("/lab_test", status_code=status.HTTP_201_CREATED)
def create_lab_test(lab_test: schemas.LabTestCreate, db: Session = Depends(get_db)):
    new_lab_test = models.LabTest(**lab_test.dict())
    db.add(new_lab_test)
    db.commit()
    db.refresh(new_lab_test)
    return new_lab_test

#Read one lab test 
@app.get("/lab_test/{id}", response_model=schemas.LabTestResponse)
def get_lab_test(id: int, db: Session = Depends(get_db)):
    lab_test = db.query(models.LabTest).filter(models.LabTest.id == id).first()

    if not lab_test:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test with id: {id} was not found")
    return  lab_test

#Read All lab tests
@app.get("/lab_test", response_model=List[schemas.LabTestResponse])
def get_lab_tests(db: Session = Depends(get_db)):
    lab_tests = db.query(models.LabTest).all()
    return lab_tests

#Update lab tests 
@app.put("/lab_test/{id}", response_model=schemas.LabTestResponse)
def update_lab_test(id: int, updated_lab_test: schemas.LabTestCreate, db: Session = Depends(get_db)):

    lab_test_query = db.query(models.LabTest).filter(models.LabTest.id == id)

    lab_test = lab_test_query.first()

    if lab_test == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test with id: {id} does not exist")
    
    lab_test_query.update(updated_lab_test.dict(), synchronize_session=False)
    db.commit()
    return lab_test_query.first()


#Delete lab test
@app.delete("/lab_test/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lab_test(id: int, db: Session = Depends(get_db)):

    lab_test = db.query(models.LabTest).filter(models.LabTest.id == id)

    if lab_test.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test with id: {id} does not exist")
    
    lab_test.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



""" LAB TEST ORDER APIs """
#Create lab test order 
@app.post("/lab_test_order", status_code=status.HTTP_201_CREATED)
def create_lab_test_order(lab_test_order: schemas.LabTestOrderCreate, db: Session = Depends(get_db)):
    new_lab_test_order = models.LabTestOrder(**lab_test_order.dict())
    db.add(new_lab_test_order)
    db.commit()
    db.refresh(new_lab_test_order)
    return new_lab_test_order

#Read one lab test order
@app.get("/lab_test_order/{id}", response_model=schemas.LabTestOrderResponse)
def get_lab_test_order(id: int, db: Session = Depends(get_db)):
    lab_test_order = db.query(models.LabTestOrder).filter(models.LabTestOrder.id == id).first()

    if not lab_test_order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test order with id: {id} was not found")
    return  lab_test_order

#Read All lab tests
@app.get("/lab_test_order", response_model=List[schemas.LabTestOrderResponse])
def get_lab_test_orders(db: Session = Depends(get_db)):
    lab_test_orders = db.query(models.LabTestOrder).all()
    return lab_test_orders

#Update lab tests 
@app.put("/lab_test_order/{id}", response_model=schemas.LabTestOrderResponse)
def update_lab_test_order(id: int, updated_lab_test_order: schemas.LabTestOrderCreate, db: Session = Depends(get_db)):

    lab_test_order_query = db.query(models.LabTestOrder).filter(models.LabTestOrder.id == id)

    lab_test_order = lab_test_order_query.first()

    if lab_test_order == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test order with id: {id} does not exist")
    
    lab_test_order_query.update(updated_lab_test_order.dict(), synchronize_session=False)
    db.commit()
    return lab_test_order_query.first()


#Delete lab test
@app.delete("/lab_test_order/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lab_test_order(id: int, db: Session = Depends(get_db)):

    lab_test_order = db.query(models.LabTestOrder).filter(models.LabTestOrder.id == id)

    if lab_test_order.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test order with id: {id} does not exist")
    
    lab_test_order.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



""" LAB TEST RESULT APIs """
#Create lab test result 
@app.post("/lab_test_result", status_code=status.HTTP_201_CREATED)
def create_lab_test_result(lab_test_result: schemas.LabTestResultCreate, db: Session = Depends(get_db)):
    new_lab_test_result = models.LabTestResult(**lab_test_result.dict())
    db.add(new_lab_test_result)
    db.commit()
    db.refresh(new_lab_test_result)
    return new_lab_test_result

#Read one lab test result
@app.get("/lab_test_result/{id}", response_model=schemas.LabTestResultResponse)
def get_lab_test_result(id: int, db: Session = Depends(get_db)):
    lab_test_result = db.query(models.LabTestResult).filter(models.LabTestResult.id == id).first()

    if not lab_test_result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test result with id: {id} was not found")
    return  lab_test_result

#Read All lab tests result
@app.get("/lab_test_result", response_model=List[schemas.LabTestResultResponse])
def get_lab_test_result(db: Session = Depends(get_db)):
    lab_test_results = db.query(models.LabTestResult).all()
    return lab_test_results

#Update lab tests result
@app.put("/lab_test_result/{id}", response_model=schemas.LabTestResultResponse)
def update_lab_test_result(id: int, updated_lab_test_result: schemas.LabTestResultCreate, db: Session = Depends(get_db)):

    lab_test_result_query = db.query(models.LabTestResult).filter(models.LabTestResult.id == id)

    lab_test_result = lab_test_result_query.first()

    if lab_test_result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test result with id: {id} does not exist")
    
    lab_test_result_query.update(updated_lab_test_result.dict(), synchronize_session=False)
    db.commit()
    return lab_test_result_query.first()


#Delete lab test result
@app.delete("/lab_test_result/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lab_test_result(id: int, db: Session = Depends(get_db)):

    lab_test_result = db.query(models.LabTestResult).filter(models.LabTestResult.id == id)

    if lab_test_result.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test result with id: {id} does not exist")
    
    lab_test_result.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



""" LAB TEST INTERPRETATION APIs """ #API -ERROR
#Create lab test interpretation 
@app.post("/lab_test_interpretation", status_code=status.HTTP_201_CREATED)
def create_lab_test_interpretation(lab_test_interpretation: schemas.LabTestInterpretationCreate, db: Session = Depends(get_db)):
    new_lab_test_interpretation = models.LabTestInterpretation(**lab_test_interpretation.dict())
    db.add(new_lab_test_interpretation)
    db.commit()
    db.refresh(new_lab_test_interpretation)
    return new_lab_test_interpretation

#Read one lab test interpretation
@app.get("/lab_test_interpretation/{id}", response_model=schemas.LabTestInterpretationResponse)
def get_lab_test_interpretation(id: int, db: Session = Depends(get_db)):
    lab_test_interpretation = db.query(models.LabTestInterpretation).filter(models.LabTestInterpretation.id == id).first()

    if not lab_test_interpretation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test interpretation with id: {id} was not found")
    return  lab_test_interpretation

#Read All lab tests result
@app.get("/lab_test_interpretation", response_model=List[schemas.LabTestInterpretationResponse])
def get_lab_test_interpretation(db: Session = Depends(get_db)):
    lab_test_interpretations = db.query(models.LabTestInterpretation).all()
    return lab_test_interpretations

#Update lab tests interpretation
@app.put("/lab_test_interpretation/{id}", response_model=schemas.LabTestInterpretationResponse)
def update_lab_test_interpretation(id: int, updated_lab_test_interpretation: schemas.LabTestInterpretationCreate, db: Session = Depends(get_db)):

    lab_test_interpretation_query = db.query(models.LabTestInterpretation).filter(models.LabTestInterpretation.id == id)

    lab_test_interpretation = lab_test_interpretation_query.first()

    if lab_test_interpretation == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test interpretation with id: {id} does not exist")
    
    lab_test_interpretation_query.update(updated_lab_test_interpretation.dict(), synchronize_session=False)
    db.commit()
    return lab_test_interpretation_query.first()


#Delete lab test interpretation
@app.delete("/lab_test_interpretation/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lab_test_interpretation(id: int, db: Session = Depends(get_db)):

    lab_test_interpretation = db.query(models.LabTestInterpretation).filter(models.LabTestInterpretation.id == id)

    if lab_test_interpretation.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test interpretation with id: {id} does not exist")
    
    lab_test_interpretation.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" MEDICATION ALERTS APIs """
#Create medication alerts 
@app.post("/medical_alert", status_code=status.HTTP_201_CREATED)
def create_medical_alert(medication_alert: schemas.MedicationAlertCreate, db: Session = Depends(get_db)):
    new_medical_alert = models.MedicationAlert(**medication_alert.dict())
    db.add(new_medical_alert)
    db.commit()
    db.refresh(new_medical_alert)
    return new_medical_alert

#Read one medical alert 
@app.get("/medical_alert/{id}", response_model=schemas.MedicationAlertResponse)
def get_medical_alert(id: int, db: Session = Depends(get_db)):
    medical_alert = db.query(models.MedicationAlert).filter(models.MedicationAlert.id == id).first()

    if not medical_alert:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical alert with id: {id} was not found")
    return  medical_alert

#Read All medical alerts
@app.get("/medical_alert", response_model=List[schemas.MedicationAlertResponse])
def get_medical_alerts(db: Session = Depends(get_db)):
    medical_alerts = db.query(models.MedicationAlert).all()
    return medical_alerts

#Update medical alerts
@app.put("/medical_alert/{id}", response_model=schemas.MedicationAlertResponse)
def update_medical_alert(id: int, updated_medical_alert: schemas.MedicationAlertCreate, db: Session = Depends(get_db)):

    medical_alert_query = db.query(models.MedicationAlert).filter(models.MedicationAlert.id == id)

    medical_alert = medical_alert_query.first()

    if medical_alert == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical alert with id: {id} does not exist")
    
    medical_alert_query.update(updated_medical_alert.dict(), synchronize_session=False)
    db.commit()
    return medical_alert_query.first()


#Delete medical alert
@app.delete("/medical_alert/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_alert(id: int, db: Session = Depends(get_db)):

    medical_alert = db.query(models.MedicationAlert).filter(models.MedicationAlert.id == id)

    if medical_alert.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical alert with id: {id} does not exist")
    
    medical_alert.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" MEDICAL CONDITION APIs """
#Create medical condition 
@app.post("/medical_condition", status_code=status.HTTP_201_CREATED)
def create_medical_condition(medical_condition: schemas.MedicalConditionCreate, db: Session = Depends(get_db)):
    new_medical_condition = models.MedicalCondition(**medical_condition.dict())
    db.add(new_medical_condition)
    db.commit()
    db.refresh(new_medical_condition)
    return new_medical_condition

#Read one medical condition  
@app.get("/medical_condition/{id}", response_model=schemas.MedicalConditionResponse)
def get_medical_condition(id: int, db: Session = Depends(get_db)):
    medical_condition = db.query(models.MedicalCondition).filter(models.MedicalCondition.id == id).first()

    if not medical_condition:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical condition with id: {id} was not found")
    return  medical_condition

#Read All medical condition 
@app.get("/medical_condition", response_model=List[schemas.MedicalConditionResponse])
def get_medical_condition(db: Session = Depends(get_db)):
    medical_condition = db.query(models.MedicalCondition).all()
    return medical_condition

#Update medical condition  
@app.put("/medical_condition/{id}", response_model=schemas.MedicalConditionResponse)
def update_medical_condition(id: int, updated_medical_condition: schemas.MedicalConditionCreate, db: Session = Depends(get_db)):

    medical_condition_query = db.query(models.MedicalCondition).filter(models.MedicalCondition.id == id)

    medical_condition = medical_condition_query.first()

    if medical_condition == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical condition with id: {id} does not exist")
    
    medical_condition_query.update(updated_medical_condition.dict(), synchronize_session=False)
    db.commit()
    return medical_condition_query.first()


#Delete medical condition 
@app.delete("/medical_condition/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_condition(id: int, db: Session = Depends(get_db)):

    medical_condition = db.query(models.MedicalCondition).filter(models.MedicalCondition.id == id)

    if medical_condition.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical condition with id: {id} does not exist")
    
    medical_condition.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

 
""" MEDICAL DEVICES APIs """ #API ERROR
#Create medical devices 
@app.post("/medical_device", status_code=status.HTTP_201_CREATED)
def create_medical_device(medical_device: schemas.MedicalDeviceCreate, db: Session = Depends(get_db)):
    new_medical_device = models.MedicalDevice(**medical_device.dict())
    db.add(new_medical_device)
    db.commit()
    db.refresh(new_medical_device)
    return new_medical_device

#Read one medical device  
@app.get("/medical_device/{id}", response_model=schemas.MedicalDeviceResponse)
def get_medical_device(id: int, db: Session = Depends(get_db)):
    medical_device = db.query(models.MedicalDevice).filter(models.MedicalDevice.id == id).first()

    if not medical_device:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical device with id: {id} was not found")
    return  medical_device

#Read All medical device 
@app.get("/medical_device", response_model=List[schemas.MedicalDeviceResponse])
def get_medical_devices(db: Session = Depends(get_db)):
    medical_devices = db.query(models.MedicalDevice).all()
    return medical_devices

#Update medical device  
@app.put("/medical_device/{id}", response_model=schemas.MedicalDeviceResponse)
def update_medical_device(id: int, updated_medical_device: schemas.MedicalDeviceCreate, db: Session = Depends(get_db)):

    medical_device_query = db.query(models.MedicalDevice).filter(models.MedicalDevice.id == id)

    medical_devices = medical_device_query.first()

    if medical_devices == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical device with id: {id} does not exist")
    
    medical_device_query.update(updated_medical_device.dict(), synchronize_session=False)
    db.commit()
    return medical_device_query.first()


#Delete medical device 
@app.delete("/medical_device/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_device(id: int, db: Session = Depends(get_db)):

    medical_device = db.query(models.MedicalDevice).filter(models.MedicalDevice.id == id)

    if medical_device.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical device with id: {id} does not exist")
    
    medical_device.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



""" MEDICAL IMAGES APIs """
#Create medical images 
@app.post("/medical_image", status_code=status.HTTP_201_CREATED)
def create_medical_image(medical_image: schemas.MedicalImageCreate, db: Session = Depends(get_db)):
    new_medical_image = models.MedicalImage(**medical_image.dict())
    db.add(new_medical_image)
    db.commit()
    db.refresh(new_medical_image)
    return new_medical_image

#Read one medical image  
@app.get("/medical_image/{id}", response_model=schemas.MedicalImageResponse)
def get_medical_image(id: int, db: Session = Depends(get_db)):
    medical_image = db.query(models.MedicalImage).filter(models.MedicalImage.id == id).first()

    if not medical_image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical image with id: {id} was not found")
    return  medical_image

#Read All medical images
@app.get("/medical_image", response_model=List[schemas.MedicalImageResponse])
def get_medical_images(db: Session = Depends(get_db)):
    medical_images = db.query(models.MedicalImage).all()
    return medical_images

#Update medical images  
@app.put("/medical_image/{id}", response_model=schemas.MedicalImageResponse)
def update_medical_image(id: int, updated_medical_image: schemas.MedicalImageCreate, db: Session = Depends(get_db)):

    medical_image_query = db.query(models.MedicalImage).filter(models.MedicalImage.id == id)

    medical_image = medical_image_query.first()

    if medical_image == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical image with id: {id} does not exist")
    
    medical_image_query.update(updated_medical_image.dict(), synchronize_session=False)
    db.commit()
    return medical_image_query.first()


#Delete medical image 
@app.delete("/medical_image/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_image(id: int, db: Session = Depends(get_db)):

    medical_image = db.query(models.MedicalImage).filter(models.MedicalImage.id == id)

    if medical_image.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical image with id: {id} does not exist")
    
    medical_image.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

""" MEDICAL NOTES APIs """
#Create medical notes 
@app.post("/medical_note", status_code=status.HTTP_201_CREATED)
def create_medical_note(medical_note: schemas.MedicalNoteCreate, db: Session = Depends(get_db)):
    new_medical_note = models.MedicalNote(**medical_note.dict())
    db.add(new_medical_note)
    db.commit()
    db.refresh(new_medical_note)
    return new_medical_note

#Read one medical note  
@app.get("/medical_note/{id}", response_model=schemas.MedicalNoteResponse)
def get_medical_note(id: int, db: Session = Depends(get_db)):
    medical_note = db.query(models.MedicalNote).filter(models.MedicalNote.id == id).first()

    if not medical_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical note with id: {id} was not found")
    return  medical_note

#Read All medical notes
@app.get("/medical_note", response_model=List[schemas.MedicalNoteResponse])
def get_medical_note(db: Session = Depends(get_db)):
    medical_notes = db.query(models.MedicalNote).all()
    return medical_notes

#Update medical note  
@app.put("/medical_note/{id}", response_model=schemas.MedicalNoteResponse)
def update_medical_note(id: int, updated_medical_note: schemas.MedicalNoteCreate, db: Session = Depends(get_db)):

    medical_note_query = db.query(models.MedicalNote).filter(models.MedicalNote.id == id)

    medical_note = medical_note_query.first()

    if medical_note == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical note with id: {id} does not exist")
    
    medical_note_query.update(updated_medical_note.dict(), synchronize_session=False)
    db.commit()
    return medical_note_query.first()


#Delete medical note 
@app.delete("/medical_note/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_note(id: int, db: Session = Depends(get_db)):

    medical_note = db.query(models.MedicalNote).filter(models.MedicalNote.id == id)

    if medical_note.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical note with id: {id} does not exist")
    
    medical_note.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

""" MEDICAL PROCEDURES APIs """
#Create medical procedure 
@app.post("/medical_procedure", status_code=status.HTTP_201_CREATED)
def create_medical_procedure(medical_procedure: schemas.MedicalProcedureCreate, db: Session = Depends(get_db)):
    new_medical_procedure = models.MedicalProcedure(**medical_procedure.dict())
    db.add(new_medical_procedure)
    db.commit()
    db.refresh(new_medical_procedure)
    return new_medical_procedure

#Read one medical procedure  
@app.get("/medical_procedure/{id}", response_model=schemas.MedicalProcedureResponse)
def get_medical_procedure(id: int, db: Session = Depends(get_db)):
    medical_procedure = db.query(models.MedicalProcedure).filter(models.MedicalProcedure.id == id).first()

    if not medical_procedure:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical procedure with id: {id} was not found")
    return  medical_procedure

#Read All medical procedures
@app.get("/medical_procedure", response_model=List[schemas.MedicalProcedureResponse])
def get_medical_procedure(db: Session = Depends(get_db)):
    medical_procedures = db.query(models.MedicalProcedure).all()
    return medical_procedures

#Update medical procedure  
@app.put("/medical_procedure/{id}", response_model=schemas.MedicalProcedureResponse)
def update_medical_procedure(id: int, updated_medical_procedure: schemas.MedicalProcedureCreate, db: Session = Depends(get_db)):

    medical_procedure_query = db.query(models.MedicalProcedure).filter(models.MedicalProcedure.id == id)

    medical_procedure = medical_procedure_query.first()

    if medical_procedure == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical procedure with id: {id} does not exist")
    
    medical_procedure_query.update(updated_medical_procedure.dict(), synchronize_session=False)
    db.commit()
    return medical_procedure_query.first()


#Delete medical procedure 
@app.delete("/medical_procedure/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_procedure(id: int, db: Session = Depends(get_db)):

    medical_procedure = db.query(models.MedicalProcedure).filter(models.MedicalProcedure.id == id)

    if medical_procedure.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical procedure with id: {id} does not exist")
    
    medical_procedure.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" MEDICAL STAFF APIs """
#Create medical staff 
@app.post("/medical_staff", status_code=status.HTTP_201_CREATED)
def create_medical_staff(medical_staff: schemas.MedicalStaffCreate, db: Session = Depends(get_db)):
    new_medical_staff = models.MedicalStaff(**medical_staff.dict())
    db.add(new_medical_staff)
    db.commit()
    db.refresh(new_medical_staff)
    return new_medical_staff

#Read one medical staff  
@app.get("/medical_staff/{id}", response_model=schemas.MedicalStaffResponse)
def get_medical_staff(id: int, db: Session = Depends(get_db)):
    medical_staff = db.query(models.MedicalStaff).filter(models.MedicalStaff.id == id).first()

    if not medical_staff:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical staff with id: {id} was not found")
    return  medical_staff

#Read All medical staff
@app.get("/medical_staff", response_model=List[schemas.MedicalStaffResponse])
def get_medical_staff(db: Session = Depends(get_db)):
    medical_staff = db.query(models.MedicalStaff).all()
    return medical_staff

#Update medical staff  
@app.put("/medical_staff/{id}", response_model=schemas.MedicalStaffResponse)
def update_medical_staff(id: int, updated_medical_staff: schemas.MedicalStaffCreate, db: Session = Depends(get_db)):

    medical_staff_query = db.query(models.MedicalStaff).filter(models.MedicalStaff.id == id)

    medical_staff = medical_staff_query.first()

    if medical_staff == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical staff with id: {id} does not exist")
    
    medical_staff_query.update(updated_medical_staff.dict(), synchronize_session=False)
    db.commit()
    return medical_staff_query.first()


#Delete medical staff 
@app.delete("/medical_staff/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_staff(id: int, db: Session = Depends(get_db)):

    medical_staff = db.query(models.MedicalStaff).filter(models.MedicalStaff.id == id)

    if medical_staff.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical staff with id: {id} does not exist")
    
    medical_staff.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" MEDICATION APIs """
#Create medication
@app.post("/medication", status_code=status.HTTP_201_CREATED)
def create_medication(medication: schemas.MedicationCreate, db: Session = Depends(get_db)):
    new_medication = models.Medication(**medication.dict())
    db.add(new_medication)
    db.commit()
    db.refresh(new_medication)
    return new_medication

#Read one medication  
@app.get("/medication/{id}", response_model=schemas.MedicationResponse)
def get_medication(id: int, db: Session = Depends(get_db)):
    medication = db.query(models.Medication).filter(models.Medication.id == id).first()

    if not medication:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medication with id: {id} was not found")
    return  medication

#Read All medication
@app.get("/medication", response_model=List[schemas.MedicationResponse])
def get_medication(db: Session = Depends(get_db)):
    medication = db.query(models.Medication).all()
    return medication

#Update medication  
@app.put("/medication/{id}", response_model=schemas.MedicationResponse)
def update_medication(id: int, updated_medication: schemas.MedicationCreate, db: Session = Depends(get_db)):

    medication_query = db.query(models.Medication).filter(models.Medication.id == id)

    medication = medication_query.first()

    if medication == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medication with id: {id} does not exist")
    
    medication_query.update(updated_medication.dict(), synchronize_session=False)
    db.commit()
    return medication_query.first()


#Delete medication 
@app.delete("/medication/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medication(id: int, db: Session = Depends(get_db)):

    medication = db.query(models.Medication).filter(models.Medication.id == id)

    if medication.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medication with id: {id} does not exist")
    
    medication.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



""" PATIENT CONSENT APIs """
#Create patient consent
@app.post("/patient_consent", status_code=status.HTTP_201_CREATED)
def create_patient_consent(patient_consent: schemas.PatientConsentCreate, db: Session = Depends(get_db)):
    patient_consent = models.PatientConsent(**patient_consent.dict())
    db.add(patient_consent)
    db.commit()
    db.refresh(patient_consent)
    return patient_consent

#Read single patient consent  
@app.get("/patient_consent/{id}", response_model=schemas.PatientConsentResponse)
def get_patient_consent(id: int, db: Session = Depends(get_db)):
    patient_consent = db.query(models.PatientConsent).filter(models.PatientConsent.id == id).first()

    if not patient_consent:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient consent with id: {id} was not found")
    return  patient_consent

#Read All patient consents
@app.get("/patient_consent", response_model=List[schemas.PatientConsentResponse])
def get_patient_consent(db: Session = Depends(get_db)):
    patient_consent = db.query(models.PatientConsent).all()
    return patient_consent

#Update patient consent   
@app.put("/patient_consent/{id}", response_model=schemas.PatientConsentResponse)
def update_patient_consent(id: int, updated_patient_consent: schemas.PatientConsentCreate, db: Session = Depends(get_db)):

    patient_consent_query = db.query(models.PatientConsent).filter(models.PatientConsent.id == id)

    patient_consent = patient_consent_query.first()

    if patient_consent == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient consent with id: {id} does not exist")
    
    patient_consent_query.update(updated_patient_consent.dict(), synchronize_session=False)
    db.commit()
    return patient_consent_query.first()


#Delete patient consent 
@app.delete("/patient_consent/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient_consent(id: int, db: Session = Depends(get_db)):

    patient_consent = db.query(models.PatientConsent).filter(models.PatientConsent.id == id)

    if patient_consent.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient consent with id: {id} does not exist")
    
    patient_consent.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" PATIENT FEEDBACK APIs """
#Create patient feedback
@app.post("/patient_feedback", status_code=status.HTTP_201_CREATED)
def create_patient_feedback(patient_feedback: schemas.PatientFeedbackCreate, db: Session = Depends(get_db)):
    patient_feedback = models.PatientFeedback(**patient_feedback.dict())
    db.add(patient_feedback)
    db.commit()
    db.refresh(patient_feedback)
    return patient_feedback

#Read single patient feedback  
@app.get("/patient_feedback/{id}", response_model=schemas.PatientFeedbackResponse)
def get_patient_feedback(id: int, db: Session = Depends(get_db)):
    patient_feedback = db.query(models.PatientFeedback).filter(models.PatientFeedback.id == id).first()

    if not patient_feedback:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient feedback with id: {id} was not found")
    return  patient_feedback

#Read All patient feedback
@app.get("/patient_feedback", response_model=List[schemas.PatientFeedbackResponse])
def get_patient_feedback(db: Session = Depends(get_db)):
    patient_feedback = db.query(models.PatientFeedback).all()
    return patient_feedback

#Update patient feedback   
@app.put("/patient_feedback/{id}", response_model=schemas.PatientFeedbackResponse)
def update_patient_feedback(id: int, updated_patient_feedback: schemas.PatientFeedbackCreate, db: Session = Depends(get_db)):

    patient_feedback_query = db.query(models.PatientFeedback).filter(models.PatientFeedback.id == id)

    patient_feedback = patient_feedback_query.first()

    if patient_feedback == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient feedback with id: {id} does not exist")
    
    patient_feedback_query.update(updated_patient_feedback.dict(), synchronize_session=False)
    db.commit()
    return patient_feedback_query.first()


#Delete patient feedback 
@app.delete("/patient_feedback/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient_feedback(id: int, db: Session = Depends(get_db)):

    patient_feedback = db.query(models.PatientFeedback).filter(models.PatientFeedback.id == id)

    if patient_feedback.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient feedback with id: {id} does not exist")
    
    patient_feedback.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



""" PATIENT VISIT APIs """
#Create patient visit
@app.post("/patient_visit", status_code=status.HTTP_201_CREATED)
def create_patient_visit(patient_visit: schemas.PatientVisitCreate, db: Session = Depends(get_db)):
    patient_visit = models.PatientVisit(**patient_visit.dict())
    db.add(patient_visit)
    db.commit()
    db.refresh(patient_visit)
    return patient_visit

#Read single patient visit  
@app.get("/patient_visit/{id}", response_model=schemas.PatientVisitResponse)
def get_patient_visit(id: int, db: Session = Depends(get_db)):
    patient_visit = db.query(models.PatientVisit).filter(models.PatientVisit.id == id).first()

    if not patient_visit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient visit with id: {id} was not found")
    return  patient_visit

#Read All patient visit
@app.get("/patient_visit", response_model=List[schemas.PatientVisitResponse])
def get_patient_visit(db: Session = Depends(get_db)):
    patient_visit = db.query(models.PatientVisit).all()
    return patient_visit

#Update patient visit   
@app.put("/patient_visit/{id}", response_model=schemas.PatientVisitResponse)
def update_patient_visit(id: int, updated_patient_visit: schemas.PatientVisitCreate, db: Session = Depends(get_db)):

    patient_visit_query = db.query(models.PatientVisit).filter(models.PatientVisit.id == id)

    patient_visit = patient_visit_query.first()

    if patient_visit == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient visit with id: {id} does not exist")
    
    patient_visit_query.update(updated_patient_visit.dict(), synchronize_session=False)
    db.commit()
    return patient_visit_query.first()


#Delete patient visit 
@app.delete("/patient_visit/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient_visit(id: int, db: Session = Depends(get_db)):

    patient_visit = db.query(models.PatientVisit).filter(models.PatientVisit.id == id)

    if patient_visit.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient visit with id: {id} does not exist")
    
    patient_visit.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" PATIENT APIs """
#Create patient 
@app.post("/patient", status_code=status.HTTP_201_CREATED)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    patient = models.Patient(**patient.dict())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

#Read single patient
@app.get("/patient/{id}", response_model=schemas.PatientResponse)
def get_patient(id: int, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == id).first()

    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id: {id} was not found")
    return  patient

#Read All patient 
@app.get("/patient", response_model=List[schemas.PatientResponse])
def get_patient(db: Session = Depends(get_db)):
    patient = db.query(models.Patient).all()
    return patient

#Update patient   
@app.put("/patient/{id}", response_model=schemas.PatientResponse)
def update_patient(id: int, updated_patient: schemas.PatientCreate, db: Session = Depends(get_db)):

    patient_query = db.query(models.Patient).filter(models.Patient.id == id)

    patient = patient_query.first()

    if patient == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id: {id} does not exist")
    
    patient_query.update(updated_patient.dict(), synchronize_session=False)
    db.commit()
    return patient_query.first()


#Delete patient 
@app.delete("/patient/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(id: int, db: Session = Depends(get_db)):

    patient = db.query(models.Patient).filter(models.Patient.id == id)

    if patient.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id: {id} does not exist")
    
    patient.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

""" PRESCRIPTION """
#Create prescription 
@app.post("/prescription", status_code=status.HTTP_201_CREATED)
def create_prescription(prescription: schemas.PrescriptionCreate, db: Session = Depends(get_db)):
    prescription = models.Prescription(**prescription.dict())
    db.add(prescription)
    db.commit()
    db.refresh(prescription)
    return prescription

#Read single prescription
@app.get("/prescription/{id}", response_model=schemas.PrescriptionResponse)
def get_prescription(id: int, db: Session = Depends(get_db)):
    prescription = db.query(models.Prescription).filter(models.Prescription.id == id).first()

    if not prescription:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Prescription with id: {id} was not found")
    return  prescription

#Read All prescription 
@app.get("/prescription", response_model=List[schemas.PrescriptionResponse])
def get_prescription(db: Session = Depends(get_db)):
    prescriptions = db.query(models.Prescription).all()
    return prescriptions

#Update prescription   
@app.put("/prescription/{id}", response_model=schemas.PrescriptionResponse)
def update_prescription(id: int, updated_prescription: schemas.PrescriptionCreate, db: Session = Depends(get_db)):

    prescription_query = db.query(models.Prescription).filter(models.Prescription.id == id)

    prescription = prescription_query.first()

    if prescription == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Prescription with id: {id} does not exist")
    
    prescription_query.update(updated_prescription.dict(), synchronize_session=False)
    db.commit()
    return prescription_query.first()


#Delete prescription 
@app.delete("/prescription/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_prescription(id: int, db: Session = Depends(get_db)):

    prescription = db.query(models.Prescription).filter(models.Prescription.id == id)

    if prescription.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Prescription with id: {id} does not exist")
    
    prescription.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" REFERRALS """
#Create referrals 
@app.post("/referral", status_code=status.HTTP_201_CREATED)
def create_referral(referral: schemas.ReferralCreate, db: Session = Depends(get_db)):
    referral = models.Referral(**referral.dict())
    db.add(referral)
    db.commit()
    db.refresh(referral)
    return referral

#Read single referral
@app.get("/referral/{id}", response_model=schemas.ReferralResponse)
def get_referral(id: int, db: Session = Depends(get_db)):
    referral = db.query(models.Referral).filter(models.Referral.id == id).first()

    if not referral:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Referral with id: {id} was not found")
    return  referral

#Read All referrals 
@app.get("/referral", response_model=List[schemas.ReferralResponse])
def get_referrals(db: Session = Depends(get_db)):
    referrals = db.query(models.Referral).all()
    return referrals

#Update referrals   
@app.put("/referral/{id}", response_model=schemas.ReferralResponse)
def update_referral(id: int, updated_referral: schemas.ReferralCreate, db: Session = Depends(get_db)):

    referral_query = db.query(models.Referral).filter(models.Referral.id == id)

    referral = referral_query.first()

    if referral == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Referral with id: {id} does not exist")
    
    referral_query.update(updated_referral.dict(), synchronize_session=False)
    db.commit()
    return referral_query.first()


#Delete referral 
@app.delete("/referral/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_referral(id: int, db: Session = Depends(get_db)):

    referral = db.query(models.Referral).filter(models.Referral.id == id)

    if referral.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Referral with id: {id} does not exist")
    
    referral.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

""" USERS APIs"""
#Create user account 
@app.post("/user_account", status_code=status.HTTP_201_CREATED)
def create_user_account(user_account: schemas.UserCreate, db: Session = Depends(get_db)):
    user_account = models.User(**user_account.dict())
    db.add(user_account)
    db.commit()
    db.refresh(user_account)
    return user_account

#Read single user account 
@app.get("/user_account/{id}", response_model=schemas.UserResponse)
def get_user_account(id: int, db: Session = Depends(get_db)):
    user_account = db.query(models.User).filter(models.User.id == id).first()

    if not user_account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User account with id: {id} was not found")
    return  user_account

#Read All user account  
@app.get("/user_account", response_model=List[schemas.UserResponse])
def get_user_accounts(db: Session = Depends(get_db)):
    user_accounts = db.query(models.User).all()
    return user_accounts

#Update user account    
@app.put("/user_account/{id}", response_model=schemas.UserResponse)
def update_user_account(id: int, updated_user_account: schemas.UserCreate, db: Session = Depends(get_db)):

    user_account_query = db.query(models.User).filter(models.User.id == id)

    user_account = user_account_query.first()

    if user_account == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User account with id: {id} does not exist")
    
    user_account_query.update(updated_user_account.dict(), synchronize_session=False)
    db.commit()
    return user_account_query.first()


#Delete user account  
@app.delete("/user_account/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_account(id: int, db: Session = Depends(get_db)):

    user_account = db.query(models.User).filter(models.User.id == id)

    if user_account.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User account with id: {id} does not exist")
    
    user_account.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

""" VACCINATION APIs """
#Create vaccination 
@app.post("/vaccination", status_code=status.HTTP_201_CREATED)
def create_vaccination(vaccination: schemas.VaccinationCreate, db: Session = Depends(get_db)):
    vaccination = models.Vaccination(**vaccination.dict())
    db.add(vaccination)
    db.commit()
    db.refresh(vaccination)
    return vaccination

#Read single vaccination 
@app.get("/vaccination/{id}", response_model=schemas.VaccinationResponse)
def get_vaccination(id: int, db: Session = Depends(get_db)):
    vaccination = db.query(models.Vaccination).filter(models.Vaccination.id == id).first()

    if not vaccination:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Vaccination with id: {id} was not found")
    return  vaccination

#Read All vaccination  
@app.get("/vaccination", response_model=List[schemas.VaccinationResponse])
def get_vaccination(db: Session = Depends(get_db)):
    vaccination = db.query(models.Vaccination).all()
    return vaccination

#Update vaccination    
@app.put("/vaccination/{id}", response_model=schemas.VaccinationResponse)
def update_vaccination(id: int, updated_vaccination: schemas.VaccinationCreate, db: Session = Depends(get_db)):

    vaccination_query = db.query(models.Vaccination).filter(models.Vaccination.id == id)

    vaccination = vaccination_query.first()

    if vaccination == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Vaccination with id: {id} does not exist")
    
    vaccination_query.update(updated_vaccination.dict(), synchronize_session=False)
    db.commit()
    return vaccination_query.first()


#Delete vaccination  
@app.delete("/vaccination/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vaccination(id: int, db: Session = Depends(get_db)):

    vaccination = db.query(models.Vaccination).filter(models.Vaccination.id == id)

    if vaccination.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Vaccination with id: {id} does not exist")
    
    vaccination.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


""" VITAL SIGN APIs """
#Create vital sign 
@app.post("/vital_sign", status_code=status.HTTP_201_CREATED)
def create_vital_sign(vital_sign: schemas.VitalSignCreate, db: Session = Depends(get_db)):
    vital_sign = models.VitalSign(**vital_sign.dict())
    db.add(vital_sign)
    db.commit()
    db.refresh(vital_sign)
    return vital_sign

#Read single vital sign 
@app.get("/vital_sign/{id}", response_model=schemas.VitalSignResponse)
def get_vital_sign(id: int, db: Session = Depends(get_db)):
    vital_sign = db.query(models.VitalSign).filter(models.VitalSign.id == id).first()

    if not vital_sign:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Vital sign with id: {id} was not found")
    return  vital_sign

#Read All vaccination  
@app.get("/vital_sign", response_model=List[schemas.VitalSignResponse])
def get_vital_sign(db: Session = Depends(get_db)):
    vital_sign = db.query(models.VitalSign).all()
    return vital_sign

#Update vaccination    
@app.put("/vital_sign/{id}", response_model=schemas.VitalSignResponse)
def update_vital_sign(id: int, updated_vital_sign: schemas.VitalSignCreate, db: Session = Depends(get_db)):

    vital_sign_query = db.query(models.VitalSign).filter(models.VitalSign.id == id)

    vital_sign = vital_sign_query.first()

    if vital_sign == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Vital sign with id: {id} does not exist")
    
    vital_sign_query.update(updated_vital_sign.dict(), synchronize_session=False)
    db.commit()
    return vital_sign_query.first()


#Delete vaccination  
@app.delete("/vital_sign/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vital_sign(id: int, db: Session = Depends(get_db)):

    vital_sign = db.query(models.VitalSign).filter(models.VitalSign.id == id)

    if vital_sign.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Vital sign with id: {id} does not exist")
    
    vital_sign.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


"""WARD APIs """
#Create ward 
@app.post("/ward", status_code=status.HTTP_201_CREATED)
def create_ward(ward: schemas.WardCreate, db: Session = Depends(get_db)):
    ward = models.Ward(**ward.dict())
    db.add(ward)
    db.commit()
    db.refresh(ward)
    return ward

#Read single ward 
@app.get("/ward/{id}", response_model=schemas.WardResponse)
def get_ward(id: int, db: Session = Depends(get_db)):
    ward = db.query(models.Ward).filter(models.Ward.id == id).first()

    if not ward:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Ward with id: {id} was not found")
    return  ward

#Read All ward  
@app.get("/ward", response_model=List[schemas.WardResponse])
def get_ward(db: Session = Depends(get_db)):
    ward = db.query(models.Ward).all()
    return ward

#Update ward    
@app.put("/ward/{id}", response_model=schemas.WardResponse)
def update_ward(id: int, updated_ward: schemas.WardCreate, db: Session = Depends(get_db)):

    ward_query = db.query(models.Ward).filter(models.Ward.id == id)

    ward = ward_query.first()

    if ward == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Ward with id: {id} does not exist")
    
    ward_query.update(updated_ward.dict(), synchronize_session=False)
    db.commit()
    return ward_query.first()


#Delete ward  
@app.delete("/ward/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ward(id: int, db: Session = Depends(get_db)):

    ward = db.query(models.Ward).filter(models.Ward.id == id)

    if ward.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Ward with id: {id} does not exist")
    
    ward.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



