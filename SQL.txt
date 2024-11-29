CREATE TABLE Clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(300),
    telefone VARCHAR(20),
    email VARCHAR(100),
    data_nascimento DATE,
    cnh VARCHAR(20) UNIQUE NOT NULL,
    data_cadastro DATE DEFAULT CURRENT_DATE
);
INSERT INTO Clientes (id_cliente, nome, endereco, telefone, email, data_nascimento, cnh, data_cadastro) VALUES
(1,'Ana', 'Rua das Flores, 123', '(11) 91234-5678', 'ana@gmail.com', '1990-05-15', '12345678900', '10-01-2024'),
(2,'Bruno', 'Avenida Brasil, 456', '(21) 99876-5432', 'bruno@hotmail.com', '1985-08-20', '23456789001', '15-02-2024'),
(3,'Carla', 'Rua da Paz, 789', '(31) 98765-4321', 'carla@gmail.com', '1992-11-30', '34567890102', '03-05-2024'),
(4,'Daniel', 'Praça da Alegria, 101', '(41) 97654-3210', 'daniel@hotmail.com', '1988-01-25', '45678901203', '04-12-2024'),
(5,'Eduarda', 'Rua do Sol, 202', '(51) 96543-2109', 'eduarda@gmail.com', '1995-03-18', '56789012304', '22-05-2024'),
(6,'Felipe', 'Avenida do Mar, 303', '(61) 95432-1098', 'felipe@hotmail.com', '1991-07-09', '67890123405', '30-60-2024'),
(7,'Gabriela', 'Rua das Árvores, 404', '(71) 94321-0987', 'gabriela@gmail.com', '1987-12-12', '78901234506', '15-07-2024'),
(8,'Henrique', 'Avenida Central, 505', '(81) 93210-9876', 'henrique@hotmail.com', '1993-04-14', '89012345607', '15-07-2024'),
(9,'Isabela', 'Rua do Comércio, 606', '(91) 92109-8765', 'isabela@gmail.com', '1989-09-09', '90123456708', '12-04-2024'),
(10,'João', 'Rua da Liberdade, 707', '(11) 91098-7654', 'joao@hotmail.com', '1986-10-30', '01234567809', '12-04-2024'),
(11,'Karina', 'Avenida da Saúde, 808', '(21) 90987-6543', 'karina@gmail.com', '1994-06-21', '12345678910', '10-11-2024'),
(12,'Lucas', 'Rua do Futuro, 909', '(31) 89876-5432', 'lucas@hotmail.com', '1990-02-02', '23456789011', '12-12-2024'),
(13,'Mariana', 'Praça da Esperança, 111', '(41) 88765-4321', 'mariana@gmail.com', '1996-07-07', '34567890112', '01-01-2024'),
(14,'Nicolas', 'Rua do Conhecimento, 222', '(51) 87654-3210', 'nicolas@hotmail.com', '1984-03-30', '45678901213', '01-01-2024'),
(15,'Olivia', 'Avenida das Estrelas, 333', '(61) 76543-2109', 'olivia@gmail.com', '1998-11-11', '56789012314', '01-01-2024');

