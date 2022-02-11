\c bank
drop trigger newbaltrigger on transaction;
alter table transaction drop column oldbalance;
alter table transaction drop column newbalance;
CREATE OR REPLACE FUNCTION debitfunc() returns trigger AS $$
BEGIN
UPDATE account SET balance=balance+New.transactionamount WHERE accountnumber = new.accountnumber;
If exists (select * from account where balance<0) then
	UPDATE account SET balance=balance-New.transactionamount WHERE accountnumber = new.accountnumber;
	Raise exception 'Insufficienst Funds'; end if;
return new;
END; $$
LANGUAGE plpgsql;

create trigger newbaltrigger after insert on transaction for each row execute procedure debitfunc();

alter table creditcard add column Creditscore int Not NULL default 100 check(creditscore>0);

alter table account add constraint balchk check(balance>=2000);


