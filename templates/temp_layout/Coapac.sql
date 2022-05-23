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
);
