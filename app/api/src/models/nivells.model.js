'user strict';
var dbConn = require('../../config/db.config');

//Criteri object create
var Criteri = function (nivell) {
    this.nom = nivell.nom;
    this.nom_criteri = nivell.nom_criteri;
    this.nom_rubrica = nivell.nom_rubrica;
    this.descripcio = nivell.descripcio;
    this.qualificacio = nivell.qualificacio;
};
Criteri.create = function (newEmp, result) {
    dbConn.query("INSERT INTO employees set ?", newEmp, function (err, res) {
        if (err) {
            console.log("error: ", err);
            result(err, null);
        }
        else {
            console.log(res.insertId);
            result(null, res.insertId);
        }
    });
};
Criteri.findById = function (id, result) {
    dbConn.query("Select * from employees where id = ? ", id, function (err, res) {
        if (err) {
            console.log("error: ", err);
            result(err, null);
        }
        else {
            result(null, res);
        }
    });
};
Criteri.findAll = function (result) {
    dbConn.query(
        "SELECT nom, nom_criteri, nom_rubrica, descripcio, qualificacio \
        FROM Nivell \
        ORDER BY qualificacio",
        function (err, res) {
            if (err) {
                console.log("error: ", err);
                result(null, err);
            }
            else {
                console.log('criteri : ', res);
                result(null, res);
            }
        });
};
Criteri.update = function (id, employee, result) {
    dbConn.query("UPDATE employees SET first_name=?,last_name=?,email=?,phone=?,organization=?,designation=?,salary=? WHERE id = ?", [employee.first_name, employee.last_name, employee.email, employee.phone, employee.organization, employee.designation, employee.salary, id], function (err, res) {
        if (err) {
            console.log("error: ", err);
            result(null, err);
        } else {
            result(null, res);
        }
    });
};
Criteri.delete = function (id, result) {
    dbConn.query("DELETE FROM employees WHERE id = ?", [id], function (err, res) {
        if (err) {
            console.log("error: ", err);
            result(null, err);
        }
        else {
            result(null, res);
        }
    });
};

module.exports = Criteri;