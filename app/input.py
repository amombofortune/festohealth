from datetime import date, time, datetime
from sqlalchemy.orm import sessionmaker
from .database import engine, SessionLocal
from .models import Patient, Doctor, Hospital, Nurse, InsuranceProvider, LabTechnician, Pharmacist, Admission,\
    AdverseReaction, Allergy, AppointmentReminder, Appointment, AppointmentType, Bed, Billing, ChronicCondition, Country,\
    Department, Diagnosis, Disease, GeneticCondition, Immunization, InsuranceClaim, LabTechnician, \
    LabTest, LabResult, MedicationAlert, MedicalCondition, MedicalDevice, MedicalImage, MedicalNote, \
    MedicalProcedure, Medication, PatientConsent, PatientFeedback, PatientVisit, Prescription, \
    Referral, Specialty, TimeSlot, User, Vaccination, VitalSign, Ward, WorkSchedule

Session = sessionmaker(bind=engine)
session = SessionLocal()
patient = Patient(
    firstname="salome",
    middlename="nzisa",
    lastname="amombo",
    dob=date(2015, 8, 15),
    gender="male",
    phonenumber="745369800",
    email="amombofortune77@gmail.com",
    address="P.O Box 980",
    city="Nairobi",
    state="Kileleshwa",
    postal_code="00100",
    country="Kenya",
    emergency_contact_name="Dennis Okutoyi",
    emergency_contact_phone="735400400",
    relationship="son",
    insurance=False,
    provider_name="Britam Insurance",
    policy_number="28930",
    group_number="34829",
    effective_date=date(2023, 12, 12),
    expiration_date=date(2025, 12, 19)
)
session.add(patient)
session.commit()

doctor = Doctor(
    firstname="salome",
    middlename="nzisa",
    lastname="amombo",
    dob=date(2015, 8, 15),
    gender="male",
    phone_number="745369800",
    email="amombofortune77@gmail.com",
    specialty="Neurosurgeon",
    licence_number = "5839202",
    address="P.O Box 980",
    city="Nairobi",
    state="Kileleshwa",
    postal_code="00100",
    country="Kenya",
    consultation_fee= 5000,
    rating=5,
    verified = True, 
)
session.add(doctor)
session.commit()

hospital = Hospital(
    name="Kibaki Hospital",
    address="P.O Box 980",
    city="Nairobi",
    state="Kileleshwa",
    postal_code="00100",
    country="Kenya",
    email = "info@gmail.com",
    phone_number= "745689800",
    website= "kh.co.ke",
    rating = 5, 
    verified = True,
)
session.add(hospital)
session.commit()

nurse = Nurse(
    firstname="salome",
    lastname="amombo",
    dob=date(2015, 8, 15),
    gender="male",
    phone_number="745369800",
    email="amombofortune77@gmail.com",
    licence_number = "5839202",
    hospital_id = hospital.id,
    address="P.O Box 980",
    city="Nairobi",
    state="Kileleshwa",
    postal_code="00100",
    country="Kenya",
    work_schedule= "Mon, Tue, Wed",
    verified = True, 
)
session.add(nurse)
session.commit()

insurance_provider = InsuranceProvider(
    name="Other",
    type="Health",
    licence_number = "89373",
    address="P.O Box 980",
    city="Nairobi",
    state="Kileleshwa",
    postal_code="00100",
    country="Kenya",
    phone_number="745369800",
    email="amombofortune77@gmail.com",
    website= "website.co.ke",
    verified = True, 
)
session.add(insurance_provider)
session.commit()

lab_technician = LabTechnician(
    firstname="salome",
    lastname="amombo",
    dob=date(2015, 8, 15),
    gender="male",
    phone_number="745369800",
    email="amombofortune77@gmail.com",
    hospital_id = hospital.id,
    address="P.O Box 980",
    city="Nairobi",
    state="Kileleshwa",
    postal_code="00100",
    country="Kenya",
)
session.add(lab_technician)
session.commit()

pharmacist = Pharmacist(
    firstname="salome",
    lastname="amombo",
    dob=date(2015, 8, 15),
    gender="male",
    phone_number="745369800",
    email="amombofortune77@gmail.com",
    licence_number = "licence_number",
    address="P.O Box 980",
    city="Nairobi",
    state="Kileleshwa",
    postal_code="00100",
    country="Kenya",
    verified=True,
)
session.add(pharmacist)
session.commit()


admission = Admission(
    patient_id=patient.id,
    admission_date=date(2023, 9, 12),
    admission_time=time(12, 45),
    discharge_date=date(2023, 10, 12),
    discharge_time=time(19, 1),
    reason="Referral",
    diagnosis="Medical pills",
    treatment="Surgery",
    doctor_id= doctor.id,
)
session.add(admission)
session.commit()


