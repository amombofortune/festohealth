from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine
import time
from fastapi.middleware.cors import CORSMiddleware
from .routers import administrator, admission, adverse_reaction_type, adverse_reaction, allergy, \
appointment_reminder, appointment_type, appointment, bed_assignment, bed, billing, chronic_condition,\
country, department, diagnosis, disease, doctor, genetic_condition, hospital, immunization, insurance_claim, \
insurance_provider_type, insurance_provider, it_staff, lab_technician, lab_test_result, lab_test, auth, \
medical_condition, medical_device, medical_images, medical_note, medical_procedure, medication_alert,\
medication, nurses, patient_consent, patient_feedback, patient_visit, patient, pharmacist, prescription, \
receptionist, referral, specialty, time_slot, user, vaccination, vital_sign, ward, work_schedule

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",  # webapp
    "http://localhost:19006"  # mobileapp

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)


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


app.include_router(administrator.router)
app.include_router(admission.router)
app.include_router(adverse_reaction_type.router)
app.include_router(adverse_reaction.router)
app.include_router(allergy.router)
app.include_router(appointment_reminder.router)
app.include_router(appointment_type.router)
app.include_router(appointment.router)
app.include_router(bed_assignment.router)
app.include_router(bed.router)
app.include_router(billing.router)
app.include_router(chronic_condition.router)
app.include_router(country.router)
app.include_router(department.router)
app.include_router(diagnosis.router)
app.include_router(disease.router)
app.include_router(doctor.router)
app.include_router(genetic_condition.router)
app.include_router(hospital.router)
app.include_router(immunization.router)
app.include_router(insurance_claim.router)
app.include_router(insurance_provider_type.router)
app.include_router(insurance_provider.router)
app.include_router(it_staff.router)
app.include_router(lab_technician.router)
app.include_router(lab_test_result.router)
app.include_router(lab_test.router)
app.include_router(auth.router)
app.include_router(medical_condition.router)
app.include_router(medical_device.router)
app.include_router(medical_images.router)
app.include_router(medical_note.router)
app.include_router(medical_procedure.router)
app.include_router(medication_alert.router)
app.include_router(medication.router)
app.include_router(nurses.router)
app.include_router(patient_consent.router)
app.include_router(patient_feedback.router)
app.include_router(patient_visit.router)
app.include_router(patient.router)
app.include_router(pharmacist.router)
app.include_router(prescription.router)
app.include_router(receptionist.router)
app.include_router(referral.router)
app.include_router(specialty.router)
app.include_router(time_slot.router)
app.include_router(user.router)
app.include_router(vaccination.router)
app.include_router(vital_sign.router)
app.include_router(ward.router)
app.include_router(work_schedule.router)

@app.get("/")
def root():
    return {"message": "Hello World"}