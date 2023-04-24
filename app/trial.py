import sqlalchemy
from .database import Session
from .models import Admission, AdverseReaction, Appointment, AppointmentReminder, Billing, CareTeam, ChronicCondition, Country, Diagnosis, Disease, Doctor, GeneticCondition, Hospital, Department, Bed, BedAssignment, Imaging, Immunization, InsuranceClaim, InsuranceCompany, LabTest, MedicalAlert, MedicalCondition, MedicalDevice, MedicalImage, MedicalProcedure, MedicalStaff, Medication, Patient, Allergy, PatientConsent, PatientFeedback, PatientVisit, Referral, UserAccount, Vaccination, VitalSign
from datetime import date, datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password@localhost/health'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


""" PATIENT """
session = Session()
# create a patient
patient = Patient(
    patient_id= 4,
    admission_date=datetime.date(1970, 1, 1),
    discharge_date=datetime.date(1970, 10, 10),
)
session.add(patient)
session.commit()
""" ADMISSION """
session = Session()

# create an admission for the patient
admission = Admission(
    patient=patient,
    admission_date=datetime.now(),
    admission_date=datetime.date(1970, 1, 1),
    discharge_date=datetime.date(1970, 10, 10),
)
session.add(admission)
session.commit()

# find all admissions for a given patient
admissions = session.query(Admission).filter_by(patient_id=patient.id).all()



""" ALLERGY """
session = Session()

# create a patient
patient = Patient(name='John Doe')
session.add(patient)
session.commit()

# create an allergy
allergy = Allergy(name='Peanuts')
session.add(allergy)
session.commit()

# associate the allergy with the patient
patient.allergies.append(allergy)
session.commit()

# find all patients with a given allergy
patients_with_peanut_allergy = session.query(Patient).join(Patient.allergies).filter(Allergy.name == 'Peanuts').all()

# find all allergies for a given patient
patient_allergies = session.query(Allergy).join(Allergy.patients).filter(Patient.name == 'John Doe').all()

""" ADVERSE REACTIONS """
session = Session()

# create a patient
patient = Patient(name='John Doe')
session.add(patient)
session.commit()

# create an adverse reaction
reaction = AdverseReaction(allergen='Peanuts', reaction='Anaphylaxis', date=datetime.now(), patient=patient)
session.add(reaction)
session.commit()

# find all adverse reactions for a given patient
reactions = session.query(AdverseReaction).filter_by(patient_id=patient.id).all()

# find all patients with a given allergen
patients_with_peanut_allergy = session.query(Patient).join(Patient.adverse_reactions).filter(AdverseReaction.allergen == 'Peanuts').all()


""" APPOINTMENT REMINDERS """
session = Session()

# create a patient
patient = Patient(name='John Doe')
session.add(patient)
session.commit()

# create a doctor
doctor = Doctor(name='Jane Smith')
session.add(doctor)
session.commit()

# create an appointment reminder
reminder = AppointmentReminder(
    patient=patient,
    doctor=doctor,
    appointment_date=datetime.now() + timedelta(days=1),
    message='You have an appointment tomorrow at 10am'
)
session.add(reminder)
session.commit()

# find all appointment reminders for a given patient
reminders = session.query(AppointmentReminder).filter_by(patient_id=patient.id).all()

# find all appointment reminders for a given doctor
reminders = session.query(AppointmentReminder).filter_by(doctor_id=doctor.id).all()

""" APPOINTMENT """
session = Session()

# create a patient
patient = Patient(name='John Doe')
session.add(patient)
session.commit()

# create a doctor
doctor = Doctor(name='Jane Smith')
session.add(doctor)
session.commit()

# create an appointment
appointment = Appointment(
    patient=patient,
    doctor=doctor,
    appointment_date=datetime.now() + timedelta(days=1),
    appointment_type='checkup'
)
session.add(appointment)
session.commit()

