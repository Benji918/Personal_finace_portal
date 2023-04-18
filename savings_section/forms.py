from django import forms
from django.core.exceptions import ValidationError
from .models import SavingsAccount, Deposit, Withdrawal, SavingsGoal


class DateInput(forms.DateInput):
    input_type = 'date'


class SavingsAccountForm(forms.ModelForm):
    def is_valid(self):
        is_valid = super().is_valid()
        # add custom validation logic for the name field
        if 'name' in self.cleaned_data:
            name = self.cleaned_data['name']
            if name.startswith('X'):  # name should not start with 'X'
                self.add_error(field='name', error='Name should not start with X')
                is_valid = False
        if 'balance' in self.cleaned_data:
            balance = self.cleaned_data['balance']
            if balance <= 0:
                self.add_error(field='balance', error='balance must be greater than zero')
                is_valid = False
            elif balance != int(balance):
                self.add_error(field='balance', error='balance must be a whole number')
                is_valid = False
        return is_valid

    class Meta:
        model = SavingsAccount
        fields = ['name', 'balance', 'description']


class DepositForm(forms.ModelForm):
    def is_valid(self):
        is_valid = super().is_valid()
        # add custom validation logic for the name field
        if 'name' in self.cleaned_data:
            name = self.cleaned_data['name']
            if name.startswith('X'):  # name should not start with 'X'
                self.add_error(field='name', error='Name should not start with X')
                is_valid = False
        if 'amount' in self.cleaned_data:
            amount = self.cleaned_data['amount']
            if amount <= 0:
                self.add_error(field='amount', error='amount must be greater than zero')
                is_valid = False
            elif amount != int(amount):
                self.add_error(field='amount', error='amount must be a whole number')
                is_valid = False
        return is_valid

    class Meta:
        model = Deposit
        fields = ['name', 'amount', 'description']


class WithdrawalForm(forms.ModelForm):
    def is_valid(self):
        is_valid = super().is_valid()
        # add custom validation logic for the name field
        if 'name' in self.cleaned_data:
            name = self.cleaned_data['name']
            if name.startswith('X'):  # name should not start with 'X'
                self.add_error(field='name', error='Name should not start with X')
                is_valid = False
        if 'amount' in self.cleaned_data:
            amount = self.cleaned_data['amount']
            if amount <= 0:
                self.add_error(field='amount', error='amount must be greater than zero')
                is_valid = False
            elif amount != int(amount):
                self.add_error(field='amount', error='amount must be a whole number')
                is_valid = False
        return is_valid

    class Meta:
        model = Withdrawal
        fields = ['name', 'amount', 'description']


class SavingsGoalForm(forms.ModelForm):
    def is_valid(self):
        is_valid = super().is_valid()
        # add custom validation logic for the name field
        if 'name' in self.cleaned_data:
            name = self.cleaned_data['name']
            if name.startswith('X'):  # name should not start with 'X'
                self.add_error(field='name', error='Name should not start with X')
                is_valid = False
        if 'amount' in self.cleaned_data:
            amount = self.cleaned_data['amount']
            if amount <= 0:
                self.add_error(field='amount', error='amount must be greater than zero')
                is_valid = False
            elif amount != int(amount):
                self.add_error(field='amount', error='amount must be a whole number')
                is_valid = False
        return is_valid

    class Meta:
        model = SavingsGoal
        fields = ['name', 'amount', 'description']