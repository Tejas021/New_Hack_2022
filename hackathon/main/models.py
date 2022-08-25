from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings

# Create your models here.


class CompanyInfo(models.Model):
    company_logo = models.ImageField(blank=True)
    company_name = models.CharField(max_length=150)
    company_problem_statement = models.CharField(max_length=500)

    def __str__(self):
        return str(self.company_name).capitalize()


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

PREFERENCE_CHOICE = (("1", "1"), ("2", "2"),
                     ("3", "3"), ("4", "4"), ("5", "5"))


class StudentForm(models.Model):

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Please Enter a Valid Number.")
    alter_phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Please Enter a Valid Number.")

    # TSIZE_CHOICES = (
    #     ('S','S-36'),
    #     ('M','M-38'),
    #     ('L','L-40'),
    #     ('XL','XL-42'),
    #     ('XXL','XXL-44'),
    # )

    # YEAR_CHOICES = (
    #     ('I','First Year'),
    #     ('II','Second Year'),
    #     ('III','Third Year'),
    #     ('IV','Fourth Year'),
    # )

    # problem_statement_1 = models.TextField(default="")
    abstract_1 = models.TextField(default="")
    # domain_1 = models.CharField(max_length=500, blank=True, null=True)
    # features_1 = models.TextField(default="")
    technology_stack_1 = models.CharField(
        max_length=500, blank=True, null=True)
    problem_statement_1_preference = models.CharField(
        ('Preference'), max_length=5, choices=PREFERENCE_CHOICE, default="1")

    # problem_statement_2 = models.TextField(default="")
    abstract_2 = models.TextField(default="")
    # domain_2 = models.CharField(max_length=500, blank=True, null=True)
    # features_2 = models.TextField(default="")
    technology_stack_2 = models.CharField(
        max_length=500, blank=True, null=True)
    problem_statement_2_preference = models.CharField(
        ('Preference'), max_length=5, choices=PREFERENCE_CHOICE, default="2")

    # problem_statement_3 = models.TextField(default="")
    abstract_3 = models.TextField(default="")
    # domain_3 = models.CharField(max_length=500, blank=True, null=True)
    # features_3 = models.TextField(default="")
    technology_stack_3 = models.CharField(
        max_length=500, blank=True, null=True)
    problem_statement_3_preference = models.CharField(
        ('Preference'), max_length=5, choices=PREFERENCE_CHOICE, default="3")

    # problem_statement_3 = models.TextField(default="")
    abstract_4 = models.TextField(default="")
    # domain_4 = models.CharField(max_length=500, blank=True, null=True)
    # features_4 = models.TextField(default="")
    technology_stack_4 = models.CharField(
        max_length=500, blank=True, null=True)
    problem_statement_4_preference = models.CharField(
        ('Preference'), max_length=5, choices=PREFERENCE_CHOICE, default="4")

    # problem_statement_3 = models.TextField(default="")
    abstract_5 = models.TextField(default="")
    # domain_5 = models.CharField(max_length=500, blank=True, null=True)
    # features_5 = models.TextField(default="")
    technology_stack_5 = models.CharField(
        max_length=500, blank=True, null=True)
    problem_statement_5_preference = models.CharField(
        ('Preference'), max_length=5, choices=PREFERENCE_CHOICE, default="5")

    # problem_statement_4 = models.CharField(max_length=300)
    # abstract_4 = models.TextField(default="")

    team_name = models.CharField(max_length=150)

    # Team Leader
    team_leader_name = models.CharField(max_length=200)
    team_leader_college_name = models.CharField(max_length=300)
    team_leader_course_year = models.CharField(max_length=50)
    team_leader_email = models.EmailField(max_length=150)
    team_leader_tel_number = models.CharField(
        validators=[phone_regex], max_length=15)
    team_leader_alter_tel_number = models.CharField(
        validators=[alter_phone_regex], max_length=15, blank=True, null=True)
    # team_leader_tsize = models.CharField(('T-SHIRT'),max_length=5,choices=TSIZE_CHOICES)
    team_leader_gender = models.CharField(
        ('Gender'), max_length=5, choices=GENDER_CHOICES)

    # Teammate 1
    teammate1_name = models.CharField(max_length=200, blank=True, null=True)
    teammate1_college_name = models.CharField(
        max_length=300, blank=True, null=True)
    teammate1_course_year = models.CharField(
        max_length=50, blank=True, null=True)
    teammate1_email = models.EmailField(max_length=150, blank=True, null=True)
    teammate1_tel_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=True, null=True)
    teammate1_alter_tel_number = models.CharField(
        validators=[alter_phone_regex], max_length=15, blank=True, null=True)
    # teammate1_tsize = models.CharField(('T-SHIRT'),max_length=5,choices=TSIZE_CHOICES,blank=True,null=True,default='S')
    teammate1_gender = models.CharField(
        ('Gender'), max_length=5, choices=GENDER_CHOICES, default='M', blank=True, null=True)

    # Teammate 2
    teammate2_name = models.CharField(max_length=200, blank=True, null=True)
    teammate2_college_name = models.CharField(
        max_length=300, blank=True, null=True)
    teammate2_course_year = models.CharField(
        max_length=50, blank=True, null=True)
    teammate2_email = models.EmailField(max_length=150, blank=True, null=True)
    teammate2_tel_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=True, null=True)
    teammate2_alter_tel_number = models.CharField(
        validators=[alter_phone_regex], max_length=15, blank=True, null=True)
    # teammate2_tsize = models.CharField(('T-SHIRT'),max_length=5,choices=TSIZE_CHOICES,blank=True,null=True,default='S')
    teammate2_gender = models.CharField(
        ('Gender'), max_length=5, choices=GENDER_CHOICES, default='M', blank=True, null=True)

    # Teammate 3
    teammate3_name = models.CharField(max_length=200, blank=True, null=True)
    teammate3_college_name = models.CharField(
        max_length=300, blank=True, null=True)
    teammate3_course_year = models.CharField(
        max_length=50, blank=True, null=True)
    teammate3_email = models.EmailField(max_length=150, blank=True, null=True)
    teammate3_tel_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=True, null=True)
    teammate3_alter_tel_number = models.CharField(
        validators=[alter_phone_regex], max_length=15, blank=True, null=True)
    # teammate3_tsize = models.CharField(('T-SHIRT'),max_length=5,choices=TSIZE_CHOICES,blank=True,null=True,default='S')
    teammate3_gender = models.CharField(
        ('Gender'), max_length=5, choices=GENDER_CHOICES, default='M', blank=True, null=True)

    application_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Student_Form'

    def __str__(self):
        return self.team_name + " - " + self.team_leader_college_name


class SiteConfig(models.Model):
    live_updates_section = models.BooleanField(default=False)
    youtube_embed_url = models.CharField(
        max_length=255, blank=True, null=True, default=settings.YT_URL)
    twitter_embed_url = models.CharField(
        max_length=255, blank=True, null=True, default=settings.TWITTER_URL)

    def __str__(self):
        return "Live Updates: " + str(self.live_updates_section)
