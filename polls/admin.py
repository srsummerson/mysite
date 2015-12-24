from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3  # provides 3 blank lines for adding additional choices to associated question

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Main information', {'fields':['question_text']}),
		('Date information', {'fields': ['pub_date'],'classes':['collapse']})
	]

	inlines = [ChoiceInLine]  # associates choice model entries on question admin page
	list_display = ('question_text','pub_date','was_published_recently')  # defines fields that are shown on admin page that displays all the questions in the system
	list_filter = ['pub_date']  # adds filter sidebar to allow filtering by pub_date field
	search_fields = ['question_text']	# adds a search box at the top of the change list (page where all questions are shown)

admin.site.register(Question, QuestionAdmin)
