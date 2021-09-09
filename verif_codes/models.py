from django.db import models

class ParamsVerificationCodeTypes(models.Model):
    description = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return self.description
    class Meta:
        managed = False
        db_table = 'PARAMS_VERIFICATION_CODE_TYPES'
        verbose_name_plural = "Verification Code Types"
        verbose_name = "Verification Code Type"

class ParamsVerificationEntityTypes(models.Model):
    description = models.CharField(max_length=45)
    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'PARAMS_VERIFICATION_ENTITY_TYPES'
        verbose_name_plural = "Entity Types"
        verbose_name = "Entity Type"


class VerificationCodes(models.Model):
    
    id_code = models.AutoField(primary_key=True)
    code = models.IntegerField()
    identity = models.CharField(max_length=45)
    expiration_date = models.DateTimeField()
    entity_type = models.ForeignKey(ParamsVerificationEntityTypes, models.DO_NOTHING, db_column='entity_type', blank=True, null=True)
    code_type = models.ForeignKey(ParamsVerificationCodeTypes, models.DO_NOTHING, db_column='code_type', blank=True, null=True)
    message_id = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return f"VCODE {self.code} <{self.identity}>"
    class Meta:
        managed = False
        db_table = 'VERIFICATION_CODES'
        verbose_name_plural = "Verification Codes"
        verbose_name = "Verification Code"
