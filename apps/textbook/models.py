from django.db import models
from apps.core.models import BaseModel

class TextBook(BaseModel):
    """
    Stores information about textbooks.
    Each textbook has a title, body (description/content),
    and an uploaded PDF file.
    """
    title = models.CharField(max_length=255)  # Title of the textbook
    description = models.TextField()                 # Description or content
    pdf_file = models.FileField(upload_to="textbooks/", verbose_name="PDF File")  
    # FileField with upload path set to 'media/textbooks/'

    def __str__(self):
        return f'Title: {self.title}'
