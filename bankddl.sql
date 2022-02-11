drop database bank;
create database bank;
\c bank;

CREATE TABLE 	BRANCH
	(	
		BranchID VARCHAR(8),
		IFSC_Code VARCHAR(11) NOT NULL UNIQUE,
		BranchPhone DECIMAL(8,0) NOT NULL,
		BranchEmail VARCHAR,
		PRIMARY KEY (BranchID)
	);

CREATE TABLE 	CUSTOMER
	(	
		CIFNumber DECIMAL(11,0),
		Name VARCHAR NOT NULL,
		UID VARCHAR(16) NOT NULL UNIQUE,
		Username VARCHAR,
		Password VARCHAR,
		CustPhone DECIMAL(10,0)  NOT NULL,
		CustEmail VARCHAR,
		PRIMARY KEY (CIFNumber)
	);

CREATE TABLE 	ACCOUNT
	(	
		AccountNumber DECIMAL(11,0),
		BranchID VARCHAR(8) NOT NULL,
		CIFNumber DECIMAL(11,0) NOT NULL,
		Balance INT,
		PRIMARY KEY (AccountNumber),
		FOREIGN KEY (CIFNumber) REFERENCES 		Customer(CIFNumber) ON update cascade On delete set null,
		FOREIGN KEY (BranchID) REFERENCES 		Branch(BranchID)ON update cascade On delete set null
	);

CREATE TABLE 	DEBITCARD
	(
	 	DebitCardNumber DECIMAL(16,0),
	 	AccountNumber DECIMAL(11,0) NOT NULL UNIQUE,
		CVV DECIMAL(3,0) NOT NULL,
		PIN DECIMAL(4,0),
		ExpiryDate DATE NOT NULL,
		PRIMARY KEY (DebitCardNumber),
		FOREIGN KEY (AccountNumber) REFERENCES 		ACCOUNT(AccountNumber) ON update cascade On delete set null      
	);
	
CREATE TABLE 	CREDITCARD
	(
	 	CreditCardNumber DECIMAL(16,0),
	 	AccountNumber DECIMAL(11,0) NOT NULL UNIQUE,
		CVV DECIMAL(3,0) NOT NULL,
		PIN DECIMAL(4,0),
		ExpiryDate DATE NOT NULL,
		PRIMARY KEY (CreditCardNumber),
		FOREIGN KEY (AccountNumber) REFERENCES 		ACCOUNT(AccountNumber)  ON update cascade On delete set null     
	);

CREATE TABLE 	STAFF
 	(	
		StaffID DECIMAL(13,0),
		BranchID VARCHAR(8) NOT NULL,
		NAME VARCHAR NOT NULL, 
		JobID DECIMAL(3,0),
		JobName VARCHAR,
		UID VARCHAR(16) NOT NULL UNIQUE,
		Salary INT,
		StaffPhone DECIMAL(10,0),
		CIFNumber DECIMAL(11,0),
		PRIMARY KEY (StaffID),
		FOREIGN KEY (CIFNumber) REFERENCES CUSTOMER(CIFNumber)ON update cascade On delete set null,
		FOREIGN KEY (BranchID) REFERENCES BRANCH(BranchID)	ON update cascade On delete set null
	);


CREATE TABLE 	LOANS
	(	
		LoanID DECIMAL(10),
		CIFNumber DECIMAL(11) NOT NULL,
		AccountNumber DECIMAL(11),
		LoanDuration FLOAT,
		LoanType VARCHAR,
		LoanAmount INT,
		Interest FLOAT,
		PRIMARY KEY (LoanID),
		FOREIGN KEY (CIFNumber) REFERENCES CUSTOMER(CIFNumber)ON update cascade On delete set null,
		FOREIGN KEY (AccountNumber) REFERENCES 		ACCOUNT(AccountNumber) 	ON update cascade On delete set null
	);
	
CREATE TABLE 	INVESTMENTS
	(	
		InvestmentID DECIMAL(10,0),
		CIFNumber DECIMAL(11,0) NOT NULL,
		AccountNumber DECIMAL(11,0),
		InvestmentDuration FLOAT,
		InvestmentType VARCHAR,
		InvestmentAmount INT,
		Interest FLOAT,
		PRIMARY KEY (InvestmentID),
		FOREIGN KEY (CIFNumber) REFERENCES CUSTOMER(CIFNumber)ON update cascade On delete set null,
		FOREIGN KEY (AccountNumber) REFERENCES 		ACCOUNT(AccountNumber) 	ON update cascade On delete set null
	);

CREATE TABLE INSURANCE
	(
		InsuranceID DECIMAL(10,0),
		CIFNumber DECIMAL(11,0) NOT NULL,
		InsuranceType VARCHAR,
		AnnualRate FLOAT,
		PRIMARY KEY (InsuranceID),
		FOREIGN KEY (CIFNumber) REFERENCES CUSTOMER(CIFNumber)ON update cascade On delete set null
	);

CREATE TABLE	BENEFICIARY
	(
		BeneficiaryName VARCHAR NOT NULL,
		CustomerCIFNumber DECIMAL(11,0),
		Relationship VARCHAR,
		BeneficiaryCIFNumber DECIMAL(11,0),
		PRIMARY KEY (BeneficiaryName,CustomerCIFNumber),
		FOREIGN KEY (CustomerCIFNumber) REFERENCES CUSTOMER(CIFNumber)ON update cascade On delete set null,
		FOREIGN KEY (BeneficiaryCIFNumber) REFERENCES CUSTOMER(CIFNumber)ON update cascade On delete set null
	);
CREATE TABLE	TRANSACTION
	(
		TransactionID DECIMAL(10,0) ,
		AccountNumber DECIMAL(11,0),
		DebitCardNumber DECIMAL(16,0),
		CreditCardNumber DECIMAL(16,0),
		LoanID DECIMAL(10,0),
		InvestmentID DECIMAL(10,0),
		TransactionAmount INT,
		OldBalance INT,
		NewBalance INT,
		PRIMARY KEY (TransactionID,AccountNumber),
		FOREIGN KEY (AccountNumber) REFERENCES ACCOUNT(AccountNumber)ON update cascade On delete set null,
		FOREIGN KEY (DebitCardNumber) REFERENCES DEBITCARD(DebitCardNumber)ON update cascade On delete set null,
		FOREIGN KEY (CreditCardNumber) REFERENCES CREDITCARD(CreditCardNumber)ON update cascade On delete set null,
		FOREIGN KEY (LoanID) REFERENCES LOANS(LoanID)ON update cascade On delete set null,
		FOREIGN KEY (InvestmentID) REFERENCES INVESTMENTS(InvestmentID)ON update cascade On delete set null
	);