CREATE TABLE Veiculos (
    id_veiculo VARCHAR INTEGER PRIMARY KEY,
    modelo VARCHAR(50) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    ano INT CHECK (ano > 2020),
    placa VARCHAR(10) UNIQUE NOT NULL,
    cor VARCHAR(20),
    tipo_combustivel TEXT CHECK (tipo_combustivel IN ('Flex', 'Gasolina', 'Diesel', 'Eletrico')) NOT NULL,
    quilometragem DECIMAL(10, 5) DEFAULT 0,
    status TEXT CHECK (status IN ('Disponível', 'Alugado', 'Manutencao')) DEFAULT 'Disponível'
);
INSERT INTO Veiculos (id_veiculo, modelo, marca, ano, placa, cor, tipo_combustivel, quilometragem, status) VALUES
(1,'Civic', 'Honda', 2024, 'ABC1D23', 'Preto', 'Gasolina', 1500.00, 'Disponível'),
(2,'Corolla', 'Toyota', 2024, 'XYZ2E34', 'Prata', 'Flex', 2500.00, 'Disponível'),
(3,'Model 3', 'Tesla', 2024, 'TES3456', 'Branco', 'Eletrico', 0.00, 'Disponível'),
(4,'Onix', 'Chevrolet', 2024, 'DEF7G89', 'Vermelho', 'Flex', 3500.00, 'Disponível'),
(5,'Kwid', 'Renault', 2024, 'JKL8M90', 'Azul', 'Flex', 4200.00, 'Disponível'),
(6,'Tucson', 'Hyundai', 2024, 'UVW1X23', 'Cinza', 'Gasolina', 1000.00, 'Disponível'),
(7,'HR-V', 'Honda', 2024, 'RST2Y34', 'Preto', 'Gasolina', 4800.00, 'Disponível'),
(8,'Nivus', 'Volkswagen', 2024, 'NOP3Z45', 'Branco', 'Flex', 2200.00, 'Disponível'),
(9,'Tracker', 'Chevrolet', 2024, 'ABC4D56', 'Prata', 'Flex', 3000.00, 'Disponível'),
(10,'A3', 'Audi', 2024, 'FGH5I67', 'Azul', 'Gasolina', 4500.00, 'Disponível'),
(11,'C3', 'Citroën', 2024, 'JKL6M78', 'Vermelho', 'Gasolina', 1800.00, 'Disponível'),
(12,'Polo', 'Volkswagen', 2024, 'XYZ7N89', 'Cinza', 'Flex', 3900.00, 'Disponível'),
(13,'Compass', 'Jeep', 2024, 'RST8O90', 'Preto', 'Flex', 500.00, 'Disponível'),
(14,'Duster', 'Renault', 2024, 'NOP9P12', 'Branco', 'Flex', 4200.00, 'Disponível'),
(15,'Kicks', 'Nissan', 2024, 'ABC0Q23', 'Vermelho', 'Gasolina', 2600.00, 'Disponível');

CREATE TABLE Locacoes (
    id_locacao INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    id_veiculo INTEGER,
    data_inicio DATE NOT NULL,
    data_fim DATE,
    valor_total DECIMAL(10, 2) NOT NULL,
    status_pagamento TEXT CHECK (status_pagamento IN ('pendente', 'pago')) DEFAULT 'pendente',
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_veiculo) REFERENCES Veiculos(id_veiculo)
);
INSERT INTO Locacoes (id_locacao, id_cliente, id_veiculo, data_inicio, data_fim, valor_total, status_pagamento) VALUES
(1, 1, 1, '01-01-2024', '10-01-2024', 500.00, 'pago'),
(2, 2, 2, '05-01-2024', '12-01-2024', 300.00, 'pago'),
(3, 3, 3, '03-01-2024', '15-01-2024', 700.00, 'pendente'),
(4, 4, 4, '07-01-2024', '14-01-2024', 450.00, 'pago'),
(5, 5, 5, '10-01-2024', '20-01-2024', 600.00, 'pendente'),
(6, 6, 6, '02-01-2024', '09-01-2024', 400.00, 'pago'),
(7, 7, 7, '04-01-2024', '11-01-2024', 550.00, 'pendente'),
(8, 8, 8, '06-01-2024', '13-01-2024', 350.00, 'pago'),
(9, 9, 9, '08-01-2024', '15-01-2024', 500.00, 'pendente'),
(10, 10, 10, '09-01-2024', '16-01-2024', 450.00, 'pago'),
(11, 11, 11, '11-01-2024', '18-01-2024', 600.00, 'pendente'),
(12, 12, 12, '12-01-2024', '19-01-2024', 700.00, 'pago'),
(13, 13, 13, '13-01-2024', '20-01-2024', 800.00, 'pendente'),
(14, 14, 14, '14-01-2024', '21-01-2024', 300.00, 'pago'),
(15, 15, 15, '15-01-2024', '22-01-2024', 400.00, 'pendente');


