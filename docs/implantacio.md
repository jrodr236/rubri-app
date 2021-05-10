```bash
mysql -u root

DROP DATABASE IF EXISTS rubriDB;
CREATE DATABASE rubriDB;
USE rubriDB;
CREATE USER 'rubriUserDB'@'localhost' IDENTIFIED BY 'qwerty776';
GRANT ALL PRIVILEGES ON * . * TO 'rubriUserDB'@'localhost';
FLUSH PRIVILEGES;
EXIT
```

La contrasenya utilitzada a ********** ha de configurar-se també al fitxer logica/claus.py
