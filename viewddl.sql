\c bank
drop owned by jones2001;
drop user jones2001;
drop owned by alex2001;
drop user alex2001;
drop owned by james2001;
drop user james2001;
drop owned by staff1;
drop user staff1;
drop owned by staff2;
drop user staff2;
create user JONES2001 with encrypted password 'JONES123';
create user ALEX2001 with encrypted password 'ALEX123';
create user JAMES2001 with encrypted password 'JAMES123';
create user staff1 with encrypted password 'staff1';
create user staff2 with encrypted password 'staff2';
create user DBA;
grant insert on transaction to JONES2001;
grant insert on transaction to ALEX2001;
grant insert on transaction to JAMES2001;

create view custjoinedview as (
select * from customer natural left outer join account A natural left outer join debitcard natural left outer join creditcard as cr(creditcardnumber,accountnumber,cvv_cr,pin_cr,expirydate_cr) left outer join beneficiary on customercifnumber= cifnumber natural left outer join insurance natural left outer join loans as lon(loandid,cifnumber,accnum,loanduration,loantype,loanamount,loaninterest) natural left outer join investments as inv(investmentid,cifnumber,acno,investmentduration,investmenttype,investmentamount,inv_interest));


create view jones2001v as (select * from custjoinedview where username='JONES2001');

create view james2001v as (select * from custjoinedview where username='JAMES2001');

create view alex2001v as (select * from custjoinedview where username='ALEX2001');

grant select on jones2001v to JONES2001;
grant select on james2001v to JAMES2001;
grant select on alex2001v to ALEX2001;

grant all privileges on account,beneficiary,branch,customer,insurance,investments,loans,staff,transaction to staff1;
grant all privileges on account,beneficiary,branch,customer,insurance,investments,loans,staff,transaction to staff2;
grant all privileges on database bank to DBA;

