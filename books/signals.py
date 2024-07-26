from django.db.models.signals import pre_save
from django.dispatch import receiver
import google.generativeai as genai
from .models import Book



@receiver(pre_save, sender=Book)
def synopsis_ia_pre_save(sender, instance, **kwargs):
   
    if not instance.synopsis:
        #esconder ela, dado sensivel
        API_KEY = 'AIzaSyAMpIJ9Zw5D5hNvgWwfafJ7QOzf6aKSWYo'
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-pro')

        response = model.generate_content(f'Faça um resumo de {instance.title} sem spoiler com no maximo 200 caracteres, em pt-br.')
        
        if response and response._result.candidates:

            instance.synopsis = response._result.candidates[0].content.parts[0].text