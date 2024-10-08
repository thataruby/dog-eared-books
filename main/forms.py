from django.forms import ModelForm
from main.models import BookEntry
from django.utils.html import strip_tags

class BookEntryForm(ModelForm):
    class Meta:
        model = BookEntry
        fields = ["title", "author", "price", "genre", "summary"]

    def clean_title(self):
        title = self.cleaned_data["title"]
        return strip_tags(title)

    def clean_author(self):
        author = self.cleaned_data["author"]
        return strip_tags(author)

    def clean_genre(self):
        genre = self.cleaned_data["genre"]
        return strip_tags(genre)
    
    def clean_summary(self):
        summary = self.cleaned_data["summary"]
        return strip_tags(summary)