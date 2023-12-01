from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "tags", "due_date"]

    # Override the clean_tags method to handle updating the tags field
    def clean_tags(self):
        new_tags = self.cleaned_data.get('tags', '')
        current_tags = self.instance.tags

        # Combine existing tags with new tags (if any)
        updated_tags = f"{current_tags}, {new_tags}" if current_tags else new_tags

        return updated_tags

    # Ensure that 'status' is required
    def clean_status(self):
        status = self.cleaned_data.get('status')
        if not status:
            raise forms.ValidationError("This field is required.")
        return status
