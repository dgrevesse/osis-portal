from django.contrib import admin

from .models import AcademicYear
from .models import Offer
from .models import OfferYear
from .models import Student
from .models import OfferEnrollment
from .models import Tutor
from .models import Structure
from .models import LearningUnit
from .models import LearningUnitYear
from .models import LearningUnitEnrollment
from .models import Exam
from .models import ExamEnrollment
from .models import ExamEnrollmentHistory
from .models import Attribution
from .models import Configuration

admin.site.register(AcademicYear)
admin.site.register(Offer)
admin.site.register(OfferYear)
admin.site.register(Student)
admin.site.register(OfferEnrollment)
admin.site.register(Tutor)
admin.site.register(Structure)
admin.site.register(LearningUnit)
admin.site.register(LearningUnitYear)
admin.site.register(LearningUnitEnrollment)
admin.site.register(Exam)
admin.site.register(ExamEnrollment)
admin.site.register(ExamEnrollmentHistory)
admin.site.register(Attribution)
admin.site.register(Configuration)
