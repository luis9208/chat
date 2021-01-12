from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib import messages
from chat.forms import UserRegisterForm, MessagesForm
from chat.serializers import ProfileSerializer, UserSerializer, MessageSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from chat.models import Mensajes, Profile

class Register(APIView):
    __template= 'register.html'
    def get(self, request):
        form = UserRegisterForm()
        context={'form': form}
        return render(request, self.__template, context )
    
    def post(self, request):
        data = request.data
        form = UserRegisterForm(data)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = make_password(form.cleaned_data['password2'])
            data_user = {
                'username': username,
                'password': password,
                'email':form.cleaned_data['email']
            }
            user = UserSerializer(data= data_user)
            if user.is_valid():
                messages.success(request, f'el usuario {username} ha sido creado con exito')
                user.save()
            else:
                messages.error(request, f'el usuario {username} no se pudo crear')
                
        context={'form': form}
        
        return render(request, self.__template, context)
    
class Chat(APIView):
    __template_name = 'chat.html'
    __context = {}
    
    def getContext(self):
        return self.__context
    def setcontext(self, context):
        self.__context = context
        
    def get(self, request):
        if request.user.is_authenticated:
            current_user = request.user
            model = Mensajes.objects.all()
            users = Profile.objects.all()
            cant_messages = model.filter(user_id=current_user.pk)
            form = MessagesForm()
            
            # image_profile = Profile.objects.get(user=current_user)
            context = {
                'current_user':current_user,
                'cant_messages':len(cant_messages),
                'users':users,
                'mensajes': model,
                'form':form
            }
            self.setcontext(context)
            return render(request, self.__template_name, self.getContext())
        else:
            return redirect('login')
        
    def post(self, request):
        if request.user.is_authenticated:
            context = self.getContext()
            
            current_user = request.user
            if request.POST.get('click', True):
                data = request.data
                form = MessagesForm(data)
                context.update( {
                    'form':form
                    })
               
                data_msg = {
                    'user': request.user.pk,
                    'content': data['content']
                }
                
                
                if form.is_valid():
                    print('vamos bien')
                    msg =  MessageSerializer(data=data_msg)
                    if msg.is_valid():
                        msg.save()
                else:
                    print('vamos mal')
                    
                return self.get(request)
                
            # return render(request, self.__template_name, context)
            