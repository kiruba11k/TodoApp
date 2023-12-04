from django import forms
from .models import Task
import re


class TaskForm(forms.ModelForm):
    """
    Form for creating and updating Task instances.
    """

    class Meta:
        model = Task
        fields = ["title", "description", "status", "tags", "due_date"]
        widgets = {'due_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}), }

    def clean_tags(self):
        """
        Clean method for handling the 'tags' field.
        """
        new_tags = self.cleaned_data.get('tags', '')
        current_tags = self.instance.tags

        # Combine existing tags with new tags (if any)
        updated_tags = f"{current_tags}, {new_tags}" if current_tags else new_tags

        return updated_tags

    def clean_status(self):
        """
        Clean method for ensuring 'status' is required.
        """
        status = self.cleaned_data.get('status')
        if not status:
            raise forms.ValidationError("This field is required.")
        return status

    def clean_due_date(self):
        """
        Clean method for handling the 'due_date' field.
        """
        due_date = self.cleaned_data.get('due_date')
        if due_date and not re.match(r'\d{4}-\d{2}-\d{2}', str(due_date)):
            raise forms.ValidationError("Enter a valid date format (YYYY-MM-DD).")
        return due_date
