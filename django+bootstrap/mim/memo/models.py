# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DoaTDrc(models.Model):
    md5 = models.CharField(primary_key=True, max_length=32)
    data_name = models.CharField(max_length=50)
    data_security_level = models.CharField(max_length=1)
    data_size = models.IntegerField()
    data_format = models.CharField(max_length=10)
    data_owner = models.CharField(max_length=18)
    data_registeration_time = models.DateTimeField(blank=True, null=True)
    data_source = models.CharField(max_length=50)
    data_storage = models.CharField(max_length=1000)
    data_record_address = models.CharField(max_length=1000)
    theme = models.CharField(max_length=100, blank=True, null=True)
    null1 = models.CharField(max_length=100, blank=True, null=True)
    null2 = models.CharField(max_length=100, blank=True, null=True)
    null3 = models.CharField(max_length=100, blank=True, null=True)
    null4 = models.CharField(max_length=100, blank=True, null=True)
    null5 = models.CharField(max_length=100, blank=True, null=True)
    null6 = models.CharField(max_length=100, blank=True, null=True)
    null7 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DOA_T_DRC'


class DoaTPublicKey(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    psapk = models.CharField(db_column='PSAPK', max_length=1026)  # Field name made lowercase.
    rsa_aes = models.CharField(db_column='RSA_AES', max_length=1026, blank=True, null=True)  # Field name made lowercase.
    null1 = models.CharField(max_length=100, blank=True, null=True)
    null2 = models.CharField(max_length=100, blank=True, null=True)
    null3 = models.CharField(max_length=100, blank=True, null=True)
    null4 = models.CharField(max_length=100, blank=True, null=True)
    null5 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DOA_T_PUBLIC_KEY'


class DoaTUser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    regist_id = models.CharField(unique=True, max_length=20)
    regist_passwd = models.CharField(max_length=20)
    name = models.CharField(max_length=50, blank=True, null=True)
    birth = models.DateTimeField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    psapk = models.CharField(db_column='PSAPK', max_length=1026, blank=True, null=True)  # Field name made lowercase.
    register_drc_date = models.DateTimeField(blank=True, null=True)
    post = models.CharField(max_length=20, blank=True, null=True)
    politic = models.CharField(max_length=6, blank=True, null=True)
    regnum = models.CharField(db_column='regNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    test111111 = models.CharField(max_length=100, blank=True, null=True)
    null3 = models.CharField(max_length=100, blank=True, null=True)
    null4 = models.CharField(max_length=100, blank=True, null=True)
    null5 = models.CharField(max_length=100, blank=True, null=True)
    null6 = models.CharField(max_length=100, blank=True, null=True)
    null7 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DOA_T_USER'


class TActivity(models.Model):
    id = models.IntegerField(primary_key=True)
    poster_address = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    introduction = models.CharField(max_length=200, blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    md5 = models.CharField(max_length=32)
    start_date = models.DateTimeField(blank=True, null=True)
    data_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    null1 = models.CharField(max_length=100, blank=True, null=True)
    null2 = models.CharField(max_length=100, blank=True, null=True)
    null3 = models.CharField(max_length=100, blank=True, null=True)
    null4 = models.CharField(max_length=100, blank=True, null=True)
    null5 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_ACTIVITY'


class TAdvertisement(models.Model):
    company_id = models.CharField(primary_key=True, max_length=50)
    poster_address = models.CharField(max_length=100, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    md5 = models.CharField(max_length=32, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    data_date = models.DateTimeField(blank=True, null=True)
    null1 = models.CharField(max_length=100, blank=True, null=True)
    null2 = models.CharField(max_length=100, blank=True, null=True)
    null3 = models.CharField(max_length=100, blank=True, null=True)
    null4 = models.CharField(max_length=100, blank=True, null=True)
    null5 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_ADVERTISEMENT'


class TCandidateInfo1(models.Model):
    user_id = models.CharField(db_column='USER_ID', primary_key=True, max_length=18)  # Field name made lowercase.
    name = models.CharField(max_length=20, blank=True, null=True)
    position_applied = models.CharField(max_length=100)
    resume_name = models.CharField(max_length=50, blank=True, null=True)
    previous_company_1 = models.CharField(max_length=50, blank=True, null=True)
    school_1 = models.CharField(max_length=50, blank=True, null=True)
    specialty_1 = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=30, blank=True, null=True)
    work_experience_date = models.FloatField(blank=True, null=True)
    expected_salary = models.CharField(max_length=11, blank=True, null=True)
    delivery_time = models.DateTimeField(blank=True, null=True)
    position_type = models.CharField(max_length=2, blank=True, null=True)
    previous_company_2 = models.CharField(max_length=50, blank=True, null=True)
    hiredate_2 = models.DateTimeField(blank=True, null=True)
    departure_2 = models.DateTimeField(blank=True, null=True)
    hiredate_1 = models.DateTimeField(blank=True, null=True)
    departure_1 = models.DateTimeField(blank=True, null=True)
    previous_position_1 = models.CharField(max_length=50, blank=True, null=True)
    previous_position_2 = models.CharField(max_length=50, blank=True, null=True)
    graduation_date_1 = models.DateTimeField(blank=True, null=True)
    school_2 = models.CharField(max_length=50, blank=True, null=True)
    specialty_2 = models.CharField(max_length=100, blank=True, null=True)
    graduation_date_2 = models.DateTimeField(blank=True, null=True)
    self_description = models.TextField(db_column='self-description', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    supplement = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    data_date = models.DateTimeField(blank=True, null=True)
    null1 = models.CharField(max_length=100, blank=True, null=True)
    null2 = models.CharField(max_length=100, blank=True, null=True)
    null3 = models.CharField(max_length=100, blank=True, null=True)
    null4 = models.CharField(max_length=100, blank=True, null=True)
    null5 = models.CharField(max_length=100, blank=True, null=True)
    null6 = models.CharField(max_length=100, blank=True, null=True)
    null7 = models.CharField(max_length=100, blank=True, null=True)
    com_app_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'T_CANDIDATE_INFO_1'


class TCandidateInfo2(models.Model):
    user_id = models.CharField(db_column='USER_ID', primary_key=True, max_length=18)  # Field name made lowercase.
    chinese_name = models.CharField(max_length=10, blank=True, null=True)
    english_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    md5 = models.CharField(max_length=32, blank=True, null=True)
    null1 = models.CharField(max_length=100, blank=True, null=True)
    null2 = models.CharField(max_length=100, blank=True, null=True)
    null3 = models.CharField(max_length=100, blank=True, null=True)
    null4 = models.CharField(max_length=100, blank=True, null=True)
    null5 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_CANDIDATE_INFO_2'


class TCandidateInfo3(models.Model):
    user_id = models.CharField(db_column='USER_ID', max_length=18)  # Field name made lowercase.
    project_name = models.CharField(max_length=20, blank=True, null=True)
    project_profile = models.CharField(max_length=3000, blank=True, null=True)
    display = models.CharField(max_length=100, blank=True, null=True)
    md5 = models.CharField(max_length=32, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    null1 = models.CharField(max_length=100, blank=True, null=True)
    null2 = models.CharField(max_length=100, blank=True, null=True)
    null3 = models.CharField(max_length=100, blank=True, null=True)
    null4 = models.CharField(max_length=100, blank=True, null=True)
    null5 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_CANDIDATE_INFO_3'


class TCompanyInfo(models.Model):
    company_id = models.CharField(primary_key=True, max_length=100)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    company_type = models.CharField(max_length=7, blank=True, null=True)
    industry_categroy = models.CharField(max_length=50, blank=True, null=True)
    company_scale = models.CharField(max_length=10, blank=True, null=True)
    company_representative_name = models.CharField(max_length=10, blank=True, null=True)
    contact_position = models.CharField(max_length=30, blank=True, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    company_profile = models.CharField(max_length=300, blank=True, null=True)
    provence = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    region = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=30, blank=True, null=True)
    certification = models.CharField(max_length=1, blank=True, null=True)
    vip = models.CharField(max_length=1, blank=True, null=True)
    md5_1 = models.CharField(max_length=32, blank=True, null=True)
    md5_2 = models.CharField(max_length=32, blank=True, null=True)
    register_id = models.CharField(max_length=20)
    job_count = models.CharField(max_length=20, blank=True, null=True)
    activity_degree = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    data_date = models.DateTimeField(blank=True, null=True)
    null1 = models.CharField(max_length=100, blank=True, null=True)
    null2 = models.CharField(max_length=100, blank=True, null=True)
    null3 = models.CharField(max_length=100, blank=True, null=True)
    null4 = models.CharField(max_length=100, blank=True, null=True)
    null5 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_COMPANY_INFO'


class TCompanyRegister(models.Model):
    register_id = models.CharField(primary_key=True, max_length=20)
    passwd = models.CharField(max_length=20)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    data_date = models.DateTimeField(blank=True, null=True)
    null1 = models.CharField(max_length=100, blank=True, null=True)
    null2 = models.CharField(max_length=100, blank=True, null=True)
    null3 = models.CharField(max_length=100, blank=True, null=True)
    null4 = models.CharField(max_length=100, blank=True, null=True)
    null5 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_COMPANY_REGISTER'


class TInterviewEvaluation(models.Model):
    company_id = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    application = models.CharField(max_length=20, blank=True, null=True)
    interview_job = models.CharField(max_length=20, blank=True, null=True)
    dot = models.IntegerField(blank=True, null=True)
    overall = models.CharField(max_length=40, blank=True, null=True)
    date = models.DateTimeField()
    interview_process = models.CharField(max_length=200, blank=True, null=True)
    other = models.CharField(max_length=200, blank=True, null=True)
    overall_score = models.IntegerField(blank=True, null=True)
    description_score = models.IntegerField(blank=True, null=True)
    interviewer_score = models.IntegerField(blank=True, null=True)
    environment_score = models.IntegerField(blank=True, null=True)
    p_overall_score = models.IntegerField(blank=True, null=True)
    offline = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    data_date = models.DateTimeField(blank=True, null=True)
    null1 = models.CharField(max_length=100, blank=True, null=True)
    null2 = models.CharField(max_length=100, blank=True, null=True)
    null3 = models.CharField(max_length=100, blank=True, null=True)
    null4 = models.CharField(max_length=100, blank=True, null=True)
    null5 = models.CharField(max_length=100, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'T_INTERVIEW_EVALUATION'


class TJobPublish(models.Model):
    company_id = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    job = models.CharField(max_length=20, blank=True, null=True)
    release_time = models.DateTimeField(blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)
    experience_required = models.CharField(max_length=5, blank=True, null=True)
    education_required = models.CharField(max_length=4, blank=True, null=True)
    job_description = models.CharField(max_length=300, blank=True, null=True)
    job_required = models.CharField(max_length=300, blank=True, null=True)
    job_label = models.CharField(max_length=100, blank=True, null=True)
    is_exigency = models.CharField(max_length=1, blank=True, null=True)
    job_category = models.CharField(max_length=2, blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    data_date = models.DateTimeField(blank=True, null=True)
    null1 = models.CharField(max_length=100, blank=True, null=True)
    null2 = models.CharField(max_length=100, blank=True, null=True)
    null3 = models.CharField(max_length=100, blank=True, null=True)
    null4 = models.CharField(max_length=100, blank=True, null=True)
    null5 = models.CharField(max_length=100, blank=True, null=True)
    null6 = models.CharField(max_length=100, blank=True, null=True)
    null7 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_JOB_PUBLISH'


class TPersonalRegister(models.Model):
    register_id = models.CharField(primary_key=True, max_length=20)
    passwd = models.CharField(max_length=20)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    data_date = models.DateTimeField(blank=True, null=True)
    null1 = models.CharField(max_length=100, blank=True, null=True)
    null2 = models.CharField(max_length=100, blank=True, null=True)
    null3 = models.CharField(max_length=100, blank=True, null=True)
    null4 = models.CharField(max_length=100, blank=True, null=True)
    null5 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_PERSONAL_REGISTER'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