adverse_reaction = AdverseReaction(
    patient_id=patient.id,
    reaction_date=date(2023, 9, 12),
    reaction_time=time(12, 45),
    reaction_type = "Reaction Type",
    reaction_details="Reaction happened very fast",
    medication_name="Ibufofren Painkillers",
    dosage="Twice a day",
    severity="Very Severe",
    treatment="Surgery required"
)
session.add(adverse_reaction)
session.commit()

allergy = Allergy(
    name="Other",
    patient_id= patient.id,
)
session.add(allergy)
session.commit()


appointment = Appointment(
    patient_id=patient.id,
    doctor_id=doctor.id,
    appointment_type = "Online",
    appointment_date=date(2023, 9, 12),
    appointment_start_time=time(12, 45),
    appointment_end_time=time(12, 45),
    description="Reaction happened very fast",
    status="Ibufofren Painkillers",

)
session.add(appointment)
session.commit()

appointment_reminder = AppointmentReminder(
    appointment_id = appointment.id,
    patient_id=patient.id,
    doctor_id=doctor.id,
    user_id = 45,
    reminder_date=date(2023, 9, 12),
    reminder_time=time(12, 45),
    reminder_type = "Push Notification",
    status = "Successful",
)
session.add(appointment_reminder)
session.commit()

ward = Ward(
    hospital_id=hospital.id,
    name="name",
    type= "type",
    capacity= "300",
    location= "location",
)
session.add(ward)
session.commit()

bed = Bed(
    ward = "Eye Clinic", #foreignkey
    bed_no=34,
    bed_type="Surgery",
    availability = True,
    occupied_by = patient.id,
    assigned_by = "A Nurse Toto",
 
)
session.add(bed)
session.commit()

billing = Billing(
    patient_id=patient.id,
    bill_date=date(2023, 9, 12),
    amount_due= 3900,
    amount_paid = 3900,
    payment_method = "M-Pesa",
    status = "Successful",
)
session.add(billing)
session.commit()

chronic_condition = ChronicCondition(
    name = "Other",
    description = "Other",
    patient_id=patient.id,
)
session.add(chronic_condition)
session.commit()

country = Country(
    name="Seychelles",
    code= 299,
    patient_id=patient.id,
    doctor_id=doctor.id,
    nurse_id=nurse.id,
    hospital_id=hospital.id,
    insurance_provider_id=insurance_provider.id,
  
)
session.add(country)
session.commit()

department = Department(
    name="Other",
    description= "description",
    hospital_id=hospital.id,
    doctor_id=doctor.id,
    nurse_id=nurse.id,
  
)
session.add(department)
session.commit()

diagnosis = Diagnosis(
    patient_id=patient.id,
    doctor_id=doctor.id,
    hospital_id=hospital.id,
    disease = "disease",
    diagnosis = "diagnosis",
    date=date(2023, 9, 12),
    notes = "Push Notification",
)
session.add(diagnosis)
session.commit()

disease = Disease(
    patient_id=patient.id,
    name = "disease",
    description = "diagnosis",
    symptoms = "symptoms",
    treatment = "Push Notification",
    prevention = "Push Notification",
)
session.add(disease)
session.commit()

genetic_condition = GeneticCondition(
    patient_id=patient.id,
    name = "disease",
    description = "diagnosis",
    inheritance_pattern = "inheritance_pattern",
)
session.add(genetic_condition)
session.commit()

immunization = Immunization(
    patient_id=patient.id,
    administering_provider="administering_provider",
    vaccine_name="vaccine_name",
    dose_number = "239",
    date_given=date(2023, 9, 12),
    expiration_date=date(2023, 9, 12),
)
session.add(immunization)
session.commit()

insurance_claim = InsuranceClaim(
    patient_id=patient.id,
    provider_id=insurance_provider.id,
    date_of_service=date(2023, 9, 12),
    procedure_code="procedure_code",
    diagnosis_code="diagnosis_code",
    billed_amount = "2390",
    insurance_paid = "390",
    patient_paid = "4000",
    status = "pending",
)
session.add(insurance_claim)
session.commit()

lab_test = LabTest(
    patient_id=patient.id,
    lab_technician_id=lab_technician.id,
    test_name="test_name",
    test_date=date(2023, 9, 12),
    test_description="test_description",
    test_type = "test_type",
    test_cost = "390",
    test_result = "test_result",
    comments = "comments",
)
session.add(lab_test)
session.commit()

lab_result = LabResult(
    patient_id=patient.id,
    test_result = "test_result",
    comments = "comments",
)
session.add(lab_result)
session.commit()

