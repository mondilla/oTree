# -*- coding: utf-8 -*-
import demo_game.models as models
from django import forms
from demo_game._builtin import Form
from crispy_forms.layout import HTML
from django.utils.translation import ugettext_lazy as _, ugettext


# show case forms
class DemoForm(Form):
    '''A form to demo_game various form elements'''
    class Meta:
        model = models.Player
        #fields = ['demo_field1', 'demo_field2', 'demo_field3', 'demo_field4', 'demo_field5']
        fields = ['demo_field1', 'demo_field3']
        # custom form widgets
        widgets = {
            'demo_field1': forms.RadioSelect(),
            #'demo_field2': forms.Textarea(),
            'demo_field3': forms.TextInput(),
            #'demo_field4': forms.SelectMultiple(),
            #'demo_field5': forms.TextInput()
        }

    def labels(self):
        return {
            'demo_field1': '<p>Here is a radio button which is when there is only one correct answer:</p>'
                           '<p><i>I am a radio button. How many answers can you select here?</i></p>',
            'demo_field3': '<p>I am a text input field, meaning I have a restriction of characters, in this case to 5 \
            characters. For unlimited character entry one would use a text area field (these field names are Django \
            jargon by the way which is familiar to many Python programmers).</p><p><i> I am a text input field. Please enter no more than 5 letters or numbers. \
            What is the name of this software platform?</i></p>',
            #'demo_field3': 'TextInput',
            #'demo_field4': 'Select',
            #'demo_field5': 'Numerical Input',
        }

    def demo_field5_error_message(self, value):
        '''Validating demo_field6 to allow only odd and positive numbers'''
        if value % 2 == 0 or value < 0:
            return 'The number should be odd and greater than zero'
    '''
    def order(self):
        return ['demo_field1', HTML('<p>Allows only selection of one input.</p>'),
                'demo_field3', HTML('<p>Allows for entry of text inputs, restricted to 50 letters</p>'),
                'demo_field2', HTML('<p>Allows for entry of text input. No limit of words or characters used.</p>'),
                'demo_field4', HTML('<p>Allows for selection of only one input from the given select list</p>'),
                'demo_field5', HTML('<p>Allows for entry of only positive odd numbers</p>'),
                ]
    '''


class QuestionForm1(Form):

    class Meta:
        model = models.Player
        fields = ['training_question_1']

    def order(self):
        return [
            HTML(u'<p>{}</p>'.format(ugettext('How many understanding questions are there? \
            Please enter an odd negative number, zero or any positive number:'),)),
            'training_question_1',
        ]


class QuestionForm2(Form):

    class Meta:
        model = models.Player
        fields = ['training_question_2']

        widgets = {'training_question_2': forms.RadioSelect()}

    def order(self):
        return [
            HTML(u'<h4>{}</h4>'.format(ugettext('All the following are possible in oTree except one?'),)),
            'training_question_2',
        ]