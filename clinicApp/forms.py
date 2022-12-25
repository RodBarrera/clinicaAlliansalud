from django import forms
from django.core import validators
from django.core.validators import RegexValidator
from .models import Secretaria, Medico, Paciente, HojaAtencion


class SecretariaForm(forms.Form):
    Rut = forms.CharField()
    Nombres = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
        validators.MinLengthValidator(3, message='El nombre debe tener minimo 3 caracteres'),
        validators.MaxLengthValidator(50, message='El nombre debe tener maximo 15 caracteres'),
        ]
    )

    Apellido_Paterno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
         ]
    )
    Apellido_Materno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
        ]
    )


    Rut.widget.attrs['class'] = 'form-control'
    Nombres.widget.attrs['class'] = 'form-control'
    Apellido_Paterno.widget.attrs['class'] = 'form-control'
    Apellido_Materno.widget.attrs['class'] = 'form-control'

class SecretariaForm(forms.ModelForm):
    class Meta:
        model = Secretaria
        fields = '__all__'

    Rut = forms.CharField()
    Nombres = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
        validators.MinLengthValidator(3, message='El nombre debe tener minimo 3 caracteres'),
        validators.MaxLengthValidator(50, message='El nombre debe tener maximo 15 caracteres'),
        ]
    )

    Apellido_Paterno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
         ]
    )
    Apellido_Materno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
        ]
    )



    Rut.widget.attrs['class'] = 'form-control'
    Nombres.widget.attrs['class'] = 'form-control'
    Apellido_Paterno.widget.attrs['class'] = 'form-control'
    Apellido_Materno.widget.attrs['class'] = 'form-control'

class Especialidades(forms.Form):
    name = forms.CharField(max_length=50)
    class Meta:
        model = Medico
        fields = '__all__'


#medico


class MedicoForm(forms.Form):
    Rut = forms.CharField()
    Nombres = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
        validators.MinLengthValidator(3, message='El nombre debe tener minimo 3 caracteres'),
        validators.MaxLengthValidator(50, message='El nombre debe tener maximo 15 caracteres'),
        ]
    )

    Apellido_Paterno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El apellido debe tener maximo 15 caracteres'),
         ]
    )
    Apellido_Materno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(25, message='El apellido debe tener maximo 15 caracteres'),
        ]
    )

    Especialidad = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='La Especialidad debe contener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='La Especialidad debe contener maximo 15 caracteres'),
        ]
    )


    Rut.widget.attrs['class'] = 'form-control'
    Nombres.widget.attrs['class'] = 'form-control'
    Apellido_Paterno.widget.attrs['class'] = 'form-control'
    Apellido_Materno.widget.attrs['class'] = 'form-control'
    Especialidad.widget.attrs['class'] = 'form-control'

class MedicoForm(forms.ModelForm):
        class Meta:
            model = Medico
            fields = '__all__'

        Rut = forms.CharField()
        Nombres = forms.CharField(
            validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                       message='La primera letra debe contener mayuscula y debe ser caracteres'),
                        validators.MinLengthValidator(3, message='El nombre debe tener minimo 3 caracteres'),
                        validators.MaxLengthValidator(50, message='El nombre debe tener maximo 15 caracteres'),
                        ]
        )

        Apellido_Paterno = forms.CharField(
            validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                       message='La primera letra debe contener mayuscula y debe ser caracteres'),
                        validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                        validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
                        ]
        )
        Apellido_Materno = forms.CharField(
            validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                       message='La primera letra debe contener mayuscula y debe ser caracteres'),
                        validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                        validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
                        ]
        )
        Especialidad = forms.CharField(
            validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                       message='La primera letra debe contener mayuscula y debe ser caracteres'),
                        validators.MinLengthValidator(3, message='La Especialidad debe contener minimo 3 caracteres'),
                        validators.MaxLengthValidator(50, message='La especialdad debe contener maximo 15 caracteres'),
                        ]
        )
        Rut.widget.attrs['class'] = 'form-control'
        Nombres.widget.attrs['class'] = 'form-control'
        Apellido_Paterno.widget.attrs['class'] = 'form-control'
        Apellido_Materno.widget.attrs['class'] = 'form-control'
        Especialidad.widget.attrs['class'] = 'form-control'

       #paciente
class PacienteForm(forms.Form):
    Rut = forms.CharField()
    Nombres = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
        validators.MinLengthValidator(3, message='El nombre debe tener minimo 3 caracteres'),
        validators.MaxLengthValidator(50, message='El nombre debe tener maximo 15 caracteres'),
        ]
    )

    Apellido_Paterno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$', message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
         ]
    )
    Apellido_Materno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
        ]
    )

    Genero = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El Genero debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El Genero debe tener maximo 15 caracteres'),

                    ]
    )

    Fecha_Nacimiento = forms.CharField(
        validators=[]
    )

    Direccion = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z][0-9]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El adress debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El adress debe tener maximo 15 caracteres'),

                    ]
    )

    Comuna = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='La comuna debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='La comuna debe tener maximo 15 caracteres'),

                    ]
    )

    Telefono = forms.IntegerField()
    Contacto_de_Emergencia = forms.IntegerField()

    Telefono_de_Emergencia = forms.IntegerField()


    Nacionalidad = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El Nacionalidad debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El Nacionalidad debe tener maximo 15 caracteres'),

                    ]
    )

    Sistema_de_Salud = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El  campo salud tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo salud debe tener maximo 15 caracteres'),

                    ]
    )