# find all appointments for a given patient
appointments = session.query(Appointment).filter_by(patient_id=patient.id).all()

# find all appointments for a given doctor
appointments = session.query(Appointment).filter_by(doctor_id=doctor.id).all()

"""BED """
session = Session()

# create a hospital
hospital = Hospital(name='Karen Hospital')
session.add(hospital)
session.commit()

# create a department in the hospital
department = Department(name='Theatre', hospital=hospital)
session.add(department)
session.commit()

# create a bed in the department
bed = Bed(number_of_beds=10, department=department)
session.add(bed)
session.commit()

# assign a patient to the bed
bed_assignment = BedAssignment(bed=bed, patient='John Doe', is_occupied=True, occupied_start_time=datetime.now())
session.add(bed_assignment)
session.commit()

# find all occupied beds
occupied_beds = session.query(BedAssignment).filter(BedAssignment.is_occupied == True).all()

# find all bed assignments for a given patient
bed_assignments = session.query(BedAssignment).filter(BedAssignment.patient == 'John Doe').all()

""" BILLING """
session = Session()

# create a patient
patient = Patient(name='John Doe')
session.add(patient)
session.commit()

# create a billing
billing = Billing(
    patient=patient,
    billing_date=datetime.now(),
    total_amount=100.0
)
session.add(billing)
session.commit()

# find all billings for a given patient
billings = session.query(Billing).filter_by(patient_id=patient.id).all()

""" CARE TEAM """
session = Session()

# create an admission
admission = Admission(
    patient_id=1,
    admission_date=datetime.now()
)
session.add(admission)
session.commit()

# create care team members
doctor = CareTeam(
    admission=admission,
    member_name='Dr. John Smith',
    member_role='Primary physician'
)
nurse = CareTeam(
    admission=admission,
    member_name='Jane Doe, RN',
    member_role='Nurse'
)
session.add(doctor)
session.add(nurse)
session.commit()

# find all care team members for a given admission
care_team = session.query(CareTeam).filter_by(admission_id=admission.id).all()

""" CHRONIC CONDITIONS """
session = Session()

# create a patient
patient = Patient(
    name='John Doe',
    dob=datetime.date(1970, 1, 1),
    gender='M'
)
session.add(patient)
session.commit()

# create a chronic condition for the patient
chronic_condition = ChronicCondition(
    patient=patient,
    condition='Diabetes',
    description='High blood sugar levels'
)
session.add(chronic_condition)
session.commit()

# find all chronic conditions for a given patient
conditions = session.query(ChronicCondition).filter_by(patient_id=patient.id).all()

""" COUNTRY """
session = Session()

# create a country
country = Country(
    name='United States'
)
session.add(country)
session.commit()

# create a hospital in the country
hospital = Hospital(
    name='Example Hospital',
    country=country
)
session.add(hospital)
session.commit()

# create a doctor in the country
doctor = Doctor(
    name='John Smith',
    country=country
)
session.add(doctor)
session.commit()

# create a patient in the country
patient = Patient(
    name='Jane Doe',
    country=country
)
session.add(patient)
session.commit()

# find all hospitals in a given country
hospitals = session.query(Hospital).filter_by(country_id=country.id).all()

# find all doctors in a given country
doctors = session.query(Doctor).filter_by(country_id=country.id).all()

# find all patients in a given country
patients = session.query(Patient).filter_by(country_id=country.id).all()

""" DEPARTMENT """
session = Session()

# create a hospital
hospital = Hospital(
    name='Example Hospital'
)
session.add(hospital)
session.commit()

# create a department in the hospital
department = Department(
    name='Cardiology',
    hospital=hospital
)
session.add(department)
session.commit()

# create a doctor in the department
doctor = Doctor(
    name='John Smith',
    department=department
)
session.add(doctor)
session.commit()

# create a team member in the department
team_member = MedicalStaff(
    name='Jane Doe',
    department=department
)
session.add(team_member)
session.commit()

