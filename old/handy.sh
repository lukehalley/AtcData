mysqldump --host='atcdbinstance.castyrwvsdr7.eu-west-1.rds.amazonaws.com' --user='atc_user' --password='arRr21<Qq?D68?Md' atc > atc_dump.sql

mysqldump --host='atcrestore.castyrwvsdr7.eu-west-1.rds.amazonaws.com' --user='atc_user' --password='arRr21<Qq?D68?Md' atc > atc_dump.sql





mysqldump --host='localhost' --user='root' --password='localatcdb' atc > atc_dump_local.sql

mysql --host='atcdbinstance.castyrwvsdr7.eu-west-1.rds.amazonaws.com' --user='atc_user' --password='arRr21<Qq?D68?Md' atc < atc_dump_local.sql
mysql --host='localhost' --user='root' --password='localatcdb' atc < atc_dump.sql