CREATE TABLE Manutencoes (
    id_manutencao INTEGER PRIMARY KEY,
    id_veiculo INTEGER,
    data_manutencao DATE NOT NULL,
    descricao_servico TEXT,
    custo DECIMAL(10, 2) NOT NULL,
    id_funcionario INTEGER,
    FOREIGN KEY (id_veiculo) REFERENCES Veiculos(id_veiculo),
    FOREIGN KEY (id_funcionario) REFERENCES Funcionarios(id_funcionario)
);
INSERT INTO Manutencoes (id_manutencao, id_veiculo, data_manutencao, descricao_servico, custo, id_funcionario) VALUES
(1, 1, '10-01-2024', 'Troca de óleo', 350.00, 1),  
(2, 2, '15-01-2024', 'Alinhamento e balanceamento', 200.00, 1),  
(3, 3, '20-01-2024', 'Substituição de pastilhas de freio', 450.00, 1),  
(4, 4, '05-02-2024', 'Revisão geral', 1200.00, 4),  
(5, 5, '10-02-2024', 'Troca de pneus', 1800.00, 4),  
(6, 6, '01-03-2024', 'Verificação de sistema elétrico', 600.00, 1), 
(7, 7, '15-03-2024', 'Troca de filtro de ar', 200.00, 7), 
(8, 8, '01-04-2024', 'Limpeza de injetores', 500.00, 1), 
(9, 9, '10-04-2024', 'Troca de bateria', 450.00, 1), 
(10, 10, '20-04-2024', 'Reparo de suspensão', 1500.00, 12), 
(11, 11, '05-05-2024', 'Troca de fluido de freio', 350.00, 1), 
(12, 12, '15-05-2024', 'Verificação de arrefecimento', 200.00, 12), 
(13, 13, '01-06-2024', 'Substituição de correia dentada', 1500.00, 1), 
(14, 14, '10-06-2024', 'Troca de lâmpadas', 200.00, 14), 
(15, 15, '01-07-2024', 'Inspeção veicular', 500.00, 14); 

CREATE TABLE Pagamentos (
    id_pagamento INTEGER PRIMARY KEY,
    id_locacao INTEGER,
    data_pagamento DATE DEFAULT CURRENT_DATE,
    metodo_pagamento TEXT CHECK (metodo_pagamento IN ('cartão de crédito', 'cartão de débito', 'dinheiro', 'transferência bancária')) NOT NULL,
    valor_pago DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_locacao) REFERENCES Locacoes(id_locacao)
);
INSERT INTO Pagamentos (id_pagamento, id_locacao, data_pagamento, metodo_pagamento, valor_pago) VALUES
(1, 1, '15-01-2024', 'cartão de crédito', 1500.00),
(2, 2, '20-01-2024', 'dinheiro', 800.00),
(3, 3, '05-02-2024', 'cartão de débito', 1200.00),
(4, 4, '10-02-2024', 'transferência bancária', 2000.00),
(5, 5, '01-03-2024', 'cartão de crédito', 950.00),
(6, 6, '15-03-2024', 'dinheiro', 500.00),
(7, 7, '10-04-2024', 'cartão de débito', 1100.00),
(8, 8, '20-04-2024', 'transferência bancária', 1750.00),
(9, 9, '05-05-2024', 'cartão de crédito', 1300.00),
(10, 10, '15-05-2024', 'dinheiro', 600.00),
(11, 11, '01-06-2024', 'cartão de débito', 1400.00),
(12, 12, '10-06-2024', 'transferência bancária', 2200.00),
(13, 13, '05-07-2024', 'cartão de crédito', 1600.00),
(14, 14, '15-07-2024', 'dinheiro', 750.00),
(15, 15, '01-08-2024', 'cartão de débito', 1300.00);


CREATE TABLE Funcionarios (
    id_funcionario INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(50),
    data_admissao DATE DEFAULT CURRENT_DATE,
    salario DECIMAL(10, 2)
);
INSERT INTO Funcionarios (id_funcionario, nome, cargo, data_admissao, salario) VALUES
(1, 'João', 'Mecânico', '01-02-2024', 2500.00),
(2, 'Maria', 'Atendente', '01-02-2024', 1800.00),
(3, 'Carlos', 'Gerente', '01-02-2024', 4000.00),
(4, 'Ana', 'Mecânico', '01-02-2024', 2700.00),
(5, 'Lucas', 'Assistente', '10-02-2024', 1500.00),
(6, 'Fernanda', 'Recepcionista', '01-02-2024', 2000.00),
(7, 'Roberto', 'Mecânico', '01-02-2024', 3000.00),
(8, 'Patrícia', 'Gerente de Oficina', '01-06-2024', 4500.00),
(9, 'Juliana', 'Assistente', '01-06-2024', 2200.00),
(10, 'Ricardo', 'Mecânico', '01-06-2024', 2800.00),
(11, 'Sofia', 'Atendente', '01-06-2024', 1900.00),
(12, 'Eduardo', 'Mecânico', '01-06-2024', 2600.00),
(13, 'Cláudia', 'Gerente', '01-06-2024', 4200.00),
(14, 'Thiago', 'Mecânico', '01-06-2024', 3000.00),
(15, 'Isabela', 'Recepcionista', '01-06-2024', 2100.00);