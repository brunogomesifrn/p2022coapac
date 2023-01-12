from django.db import models
from django.contrib.auth.models import AbstractUser

class Tipo(models.Model):
    nome = models.CharField('Nome', max_length=100)
    def __str__(self):
        return self.nome

class Objeto(models.Model):
    nome = models.CharField('Nome', max_length=100) 
    prazo = models.IntegerField("Prazo")
    tipos = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Usuario(AbstractUser):
    matricula = models.CharField('Matricula',max_length=14, primary_key=True)
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email')
    senha = models.CharField('Senha', max_length=40)
    telefone = models.CharField('Telefone', max_length=9)
    def __str__(self):
        return self.nome

    USERNAME_FIELD = 'matricula'

    class Meta:
        permissions = [
            ("servidor","Permissão para usuários Servidor, pode consultar situação de empréstimos"),
            ("coapac","Permissão para usuários COAPAC, pode gerenciar empréstimos, objetos, gerenciar tipos_objetos, gerenciar status e gerar relatórios"),
            ("administrador","Permissão para usuários Administrador, pode gerenciar empréstimos, objetos, gerenciar tipos_objetos, gerenciar status e gerar relatórios")
                        
        ]  

class Emprestimo(models.Model):
    quantidade = models.IntegerField("Quantidade")
    data_emprestimo = models.DateTimeField("Data de Empréstimo")
    data_devolucao = models.DateTimeField("Data de Devolução")
    observacao = models.TextField("Observação")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    objeto = models.ManyToManyField(Objeto)  
    def __str__(self):
        return self.objeto
'''
CREATE DATABASE IF NOT EXISTS coapac;

USE coapac;

CREATE TABLE IF NOT EXISTS usuario(
    matricula VARCHAR(14) NOT NULL PRIMARY KEY,
    nome VARCHAR(100),
    senha CHAR(40), 
    telefone VARCHAR(9)
);

CREATE TABLE IF NOT EXISTS emprestimo(
    id INT NOT NULL auto_increment PRIMARY KEY,
    quantidade INT,
    data_emprestimo DATETIME,
    data_devolucao DATETIME,
    observacao TEXT
);

CREATE TABLE IF NOT EXISTS tipo(
    id INT NOT NULL auto_increment PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS objeto(
    id INT NOT NULL auto_increment PRIMARY KEY,
    nome VARCHAR(100),
    id_tipo INT,
    prazo INT,
    FOREIGN KEY (id_tipo) REFERENCES tipo(id)
);

CREATE TABLE IF NOT EXISTS responsavel(
    id INT NOT NULL auto_increment PRIMARY KEY,
    id_objeto INT ,
    matricula_usuario VARCHAR(14),
    FOREIGN KEY (id_objeto) REFERENCES objeto(id),
    FOREIGN KEY (matricula_usuario) REFERENCES usuario(matricula)
);

CREATE TABLE IF NOT EXISTS objeto_emprestimo(
    id INT NOT NULL auto_increment PRIMARY KEY,
    id_objeto INT,   
    id_emprestimo INT,
    
    FOREIGN KEY (id_objeto) REFERENCES objeto(id),
    FOREIGN KEY (id_emprestimo) REFERENCES emprestimo(id)

'''