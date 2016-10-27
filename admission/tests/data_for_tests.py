from django.contrib.auth.models import User
from admission import models as mdl
from base import models as mdl_base
from reference import models as mdl_reference
from osis_common import models as mdl_osis_common
from performance import models as mdl_performance
import datetime
import json


def create_user():
    a_user = User.objects.create_user('testo', password='testopw')
    a_user.save()
    return a_user


def create_person():
    a_person = mdl_base.person.Person(first_name="first", last_name="last")
    a_person.save()
    return a_person


def create_student():
    a_student = mdl_base.student.Student(registration_id="64641200", person=create_person())
    a_student.save()
    return a_student


def create_student_with_specific_registration_id(registration_id):
    a_student = mdl_base.student.Student(registration_id=registration_id, person=create_person())
    a_student.save()
    return a_student


def create_applicant_by_user(user):
    an_applicant = mdl.applicant.Applicant(user=user)
    an_applicant.save()
    return an_applicant


def create_applicant():
    an_applicant = mdl.applicant.Applicant(user=create_user())
    an_applicant.save()
    return an_applicant


def create_secondary_education():
    a_secondary_education = mdl.secondary_education.SecondaryEducation(person=create_applicant())
    a_secondary_education.save()
    return a_secondary_education


def create_secondary_education_exam(secondary_education, a_type):
        an_admission_exam = mdl.secondary_education_exam.SecondaryEducationExam(
            secondary_education=secondary_education,
            type=a_type)
        an_admission_exam.save()
        return an_admission_exam


def create_secondary_education_with_exams():
    secondary_education = create_secondary_education()
    create_secondary_education_exam(secondary_education, 'ADMISSION')
    create_secondary_education_exam(secondary_education, 'PROFESSIONAL')
    create_secondary_education_exam(secondary_education, 'LANGUAGE')
    return secondary_education


def create_application(an_applicant):
    an_application = mdl.application.Application(applicant=an_applicant,
                                                 offer_year=create_offer_year(),
                                                 application_type='ADMISSION')
    an_application.save()
    return an_application


def create_offer_year():
    an_offer_year = mdl_base.offer_year.OfferYear()
    an_offer_year.academic_year = create_academic_year()
    an_offer_year.acronym = "VETE11BA"
    an_offer_year.title = "Première année de bachelier en médecine vétérinaire"
    an_offer_year.save()
    return an_offer_year


def create_offer_year_with_acronym(acronym):
    an_offer_year = mdl_base.offer_year.OfferYear()
    an_offer_year.academic_year = create_academic_year()
    an_offer_year.acronym = acronym
    an_offer_year.title = "Première année de bachelier en médecine vétérinaire"
    an_offer_year.save()
    return an_offer_year


def create_offer_year_with_academic_year(academic_year):
    an_offer_year = mdl_base.offer_year.OfferYear()
    an_offer_year.academic_year = academic_year
    an_offer_year.acronym = "VETE11BA"
    an_offer_year.title = "Première année de bachelier en médecine vétérinaire"
    an_offer_year.save()
    return an_offer_year


def create_academic_year():
    an_academic_year = mdl_base.academic_year.AcademicYear()
    an_academic_year.year = 2016
    an_academic_year.save()
    return an_academic_year


def create_grade_type(a_name, an_institutional_grade_type):
    a_grade_type = mdl_reference.grade_type.GradeType(name=a_name, institutional_grade_type=an_institutional_grade_type)
    a_grade_type.save()
    return a_grade_type


def create_document_file(description=None, user=None):
    a_document_file = mdl_osis_common.document_file.DocumentFile(description=description)
    a_document_file.file_name = "test.jpg"
    a_document_file.storage_duration = 1
    a_document_file.user = user
    a_document_file.save()
    return a_document_file


def create_application_document_file(an_application, a_user, description=None):
    a_document_file = create_document_file(description, a_user)
    an_application_document_file = mdl.application_document_file.ApplicationDocumentFile()
    an_application_document_file.application = an_application
    an_application_document_file.document_file = a_document_file
    an_application_document_file.save()
    return an_application_document_file


def create_student_performance():
    with open("performance/tests/ressources/points.json") as f:
        data = json.load(f)
    a_student_performance = mdl_performance.\
        student_performance.StudentPerformance(offer_year=create_offer_year_with_acronym("SINF2MS/G"), student=create_student(),
                                               update_date=datetime.date.today(), data=data)
    a_student_performance.save()
    return a_student_performance


def create_profession(a_name, an_adhoc):
    return mdl.profession.Profession(name=a_name, adhoc=an_adhoc)
