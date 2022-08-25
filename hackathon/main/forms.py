from django import forms
from main import models


def getChoices():
    return tuple(models.CompanyInfo.objects.values_list('company_problem_statement', 'company_problem_statement'))


class TeamRegForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeamRegForm, self).__init__(*args, **kwargs)
        # problem_list = getChoices()
        # self.fields['problem_statement_1'].choices = problem_list
        # self.fields['problem_statement_2'].choices = problem_list
        # self.fields['problem_statement_3'].choices = problem_list
        # self.fields['problem_statement_4'].choices = problem_list
        self.fields['team_leader_gender'].choices = self.fields['teammate1_gender'].choices = self.fields[
            'teammate2_gender'].choices = self.fields['teammate3_gender'].choices = models.GENDER_CHOICES

    def clean(self):
        cleaned_data = super(TeamRegForm, self).clean()
        p1 = cleaned_data.get('problem_statement_1')
        p2 = cleaned_data.get('problem_statement_2')
        p3 = cleaned_data.get('problem_statement_3')
        # p4 = cleaned_data.get('problem_statement_4')

        # if (p1==p2 or p1==p3) or (p2==p3) :
        #     raise forms.ValidationError('All three problem statement must be different')

    class Meta:
        model = models.StudentForm
        fields = '__all__'
