from datetime import date, datetime, time,timedelta
from pydantic import BaseModel, EmailStr
from typing import Optional, List


"""User"""
class UserBase(BaseModel):
    email: EmailStr
    password: str
    user_type: str

class UserCreate(UserBase):
    email: EmailStr
    password: str
    user_type: str



class UserResponse(UserBase):#what we are returning for the user to see
    id: str
    email: EmailStr
    user_type: str
    registration_date: datetime
    registration_form_completed: bool

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: str
    email: str
    user_type: str
    registration_form_completed: bool

class TokenData(BaseModel):
    id: Optional[str] = None



"""Administrator"""
class AdministratorBase(BaseModel):
    firstname: str
    lastname: str
    dob: date
    gender: str
    phone_number: str
    email: EmailStr
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
    user_id: str

    class Config:
        orm_mode = True


"""Admission"""
class AdmissionBase(BaseModel):
    patient_id: str
    doctor_id: str
    admission_date: date
    admission_time: time
    discharge_date: date
    discharge_time: time
    reason: str
    diagnosis: str
    treatment: str


class AdmissionCreate(AdmissionBase):
    pass


class AdmissionResponse(AdmissionBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse

    class Config:
        orm_mode = True


"""Adverse Reaction"""
class AdverseReactionBase(BaseModel):
    patient_id: str
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
    user_id: str
    user: UserResponse


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
    patient_id: str


class AllergyCreate(AllergyBase):
    pass


class AllergyResponse(AllergyBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Appointment Reminder"""
class AppointmentReminderBase(BaseModel):
    appointment_id: int
    patient_id: str
    doctor_id: str
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
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Appointment"""
class AppointmentBase(BaseModel):
    patient_id: str
    doctor_id: str
    type: str
    date: date
    start_time: str
    end_time: str
    description: str
    status: str


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


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
    occupied_by: str
    assigned_by: str


class BedCreate(BedBase):
    pass


class BedResponse(BedBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Availability """
class AvailabilityBase(BaseModel):
    date: str
    start_time: List[str]
    end_time: List[str]


class AvailabilityCreate(AvailabilityBase):
    pass


class AvailabilityResponse(AvailabilityBase):
    id: int
    created_at: datetime
    user_id: str


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
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Billing"""
class BillingBase(BaseModel):
    patient_id: str
    bill_date: date
    amount_due: float
    amount_paid: float
    payment_method: str
    status: str


class BillingCreate(BillingBase):
    pass


class BillingResponse(BillingBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True




"""Chronic condition"""
class ChronicConditionBase(BaseModel):
    name: str
    description: str
    patient_id: str


class ChronicConditionCreate(ChronicConditionBase):
    pass


class ChronicConditionResponse(ChronicConditionBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


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
    user_id: str


    class Config:
        orm_mode = True


"""Department"""
class DepartmentBase(BaseModel):
    name: str
    description: str
    hospital_id: str
    doctor_id: str
    nurse_id: str


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentResponse(DepartmentBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Diagnosis"""
class DiagnosisBase(BaseModel):
    patient_id: str
    doctor_id: str
    hospital_id: str
    disease: str
    diagnosis: str
    date: date
    notes: str


class DiagnosisCreate(DiagnosisBase):
    pass


class DiagnosisResponse(DiagnosisBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


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
    email: EmailStr
    specialty: str
    licence_number: str
    address: str
    city: str
    state: str
    postal_code: str
    country: str
    consultation_fee:  Optional[float] = None
    rating:  Optional[float] = None
    membership: str
    organization_name: Optional[str] = None
    membership_type: Optional[str] = None
    membership_number: Optional[str] = None
    start_date: Optional[date] = None
    expiration_date: Optional[date] = None
    membership_status: Optional[str] = None
    verified: Optional[bool] = None


class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    id: str
    created_at: datetime
    user_id: str


    class Config:
        orm_mode = True


"""Doctor Memberships"""
class DoctorMembershipBase(BaseModel):
    user_id: str
    name: str

class DoctorMembershipCreate(DoctorMembershipBase):
    pass


class DoctorMembershipResponse(DoctorMembershipBase):
    id: int
    created_at: datetime


    class Config:
        orm_mode = True

"""Genetic Condition"""
class GeneticConditionBase(BaseModel):
    patient_id: str
    name: str
    description: str
    patient_id: int
    inheritance_pattern: str


class GeneticConditionCreate(GeneticConditionBase):
    pass


class GeneticConditionResponse(GeneticConditionBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


""" Hospital """
class HospitalBase(BaseModel):
    name: str
    address: str
    city: str
    state: str
    postal_code: str
    country: str
    phone_number: str
    email: EmailStr
    website: str
    licence_number: str
    accreditation: str
    accreditation_authority: Optional[str] = None
    accreditation_date: Optional[date] = None
    accreditation_level: Optional[str] = None
    expiry_date: Optional[date] = None
    rating: float
    verified: str


class HospitalCreate(HospitalBase):
    pass


class HospitalResponse(HospitalBase):
    id: str
    created_at: datetime
    user_id: str


    class Config:
        orm_mode = True


"""Immunization"""
class ImmunizationBase(BaseModel):
    patient_id: str
    administering_provider: str
    vaccine_name: str
    dose_number: int
    date_given: date
    expiration_date: date


class ImmunizationCreate(ImmunizationBase):
    pass


class ImmunizationResponse(ImmunizationBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


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
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Insurance provider"""
class InsuranceProviderBase(BaseModel):
    name: str
    description: str
    products: str
    address: str
    city: str
    state: str
    postal_code: str
    country: str
    phone_number: int
    email: EmailStr
    website: str
    licence_number: str
    certification: str
    certification_type: Optional[str] = None
    certification_number: Optional[str] = None
    issuing_authority: Optional[str] = None
    issue_date: Optional[date] = None
    expiration_date: Optional[date] = None
    customer_support_phone: str
    customer_support_email: str
    rating: float
    verified: str


class InsuranceProviderCreate(InsuranceProviderBase):
    pass


class InsuranceProviderResponse(InsuranceProviderBase):
    id: str
    created_at: datetime
    user_id: str


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
    user_id: str

    class Config:
        orm_mode = True


"""IT Staff"""
class ItstaffBase(BaseModel):
    firstname: str
    lastname: str
    dob: date
    gender: str
    phone_number: str
    email: EmailStr
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
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Lab Technician"""
class LabTechnicianBase(BaseModel):
    firstname: str
    lastname: str
    dob: date
    gender: str
    phone_number: str
    email: EmailStr
    hospital_id: str
    address: str
    city: str
    state: str
    postal_code: str
    country: str


class LabTechnicianCreate(LabTechnicianBase):
    pass


class LabTechnicianResponse(LabTechnicianBase):
    id: str
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Lab test"""
class LabTestBase(BaseModel):
    patient_id: str
    lab_technician_id: str
    test_name: str
    test_date: date
    test_description: str
    test_type: str
    test_cost: float
    test_result: str
    comments: str


class LabTestCreate(LabTestBase):
    pass


class LabTestResponse(LabTestBase):
    id: int
    created_at: datetime
    updated_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Lab Result"""
class LabResultBase(BaseModel):
    patient_id: str
    test_result: str
    comments: str


class LabResultCreate(LabResultBase):
    pass


class LabResultResponse(LabResultBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Medication Alerts"""
class MedicationAlertBase(BaseModel):
    patient_id: str
    doctor_id: str
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
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Medical conditions"""
class MedicalConditionBase(BaseModel):
    patient_id: str
    name: str
    description: str
    diagnosis_date: date
    treatment: str


class MedicalConditionCreate(MedicalConditionBase):
    pass


class MedicalConditionResponse(MedicalConditionBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Medical devices"""
class MedicalDeviceBase(BaseModel):
    name: str
    manufacturer: str
    model: str
    serial_number: str
    hospital_id: str
    department_id: str
    last_maintenance: date
    next_maintenance: date  


class MedicalDeviceCreate(MedicalDeviceBase):
    pass


class MedicalDeviceResponse(MedicalDeviceBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Medical images"""
class MedicalImageBase(BaseModel):
    patient_id: str
    image_type: str
    image_date: date


class MedicalImageCreate(MedicalImageBase):
    pass


class MedicalImageResponse(MedicalImageBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Medical notes"""
class MedicalNoteBase(BaseModel):
    patient_id: str
    doctor_id: str
    date: date
    note: str


class MedicalNoteCreate(MedicalNoteBase):
    pass


class MedicalNoteResponse(MedicalNoteBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Medical procedures"""
class MedicalProcedureBase(BaseModel):
    patient_id: str
    doctor_id: str
    name: str
    date: date
    notes: str


class MedicalProcedureCreate(MedicalProcedureBase):
    pass


class MedicalProcedureResponse(MedicalProcedureBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Medication"""
class MedicationBase(BaseModel):
    name: str

class MedicationCreate(MedicationBase):
    pass


class MedicationResponse(MedicationBase):
    id: int
    created_at: datetime
    user_id: str


    class Config:
        orm_mode = True


"""Nurse"""
class NurseBase(BaseModel):
    firstname: str
    lastname: str
    dob: date
    gender: str
    phone_number: str
    email: EmailStr
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
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Patient consent"""
class PatientConsentBase(BaseModel):
    patient_id: str
    consent_type: str
    consent_date: date
    expiration_date: date


class PatientConsentCreate(PatientConsentBase):
    pass


class PatientConsentResponse(PatientConsentBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Patient feedback"""
class PatientFeedbackBase(BaseModel):
    patient_id: str
    doctor_id: str
    date: date
    text: str
    rating: int


class PatientFeedbackCreate(PatientFeedbackBase):
    pass


class PatientFeedbackResponse(PatientFeedbackBase):
    id: int
    # created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Patient visit"""
class PatientVisitBase(BaseModel):
    patient_id: str
    doctor_id: str
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
    user_id: str
    user: UserResponse


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
    email: EmailStr
    address: str
    city: str
    state: str
    postal_code: str
    country: str
    emergency_contact_name: str
    emergency_contact_phone: str
    relationship: str
    insurance: str
    provider_name: Optional[str] = None
    policy_number: Optional[str] = None
    group_number: Optional[str] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):
    id: str
    created_at: datetime
    user_id: str


    class Config:
        orm_mode = True




  

"""Pharmacist"""
class PharmacistBase(BaseModel):
    firstname: str
    lastname: str
    dob: date
    gender: str
    phone_number: str
    email: EmailStr
    licence_number: str
    address: str
    city: str
    state: str
    postal_code: str
    country: str
    verified: bool


class PharmacistCreate(PharmacistBase):
    pass


class PharmacistResponse(PharmacistBase):
    id: str
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Prescription"""
class PrescriptionBase(BaseModel):
    patient_id: str
    doctor_id: str
    medication: str
    dosage: str
    instructions: str


class PrescriptionCreate(PrescriptionBase):
    pass


class PrescriptionResponse(PrescriptionBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Receptionist"""
class ReceptionistBase(BaseModel):
    firstname: str
    lastname: str
    dob: date
    gender: str
    phone_number: str
    email: EmailStr
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
    user_id: str
    user: UserResponse


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
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Specialty"""
class SpecialtyBase(BaseModel):
    name: str
    description: str
    doctor_id: str


class SpecialtyCreate(SpecialtyBase):
    pass


class SpecialtyResponse(SpecialtyBase):
    id: int
    created_at: datetime
    user_id: str



    class Config:
        orm_mode = True

"""Time Slots"""
class TimeSlotBase(BaseModel):
    doctor_id: str
    appointment_date: date
    appointment_start_time: str
    appointment_end_time: str
    availability: bool


class TimeSlotCreate(TimeSlotBase):
    pass


class TimeSlotResponse(TimeSlotBase):
    id: int
    created_at: datetime
    updated_at: datetime
    user_id: str
    user: UserResponse



    class Config:
        orm_mode = True



"""Vaccinations """
class VaccinationBase(BaseModel):
    patient_id: str
    vaccine_name: str
    administered_by: str
    administered_at: date
    next_dose_due: date


class VaccinationCreate(VaccinationBase):
    pass


class VaccinationResponse(VaccinationBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Vital signs """
class VitalSignBase(BaseModel):
    patient_id: str
    doctor_id: str
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
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True


"""Ward """


class WardBase(BaseModel):
    hospital_id: str
    name: str
    type: str
    capacity: int


class WardCreate(WardBase):
    pass


class WardResponse(WardBase):
    id: int
    created_at: datetime


    class Config:
        orm_mode = True


"""Work Schedule """
class WorkScheduleBase(BaseModel):
    doctor_id: str
    nurse_id: str
    day_of_week: str
    start_time: datetime
    end_time: datetime


class WorkScheduleCreate(WorkScheduleBase):
    pass


class WorkScheduleResponse(WorkScheduleBase):
    id: int
    created_at: datetime
    user_id: str
    user: UserResponse


    class Config:
        orm_mode = True