INSERT INTO pos_portal_studentaccounts (id,accountnumber,encryped_acc_no,bank_name,expirerydate,name_id,studentprofiles_id)VALUES(1,'0020197663588','0020XXXX3588','Bank XYZ','2018-01-01',1,'001');

INSERT INTO pos_portal_studentaccountswallets (id,walletname_name,max_amount,opendate,studentprofiles_id)VALUES(1,'School Fees',50000,'2016-01-01','001');
INSERT INTO pos_portal_studentaccountswallets (id,walletname_name,max_amount,opendate,studentprofiles_id)VALUES(2,'Pocket Money',5000,'2016-01-01','001');
INSERT INTO pos_portal_studentaccountswallets (id,walletname_name,max_amount,opendate,studentprofiles_id)VALUES(3,'Savings',50000,'2016-01-01','001');

INSERT INTO pos_portal_studentaccountswallets (id,walletname_name,max_amount,opendate,studentprofiles_id)VALUES(4,'School Fees',45000,'2016-01-01','002');
INSERT INTO pos_portal_studentaccountswallets (id,walletname_name,max_amount,opendate,studentprofiles_id)VALUES(5,'Pocket Money',2500,'2016-01-01','002');
INSERT INTO pos_portal_studentaccountswallets (id,walletname_name,max_amount,opendate,studentprofiles_id)VALUES(6,'Savings',1000,'2016-01-01','002');

INSERT INTO pos_portal_transactions(transaction_type,amount,transaction_date,trace_no,ref_no,currency,location_id,wallet_id,terminal_id,balance,reverse) VALUES ('Deposit',50000,NOW(),1111,3432,'KSH',1,1,1,50000,0);
INSERT INTO pos_portal_transactions(transaction_type,amount,transaction_date,trace_no,ref_no,currency,location_id,wallet_id,terminal_id,balance,reverse) VALUES ('Deposit',2000,NOW(),1111,3432,'KSH',1,2,1,2000,0);
INSERT INTO pos_portal_transactions(transaction_type,amount,transaction_date,trace_no,ref_no,currency,location_id,wallet_id,terminal_id,balance,reverse) VALUES ('Deposit',500,NOW(),1111,3432,'KSH',1,3,1,500,0);
INSERT INTO pos_portal_transactions(transaction_type,amount,transaction_date,trace_no,ref_no,currency,location_id,wallet_id,terminal_id,balance,reverse) VALUES ('Withdraw',50,NOW(),1111,3432,'KSH',1,2,1,1950,0);
INSERT INTO pos_portal_transactions(transaction_type,amount,transaction_date,trace_no,ref_no,currency,location_id,wallet_id,terminal_id,balance,reverse) VALUES ('Withdraw',30,NOW(),1111,3432,'KSH',1,2,1,1930,0);

INSERT INTO pos_portal_transactions(transaction_type,amount,transaction_date,trace_no,ref_no,currency,location_id,wallet_id,terminal_id,balance,reverse) VALUES ('Deposit',30000,NOW(),1111,3432,'KSH',1,4,1,30000,0);
INSERT INTO pos_portal_transactions(transaction_type,amount,transaction_date,trace_no,ref_no,currency,location_id,wallet_id,terminal_id,balance,reverse) VALUES ('Deposit',1500,NOW(),1111,3432,'KSH',1,5,1,1500,0);
INSERT INTO pos_portal_transactions(transaction_type,amount,transaction_date,trace_no,ref_no,currency,location_id,wallet_id,terminal_id,balance,reverse) VALUES ('Deposit',900,NOW(),1111,3432,'KSH',1,6,1,900,0);
INSERT INTO pos_portal_transactions(transaction_type,amount,transaction_date,trace_no,ref_no,currency,location_id,wallet_id,terminal_id,balance,reverse) VALUES ('Withdraw',20,NOW(),1111,3432,'KSH',1,5,1,1480,0);
INSERT INTO pos_portal_transactions(transaction_type,amount,transaction_date,trace_no,ref_no,currency,location_id,wallet_id,terminal_id,balance,reverse) VALUES ('Withdraw',40,NOW(),1111,3432,'KSH',1,5,1,1440,0);
