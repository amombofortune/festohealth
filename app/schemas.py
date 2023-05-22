from datetime import date, datetime, time
from pydantic import BaseModel


"""Administrator"""


class AdministratorBase(BaseModel):
    firstname: str
    lastname: str
    dob: date
    gender: str
    phone_number: str
    email: str
    address: str
    city: str
    state: str
    zip_code: str
    country: str
    hospital_id: str


class AdministratorCreate(AdministratorBase):
    pass


class AdministratorResponse(AdministratorBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True


"""Admission"""


class AdmissionBase(BaseModel):
    patient_id: int
    admission_date: date
    admission_time: time
    discharge_date: date
    discharge_time: time
    reason: str
    diagnosis: str
    treatment: str
    doctor_id: int


class AdmissionCreate(AdmissionBase):
    pass


class AdmissionResponse(AdmissionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Adverse Reaction"""


class AdverseReactionBase(BaseModel):
    patient_id: int
    reaction_date: date
    reaction_time: time
    reaction_type: str
    reaction_details: str
    medication_name: str
    dosage: str
    severity: str
    treatment: str


class AdverseReactionCreate(AdverseReactionBase):
    pass


class AdverseReactionResponse(AdverseReactionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Adverse Reaction Type"""


class AdverseReactionTypeBase(BaseModel):
    name: str
    description: str


class AdverseReactionTypeCreate(AdverseReactionTypeBase):
    pass


class AdverseReactionTypeResponse(AdverseReactionTypeBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Allergy"""


class AllergyBase(BaseModel):
    name: str


class AllergyCreate(AllergyBase):
    pass


class AllergyResponse(AllergyBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Appointment Reminder"""


class AppointmentReminderBase(BaseModel):
    appointment_id: int
    user_id: int
    reminder_date: date
    reminder_time: time
    reminder_type: str
    status: str


class AppointmentReminderCreate(AppointmentReminderBase):
    pass


class AppointmentReminderResponse(AppointmentReminderBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Appointment"""


class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_type: str
    appointment_date: date
    appointment_start_time: time
    appointment_end_time: time
    description: str
    status: str


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

"""Appointment type"""


class AppointmentTypeBase(BaseModel):
    name: str
    description: str


class AppointmentTypeCreate(AppointmentTypeBase):
    pass


class AppointmentTypeResponse(AppointmentTypeBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

"""Bed"""


class BedBase(BaseModel):
    ward: str
    bed_no: int
    bed_type: str
    availability: bool
    occupied_by: int


class BedCreate(BedBase):
    pass


class BedResponse(BedBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Bed Assignment"""


class BedAssignmentBase(BaseModel):
    bed_id: int
    patient_id: int
    assigned_by: int
    assigned_at: datetime
    discharged_at: datetime


class BedAssignmentCreate(BedAssignmentBase):
    pass


class BedAssignmentResponse(BedAssignmentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Billing"""


class BillingBase(BaseModel):
    patient_id: int
    bill_date: date
    amount_due: float
    amount_paid: float
    payment_method: str


class BillingCreate(BillingBase):
    pass


class BillingResponse(BillingBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True




"""Chronic condition"""


class ChronicConditionBase(BaseModel):
    name: str
    description: str


class ChronicConditionCreate(ChronicConditionBase):
    pass


class ChronicConditionResponse(ChronicConditionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Country"""


class CountryBase(BaseModel):
    name: str
    code: str


class CountryCreate(CountryBase):
    pass


class CountryResponse(CountryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Department"""


class DepartmentBase(BaseModel):
    name: str
    description: str
    hospital: str
    head_doctor: str


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentResponse(DepartmentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Diagnosis"""


class DiagnosisBase(BaseModel):
    patient_id: str
    disease: str
    diagnosis: str
    date: date
    doctor_id: str
    notes: str


class DiagnosisCreate(DiagnosisBase):
    pass


class DiagnosisResponse(DiagnosisBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Diseases"""


class DiseaseBase(BaseModel):
    name: str
    description: str
    symptoms: str
    treatment: str
    prevention: str


class DiseaseCreate(DiseaseBase):
    pass


class DiseaseResponse(DiseaseBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Doctor"""


class DoctorBase(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    dob: date
    gender: str
    phone_number: str
    email: str
    specialty: str
    licence_number: str
    address: str
    city: str
    state: str
    postal_code: str
    country: str
    consultation_fee: float
    rating: float
    verified: bool


class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True


"""Genetic Condition"""


class GeneticConditionBase(BaseModel):
    name: str
    description: str
    patient_id: int
    inheritance_pattern: str


class GeneticConditionCreate(GeneticConditionBase):
    pass


class GeneticConditionResponse(GeneticConditionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


""" Hospital """


class HospitalBase(BaseModel):
    name: str
    address: str
    city: str
    state: str
    zip_code: str
    country: str
    phone_number: str
    website: str
    rating: float


class HospitalCreate(HospitalBase):
    pass


class HospitalResponse(HospitalBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True


"""Immunization"""


class ImmunizationBase(BaseModel):
    patient_id: int
    vaccine_name: str
    dose_number: int
    date_given: date
    administering_provider: str
    expiration_date: date


class ImmunizationCreate(ImmunizationBase):
    pass


class ImmunizationResponse(ImmunizationBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Insurance claims"""


class InsuranceClaimBase(BaseModel):
    patient_id: str
    provider_id: str
    date_of_service: date
    procedure_code: str
    diagnosis_code: str
    billed_amount: float
    insurance_paid: float
    patient_paid: float
    status: str


class InsuranceClaimCreate(InsuranceClaimBase):
    pass


class InsuranceClaimResponse(InsuranceClaimBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True


"""Insurance provider"""


class InsuranceProviderBase(BaseModel):
    name: str
    type: str
    address: str
    city: str
    state: str
    postal_code: str
    country: str
    phone_number: int
    email: str
    website: str


class InsuranceProviderCreate(InsuranceProviderBase):
    pass


class InsuranceProviderResponse(InsuranceProviderBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True

"""Insurance provider type"""


class InsuranceProviderTypeBase(BaseModel):
    name: str
    description: str


class InsuranceProviderTypeCreate(InsuranceProviderTypeBase):
    pass


class InsuranceProviderTypeResponse(InsuranceProviderTypeBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""IT Staff"""


class ItstaffBase(BaseModel):
    firstname: str
    lastname: str
    dob: date
    gender: str
    phone_number: str
    email: str
    address: str
    city: str
    state: str
    zip_code: str
    country: str
    hospital_id: str


class ItstaffCreate(ItstaffBase):
    pass


class ItstaffResponse(ItstaffBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True


"""Lab Technician"""


class LabTechnicianBase(BaseModel):
    firstname: str
    lastname: str
    dob: date
    gender: str
    phone_number: str
    email: str
    address: str
    city: str
    state: str
    zip_code: str
    country: str
    hospital_id: str


class LabTechnicianCreate(LabTechnicianBase):
    pass


class LabTechnicianResponse(LabTechnicianBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True


"""Lab test"""


class LabTestBase(BaseModel):
    test_name: str
    test_description: str
    test_type: str
    test_cost: float


class LabTestCreate(LabTestBase):
    pass


class LabTestResponse(LabTestBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Lab Test Result"""


class LabTestResultBase(BaseModel):
    patient_id: int
    lab_test_name: str
    test_date: date
    test_result: str
    units: str
    comments: str


class LabTestResultCreate(LabTestResultBase):
    pass


class LabTestResultResponse(LabTestResultBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Medication Alerts"""


class MedicationAlertBase(BaseModel):
    patient_id: int
    medication_id: int
    dosage: str
    frequency: str
    alert_date: date
    alert_text: str
    status: str


class MedicationAlertCreate(MedicationAlertBase):
    pass


class MedicationAlertResponse(MedicationAlertBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Medical conditions"""


class MedicalConditionBase(BaseModel):
    patient_id: int
    name: str
    description: str
    diagnosis_date: date
    treatment: str


class MedicalConditionCreate(MedicalConditionBase):
    pass


class MedicalConditionResponse(MedicalConditionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Medical devices"""


class MedicalDeviceBase(BaseModel):
    name: str
    manufacturer: str
    model: str
    serial_number: str
    hospital: str
    department: str
    last_maintenance: date
    next_maintenance: date  


class MedicalDeviceCreate(MedicalDeviceBase):
    pass


class MedicalDeviceResponse(MedicalDeviceBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Medical images"""


class MedicalImageBase(BaseModel):
    patient_id: int
    doctor_id: int
    image_type: str
    image_date: date


class MedicalImageCreate(MedicalImageBase):
    pass


class MedicalImageResponse(MedicalImageBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Medical notes"""


class MedicalNoteBase(BaseModel):
    patient_id: int
    doctor_id: int
    date: date
    content: str


class MedicalNoteCreate(MedicalNoteBase):
    pass


class MedicalNoteResponse(MedicalNoteBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Medical procedures"""


class MedicalProcedureBase(BaseModel):
    patient_id: int
    doctor_id: int
    name: str
    date: date
    notes: str


class MedicalProcedureCreate(MedicalProcedureBase):
    pass


class MedicalProcedureResponse(MedicalProcedureBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Medication"""


class MedicationBase(BaseModel):
    name: str
    description: str
    route_of_administration: str
    dosage: str
    unit: str
    frequency: str
    patient_id: int
    doctor_id: int


class MedicationCreate(MedicationBase):
    pass


class MedicationResponse(MedicationBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Nurse"""


class NurseBase(BaseModel):
    firstname: str
    lastname: str
    dob: date
    gender: str
    phone_number: str
    email: str
    licence_number: str
    hospital_id: str
    address: str
    city: str
    state: str
    postal_code: str
    country: str
    work_schedule: str
    verified: bool


class NurseCreate(NurseBase):
    pass


class NurseResponse(NurseBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True


"""Patient consent"""


class PatientConsentBase(BaseModel):
    patient_id: int
    consent_type: str
    consent_date: date
    expiration_date: date


class PatientConsentCreate(PatientConsentBase):
    pass


class PatientConsentResponse(PatientConsentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Patient feedback"""


class PatientFeedbackBase(BaseModel):
    patient_id: int
    doctor_id: int
    date: date
    text: str
    rating: int


class PatientFeedbackCreate(PatientFeedbackBase):
    pass


class PatientFeedbackResponse(PatientFeedbackBase):
    id: int
    # created_at: datetime

    class Config:
        orm_mode = True


"""Patient visit"""


class PatientVisitBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_id: int
    visit_date: date
    chief_complaint: str
    diagnosis_id: int
    notes: str


class PatientVisitCreate(PatientVisitBase):
    pass


class PatientVisitResponse(PatientVisitBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Patient """


class PatientBase(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    dob: date
    gender: str
    phonenumber: str
    email: str
    address: str
    city: str
    state: str
    postal_code: str
    country: str
    emergency_contact_name: str
    emergency_contact_phone: str
    relationship: str
    insurance: bool
    provider_name: str
    policy_number: str
    group_number: str
    effective_date: date
    expiration_date: date


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True


"""Pharmacist"""


class PharmacistBase(BaseModel):
    firstname: str
    lastname: str
    dob: date
    gender: str
    phone_number: str
    email: str
    licence_number: str
    address: str
    city: str
    state: str
    zip_code: str
    country: str
    verified: bool


class PharmacistCreate(PharmacistBase):
    pass


class PharmacistResponse(PharmacistBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True


"""Prescription"""


class PrescriptionBase(BaseModel):
    doctor_id: int
    patient_id: int
    medication: str
    dosage: str
    instructions: str


class PrescriptionCreate(PrescriptionBase):
    pass


class PrescriptionResponse(PrescriptionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Receptionist"""


class ReceptionistBase(BaseModel):
    firstname: str
    lastname: str
    dob: date
    gender: str
    phone_number: str
    email: str
    address: str
    city: str
    state: str
    zip_code: str
    country: str
    hospital_id: str


class ReceptionistCreate(ReceptionistBase):
    pass


class ReceptionistResponse(ReceptionistBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True




"""Referrals"""


class ReferralBase(BaseModel):
    referring_patient: str
    referred_patient: str
    referring_doctor: str
    referred_doctor: str
    referring_hospital: str
    referred_hospital: str
    referral_date: date
    referral_reason: str
    status: str


class ReferralCreate(ReferralBase):
    pass


class ReferralResponse(ReferralBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Specialty"""


class SpecialtyBase(BaseModel):
    name: str
    description: str


class SpecialtyCreate(SpecialtyBase):
    pass


class SpecialtyResponse(SpecialtyBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

"""User"""


class UserBase(BaseModel):
    email: str
    password: str
    role: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: str
    registration_date: datetime

    class Config:
        orm_mode = True


"""Vaccinations """


class VaccinationBase(BaseModel):
    patient_id: int
    vaccine_name: str
    administered_by: str
    administered_at: date
    next_dose_due: date


class VaccinationCreate(VaccinationBase):
    pass


class VaccinationResponse(VaccinationBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Vital signs """


class VitalSignBase(BaseModel):
    patient_id: int
    doctor_id: int
    heart_rate: float
    blood_pressure_systolic: float
    blood_pressure_diastolic: float
    respiratory_rate: float
    temperature: float
    height: float
    weight: float
    oxygen_saturation: int
    recorded_at: date


class VitalSignCreate(VitalSignBase):
    pass


class VitalSignResponse(VitalSignBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Ward """


class WardBase(BaseModel):
    name: str
    type: str
    capacity: int
    location: str
    hospital_id: int


class WardCreate(WardBase):
    pass


class WardResponse(WardBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


"""Work Schedule """


class WorkScheduleBase(BaseModel):
    doctor: str
    nurse: str
    day_of_week: str
    start_time: datetime
    end_time: datetime


class WorkScheduleCreate(WorkScheduleBase):
    pass


class WorkScheduleResponse(WorkScheduleBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True