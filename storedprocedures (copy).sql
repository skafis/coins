DROP FUNCTION show_student_transactions_bal(refcursor,integer,char);
-- Procedure that accepts cursor names as parameters
CREATE OR REPLACE FUNCTION show_student_transactions_bal(ref1 refcursor,stdaccounts_id integer,trans_type char) 
RETURNS SETOF refcursor AS $$
BEGIN
OPEN ref1 FOR SELECT id,amount FROM netcoins_transactions WHERE studentaccounts_id IN(stdaccounts_id);   -- Open the first cursor
RETURN NEXT ref1;                                                                              -- Return the cursor to the caller
END;
$$ LANGUAGE plpgsql;

-- Start a transaction
BEGIN;
SELECT show_student_transactions_bal('studnetcoins_transactions',1,'Deposit');
FETCH ALL IN "studnetcoins_transactions";
COMMIT;




DROP FUNCTION show_student_transactions_bal(refcursor,integer,integer,integer,integer);
CREATE OR REPLACE FUNCTION show_student_transactions_bal(ref1 refcursor,stdaccounts_id integer,balance integer,wallet integer,prevwallet_id integer) 
  RETURNS SETOF varchar AS
$func$
DECLARE rec record;
DECLARE rec2 record;
BEGIN   
   FOR rec IN SELECT id,amount,transaction_type FROM pos_portal_transactions ORDER BY wallet_id ASC
   LOOP
			wallet::integer=rec.wallet_id::integer
			IF wallet_id = prevwallet_id THEN
				  IF rec.transaction_type LIKE '%Deposit%' THEN
							balance=balance::integer+rec.amount::integer;

				  ELSIF rec.transaction_type LIKE '%Withdraw%' THEN
							balance=balance::integer-rec.amount::integer;
			
      		END IF;
			ELSE:
						prevwallet_id=rec.wallet_id
						balance=0				
   END LOOP;
   RETURN NEXT balance;  
END
$func$  LANGUAGE plpgsql STABLE;

-- Start a transaction
BEGIN;
SELECT show_student_transactions_bal('recst',1,0,0,0);
/*FETCH ALL IN "recst";*/
COMMIT;