# 2do
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

    Rut = forms.CharField()
    Nombres = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El nombre debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El nombre debe tener maximo 15 caracteres'),
                    ]
    )

    Apellido_Paterno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
                    ]
    )
    Apellido_Materno = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El apellido debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El apellido debe tener maximo 15 caracteres'),
                    ]
    )

    Genero = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El Genero debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El Genero debe tener maximo 15 caracteres'),

                    ]
    )

    Fecha_Nacimiento = forms.CharField(
        validators=[]
    )

    Direccion = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El adress debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El adress debe tener maximo 15 caracteres'),

                    ]
    )

    Comuna = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='La comuna debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='La comuna debe tener maximo 15 caracteres'),

                    ]
    )

    Telefono = forms.IntegerField()


    Contacto_de_Emergencia = forms.IntegerField()


    Telefono_de_Emergencia = forms.IntegerField()


    Nacionalidad = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El Nacionalidad debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El Nacionalidad debe tener maximo 15 caracteres'),

                    ]
    )

    Sistema_de_Salud = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El Sistema_de_Salud debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El Sistema_de_Salud debe tener maximo 15 caracteres'),

                    ]
    )

    Rut.widget.attrs['class'] = 'form-control'
    Nombres.widget.attrs['class'] = 'form-control'
    Apellido_Paterno.widget.attrs['class'] = 'form-control'
    Apellido_Materno.widget.attrs['class'] = 'form-control'
    Genero.widget.attrs['class'] = 'form-control'
    Fecha_Nacimiento.widget.attrs['class'] = 'form-control'
    Direccion.widget.attrs['class'] = 'form-control'
    Comuna.widget.attrs['class'] = 'form-control'
    Telefono.widget.attrs['class'] = 'form-control'
    Contacto_de_Emergencia.widget.attrs['class'] = 'form-control'
    Telefono_de_Emergencia.widget.attrs['class'] = 'form-control'
    Nacionalidad.widget.attrs['class'] = 'form-control'
    Sistema_de_Salud.widget.attrs['class'] = 'form-control'


#hoja atencion

class HojaForm(forms.Form):
    Rut_Paciente = forms.CharField()
    Profesional_que_Atendio = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),
                    ]
    )
    Fecha_Atencion = forms.CharField(
        validators=[]
    )
    Anamnesis = forms.CharField(widget=forms.Textarea())
    Medicamentos_Recetados = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),
                    ]
    )
    Examenes_Solicitados = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    Alergias = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    Historial_de_Enfermedades= forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    Medicamentos_que_toma = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    Diagnostico = forms.CharField(widget=forms.Textarea())

    Observaciones = forms.CharField(widget=forms.Textarea())


class HojaForm(forms.ModelForm):
    class Meta:
        model = HojaAtencion
        fields = '__all__'

    Rut_Paciente = forms.CharField()
    Profesional_que_Atendio  = forms.CharField()
    Fecha_Atencion = forms.CharField(
        validators=[]
    )
    Anamnesis = forms.CharField(widget=forms.Textarea())

    Medicamentos_Recetados = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),
                    ]
    )
    Examenes_Solicitados = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),
                    ]
    )
    Alergias = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),
                    ]
    )
    Historial_de_Enfermedades = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    Medicamentos_que_toma = forms.CharField(
        validators=[RegexValidator(regex='^[A-Z][a-z]*$',
                                   message='La primera letra debe contener mayuscula y debe ser caracteres'),
                    validators.MinLengthValidator(3, message='El campo debe tener minimo 3 caracteres'),
                    validators.MaxLengthValidator(50, message='El campo debe tener maximo 15 caracteres'),

                    ]
    )

    Diagnostico = forms.CharField(widget=forms.Textarea())

    Observaciones = forms.CharField(widget=forms.Textarea())

    Rut_Paciente.widget.attrs['class'] = 'form-control'
    Profesional_que_Atendio.widget.attrs['class'] = 'form-control'
    Fecha_Atencion.widget.attrs['class'] = 'form-control'
    Medicamentos_Recetados.widget.attrs['class'] = 'form-control'
    Anamnesis.widget.attrs['class'] = 'form-control'
    Examenes_Solicitados.widget.attrs['class'] = 'form-control'
    Alergias.widget.attrs['class'] = 'form-control'
    Historial_de_Enfermedades.widget.attrs['class'] = 'form-control'
    Medicamentos_que_toma.widget.attrs['class'] = 'form-control'
    Diagnostico.widget.attrs['class'] = 'form-control'
    Observaciones.widget.attrs['class'] = 'form-control'




