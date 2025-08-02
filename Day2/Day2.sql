select * from customer;

select first_name || ' ' || last_name as full_name, email
from customer;

select now();

select * from pg_timezone_names;

set timezone= "Asia/Dhaka";
select now();

