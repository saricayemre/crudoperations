from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField

class CreateTask(FlaskForm):
    title = TextField('Görev Başlığı')
    shortdesc = TextField('Açıklama')
    priority = IntegerField('Numara')
    create = SubmitField('Ekle')

class DeleteTask(FlaskForm):
    key = TextField('Görev ID')
    title = TextField('Görev Başlığı')
    delete = SubmitField('Sil')

class UpdateTask(FlaskForm):
    key = TextField('Görev ID')
    shortdesc = TextField('Yeni Açıklama')
    update = SubmitField('Güncelle')

class ResetTask(FlaskForm):
    reset = SubmitField('Temizle')