# find all departments in a given hospital
departments = session.query(Department).filter_by(hospital_id=hospital.id).all()

# find all doctors in a given department
doctors = session.query(Doctor).filter_by(department_id=department.id).all()

# find all team members in a given department
team_members = session.query(MedicalStaff).filter_by(department_id=department.id).all()

""" DIAGNOSIS """
session = Session()

# create a disease
disease = Disease(
    name='COVID-19'
)
session.add(disease)
session.commit()

# create a diagnosis for the disease
diagnosis = Diagnosis(
    name='Positive PCR test',
    disease=disease
)
session.add(diagnosis)
session.commit()

# find all diagnoses for a given disease
diagnoses = session.query(Diagnosis).filter_by(disease_id=disease.id).all()

# find the disease for a given diagnosis
disease = session.query(Disease).filter_by(id=diagnosis.disease_id).one()

""" DISEASES """
session = Session()

# create a disease
disease = Disease(
    name='COVID-19'
)
session.add(disease)
session.commit()

# find a disease by name
disease = session.query(Disease).filter_by(name='COVID-19').one()

# find all diagnoses for a given disease
diagnoses = session.query(Diagnosis).filter_by(disease_id=disease.id).all()

""" DOCTOR """
session = Session()

# create a doctor
doctor = Doctor(
    name='John Doe',
    specialty='Cardiology'
)
session.add(doctor)
session.commit()

# find a doctor by name
doctor = session.query(Doctor).filter_by(name='John Doe').one()

# find all appointments for a given doctor
appointments = session.query(Appointment).filter_by(doctor_id=doctor.id).all()

"""GENETIC CONDITION"""
session = Session()

# create a new genetic condition for a patient
patient = session.query(Patient).filter_by(id=1).first()
genetic_condition = GeneticCondition(name='Cystic Fibrosis', description='A genetic disorder that affects the lungs, pancreas, and other organs', patient=patient)
session.add(genetic_condition)
session.commit()

# retrieve all genetic conditions for a patient
patient_genetic_conditions = session.query(GeneticCondition).filter_by(patient=patient).all()
for condition in patient_genetic_conditions:
    print(condition.name, condition.description)

# find a genetic condition with id=1
genetic_condition = session.query(GeneticCondition).filter_by(id=1).first()
if genetic_condition:
    print("Genetic condition found:", genetic_condition.name)
else:
    print("Genetic condition not found")

""" HOSPITAL """
# Create a session object using the engine
session = Session()

# Create a new Hospital object
new_hospital = Hospital(
    name='Example Hospital',
    address='123 Main St',
    city='Anytown',
    state='CA',
    zip_code='12345',
    phone='555-555-1234',
    website='http://examplehospital.com',
    rating=4.5,
    date_established=date(1980, 1, 1)
)

# Add the new hospital to the session and commit the changes
session.add(new_hospital)
session.commit()

# Close the session
session.close()

# Query all hospitals
hospitals = session.query(Hospital).all()

# Print the results
for hospital in hospitals:
    print(hospital.name, hospital.address, hospital.city, hospital.state, hospital.zip_code)

# Close the session
session.close()

# Create a session object using the engine
session = Session()

# Query hospitals in CA with a rating > 4.0, sorted by name
hospitals = session.query(Hospital).filter(Hospital.state == 'CA', Hospital.rating > 4.0).order_by(Hospital.name).all()

# Print the results
for hospital in hospitals:
    print(hospital.name, hospital.address, hospital.city, hospital.state, hospital.zip_code, hospital.rating)

# Close the session
session.close()

""" IMAGING """
from sqlalchemy.orm import Session

# Create a session object using the engine
session = Session()

