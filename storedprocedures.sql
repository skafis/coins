DROP FUNCTION show_student_transactions_bal(refcursor,integer,integer,integer,integer,integer);
CREATE OR REPLACE FUNCTION show_student_transactions_bal(ref1 refcursor,stdaccounts_id integer,balance integer,counter integer,prevstdaccounts_id integer,startone integer) 
  RETURNS SETOF varchar AS
$func$
DECLARE rec record;
DECLARE cnt integer;
BEGIN   
   FOR rec IN SELECT ppt.id,ppt.amount,ppt.transaction_type,ppt.wallet_id,pps.studentprofiles_id FROM pos_portal_transactions ppt,pos_portal_studentaccountswallets pps WHERE ppt.wallet_id=pps.id ORDER BY pps.studentprofiles_id ASC
   LOOP
			stdaccounts_id = rec.studentprofiles_id;
			IF stdaccounts_id = prevstdaccounts_id THEN			
					IF rec.transaction_type LIKE '%Deposit%' THEN
							balance=balance::integer+rec.amount::integer;

					ELSIF rec.transaction_type LIKE '%Withdraw%' THEN
							balance=balance::integer-rec.amount::integer;
			
      		END IF;
	 				--RETURN NEXT 'if';  
					SELECT INTO cnt count(*) FROM pos_portal_transactions ppt,pos_portal_studentaccountswallets pps WHERE ppt.wallet_id=pps.id AND pps.studentprofiles_id=rec.studentprofiles_id;
	 				--RETURN NEXT balance;  
			ELSIF  stdaccounts_id != prevstdaccounts_id THEN
	 				--RETURN NEXT balance;  
					IF balance>0 THEN
						balance=0;
	 					--RETURN NEXT 'BALANCE RESET TO ZERO';
					END IF;
					IF rec.transaction_type LIKE '%Deposit%' THEN
							balance=balance::integer+rec.amount::integer;

					ELSIF rec.transaction_type LIKE '%Withdraw%' THEN
							balance=balance::integer-rec.amount::integer;
			
      		END IF;
					prevstdaccounts_id = rec.studentprofiles_id;
	 				--RETURN NEXT 'ELSIF';
	 				--RETURN NEXT balance;  
			END IF;
			counter=counter+1;
			IF counter=cnt THEN
				--RETURN NEXT counter;
				--RETURN NEXT cnt;
	 			RETURN NEXT balance;  
				counter=0;
				--balance=0;
      END IF;
   END LOOP;
END
$func$  LANGUAGE plpgsql STABLE;

-- Start a transaction
BEGIN;
SELECT show_student_transactions_bal('recst',1,0,0,0,0);
/*FETCH ALL IN "recst";*/
COMMIT;
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DROP FUNCTION show_transactions(refcursor,integer,integer,integer,integer,integer);
CREATE OR REPLACE FUNCTION show_transactions(ref1 refcursor,stdaccounts_id integer,balance integer,counter integer,prevstdaccounts_id integer,startone integer) 
  RETURNS SETOF varchar AS
$func$
DECLARE rec record;
DECLARE cnt integer;
BEGIN   
   FOR rec IN SELECT ppt.id,ppt.amount,ppt.transaction_type,ppt.wallet_id,pps.studentprofiles_id,ppt.transaction_date,ppt.trace_no,ppt.ref_no,ppt.currency,ppt.location_id,ppt.terminal_id FROM pos_portal_transactions ppt,pos_portal_studentaccountswallets pps WHERE ppt.wallet_id=pps.id ORDER BY pps.studentprofiles_id ASC
--SELECT ppt.id,ppt.amount,ppt.transaction_type,ppt.wallet_id,pps.studentprofiles_id,ppt.transaction_date,ppt.trace_no,ppt.ref_no,ppt.currency,ppt.location_id,ppt.terminal_id FROM pos_portal_transactions ppt,pos_portal_studentaccountswallets pps WHERE ppt.wallet_id=pps.id ORDER BY pps.studentprofiles_id ASC
   LOOP
			stdaccounts_id = rec.studentprofiles_id;
			IF stdaccounts_id = prevstdaccounts_id THEN			
					IF rec.transaction_type LIKE '%Deposit%' THEN
							balance=balance::integer+rec.amount::integer;

					ELSIF rec.transaction_type LIKE '%Withdraw%' THEN
							balance=balance::integer-rec.amount::integer;
			
      		END IF;
	 				--RETURN NEXT 'if';  
					SELECT INTO cnt count(*) FROM pos_portal_transactions ppt,pos_portal_studentaccountswallets pps WHERE ppt.wallet_id=pps.id AND pps.studentprofiles_id=rec.studentprofiles_id;
	 				--RETURN NEXT balance;  
			ELSIF  stdaccounts_id != prevstdaccounts_id THEN
	 				--RETURN NEXT balance;  
					IF balance>0 THEN
						balance=0;
	 					--RETURN NEXT 'BALANCE RESET TO ZERO';
					END IF;
					IF rec.transaction_type LIKE '%Deposit%' THEN
							balance=balance::integer+rec.amount::integer;

					ELSIF rec.transaction_type LIKE '%Withdraw%' THEN
							balance=balance::integer-rec.amount::integer;
			
      		END IF;
					prevstdaccounts_id = rec.studentprofiles_id;
	 				--RETURN NEXT 'ELSIF';
	 				--RETURN NEXT balance;  
			END IF;
			counter=counter+1;
			IF counter=cnt THEN
				--RETURN NEXT counter;
				--RETURN NEXT cnt;
	 			RETURN NEXT rec;
				RETURN NEXT balance;  
				counter=0;
				--balance=0;
      END IF;
   END LOOP;
END
$func$  LANGUAGE plpgsql STABLE;

-- Start a transaction
BEGIN;
SELECT show_transactions('recst',1,0,0,0,0);
/*FETCH ALL IN "recst";*/
COMMIT;
