'user strict';
var dbConn = require('../../config/db.config');

//Criteri object create
var Criteri = function (criteri) {
    this.nom = criteri.nom;
    this.nom_rubrica = criteri.nom_rubrica;
    this.numero_uf = criteri.numero_uf;
    this.descripcio = criteri.descripcio;
    this.pes = criteri.pes;
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
        "SELECT nom, nom_rubrica, numero_uf, descripcio, pes \
        FROM Criteri",
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