medication_alert = MedicationAlert(
    patient_id=patient.id,
    doctor_id=doctor.id,
    medication_id="2890",
    dosage = "dosage",
    frequency = "frequency",
    alert_date=date(2023, 9, 12),
    alert_text="alert_text",
    status = "status",
   
)
session.add(medication_alert)
session.commit()

medical_condition = MedicalCondition(
    patient_id=patient.id,
    name="name",
    description="description",
    diagnosis_date=date(2023, 9, 12),
    treatment="treatment",
   
)
session.add(medical_condition)
session.commit()

medical_device = MedicalDevice(
    name="name",
    manufacturer="manufacturer",
    model ="model",
    serial_number="serial_number",
    hospital_id=hospital.id,
    department_id = department.id,
    last_maintenance=date(2023, 9, 12),
    next_maintenance=date(2023, 9, 12),
   
)
session.add(medical_device)
session.commit()

medical_image = MedicalImage(
    patient_id=patient.id,
    image_type="image_type",
    image_date=date(2023, 9, 12),
   
)
session.add(medical_image)
session.commit()

medical_note = MedicalNote(
    patient_id=patient.id,
    doctor_id=doctor.id,
    date=date(2023, 9, 12),
    note="note",
   
)
session.add(medical_image)
session.commit()

medical_procedure = MedicalProcedure(
    patient_id=patient.id,
    doctor_id=doctor.id,
    name="name",
    date=date(2023, 9, 12),
    notes="notes",
   
)
session.add(medical_procedure)
session.commit()

medication = Medication(
    patient_id=patient.id,
    doctor_id=doctor.id,
    name="name",
    description="description",
    route_of_administration="route_of_administration",
    dosage="dosage",
    unit="unit",
    frequency="frequency",
   
)
session.add(medication)
session.commit()

patient_consent = PatientConsent(
    patient_id=patient.id,
    consent_type = "Full consent",
    consent_date=date(2023, 9, 12),
    expiration_date=date(2023, 9, 12),

)
session.add(patient_consent)
session.commit()

patient_feedback = PatientFeedback(
    patient_id=patient.id,
    doctor_id=doctor.id,
    date=date(2023, 9, 12),
    text = "Text",
    rating="5",

)
session.add(patient_feedback)
session.commit()

patient_visit = PatientVisit(
    patient_id=patient.id,
    doctor_id=doctor.id,
    appointment_id= appointment.id,
    visit_date=date(2023, 9, 12),
    chief_complaint = "chief_complaint",
    diagnosis_id= "34",
    notes="notes",

)
session.add(patient_visit)
session.commit()

prescription = Prescription(
    doctor_id=doctor.id,
    patient_id=patient.id,
    medication= "medication",
    dosage = "dosage",
    instructions= "instructions",

)
session.add(prescription)
session.commit()

referral = Referral(
    referring_patient=patient.id,
    referred_patient=patient.id,
    referring_doctor=doctor.id,
    referred_doctor=doctor.id,
    referring_hospital=hospital.id,
    referred_hospital=hospital.id,
    referral_date=date(2023, 9, 12),
    referral_reason = "referral_reason",
    status="status",

)
session.add(referral)
session.commit()

specialty = Specialty(
    name="Cardiologist",
    description="Other",
    doctor_id= doctor.id,
)
session.add(specialty)
session.commit()

time_slot = TimeSlot(
    doctor_id=doctor.id,
    date=date(2015, 8, 15),
    start_time = time(12, 25),
    end_time = time(13, 25),
    is_available = True, 
)
session.add(time_slot)
session.commit()

user = User(
    email="famombo@gmail.com",
    password="password123",
    role= "Nurse",
)
session.add(user)
session.commit()

vaccination = Vaccination(
    patient_id=patient.id,
    vaccine_name="vaccine_name",
    administered_by= "administered_by",
    administered_at=datetime(2023, 9, 9, 12, 0, 0),
    next_dose_due= date(2023, 9, 12),
)
session.add(vaccination)
session.commit()

vital_sign = VitalSign(
    patient_id=patient.id,
    doctor_id=doctor.id,
    heart_rate="300",
    blood_pressure_systolic= "300",
    blood_pressure_diastolic= "300",
    respiratory_rate= "300",
    temperature= "300",
    height= "300",
    weight= "300",
    oxygen_saturation= "300",
    recorded_at=datetime(2023, 9, 9, 12, 0, 0),
)
session.add(vital_sign)
session.commit()



work_schedule = WorkSchedule(
    doctor_id=doctor.id,
    nurse_id=nurse.id,
    day_of_week="day_of_week",
    start_time= datetime(2023, 9, 9, 12, 0, 0),
    end_time= datetime(2023, 9, 9, 12, 0, 0),
)
session.add(work_schedule)
session.commit()