# Create a new Imaging object
new_imaging = Imaging(
    patient_id=1,
    doctor_id=1,
    image_data=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x02\x00\x00\x00\x01\x00\x08\x02\x00\x00\x00\xa4a\xf6\xad\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x07tIME\x07\xe6\x03\x1f\x12\x1b\x11B7Q\x00\x00\x00\tpIDAT\x18\xd3c0\x0a\x83\x01\x00\x05\xe4\xfd\xad\\\x00\x00\x00\x00IEND\xaeB`\x82',
    image_type='PNG'
)

# Add the new imaging record to the session and commit the changes
session.add(new_imaging)
session.commit()

# Close the session
session.close()

# Create a session object using the engine
session = Session()

# Query imaging records for patient ID 1
imaging_records = session.query(Imaging).filter_by(patient_id=1).all()

# Print the results
for record in imaging_records:
    print(record.id, record.patient_id, record.doctor_id, record.image_type)

# Close the session
session.close()

# Create a session object using the engine
session = Session()

# Query imaging records for patients with last name 'Smith', and include patient and doctor names
imaging_records = session.query(Imaging, Patient, Doctor).join(Patient).join(Doctor).filter(Patient.last_name == 'Smith').order_by(Imaging.id).all()

# Print the results
for record, patient, doctor in imaging_records:
    print(record.id, record.patient_id, record.doctor_id, record.image_type)

""" IMMUNIZATION """
# Create a session object using the engine
session = Session()

# Create a new Immunization object
new_immunization = Immunization(
    patient_id=1,
    vaccine_name='COVID-19',
    dose=1,
    date_given='2022-03-28'
)

# Add the new immunization record to the session and commit the changes
session.add(new_immunization)
session.commit()

# Close the session
session.close()

# Create a session object using the engine
session = Session()

# Query immunization records for patient ID 1
immunization_records = session.query(Immunization).filter_by(patient_id=1).all()

# Print the results
for record in immunization_records:
    print(record.id, record.patient_id, record.vaccine_name, record.dose, record.date_given)

# Close the session
session.close()

# Create a session object using the engine
session = Session()

# Query immunization records for patients aged 25, and include patient name
immunization_records = session.query(Immunization, Patient).join(Patient).filter(Patient.age == 25).order_by(Immunization.id).all()

# Print the results
for record, patient in immunization_records:
    print(record.id, patient.first_name, patient.last_name, record.vaccine_name, record.dose, record.date_given)

# Close the session
session.close()

""" INSURANCE CLAIMS """
from sqlalchemy.orm import Session

# Create a session object using the engine
session = Session()

# Create a new InsuranceClaim object
new_claim = InsuranceClaim(
    patient_id=1,
    insurance_company='ABC Insurance',
    claim_amount=500.0,
    date_of_claim='2022-03-28'
)

# Add the new claim record to the session and commit the changes
session.add(new_claim)
session.commit()

# Close the session
session.close()

# Create a session object using the engine
session = Session()

# Query insurance claim records for patient ID 1
claim_records = session.query(InsuranceClaim).filter_by(patient_id=1).all()

# Print the results
for record in claim_records:
    print(record.id, record.patient_id, record.insurance_company, record.claim_amount, record.date_of_claim)

# Close the session
session.close()

# Create a session object using the engine
session = Session()

# Query insurance claim records for patients aged 25, and include patient name
claim_records = session.query(InsuranceClaim, Patient).join(Patient).filter(Patient.age == 25).order_by(InsuranceClaim.id).all()

# Print the results
for record, patient in claim_records:
    print(record.id, patient.first_name, patient.last_name, record.insurance_company, record.claim_amount, record.date_of_claim)

# Close the session
session.close()

""" INSURANCE COMPANIES"""
from sqlalchemy.orm import Session

# Create a session object using the engine
session = Session()

# Create a new InsuranceCompany object
new_company = InsuranceCompany(
    name='XYZ Insurance',
    address='123 Main St, Anytown, USA',
    phone_number='555-1234'
)

# Add the new company record to the session and commit the changes
session.add(new_company)
session.commit()

# Close the session
session.close()

# Create a session object using the engine
session = Session()

# Query all insurance company records, and include their associated claims
company_records = session.query(InsuranceCompany).options(\
    sqlalchemy.orm.joinedload(InsuranceCompany.claims)).all()

# Print the results
for company in company_records:
    print(f"Company ID: {company.id}")
    print(f"Name: {company.name}")
    print(f"Address: {company.address}")
    print(f"Phone number: {company.phone_number}")
    print("Claims:")
    for claim in company.claims:
        print(f"\tClaim ID: {claim.id}")
        print(f"\tPatient ID: {claim.patient_id}")
        print(f"\tClaim amount: {claim.claim_amount}")
        print(f"\tDate of claim: {claim.date_of_claim}")
    print()

# Close the session
session.close()

""" LAB TESTS """
from sqlalchemy.orm import Session

# Create a session object using the engine
session = Session()

# Query the patient and doctor records
patient = session.query(Patient).filter_by(id=1).first()
doctor = session.query(Doctor).filter_by(id=1).first()

# Create a new LabTest object
new_test = LabTest(
    test_name='Blood Test',
    result='Normal',
    patient_id=patient.id,
    doctor_id=doctor.id,
)

# Add the new lab test record to the session and commit the changes
session.add(new_test)
session.commit()

# Close the session
session.close()

# Create a session object using the engine
session = Session()

# Query all lab test records, and include the associated doctor
test_records = session.query(LabTest).options(\
    sqlalchemy.orm.joinedload(LabTest.doctor)).all()

# Print the results
for test in test_records:
    print(f"Test ID: {test.id}")
    print(f"Test name: {test.test_name}")
    print(f"Result: {test.result}")
    print(f"Patient ID: {test.patient_id}")
    print(f"Doctor ID: {test.doctor_id}")
    print(f"Doctor name: {test.doctor.name}")
    print()

# Close the session
session.close()

"""MEDICAL ALERTS"""
session = Session()

# create a new alert object and add it to the session
new_alert = MedicalAlert(patient_id=1, alert_type='Medication Reminder', message='Take your medication at 8pm', created_at=datetime.now())
session.add(new_alert)
session.commit()

# query all alerts for a specific patient
patient_alerts = session.query(MedicalAlert).filter_by(patient_id=1).all()

# iterate over the alerts and print the message
for alert in patient_alerts:
    print(alert.message)

"""MEDICAL CONDITION """
# create a session
session = Session()

# create a new condition object and add it to the session
new_condition = MedicalCondition(patient_id=1, name='Hypertension', description='High blood pressure')
session.add(new_condition)
session.commit()

# query all conditions for a specific patient
patient_conditions = session.query(MedicalCondition).filter_by(patient_id=1).all()

# iterate over the conditions and print the name and description
for condition in patient_conditions:
    print(condition.name + ': ' + condition.description)

"""MEDICAL DEVICES"""
session = Session()

# create a new medical device object and add it to the session
new_device = MedicalDevice(name='ECG Monitor', serial_number='1234', hospital_id=1, department_id=2)
session.add(new_device)
session.commit()

# query all devices registered to a specific hospital department
department_devices = session.query(MedicalDevice).filter_by(department_id=2).all()

# iterate over the devices and print the name and serial number
for device in department_devices:
    print(device.name + ': ' + device.serial_number)

""" MEDICAL IMAGES """
session = Session()

# Create a new patient
patient = Patient(name='John Doe', age=35)
session.add(patient)

# Add an image to the patient's list of images
image_data = open('image.jpg', 'rb').read()
image = MedicalImage(name='Image 1', data=image_data, patient=patient)
session.add(image)

session.commit()

session = Session()

# Query all patients and their associated images
patients = session.query(Patient).all()
for patient in patients:
    print(f"Patient {patient.name}, {patient.age} years old")
    for image in patient.images:
        print(f"\tImage {image.name}")

# Query all images with a specific name
images = session.query(MedicalImage).filter_by(name='Image 1').all()
for image in images:
    print(f"Image {image.name} belongs to {image.patient.name}")

""" MEDICAL PROCEDURES """
session = Session()

# Retrieve a patient from the database
patient = session.query(Patient).filter_by(name='John Doe').one()

# Create a new medical procedure for the patient
procedure = MedicalProcedure(name='MRI scan', date=date(2023, 4, 7), patient=patient)
session.add(procedure)

session.commit()

# Retrieve a medical procedure with a specific id
procedure = session.query(MedicalProcedure).filter_by(id=1).one()

# Print the name and date of the procedure
print(f"Procedure name: {procedure.name}")
print(f"Procedure date: {procedure.date}")

""" MEDICAL STAFF """
session = Session()

# Create a new staff member
staff_member = MedicalStaff(name='Jane Doe', role='nurse')
session.add(staff_member)

session.commit()

# Retrieve the new staff member with a specific id
staff_member = session.query(MedicalStaff).filter_by(id=1).one()

# Print the name and role of the staff member
print(f"Staff member name: {staff_member.name}")
print(f"Staff member role: {staff_member.role}")

""" MEDICATION """
session = Session()

# Create a new disease
disease = Disease(name='Influenza')
session.add(disease)

# Create a new medication
medication = Medication(name='Tamiflu', disease=disease)
session.add(medication)

session.commit()

session = Session()

# Retrieve all medications from the database
medications = session.query(Medication).all()

# Print the name and disease of each medication
for medication in medications:
    print(f"Medication name: {medication.name}")
    print(f"Medication disease: {medication.disease.name}")

""" PATIENT CONSENT """
session = Session()

# Create a new patient
patient = Patient(name='John Doe')
session.add(patient)

# Create a new hospital
hospital = Hospital(name='General Hospital')
session.add(hospital)

# Give the hospital consent to access the patient's data
consent = PatientConsent(patient=patient, hospital=hospital, consent=True)
session.add(consent)

session.commit()

session = Session()

# Retrieve all the patient consents
consents = session.query(PatientConsent).all()

for consent in consents:
    print(f'Patient {consent.patient.name} has given {consent.hospital.name} consent to access their data: {consent.consent}')

# Retrieve all the consents for a specific patient
patient = session.query(Patient).filter_by(name='John Doe').one()
consents = session.query(PatientConsent).filter_by(patient_id=patient.id).all()

for consent in consents:
    print(f'Patient {consent.patient.name} has given {consent.hospital.name} consent to access their data: {consent.consent}')

""" PATIENT FEEDBACK """
session = Session()

# Add feedback to the database
feedback = PatientFeedback(
    patient_id=1,
    doctor_id=3,
    hospital_id=2,
    feedback='The doctor was very knowledgeable and helpful. I would definitely recommend him!',
    rating=5
)

session.add(feedback)
session.commit()

# Query the patient feedback table
all_feedback = session.query(PatientFeedback).all()

for feedback in all_feedback:
    print(f'Patient {feedback.patient.name} gave the following feedback to {feedback.hospital.name} on {feedback.feedback_date}: {feedback.feedback}. The patient gave a rating of {feedback.rating}/5.')


# Retrieve all the feedback for a specific hospital
hospital = session.query(Hospital).filter_by(name='St. Mary\'s Hospital').one()
hospital_feedback = session.query(PatientFeedback).filter_by(hospital_id=hospital.id).all()

for feedback in hospital_feedback:
    print(f'Patient {feedback.patient.name} gave the following feedback to {feedback.hospital.name} on {feedback.feedback_date}: {feedback.feedback}. The patient gave a rating of {feedback.rating}/5.')

""" PATIENT VISIT """
session = Session()

# Add a new visit to the database
new_visit = PatientVisit(
    patient_id=1,
    hospital_id=2,
    doctor_id=3,
    visit_date=datetime.now(),
    medication=Medication(
        medication_name='Ibuprofen',
        dosage='200mg'
    )
)

session.add(new_visit)
session.commit()

# Retrieve all visits
all_visits = session.query(PatientVisit).all()

# Retrieve a specific visit by ID
visit_id = 1
visit = session.query(PatientVisit).filter_by(id=visit_id).first()

""" REFERRAL """
session = Session()

# Add a new referral to the database
new_referral = Referral(
    referring_patient_id=1,
    referred_patient_id=2,
    referring_doctor_id=3,
    referred_doctor_id=4,
    referring_hospital_id=5,
    referred_hospital_id=6
)

session.add(new_referral)
session.commit()

# Retrieve all referrals
all_referrals = session.query(Referral).all()

# Retrieve a specific referral by ID
referral_id = 1
referral = session.query(Referral).filter_by(id=referral_id).first()

""" USER ACCOUNT """
session = Session()

# Add a new user account to the database
new_user = UserAccount(
    username='johndoe',
    password='password123',
    role='patient',
    email='johndoe@example.com',
    full_name='John Doe',
    phone_number='+1-555-555-5555'
)

session.add(new_user)
session.commit()

# Retrieve all user accounts
all_users = session.query(UserAccount).all()

# Retrieve a specific user account by ID
user_id = 1
user = session.query(UserAccount).filter_by(id=user_id).first()


"""VACCINATION"""
session = Session()

# Add a new vaccination record to the database
patient_id = 1
hospital_id = 1
new_vaccination = Vaccination(
    patient_id=patient_id,
    hospital_id=hospital_id,
    vaccine_name='Pfizer-BioNTech',
    vaccine_date='2022-03-31 10:00:00'
)

# Add the vaccination record to the patient's vaccinations
patient = session.query(Patient).filter_by(id=patient_id).first()
patient.vaccinations.append(new_vaccination)

# Add the vaccination record to the hospital's vaccinations
hospital = session.query(Hospital).filter_by(id=hospital_id).first()
hospital.vaccinations.append(new_vaccination)

session.add(new_vaccination)
session.commit()

# Retrieve all vaccination records
all_vaccinations = session.query(Vaccination).all()

# Retrieve all vaccination records for a specific patient
patient_id = 1
patient_vaccinations = session.query(Vaccination).filter_by(patient_id=patient_id).all()

# Retrieve all vaccination records for a specific hospital
hospital_id = 1
hospital_vaccinations = session.query(Vaccination).filter_by(hospital_id=hospital_id).all()

# Retrieve the most recent vaccination record for a specific patient
most_recent_vaccination = session.query(Vaccination).filter_by(patient_id=patient_id).order_by(Vaccination.vaccine_date.desc()).first()


""" VITAL SIGNS"""
session = Session()

# Add a new vital sign record to the database
patient_id = 1
new_vital_signs = VitalSign(
    patient_id=patient_id,
    temperature=37.5,
    blood_pressure=120,
    heart_rate=80,
    respiratory_rate=16,
    oxygen_saturation=98,
    timestamp='2022-04-07 08:30:00'
)

# Add the vital sign record to the patient's vital signs
patient = session.query(Patient).filter_by(id=patient_id).first()
patient.vital_signs.append(new_vital_signs)

session.add(new_vital_signs)
session.commit()

# Retrieve all vital sign records
all_vital_signs = session.query(VitalSign).all()

# Retrieve all vital sign records for a specific patient
patient_id = 1
patient_vital_signs = session.query(VitalSign).filter_by(patient_id=patient_id).all()

# Retrieve the most recent vital sign record for a specific patient
most_recent_vital_signs = session.query(VitalSign).filter_by(patient_id=patient_id).order_by(VitalSign.timestamp.desc()).first()














