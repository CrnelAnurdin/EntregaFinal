from django.forms import ModelForm
from .models import WatchList, NewComentarios

class CreateWatchList(ModelForm):
    class Meta:
            model = WatchList
            fields = ['name','title','category']
            
class PuntuarWatchList(ModelForm):
    class Meta:
            model = WatchList
            fields = ['rate','visto']          
            
class FormComentarios (ModelForm):
    class Meta:
        model = NewComentarios
        fields = ['name','email','telefono','mensaje']
            


